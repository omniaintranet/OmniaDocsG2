"""Offline checks for release-note review accounting; requires bash and jq."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".github/scripts/hotfix-release-notes"
BASH = os.environ.get("BASH_PATH") or shutil.which("bash")
JQ = os.environ.get("JQ_PATH") or shutil.which("jq")


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
                "reason": "Permissions change requires manual disclosure review"}]}

    def run_script(self, name, notification=False):
        (self.folder / "release-issues.json").write_text(json.dumps(self.data))
        (self.folder / "response.json").write_text(json.dumps(self.response))
        script = (SCRIPTS / name).read_text()
        for filename in ("release-issues.json", "generated-release-notes.rst", "release-notes-audit.json", "copilot-release-notes-response.txt"):
            script = script.replace("/tmp/" + filename, shell_path(self.folder / filename))
        if notification:
            # Exercise notification rendering, stopping before any GitHub mutation.
            script = script.split("project_response=$(", 1)[0] + 'cat "$issue_body_file"\n'
        path = self.folder / name
        path.write_text(script, newline="\n")
        env = dict(os.environ, TEST_PROMPT=shell_path(self.folder / "prompt.txt"),
            TEST_RESPONSE=shell_path(self.folder / "response.json"),
            GITHUB_OUTPUT=shell_path(self.folder / "outputs"), GH_TOKEN="offline-test",
            RELEASE_NOTES_URL="https://omnia-docs-g2.readthedocs.io/en/latest/release-notes/7.0/versions.html")
        return subprocess.run([BASH, "-c", f'export PATH="{shell_path(self.bin)}:{shell_path(Path(BASH).parent)}:$PATH"; bash "{shell_path(path)}"'],
            cwd=ROOT, env=env, capture_output=True, text=True)

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
        self.assertIn("has_notes=true", (self.folder / "outputs").read_text())
        self.assertIn("Sentence variation and readability", (self.folder / "prompt.txt").read_text())
        rendered = self.run_script("create-ready-project-item.sh", notification=True)
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertIn("**1** pending manual security review", rendered.stdout)
        self.assertIn("Security-sensitive issues pending manual review", rendered.stdout)
        self.assertIn("Permissions change requires manual disclosure review", rendered.stdout)

    def test_all_pending_has_no_public_notes(self):
        self.response = {"bullets": [], "omittedIssues": [], "pendingReviewIssues": [
            {"repositoryWithOwner": "omniaintranet/test", "number": n, "reason": "Manual security review required"}
            for n in (1, 2, 3)]}
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("has_notes=false", (self.folder / "outputs").read_text())
        self.assertNotIn("- ", (self.folder / "generated-release-notes.rst").read_text())
        rendered = self.run_script("create-ready-project-item.sh", notification=True)
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertIn("**3** pending manual security review", rendered.stdout)

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


if __name__ == "__main__":
    if not BASH or not JQ:
        raise SystemExit("Install bash and jq, or set BASH_PATH and JQ_PATH, before running these checks.")
    unittest.main()
