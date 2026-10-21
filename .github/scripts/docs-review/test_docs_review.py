#!/usr/bin/env python3
"""Runs the rule-based documentation checks against the fixtures in .github/docs-review/tests.

Needs Vale and gitleaks on PATH (or VALE_BIN / GITLEAKS_BIN), see .github/docs-review/README.md.
Run: python .github/scripts/docs-review/test_docs_review.py
"""

import collections
import importlib.util
import json
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

    def test_warning_parsing(self):
        line = r"C:\docs\blocks\index.rst:66: CRITICAL: Title level inconsistent:"
        match = docs_review.WARNING_LINE.match(line)
        self.assertEqual((match.group("loc"), match.group("line"), match.group("sev")),
                         (r"C:\docs\blocks\index.rst", "66", "CRITICAL"))
        match = docs_review.WARNING_LINE.match("/docs/a.rst: WARNING: document isn't included in any toctree")
        self.assertEqual((match.group("loc"), match.group("line")), ("/docs/a.rst", None))


if __name__ == "__main__":
    unittest.main(verbosity=2)
