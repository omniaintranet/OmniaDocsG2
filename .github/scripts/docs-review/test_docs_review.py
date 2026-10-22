#!/usr/bin/env python3
"""Runs the rule-based documentation checks against the fixtures in .github/docs-review/tests.

Needs Vale and gitleaks on PATH (or VALE_BIN / GITLEAKS_BIN), see .github/docs-review/README.md.
Run: python .github/scripts/docs-review/test_docs_review.py
"""

import collections
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docs_review  # noqa: E402

TESTS = docs_review.CONFIG_DIR / "tests"
FIXTURES = TESTS / "fixtures"
DIGEST_SCRIPT = docs_review.ROOT / ".github" / "scripts" / "latest-changes" / "update.py"


def expected_findings() -> dict:
    data = yaml.safe_load((TESTS / "expected.yml").read_text(encoding="utf-8"))
    result = {}
    for name, items in data.items():
        entries = []
        for item in items or []:
            line, _, rule = str(item).partition(" ")
            entries.append((None if line == "-" else int(line), rule))
        result[name] = collections.Counter(entries)
    return result


class FixtureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = tempfile.TemporaryDirectory()
        files = sorted(str(p) for p in FIXTURES.glob("*.rst.txt"))
        cls.exit_code = docs_review.main(["--files", *files, "--out", cls.out.name])
        findings = json.loads((Path(cls.out.name) / "findings.json").read_text(encoding="utf-8"))
        cls.actual = collections.defaultdict(collections.Counter)
        cls.severity = {}
        for finding in findings:
            name = Path(finding["file"]).name
            cls.actual[name][(finding["line"], finding["rule"])] += 1
            cls.severity[(name, finding["line"], finding["rule"])] = finding["severity"]

    @classmethod
    def tearDownClass(cls):
        cls.out.cleanup()

    def test_every_fixture_has_expectations(self):
        names = {p.name for p in FIXTURES.glob("*.rst.txt")}
        self.assertEqual(names, set(expected_findings()))

    def test_fixtures_match_expectations(self):
        for name, expected in expected_findings().items():
            with self.subTest(fixture=name):
                actual = self.actual.get(name, collections.Counter())
                self.assertEqual(dict(actual), dict(expected),
                                 f"{name}: missing {dict(expected - actual)}, unexpected {dict(actual - expected)}")

    def test_key_selling_point_blocks(self):
        self.assertEqual(self.severity[("tone-bad.rst.txt", 4, "Omnia.InternalLanguage")], "error")
        self.assertEqual(self.exit_code, 1)

    def test_good_fixtures_have_no_errors_or_warnings(self):
        for name in ("tone-good.rst.txt", "confidential-good.rst.txt", "structure-good.rst.txt"):
            serious = [key for key, sev in self.severity.items() if key[0] == name and sev != "info"]
            self.assertEqual(serious, [], name)


class DigestReviewTest(unittest.TestCase):
    """latest-changes.yml reviews the digest with --base HEAD before it commits anything."""

    PAGES = {"guide/index.rst": {"title": "Guide"}, "blocks/index.rst": {"title": "Blocks"}}

    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("digest", DIGEST_SCRIPT)
        cls.digest = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.digest)

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.temp = Path(temp.name)
        self.repo = self.temp / "repo"
        self.repo.mkdir()
        patcher = mock.patch.object(docs_review, "ROOT", self.repo)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.git("init", "-q")
        # Published before the review existed: unchanged lines are not reviewed again.
        self.published = [self.entry("2026-10-01", "guide/index.rst", "Described the key selling point of guides.")]
        self.write_digest(self.published)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "Published digest")

    def git(self, *args):
        subprocess.run(["git", "-c", "user.name=Test", "-c", "user.email=test@example.invalid", *args],
                       cwd=self.repo, check=True, capture_output=True)

    @staticmethod
    def entry(date, path, description):
        return {"date": date, "path": path, "classification": "Added information", "description": description}

    def write_digest(self, entries):
        path = self.repo / self.digest.DIGEST
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.digest.render(entries, self.PAGES), encoding="utf-8", newline="\n")

    def review(self, new_entry):
        self.write_digest([new_entry, *self.published])
        out = self.temp / "out"
        code = docs_review.main(["--base", "HEAD", "--build", "never", "--linkcheck", "never", "--out", str(out),
                                 "--subject", "the documentation updates digest"])
        findings = json.loads((out / "findings.json").read_text(encoding="utf-8"))
        return code, findings, (out / "summary.md").read_text(encoding="utf-8")

    def test_sales_language_in_a_new_entry_blocks_publication(self):
        code, findings, text = self.review(
            self.entry("2026-10-21", "blocks/index.rst", "Added the key selling point of the block gallery."))
        self.assertEqual(code, 1)
        lines = (self.repo / self.digest.DIGEST).read_text(encoding="utf-8").splitlines()
        bad_line = next(n for n, line in enumerate(lines, 1) if "block gallery" in line)
        self.assertEqual([(f["file"], f["line"], f["rule"], f["severity"]) for f in findings],
                         [(self.digest.DIGEST, bad_line, "Omnia.InternalLanguage", "error")])
        self.assertIn("must be fixed before publishing the documentation updates digest", text)

    def test_clean_entry_passes(self):
        code, findings, text = self.review(
            self.entry("2026-10-21", "blocks/index.rst", "Added an example of the block gallery settings."))
        self.assertEqual((code, findings), (0, []))
        self.assertIn("nothing blocks the documentation updates digest", text)


class DigestRepairTest(unittest.TestCase):
    """update.py --review: Copilot (mocked) rewords tone findings; confidentiality findings block."""

    SALES = "Release notes were reorganized to focus on key selling points."

    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("digest", DIGEST_SCRIPT)
        cls.digest = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.digest)

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.temp = Path(temp.name)
        self.repo = self.temp / "repo"
        self.state = self.repo / ".github" / "scripts" / "latest-changes" / "state.json"
        self.state.parent.mkdir(parents=True)
        (self.repo / self.digest.DIGEST).parent.mkdir()
        for path, title in (("guide/index.rst", "Guide"), ("release-notes/7.13/index.rst", "Release 7.13")):
            (self.repo / path).parent.mkdir(parents=True)
            (self.repo / path).write_text(f"{title}\n{'=' * len(title)}\n", encoding="utf-8")
        self.summary = self.temp / "summary.md"
        for patcher in (mock.patch.object(docs_review, "ROOT", self.repo), mock.patch.object(self.digest, "ROOT", self.repo),
                        mock.patch.object(self.digest, "STATE", self.state),
                        mock.patch.dict(os.environ, GITHUB_STEP_SUMMARY=str(self.summary))):
            patcher.start()
            self.addCleanup(patcher.stop)
        self.git("init", "-q")
        # The 21 Oct 2026 case: a person corrected the published page by hand, but the
        # entry in state.json kept the generated text, so the next run rendered it again.
        self.old = self.entry("2026-10-20", "release-notes/7.13/index.rst", self.SALES)
        self.save([{**self.old, "description": "Release notes were reorganized to focus on key functionality."}])
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "Published digest")

    def git(self, *args):
        subprocess.run(["git", "-c", "user.name=Test", "-c", "user.email=test@example.invalid", *args],
                       cwd=self.repo, check=True, capture_output=True)

    @staticmethod
    def entry(date, path, description):
        return {"date": date, "path": path, "classification": "Updated guidance", "description": description}

    def save(self, entries):
        self.digest.save({"version": 2, "processed_commits": {}, "entries": entries}, self.digest.pages_in(self.repo))

    def run_review(self, entries, responses):
        """Write the digest as update() does, then run the review with Copilot answering `responses`."""
        self.save(entries)
        self.summary.unlink(missing_ok=True)
        prompts = []

        def copilot(prompt):
            prompts.append(prompt)
            return json.dumps({"description": responses[min(len(prompts), len(responses)) - 1]})

        with mock.patch.object(self.digest, "ask_copilot", side_effect=copilot):
            code = self.digest.review(self.temp / "out")
        state = json.loads(self.state.read_text(encoding="utf-8"))
        page = (self.repo / self.digest.DIGEST).read_text(encoding="utf-8")
        summary = self.summary.read_text(encoding="utf-8") if self.summary.exists() else ""
        return code, prompts, state, page, summary

    def test_findings_are_given_back_and_the_entry_is_reworded(self):
        fixed = "Release notes were reorganized to focus on the main new features."
        code, prompts, state, page, summary = self.run_review([self.old], [fixed])
        self.assertEqual(code, 0)
        self.assertEqual(len(prompts), 1)
        self.assertIn("'key selling points' is internal or sales language", prompts[0])
        self.assertIn("DOCUMENTATION REVIEW RULES", prompts[0])
        self.assertEqual(state["entries"][0]["description"], fixed)
        self.assertIn(fixed, page)
        self.assertNotIn("selling", page)
        self.assertIn("Reworded after the review (1)", summary)
        self.assertIn("nothing blocks the documentation updates digest", summary)

    def test_findings_left_after_the_repair_rounds_do_not_block(self):
        code, prompts, state, page, summary = self.run_review([self.old], [self.SALES])
        self.assertEqual(code, 0)
        self.assertEqual(len(prompts), 1, "an unchanged answer ends the repair rounds")
        code, prompts, state, page, summary = self.run_review(
            [self.old], [f"Release notes now list the key selling points{'.' * n}" for n in range(1, 9)])
        self.assertEqual(code, 0)
        self.assertEqual(len(prompts), self.digest.REPAIR_ROUNDS)
        self.assertIn("Fix by hand (1, published anyway)", summary)
        self.assertIn("nothing blocks the documentation updates digest", summary)
        self.assertIn("state.json", summary)

    def test_new_entry_without_findings_needs_no_copilot(self):
        new = self.entry("2026-10-21", "guide/index.rst", "Added an example of the guide settings.")
        code, prompts, state, page, summary = self.run_review(
            [new, {**self.old, "description": "Release notes were reorganized to focus on key functionality."}], [])
        self.assertEqual((code, prompts), (0, []))

    def test_confidentiality_finding_blocks_without_rewording(self):
        new = self.entry("2026-10-21", "guide/index.rst", "Added the app id 3f2504e0-4f89-11d3-9a0c-0305e82c3301.")
        code, prompts, state, page, summary = self.run_review([new, self.old], ["Anything"])
        self.assertEqual(code, 1)
        self.assertEqual(prompts, [])
        self.assertIn("Confidential.Guid", summary)
        self.assertIn("must be fixed before publishing the documentation updates digest", summary)

    def test_secret_blocks_without_rewording(self):
        value = "".join(["Q8vT2m", "Xz7RkL", "4pWn9Y", "sB3cHd", "6JfG1aEu"])   # in pieces, so gitleaks passes this file
        new = self.entry("2026-10-21", "guide/index.rst", f'Added the setting apikey = "{value}" to the setup steps.')
        code, prompts, state, page, summary = self.run_review([new], ["Anything"])
        self.assertEqual(code, 1)
        self.assertEqual(prompts, [])
        self.assertIn("Secrets.", summary)


class GenerationRulesTest(unittest.TestCase):
    """The rules both generators put into their prompts come from the rule files themselves."""

    def test_rules_follow_the_rule_files(self):
        with tempfile.TemporaryDirectory() as temp:
            styles = Path(temp) / "Omnia"
            shutil.copytree(docs_review.VALE_STYLE, styles)
            internal = styles / "InternalLanguage.yml"
            internal.write_text(internal.read_text(encoding="utf-8") + "  - sales playbook\n", encoding="utf-8")
            with mock.patch.object(docs_review, "VALE_STYLE", styles):
                rules = docs_review.generation_rules()
        self.assertIn("sales playbook", rules)
        self.assertIn("Omnia.InternalLanguage: Must never appear.", rules)
        self.assertIn("Omnia.Superlatives: Avoid.", rules)
        self.assertIn("Confidential.TenantHost", rules)
        self.assertIn("Wrong reader", rules)                     # docs-review.instructions.md
        self.assertNotIn("How to comment", rules)

    def test_cli_prints_the_rules(self):
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            self.assertEqual(docs_review.main(["--prompt-rules"]), 0)
        self.assertEqual(out.getvalue(), docs_review.generation_rules())


class HelperTest(unittest.TestCase):
    def test_glob(self):
        self.assertTrue(docs_review.matches_any("roadmap/2027/index.rst", ["roadmap/**"]))
        self.assertTrue(docs_review.matches_any("index.rst", ["**/index.rst"]))
        self.assertFalse(docs_review.matches_any("blocks/roadmap.rst", ["roadmap/**"]))

    def test_settings_suppression(self):
        config = docs_review.Config()
        self.assertTrue(config.suppressed_by_settings("Omnia.FuturePromises", "roadmap/index.rst"))
        self.assertFalse(config.suppressed_by_settings("Omnia.FuturePromises", "pages/index.rst"))

    def test_suppression_rule_patterns(self):
        config = docs_review.Config()
        config.suppress = [{"rule": "Confidential.*", "files": ["a/**"]}, {"rule": "*", "files": ["b.rst"]}]
        self.assertTrue(config.suppressed_by_settings("Confidential.Guid", "a/x.rst"))
        self.assertFalse(config.suppressed_by_settings("Omnia.Leftovers", "a/x.rst"))
        self.assertTrue(config.suppressed_by_settings("Omnia.Leftovers", "b.rst"))

    def test_secrets_cannot_be_suppressed(self):
        config = docs_review.Config()
        config.suppress = [{"rule": "*", "files": ["**"]}]
        review = docs_review.Review(config, {})
        review.files["x.rst"] = docs_review.RstFile("x.rst", ".. vale off\n\nclient_secret = ...\n", config)
        for path in ("x.rst", "other.rst"):
            review.add("Secrets.generic-api-key", "error", path, 3, "secret")
            review.add("Omnia.Leftovers", "error", path, 3, "leftover")
        self.assertEqual([(f.rule, f.file) for f in review.findings],
                         [("Secrets.generic-api-key", "x.rst"), ("Secrets.generic-api-key", "other.rst")])

    def test_automated_text_is_blocked_only_by_confidentiality_errors(self):
        findings = [docs_review.Finding("Omnia.InternalLanguage", "error", "a.rst", 1, "sales"),
                    docs_review.Finding("Confidential.Guid", "error", "a.rst", 2, "guid"),
                    docs_review.Finding("Omnia.Superlatives", "warning", "a.rst", 3, "superlative")]
        self.assertEqual([f.repairable for f in findings], [True, False, True])
        self.assertEqual([f.rule for f in docs_review.blocking(findings, automated=False)],
                         ["Omnia.InternalLanguage", "Confidential.Guid"])
        self.assertEqual([f.rule for f in docs_review.blocking(findings, automated=True)], ["Confidential.Guid"])
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            docs_review.print_annotations(findings, automated=True)
        kinds = {re.search(r"title=([\w.]+)", line).group(1): line.split(" ", 1)[0] for line in out.getvalue().splitlines()}
        self.assertEqual(kinds, {"Omnia.InternalLanguage": "::warning", "Confidential.Guid": "::error",
                                 "Omnia.Superlatives": "::warning"})

    def test_warning_parsing(self):
        line = r"C:\docs\blocks\index.rst:66: CRITICAL: Title level inconsistent:"
        match = docs_review.WARNING_LINE.match(line)
        self.assertEqual((match.group("loc"), match.group("line"), match.group("sev")),
                         (r"C:\docs\blocks\index.rst", "66", "CRITICAL"))
        match = docs_review.WARNING_LINE.match("/docs/a.rst: WARNING: document isn't included in any toctree")
        self.assertEqual((match.group("loc"), match.group("line")), ("/docs/a.rst", None))


if __name__ == "__main__":
    unittest.main(verbosity=2)
