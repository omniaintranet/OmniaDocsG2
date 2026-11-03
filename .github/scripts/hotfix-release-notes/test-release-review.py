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
CATEGORIES = ".github/skills/hotfix-release-notes/categories.txt"
HEADING = "7.11.99\n========================================\n(Omnia 7.11.99)\n\n"


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
        # Call 1 writes prompt.txt and answers response.json; call n > 1 writes prompt.txt.<n> and
        # answers response.json.<n> (one per entry in self.follow_ups), or response.json again.
        copilot.write_text('#!/usr/bin/env bash\nn=$(( $(cat "$TEST_PROMPT.count" 2>/dev/null || echo 0) + 1 ))\n'
                           'echo "$n" > "$TEST_PROMPT.count"\n'
                           'if [ "$n" -eq 1 ]; then cat > "$TEST_PROMPT"; else cat > "$TEST_PROMPT.$n"; fi\n'
                           'if [ -f "$TEST_RESPONSE.$n" ]; then cat "$TEST_RESPONSE.$n"; else cat "$TEST_RESPONSE"; fi\n',
                           newline="\n")
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
        for n, follow_up in enumerate(getattr(self, "follow_ups", []), 2):
            (self.folder / f"response.json.{n}").write_text(json.dumps(follow_up))
        script = (SCRIPTS / name).read_text()
        categories = self.folder / "categories.txt"
        if not categories.exists():
            categories.write_text((ROOT / CATEGORIES).read_text(), newline="\n")
        for filename in ("release-issues.json", "generated-release-notes.rst", "release-notes-audit.json",
                         "copilot-release-notes-response.txt", "docs-review-release-notes",
                         "release-notes-new-categories.txt", "release-notes-removed-references.txt"):
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
            PYTHON=getattr(self, "python", shell_path(sys.executable)),
            CATEGORIES_FILE=shell_path(categories),
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
        prompt = (self.folder / "prompt.txt").read_text()
        self.assertIn("Sentence variation and readability", prompt)
        # The documentation review rules, read from the rule files at run time.
        self.assertIn("DOCUMENTATION REVIEW RULES", prompt)
        self.assertIn("key selling points?", prompt)
        self.assertLess(prompt.index("DOCUMENTATION REVIEW RULES"), prompt.index("Release data:"))
        rendered = self.run_script("create-ready-project-item.sh", notification=True)
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertIn("**1** pending manual security review", rendered.stdout)
        self.assertIn("[Review the documentation pull request](https://github.com/omniaintranet/OmniaDocsG2/pull/43)", rendered.stdout)
        self.assertIn("Security-sensitive issues pending manual review", rendered.stdout)
        self.assertIn("Permissions change requires manual disclosure review", rendered.stdout)
        self.assertIn("Suggested release note (pending approval)", rendered.stdout)
        self.assertIn(self.response["pendingReviewIssues"][0]["suggestedText"], rendered.stdout)

    def test_generation_without_review_rules_still_works(self):
        self.python = "false"
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("generating the release notes without them", result.stdout)
        self.assertNotIn("DOCUMENTATION REVIEW RULES", (self.folder / "prompt.txt").read_text())

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

    def copilot_calls(self):
        count = self.folder / "prompt.txt.count"
        return int(count.read_text()) if count.exists() else 0

    def test_prompt_names_every_issue(self):
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("The release data holds 3 issue(s): omniaintranet/test#1, omniaintranet/test#2, "
                      "omniaintranet/test#3.", (self.folder / "prompt.txt").read_text())
        self.assertEqual(self.copilot_calls(), 1)

    def test_missing_issue_is_rejected(self):
        # Copilot leaves the issue out of its first answer and of both follow-ups.
        self.response["pendingReviewIssues"] = []
        self.follow_ups = [{"bullets": [], "omittedIssues": [], "pendingReviewIssues": []}] * 2
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing from the audit: omniaintranet/test#3", result.stderr)
        self.assertIn("Follow-up requests for missing issues: 2.", result.stderr)
        self.assertEqual(self.copilot_calls(), 3)
        # Every answer is kept for the failure artifact.
        responses = (self.folder / "copilot-release-notes-response.txt").read_text()
        self.assertIn("===== Copilot response: all 3 issues =====", responses)
        self.assertIn("===== Copilot response: follow-up 2 for 1 missing issue(s) =====", responses)

    def test_missing_issue_is_asked_for_again(self):
        pending = self.response["pendingReviewIssues"]
        self.response["pendingReviewIssues"] = []
        self.follow_ups = [{"bullets": [], "omittedIssues": [], "pendingReviewIssues": pending}]
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("does not account for 1 issue(s): omniaintranet/test#3", result.stdout)
        self.assertIn("accounted for after 1 follow-up request(s)", result.stdout)
        self.assertEqual(self.copilot_calls(), 2)
        audit = json.loads((self.folder / "release-notes-audit.json").read_text())
        self.assertEqual([i["number"] for i in audit["pendingReviewIssues"]], [3])
        self.assertEqual([i["number"] for i in audit["omittedIssues"]], [2])
        # The follow-up sends only the missing issue, with the bullets already written as context.
        prompt = (self.folder / "prompt.txt.2").read_text()
        release_data = prompt.split("Release data:\n\n", 1)[1].split("\n", 1)[0]
        self.assertEqual([i["number"] for i in json.loads(release_data)["releases"][0]["issues"]], [3])
        self.assertIn("Quick Search now correctly handles document filters", prompt.split("Release data:", 1)[0])
        self.assertIn("The release data holds 1 issue(s): omniaintranet/test#3.", prompt)
        self.assertIn("Account for every issue in the release data below, and for no other issue.", prompt)
        self.assertNotIn("Account for every issue in the release data below", (self.folder / "prompt.txt").read_text())

    def test_follow_up_can_join_an_existing_bullet(self):
        self.response["pendingReviewIssues"] = []
        bullet = self.response["bullets"][0]
        self.follow_ups = [{"bullets": [dict(bullet, sourceIssues=bullet["sourceIssues"] + [
            {"repositoryWithOwner": "omniaintranet/test", "number": 3}])],
            "omittedIssues": [], "pendingReviewIssues": []}]
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        audit = json.loads((self.folder / "release-notes-audit.json").read_text())
        self.assertEqual(len(audit["bullets"]), 1)
        self.assertEqual([i["number"] for i in audit["bullets"][0]["sourceIssues"]], [1, 3])
        notes = (self.folder / "generated-release-notes.rst").read_text()
        self.assertEqual(notes.count("Quick Search now correctly handles document filters"), 1)

    def test_follow_up_adds_a_new_bullet(self):
        self.response["pendingReviewIssues"] = []
        self.follow_ups = [{"bullets": [{"text": "- Page Rollup now shows the page owner",
            "sourceIssues": [{"repositoryWithOwner": "omniaintranet/test", "number": 3}]}],
            "omittedIssues": [], "pendingReviewIssues": []}]
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        notes = (self.folder / "generated-release-notes.rst").read_text()
        self.assertIn("- Quick Search now correctly handles document filters\n- Page Rollup now shows the page owner\n", notes)

    def test_follow_up_naming_another_issue_is_rejected(self):
        self.response["pendingReviewIssues"] = []
        self.follow_ups = [{"bullets": [], "pendingReviewIssues": [], "omittedIssues": [
            {"repositoryWithOwner": "omniaintranet/test", "number": n, "reason": "Internal maintenance"} for n in (2, 3)]}]
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("The follow-up answer names issues that were not missing: omniaintranet/test#2", result.stderr)

    def test_other_audit_problems_get_no_follow_up(self):
        # Issue 3 is missing, but issue 1 is also both a bullet and pending review: no second request.
        self.response["pendingReviewIssues"][0]["number"] = 1
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing from the audit: omniaintranet/test#3", result.stderr)
        self.assertIn("In a bullet and also omitted or pending review: omniaintranet/test#1", result.stderr)
        self.assertEqual(self.copilot_calls(), 1)

    def test_issue_in_several_bullets_is_accepted(self):
        self.response["bullets"].append({"text": "- Quick Search now shows document previews",
            "sourceIssues": [{"repositoryWithOwner": "omniaintranet/test", "number": 1}]})
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        notes = (self.folder / "generated-release-notes.rst").read_text()
        self.assertIn("document previews", notes)

    def bullets(self, *categories):
        """One public bullet per category, all from issue 1."""
        self.response["bullets"] = [{"text": f"- Release note {n}", "category": category,
            "sourceIssues": [{"repositoryWithOwner": "omniaintranet/test", "number": 1}]}
            for n, category in enumerate(categories, 1)]

    def assert_categories_unchanged(self):
        self.assertEqual((self.folder / "categories.txt").read_text(), (ROOT / CATEGORIES).read_text())
        self.assertEqual((self.folder / "release-notes-new-categories.txt").read_text(), "")

    def test_ten_bullets_stay_flat(self):
        self.bullets(*["Search"] * 5 + ["Teamwork"] * 5)
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((self.folder / "generated-release-notes.rst").read_text(),
                         HEADING + "".join(f"- Release note {n}\n" for n in range(1, 11)))
        # Teamwork heads no group, so it does not join the list.
        self.assert_categories_unchanged()
        prompt = (self.folder / "prompt.txt").read_text()
        self.assertIn("Category names (categories.txt), in display order:\n\nPages and blocks\nPage Rollup\n", prompt)
        self.assertIn("Group long releases by category", prompt)

    def test_long_release_is_grouped_by_category(self):
        # Listed categories in list order, then a new one, then Other; bullets keep their order in a group.
        self.bullets("Search", "page rollup", "Teamwork", "", "Search", "Page Rollup", "**Accessibility**",
                     "Teamwork", "Other", "Search", "Page Rollup")
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((self.folder / "generated-release-notes.rst").read_text(), HEADING + (
            "**Page Rollup**\n\n- Release note 2\n- Release note 6\n- Release note 11\n\n"
            "**Search**\n\n- Release note 1\n- Release note 5\n- Release note 10\n\n"
            "**Accessibility**\n\n- Release note 7\n\n"
            "**Teamwork**\n\n- Release note 3\n- Release note 8\n\n"
            "**Other**\n\n- Release note 4\n- Release note 9\n"))
        audit = json.loads((self.folder / "release-notes-audit.json").read_text())
        self.assertEqual([b["category"] for b in audit["bullets"]][:7],
                         ["Search", "Page Rollup", "Teamwork", "Other", "Search", "Page Rollup", "Accessibility"])
        # The new category joins the list, so the next release reuses it.
        self.assertEqual((self.folder / "categories.txt").read_text(), (ROOT / CATEGORIES).read_text() + "Teamwork\n")
        self.assertEqual((self.folder / "release-notes-new-categories.txt").read_text(), "Teamwork\n")
        self.assertIn("New release-note categories", result.stdout)

    def test_long_release_in_one_category_stays_flat(self):
        self.bullets(*["Teamwork"] * 11)
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("**", (self.folder / "generated-release-notes.rst").read_text())
        self.assert_categories_unchanged()

    def test_category_with_markup_is_rejected(self):
        self.bullets("Page `Rollup`")
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("required release-note audit JSON", result.stderr)

    def test_new_category_is_named_in_the_pr(self):
        self.bullets(*["Search"] * 6 + ["Teamwork"] * 5)
        body = self.check_pr_output()
        self.assertIn("> [!NOTE]\n> New category headers, added to `", body)
        self.assertIn("categories.txt`: Teamwork. Keep them", body)

    def test_pr_without_new_categories_has_no_note(self):
        body = self.check_pr_output()
        self.assertNotIn("New category headers", body)
        self.assertNotIn("Customer references removed", body)

    def test_removed_reference_is_named_in_the_pr(self):
        self.data["releases"][0]["issues"][1]["body"] = "https://support.example/agent/tickets/59036"
        self.response["bullets"][0]["text"] += " (#59036)"
        body = self.check_pr_output()
        self.assertIn("> [!NOTE]\n> Customer references removed from bullets because no source URL on the bullet's own "
                      "issues supports them: #59036. Add one back", body)

    def validate(self, lines):
        notes = self.folder / "notes.rst"
        notes.write_text(HEADING + lines, newline="\n")
        (self.folder / "release-issues.json").write_text(json.dumps(self.data))
        command = (f'export PATH="{shell_path(self.bin)}:{shell_path(Path(BASH).parent)}:$PATH"; '
                   f'bash "{shell_path(SCRIPTS / "validate-release-notes.sh")}" '
                   f'"{shell_path(self.folder / "release-issues.json")}" "{shell_path(notes)}"')
        return subprocess.run([BASH, "-c", command], cwd=ROOT, capture_output=True, text=True)

    def test_validator_checks_category_headers(self):
        six = "".join(f"- Search note {n}\n" for n in range(6))
        five = "".join(f"- Other note {n}\n" for n in range(5))
        grouped = f"**Search**\n\n{six}\n**Other**\n\n{five}"
        result = self.validate(grouped)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for problem, lines in {
            "ten bullets": f"**Search**\n\n{six}\n**Other**\n\n- a\n- b\n- c\n- d\n",
            "bullet above the first header": f"- First\n\n{grouped}",
            "no blank line before a header": f"**Search**\n\n{six}**Other**\n\n{five}",
            "no blank line after a header": f"**Search**\n{six}\n**Other**\n\n{five}",
            "header used twice": f"**Search**\n\n{six}\n**Search**\n\n{five}",
            "header without bullets": f"**Search**\n\n{six}\n**Other**\n\n**Security**\n\n{five}",
            "markup in a header": f"**Search**\n\n{six}\n**Other `x`**\n\n{five}",
        }.items():
            with self.subTest(problem):
                self.assertNotEqual(self.validate(lines).returncode, 0)

    def test_issue_in_bullet_and_omitted_is_rejected(self):
        self.response["omittedIssues"][0]["number"] = 1
        self.response["bullets"][0]["sourceIssues"].append(
            {"repositoryWithOwner": "omniaintranet/test", "number": 2})
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("In a bullet and also omitted or pending review: omniaintranet/test#1", result.stderr)

    def test_issue_listed_twice_as_omitted_is_rejected(self):
        self.response["omittedIssues"].append(dict(self.response["omittedIssues"][0]))
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Listed more than once under omittedIssues or pendingReviewIssues: omniaintranet/test#2", result.stderr)

    def test_unknown_issue_is_rejected(self):
        self.response["bullets"][0]["sourceIssues"].append(
            {"repositoryWithOwner": "omniaintranet/test", "number": 99})
        result = self.generate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Not in the release data: omniaintranet/test#99", result.stderr)

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
        # The skill: remove a reference without evidence on the suggestion's own issue.
        self.data["releases"][0]["issues"][0]["body"] = "https://support.example/agent/tickets/59036"
        self.response["pendingReviewIssues"][0]["suggestedText"] += " (#59036)"
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Removed customer reference(s) #59036 from the suggestion for omniaintranet/test#3", result.stdout)
        audit = json.loads((self.folder / "release-notes-audit.json").read_text())
        self.assertEqual(audit["pendingReviewIssues"][0]["suggestedText"], "- Improved the reliability of permission handling")

    def test_bullet_cannot_borrow_another_issues_reference(self):
        self.data["releases"][0]["issues"][1]["body"] = "https://support.example/agent/tickets/59036"
        self.response["bullets"][0]["text"] += " (#59036)"
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Removed customer reference(s) #59036 from the bullet from omniaintranet/test#1", result.stdout)
        notes = (self.folder / "generated-release-notes.rst").read_text()
        self.assertIn("- Quick Search now correctly handles document filters\n", notes)
        self.assertNotIn("59036", notes)

    def test_bullet_keeps_references_from_its_own_issues(self):
        # Zendesk and OIM URLs count; a GitHub issue URL never does.
        self.data["releases"][0]["issues"][0]["body"] = "https://support.example/agent/tickets/59036"
        self.data["releases"][0]["issues"][2]["comments"] = [{"author": "qa", "createdAt": "2026-11-03T08:00:00Z",
            "body": "OIM https://oim.example/issues/166490 and https://github.com/omniaintranet/test/issues/77"}]
        self.response["bullets"][0]["text"] += " (#59036, #77, #166490)"
        self.response["bullets"][0]["sourceIssues"].append({"repositoryWithOwner": "omniaintranet/test", "number": 3})
        self.response["pendingReviewIssues"] = []
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Removed customer reference(s) #77 from the bullet from omniaintranet/test#1, omniaintranet/test#3",
                      result.stdout)
        notes = (self.folder / "generated-release-notes.rst").read_text()
        self.assertIn("- Quick Search now correctly handles document filters (#59036, #166490)\n", notes)

    def test_verified_suggestion_reference_is_allowed(self):
        self.data["releases"][0]["issues"][2]["body"] = "https://support.example/agent/tickets/59036"
        self.response["pendingReviewIssues"][0]["suggestedText"] += " (#59036)"
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("#59036", (self.folder / "generated-release-notes.rst").read_text())


@unittest.skipUnless(VALE and GITLEAKS, "needs Vale and gitleaks (VALE_BIN, GITLEAKS_BIN), see .github/docs-review/README.md")
class ReleaseNotesDocsReviewTests(unittest.TestCase):
    """review-release-notes.sh with the real documentation review in a scratch repository, Copilot mocked."""

    NOTES = "release-notes/7.0/versions.rst"
    PUBLISHED = "7.11.98\n========================================\n(Omnia 7.11.98)\n\n- Published before the review: a key selling point\n"
    SALES = "- Quick Search now handles document filters, a key selling point"
    FIXED = "- Quick Search now correctly handles document filters"

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.repo = self.folder / "repo"
        sources = [".github/scripts/docs-review/docs_review.py", "conf.py", ".github/skills/hotfix-release-notes/SKILL.md",
                   ".github/instructions/docs-review.instructions.md", CATEGORIES]
        sources += [f".github/scripts/hotfix-release-notes/{name}"
                    for name in ("validate-release-notes.sh", "wait-for-rn-lib.sh", "wait-for-rn-pattern.txt",
                                 "render-release-notes.jq")]
        sources += [p.relative_to(ROOT).as_posix() for p in (ROOT / ".github/docs-review").rglob("*") if p.is_file()]
        for source in sources:
            target = self.repo / source
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / source).read_bytes().replace(b"\r\n", b"\n"))
        (self.repo / self.NOTES).parent.mkdir(parents=True)
        (self.repo / self.NOTES).write_text(self.PUBLISHED, newline="\n")
        # A minimal site with the repository's conf.py, for the Sphinx build comparison.
        (self.repo / "index.rst").write_text("Omnia\n=====\n\n.. toctree::\n\n   release-notes/7.0/versions\n", newline="\n")
        for args in (["init", "-q"], ["add", "-A"], ["commit", "-q", "-m", "Published"]):
            subprocess.run(["git", "-c", "user.name=Test", "-c", "user.email=test@example.invalid", *args],
                           cwd=self.repo, check=True, capture_output=True)
        # On its n-th call, Copilot answers with responses/<n>.json, or the last response after that.
        self.bin = self.folder / "bin"
        self.prompts = self.folder / "prompts"
        self.responses = self.folder / "responses"
        for folder in (self.bin, self.prompts, self.responses):
            folder.mkdir()
        copilot = self.bin / "copilot"
        copilot.write_text('#!/usr/bin/env bash\nn=$(( $(ls "$TEST_PROMPTS" | wc -l) + 1 ))\ncat > "$TEST_PROMPTS/$n.txt"\n'
                           'last=$(ls "$TEST_RESPONSES" | sort -n | tail -1)\n'
                           'cat "$TEST_RESPONSES/$n.json" 2>/dev/null || cat "$TEST_RESPONSES/$last"\n', newline="\n")
        copilot.chmod(0o755)
        self.data = {"releases": [{"statusName": "Wait for RN - Omnia 7.11.99", "issues": [
            {"repositoryWithOwner": "omniaintranet/test", "number": 1, "body": "", "comments": []}]}]}

    def answer(self, *texts, bullet=0):
        for n, text in enumerate(texts, 1):
            (self.responses / f"{n}.json").write_text(json.dumps({"bullets": [{"bullet": bullet, "text": text}]}))

    def review(self, bullet):
        """bullet: one bullet's text, or (the generated lines below the heading, the audit's bullets)."""
        lines, bullets = (f"{bullet}\n", [{"text": bullet}]) if isinstance(bullet, str) else bullet
        (self.folder / "generated-release-notes.rst").write_text(HEADING + lines, newline="\n")
        (self.folder / "release-notes-audit.json").write_text(json.dumps({"bullets": [
            dict(b, sourceIssues=[{"repositoryWithOwner": "omniaintranet/test", "number": 1}]) for b in bullets],
            "omittedIssues": [], "pendingReviewIssues": []}))
        (self.folder / "release-issues.json").write_text(json.dumps(self.data))
        script = (SCRIPTS / "review-release-notes.sh").read_text(encoding="utf-8")
        for name in ("generated-release-notes.rst", "docs-review-release-notes", "release-notes-audit.json", "release-issues.json"):
            script = script.replace("/tmp/" + name, shell_path(self.folder / name))
        path = self.folder / "review-release-notes.sh"
        path.write_text(script, encoding="utf-8", newline="\n")
        env = dict(os.environ, PYTHON=shell_path(sys.executable), RELEASE_NOTES_FILE=self.NOTES,
                   GITHUB_OUTPUT=shell_path(self.folder / "outputs"), VALE_BIN=VALE, GITLEAKS_BIN=GITLEAKS,
                   TEST_PROMPTS=shell_path(self.prompts), TEST_RESPONSES=shell_path(self.responses))
        env.pop("GITHUB_STEP_SUMMARY", None)
        result = subprocess.run([BASH, "-c", f'export PATH="{shell_path(self.bin)}:{shell_path(Path(BASH).parent)}:$PATH"; '
                                             f'bash "{shell_path(path)}"'],
                                cwd=self.repo, env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((self.repo / self.NOTES).read_text(), self.PUBLISHED, "the release-notes file must be restored")
        review = self.folder / "docs-review-release-notes"
        self.output = result.stdout + result.stderr
        self.notes = (self.folder / "generated-release-notes.rst").read_text()
        self.audit = json.loads((self.folder / "release-notes-audit.json").read_text())
        self.calls = sorted(self.prompts.iterdir(), key=lambda p: int(p.stem))
        return (json.loads((review / "findings.json").read_text()), (review / "summary.md").read_text(encoding="utf-8"),
                (self.folder / "outputs").read_text())

    def test_sales_language_is_given_back_and_reworded(self):
        self.answer(self.FIXED)
        findings, summary, outputs = self.review(self.SALES)
        self.assertEqual(findings, [])
        self.assertEqual(len(self.calls), 1)
        prompt = self.calls[0].read_text()
        self.assertIn("'key selling point' is internal or sales language", prompt)
        self.assertIn("DOCUMENTATION REVIEW RULES", prompt)
        self.assertIn(self.SALES, prompt)
        self.assertIn(self.FIXED, self.notes)
        self.assertEqual(self.audit["bullets"][0]["text"], self.FIXED)
        self.assertIn("nothing blocks the generated release notes", summary)
        self.assertIn("Reworded after the review (1)", summary)
        self.assertIn(f"| {self.SALES} | {self.FIXED} |", summary)
        self.assertIn("errors=0", outputs)

    def test_flagged_bullet_in_a_grouped_release_is_reworded(self):
        # Audit order: five Search bullets, then the flagged Page Rollup bullet (index 5) and five more.
        search = [f"- Quick Search now shows result type {n} in the filter panel" for n in range(5)]
        rollup = [f"- Page Rollup now shows column {n} in the list view" for n in range(5)]
        bullets = ([{"text": t, "category": "Search"} for t in search] + [{"text": self.SALES, "category": "Page Rollup"}]
                   + [{"text": t, "category": "Page Rollup"} for t in rollup])

        def grouped(flagged):
            return "**Page Rollup**\n\n" + "".join(f"{t}\n" for t in [flagged] + rollup) + "\n**Search**\n\n" + "".join(f"{t}\n" for t in search)

        self.answer(self.FIXED, bullet=5)
        findings, summary, outputs = self.review((grouped(self.SALES), bullets))
        self.assertEqual(findings, [])
        self.assertEqual(len(self.calls), 1)
        self.assertIn('"bullet":5', self.calls[0].read_text())
        self.assertEqual(self.notes, HEADING + grouped(self.FIXED))
        self.assertEqual(self.audit["bullets"][5], dict(bullets[5], text=self.FIXED, sourceIssues=[
            {"repositoryWithOwner": "omniaintranet/test", "number": 1}]))
        self.assertIn("errors=0", outputs)

    def test_findings_left_after_the_repair_rounds_are_reported(self):
        self.answer("- Quick Search handles document filters, a key selling point",
                    "- Quick Search handles filters, a key selling point")
        findings, summary, outputs = self.review(self.SALES)
        self.assertEqual(len(self.calls), 2)
        self.assertEqual([(f["file"], f["line"], f["rule"], f["severity"]) for f in findings],
                         [(self.NOTES, 5, "Omnia.InternalLanguage", "error")])
        self.assertIn("must be fixed before publishing the generated release notes", summary)
        self.assertIn("Reworded after the review (2)", summary)
        self.assertIn("errors=1", outputs)

    def test_unchanged_answer_ends_the_repair(self):
        self.answer(self.SALES)
        findings, summary, outputs = self.review(self.SALES)
        self.assertEqual(len(self.calls), 1)
        self.assertIn("no usable rewording", self.output)
        self.assertNotIn("Reworded after the review", summary)
        self.assertIn("errors=1", outputs)

    def test_rewrite_must_keep_its_customer_references(self):
        self.data["releases"][0]["issues"][0]["body"] = "https://support.example/agent/tickets/59036"
        self.answer(self.FIXED)
        findings, summary, outputs = self.review(self.SALES + " (#59036)")
        self.assertIn(self.SALES + " (#59036)", self.notes)
        self.assertIn("no usable rewording", self.output)
        self.assertIn("errors=1", outputs)

    def test_rewrite_must_pass_the_release_note_validator(self):
        self.answer(self.FIXED + " (see https://private.example/card)")
        findings, summary, outputs = self.review(self.SALES)
        self.assertIn(self.SALES, self.notes)
        self.assertEqual(self.audit["bullets"][0]["text"], self.SALES)
        self.assertIn("failed validation; keeping the previous text", self.output)
        self.assertIn("errors=1", outputs)

    def test_confidential_data_is_never_sent_for_rewording(self):
        self.answer(self.FIXED)
        bullet = self.SALES + " for tenant contoso-hr.sharepoint.de.example.omniacloud.net"
        findings, summary, outputs = self.review(bullet)
        self.assertEqual(self.calls, [])
        self.assertIn("Confidentiality findings: no rewording", self.output)
        self.assertIn(bullet, self.notes)
        self.assertNotIn("Reworded after the review", summary)
        self.assertEqual(sorted(f["rule"] for f in findings), ["Confidential.TenantHost", "Omnia.InternalLanguage"])

    def test_broken_inline_reference_is_reported(self):
        # The validator accepts inline roles; only the Sphinx build comparison finds the missing page.
        findings, summary, outputs = self.review("- See :doc:`missing-page` for details")
        self.assertEqual([(f["file"], f["line"], f["rule"], f["severity"]) for f in findings],
                         [(self.NOTES, 5, "Build.BrokenReference", "error")])
        self.assertEqual(self.calls, [], "build findings are not reworded")
        self.assertIn("errors=1", outputs)

    def test_clean_generated_notes_pass(self):
        findings, summary, outputs = self.review(self.FIXED)
        self.assertEqual(findings, [])
        self.assertEqual(self.calls, [])
        self.assertIn("nothing blocks the generated release notes", summary)
        self.assertIn("errors=0", outputs)


if __name__ == "__main__":
    if not BASH or not JQ:
        raise SystemExit("Install bash and jq, or set BASH_PATH and JQ_PATH, before running these checks.")
    unittest.main()
