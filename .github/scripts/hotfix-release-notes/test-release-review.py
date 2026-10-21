"""Offline checks for release-note review accounting; requires bash and jq."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".github/scripts/hotfix-release-notes"
BASH = os.environ.get("BASH_PATH") or shutil.which("bash")
JQ = os.environ.get("JQ_PATH") or shutil.which("jq")
VALE = os.environ.get("VALE_BIN") or shutil.which("vale")
GITLEAKS = os.environ.get("GITLEAKS_BIN") or shutil.which("gitleaks")
REVIEW_MARKER = "<!-- release-notes-review -->"


def shell_path(path):
    value = Path(path).resolve().as_posix()
    if len(value) > 1 and value[1] == ":":
        return "/" + value[0].lower() + value[2:]
    return value


class ReleaseReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.bin = self.folder / "bin"
        self.bin.mkdir()
        shutil.copyfile(JQ, self.bin / ("jq.exe" if os.name == "nt" else "jq"))
        (self.bin / ("jq.exe" if os.name == "nt" else "jq")).chmod(0o755)
        copilot = self.bin / "copilot"
        copilot.write_text('#!/usr/bin/env bash\ncat > "$TEST_PROMPT"\ncat "$TEST_RESPONSE"\n')
        copilot.chmod(0o755)
        self.data = {"releases": [{"statusName": "Wait for RN - Omnia 7.11.99", "issues": [
            {"repositoryWithOwner": "omniaintranet/test", "number": n,
             "url": f"https://github.com/omniaintranet/test/issues/{n}", "body": "", "comments": []}
            for n in (1, 2, 3)
        ]}]}
        self.response = {"bullets": [{"text": "- Quick Search now correctly handles document filters",
            "sourceIssues": [{"repositoryWithOwner": "omniaintranet/test", "number": 1}]}],
            "omittedIssues": [{"repositoryWithOwner": "omniaintranet/test", "number": 2, "reason": "Internal maintenance"}],
            "pendingReviewIssues": [{"repositoryWithOwner": "omniaintranet/test", "number": 3,
                "reason": "Permissions change requires manual disclosure review",
                "suggestedText": "- Improved the reliability of permission handling"}]}

    def run_script(self, name, notification=False, cwd=ROOT):
        (self.folder / "release-issues.json").write_text(json.dumps(self.data))
        (self.folder / "response.json").write_text(json.dumps(self.response))
        script = (SCRIPTS / name).read_text()
        for filename in ("release-issues.json", "generated-release-notes.rst", "release-notes-audit.json",
                         "copilot-release-notes-response.txt", "docs-review-release-notes"):
            script = script.replace("/tmp/" + filename, shell_path(self.folder / filename))
        if notification:
            # Exercise notification rendering, stopping before any GitHub mutation.
            script = script.split("project_response=$(", 1)[0] + 'cat "$issue_body_file"\n'
        path = self.folder / name
        path.write_text(script, newline="\n")
        for support in ("wait-for-rn-lib.sh", "wait-for-rn-pattern.txt"):
            (self.folder / support).write_text((SCRIPTS / support).read_text(), newline="\n")
        env = dict(os.environ, TEST_PROMPT=shell_path(self.folder / "prompt.txt"),
            TEST_RESPONSE=shell_path(self.folder / "response.json"),
            GITHUB_OUTPUT=shell_path(self.folder / "outputs"), GH_TOKEN="offline-test",
            RELEASE_NOTES_FILE=shell_path(self.folder / "versions.rst"),
            TEST_EXISTING_PR=str(getattr(self, "existing_pr", False)).lower(),
            TEST_NO_CHANGES=str(getattr(self, "no_changes", False)).lower(),
            TEST_PR_BODY=shell_path(self.folder / "pr-body.md"),
            TEST_EXISTING_BODY=getattr(self, "existing_body", "Automatically generated draft release notes."),
            DOCUMENTATION_PR_URL=getattr(self, "pr_url", "https://github.com/omniaintranet/OmniaDocsG2/pull/43"),
            RELEASE_NOTES_URL="https://omnia-docs-g2.readthedocs.io/en/latest/release-notes/7.0/versions.html")
        return subprocess.run([BASH, "-c", f'export PATH="{shell_path(self.bin)}:{shell_path(Path(BASH).parent)}:$PATH"; bash "{shell_path(path)}"'],
            cwd=cwd, env=env, capture_output=True, text=True)

    def generate(self):
        return self.run_script("generate-release-notes.sh")

    def test_mixed_release_and_notification(self):
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        audit = json.loads((self.folder / "release-notes-audit.json").read_text())
        self.assertEqual(audit["pendingReviewIssues"][0]["number"], 3)
        notes = (self.folder / "generated-release-notes.rst").read_text()
        self.assertIn("Quick Search", notes)
        self.assertNotIn("Permissions", notes)
        self.assertNotIn("Improved the reliability of permission handling", notes)
        self.assertEqual(audit["pendingReviewIssues"][0]["suggestedText"], self.response["pendingReviewIssues"][0]["suggestedText"])
        self.assertIn("has_notes=true", (self.folder / "outputs").read_text())
        self.assertIn("Sentence variation and readability", (self.folder / "prompt.txt").read_text())
        rendered = self.run_script("create-ready-project-item.sh", notification=True)
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertIn("**1** pending manual security review", rendered.stdout)
        self.assertIn("[Review the documentation pull request](https://github.com/omniaintranet/OmniaDocsG2/pull/43)", rendered.stdout)
        self.assertIn("Security-sensitive issues pending manual review", rendered.stdout)
        self.assertIn("Permissions change requires manual disclosure review", rendered.stdout)
        self.assertIn("Suggested release note (pending approval)", rendered.stdout)
        self.assertIn(self.response["pendingReviewIssues"][0]["suggestedText"], rendered.stdout)

    def check_pr_output(self, existing=False, no_changes=False):
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        # Isolate git/gh mutations; exercise the production script and output path.
        git = self.bin / "git"
        git.write_text('#!/usr/bin/env bash\ncase "$1" in\n  config|fetch|checkout|add|commit|push) exit 0 ;;\n  rev-parse) printf \'%040d\\n\' 1 ;;\n  ls-remote) exit 2 ;;\n  diff) [ "$TEST_NO_CHANGES" = true ] ;;\n  *) echo "Unexpected mock git call: $*" >&2; exit 99 ;;\nesac\n')
        git.chmod(0o755)
        gh = self.bin / "gh"
        gh.write_text('#!/usr/bin/env bash\ncase "$1 $2" in\n  "pr list") if [ "$TEST_EXISTING_PR" = true ]; then echo 43; fi ;;\n'
                      '  "pr view") if [[ "$*" == *"--json body"* ]]; then printf \'%s\' "$TEST_EXISTING_BODY"; '
                      'else echo https://github.com/omniaintranet/OmniaDocsG2/pull/43; fi ;;\n'
                      '  "pr create"|"pr edit") while [ $# -gt 0 ]; do [ "$1" = --body-file ] && cp "$2" "$TEST_PR_BODY"; shift; done\n'
                      '    echo https://github.com/omniaintranet/OmniaDocsG2/pull/43 ;;\n'
                      '  *) echo "Unexpected mock gh call: $*" >&2; exit 99 ;;\nesac\n')
        gh.chmod(0o755)
        (self.folder / "versions.rst").write_text("7.11.98\n========\n")
        self.existing_pr = existing
        self.no_changes = no_changes
        result = self.run_script("create-pr.sh")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("pr_url=https://github.com/omniaintranet/OmniaDocsG2/pull/43", (self.folder / "outputs").read_text())
        body = self.folder / "pr-body.md"
        return body.read_text() if body.exists() else None

    def write_review(self, findings):
        """What review-release-notes.sh leaves for create-pr.sh."""
        review = self.folder / "docs-review-release-notes"
        review.mkdir()
        (review / "findings.json").write_text(json.dumps(findings))
        (review / "summary.md").write_text("<!-- docs-review-summary -->\n## Documentation review result\n")

    def test_new_pr_exports_link(self):
        self.check_pr_output()

    def test_updated_pr_exports_link(self):
        self.check_pr_output(existing=True)

    def test_unchanged_existing_pr_exports_link(self):
        self.check_pr_output(existing=True, no_changes=True)

    def test_new_pr_body_marks_blocking_review_findings(self):
        self.write_review([{"rule": "Omnia.InternalLanguage", "severity": "error", "file": "release-notes/7.0/versions.rst",
                            "line": 5, "message": "sales language"},
                           {"rule": "Omnia.Superlatives", "severity": "warning", "file": "release-notes/7.0/versions.rst",
                            "line": 6, "message": "superlative"}])
        body = self.check_pr_output()
        self.assertTrue(body.startswith("Automatically generated draft release notes for Omnia 7.11.99."), body)
        self.assertIn(REVIEW_MARKER, body)
        self.assertIn("> [!CAUTION]", body)
        self.assertIn("**1 problem(s) that must be fixed**", body)
        self.assertIn("## Documentation review result", body)

    def test_new_pr_body_with_clean_review_has_no_caution(self):
        self.write_review([{"rule": "Reference.CustomerNumber", "severity": "info", "file": "release-notes/7.0/versions.rst",
                            "line": 5, "message": "check the number"}])
        body = self.check_pr_output()
        self.assertNotIn("[!CAUTION]", body)
        self.assertIn("## Documentation review result", body)

    def test_new_pr_body_without_review_says_so(self):
        body = self.check_pr_output()
        self.assertIn("> [!WARNING]\n> The documentation review did not run", body)

    def test_updated_pr_replaces_only_the_review_section(self):
        self.write_review([])
        self.existing_body = f"Generated notes.\n\nChecked the customer references.\n\n{REVIEW_MARKER}\n\nOld review result"
        body = self.check_pr_output(existing=True)
        self.assertTrue(body.startswith(f"Generated notes.\n\nChecked the customer references.\n\n{REVIEW_MARKER}"), body)
        self.assertNotIn("Old review result", body)
        self.assertIn("## Documentation review result", body)

    def test_updated_pr_without_review_section_keeps_its_body(self):
        self.write_review([])
        self.existing_body = "Written by a person."
        body = self.check_pr_output(existing=True)
        self.assertTrue(body.startswith(f"Written by a person.\n\n{REVIEW_MARKER}"), body)

    def test_notification_without_pr_link(self):
        self.pr_url = ""
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        rendered = self.run_script("create-ready-project-item.sh", notification=True)
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertNotIn("Review the documentation pull request", rendered.stdout)

    def test_notification_rejects_unrelated_pr_link(self):
        self.pr_url = "https://github.com/another/repository/pull/43"
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        rendered = self.run_script("create-ready-project-item.sh", notification=True)
        self.assertNotEqual(rendered.returncode, 0)
        self.assertIn("must reference a pull request", rendered.stderr)

    def test_all_pending_has_no_public_notes(self):
        self.response = {"bullets": [], "omittedIssues": [], "pendingReviewIssues": [
            {"repositoryWithOwner": "omniaintranet/test", "number": n, "reason": "Manual security review required",
             "suggestedText": "- Improved the reliability of the sign-in process"}
            for n in (1, 2, 3)]}
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("has_notes=false", (self.folder / "outputs").read_text())
        self.assertNotIn("- ", (self.folder / "generated-release-notes.rst").read_text())
        rendered = self.run_script("create-ready-project-item.sh", notification=True)
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertIn("**3** pending manual security review", rendered.stdout)
        self.assertEqual(rendered.stdout.count("Suggested release note (pending approval)"), 3)

    def test_all_omitted_has_no_public_notes(self):
        self.response = {"bullets": [], "pendingReviewIssues": [], "omittedIssues": [
            {"repositoryWithOwner": "omniaintranet/test", "number": n, "reason": "Internal maintenance"}
            for n in (1, 2, 3)]}
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("has_notes=false", (self.folder / "outputs").read_text())

    def test_duplicate_pending_issue_is_rejected(self):
        self.response["pendingReviewIssues"][0]["number"] = 1
        self.assertNotEqual(self.generate().returncode, 0)

    def test_missing_issue_is_rejected(self):
        self.response["pendingReviewIssues"] = []
        self.assertNotEqual(self.generate().returncode, 0)

    def test_empty_pending_reason_is_rejected(self):
        self.response["pendingReviewIssues"][0]["reason"] = ""
        self.assertNotEqual(self.generate().returncode, 0)

    def test_private_link_in_pending_reason_is_removed(self):
        self.response["pendingReviewIssues"][0]["reason"] = "Review https://private.example/secret"
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("private.example", (self.folder / "release-notes-audit.json").read_text())


    def test_missing_suggestion_is_rejected(self):
        del self.response["pendingReviewIssues"][0]["suggestedText"]
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("required release-note audit JSON", result.stderr)

    def test_empty_suggestion_is_rejected(self):
        self.response["pendingReviewIssues"][0]["suggestedText"] = "   "
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("required release-note audit JSON", result.stderr)

    def test_private_url_in_suggestion_is_rejected(self):
        self.response["pendingReviewIssues"][0]["suggestedText"] += " https://private.example/secret"
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("contain a URL", result.stderr)

    def test_email_in_suggestion_is_rejected(self):
        self.response["pendingReviewIssues"][0]["suggestedText"] += " person@example.test"
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("contain an email", result.stderr)

    def test_suggestion_cannot_borrow_another_issues_reference(self):
        self.data["releases"][0]["issues"][0]["body"] = "https://support.example/agent/tickets/59036"
        self.response["pendingReviewIssues"][0]["suggestedText"] += " (#59036)"
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not supported by a trusted source URL", result.stderr)

    def test_verified_suggestion_reference_is_allowed(self):
        self.data["releases"][0]["issues"][2]["body"] = "https://support.example/agent/tickets/59036"
        self.response["pendingReviewIssues"][0]["suggestedText"] += " (#59036)"
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("#59036", (self.folder / "generated-release-notes.rst").read_text())


@unittest.skipUnless(VALE and GITLEAKS, "needs Vale and gitleaks (VALE_BIN, GITLEAKS_BIN), see .github/docs-review/README.md")
class ReleaseNotesDocsReviewTests(unittest.TestCase):
    """review-release-notes.sh with the real documentation review in a scratch repository."""

    NOTES = "release-notes/7.0/versions.rst"
    PUBLISHED = "7.11.98\n========================================\n(Omnia 7.11.98)\n\n- Published before the review: a key selling point\n"

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.repo = self.folder / "repo"
        sources = [".github/scripts/docs-review/docs_review.py"]
        sources += [p.relative_to(ROOT).as_posix() for p in (ROOT / ".github/docs-review").rglob("*") if p.is_file()]
        for source in sources:
            target = self.repo / source
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / source, target)
        (self.repo / self.NOTES).parent.mkdir(parents=True)
        (self.repo / self.NOTES).write_text(self.PUBLISHED, newline="\n")
        for args in (["init", "-q"], ["add", "-A"], ["commit", "-q", "-m", "Published"]):
            subprocess.run(["git", "-c", "user.name=Test", "-c", "user.email=test@example.invalid", *args],
                           cwd=self.repo, check=True, capture_output=True)

    def review(self, bullet):
        (self.folder / "generated-release-notes.rst").write_text(
            f"7.11.99\n========================================\n(Omnia 7.11.99)\n\n{bullet}\n", newline="\n")
        script = (SCRIPTS / "review-release-notes.sh").read_text(encoding="utf-8")
        for name in ("generated-release-notes.rst", "docs-review-release-notes"):
            script = script.replace("/tmp/" + name, shell_path(self.folder / name))
        path = self.folder / "review-release-notes.sh"
        path.write_text(script, encoding="utf-8", newline="\n")
        env = dict(os.environ, PYTHON=shell_path(sys.executable), RELEASE_NOTES_FILE=self.NOTES,
                   GITHUB_OUTPUT=shell_path(self.folder / "outputs"), VALE_BIN=VALE, GITLEAKS_BIN=GITLEAKS)
        env.pop("GITHUB_STEP_SUMMARY", None)
        result = subprocess.run([BASH, "-c", f'export PATH="{shell_path(Path(BASH).parent)}:$PATH"; bash "{shell_path(path)}"'],
                                cwd=self.repo, env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((self.repo / self.NOTES).read_text(), self.PUBLISHED, "the release-notes file must be restored")
        review = self.folder / "docs-review-release-notes"
        return (json.loads((review / "findings.json").read_text()), (review / "summary.md").read_text(encoding="utf-8"),
                (self.folder / "outputs").read_text())

    def test_sales_language_in_generated_notes_is_reported(self):
        findings, summary, outputs = self.review("- Quick Search now handles document filters, a key selling point")
        self.assertEqual([(f["file"], f["line"], f["rule"], f["severity"]) for f in findings],
                         [(self.NOTES, 5, "Omnia.InternalLanguage", "error")])
        self.assertIn("must be fixed before publishing the generated release notes", summary)
        self.assertIn("errors=1", outputs)

    def test_clean_generated_notes_pass(self):
        findings, summary, outputs = self.review("- Quick Search now correctly handles document filters")
        self.assertEqual(findings, [])
        self.assertIn("nothing blocks the generated release notes", summary)
        self.assertIn("errors=0", outputs)


if __name__ == "__main__":
    if not BASH or not JQ:
        raise SystemExit("Install bash and jq, or set BASH_PATH and JQ_PATH, before running these checks.")
    unittest.main()
