"""Offline tests for approval-to-Prod synchronization; no GitHub mutations."""
import base64
from copy import deepcopy
import importlib.util
from pathlib import Path
import unittest
import sys
sys.dont_write_bytecode = True
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("approval_sync", Path(__file__).with_name("sync-approved-release-notes.py"))
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

SECTION = "7.11.99\n========================================\n(Omnia 7.11.99 / WCM 7.11.99)\n\n- Final reviewer-edited release note (#59036)"
GENERATED = "7.11.99\n========================================\n(Omnia 7.11.99 / WCM 7.11.99)\n\n- Generated release note (#59036)"
PR_URL = "https://github.com/omniaintranet/OmniaDocsG2/pull/99"
DENIED = "gh: Resource not accessible by personal access token"


def draft_body(notes=GENERATED, *, extra="", markers=False):
    """The notification body as create-ready-project-item.sh writes it (markers: as it does since they exist)."""
    body = ("> [!WARNING]\n> **DRAFT - NOT APPROVED.** These release notes were generated automatically and must be "
            "reviewed before publication.\n\n"
            "Generated from **2** source issues: **1** represented in **1** draft bullets, **0** omitted, and **1** "
            "pending manual security review.\n\n"
            f"[Review the documentation pull request]({PR_URL}).\n\n"
            f"## Generated draft release notes\n\n```text\n{notes}\n```\n\n"
            "## Issues not included in the draft\n\n- None. No issues were finally omitted.\n\n"
            "## Security-sensitive issues pending manual review\n\n"
            "- [omniaintranet/OmniaMono#60001](https://github.com/omniaintranet/OmniaMono/issues/60001) - Needs review\n\n"
            "  Suggested release note (pending approval):\n\n  > - Improved security validation of URLs\n" + extra)
    return f"{sync.GENERATED_START}\n{body}\n{sync.GENERATED_END}\n" if markers else body


def fixtures():
    pr = {"head": {"ref": "hotfix-release-notes-7.11.99", "sha": "head123", "repo": {"full_name": sync.REPOSITORY}},
          "base": {"ref": "master"}, "merged": False, "state": "open", "draft": False,
          "user": {"login": "author"}, "html_url": "https://github.com/omniaintranet/OmniaDocsG2/pull/99",
          "merge_commit_sha": "merge123"}
    review = {"user": {"login": "reviewer"}, "state": "APPROVED", "commit_id": "head123",
              "author_association": "MEMBER", "submitted_at": "2026-10-16T09:00:00Z"}
    options = [{"id": "unrelated", "name": "Investigation", "color": "BLUE", "description": "Keep this"},
               {"id": "release", "name": "Wait for RN - Omnia 7.11.99 / WCM 7.11.99", "color": "GRAY", "description": "Keep this too"}]
    project = {"fields": {"nodes": [{"id": "field", "name": "Status", "options": options}]}}
    items = [{"id": "item", "status": {"optionId": "release"}, "content": {"__typename": "DraftIssue", "id": "draft",
              "title": "Release notes for Omnia 7.11.99 are now ready",
              "body": draft_body()}}]
    return pr, review, project, items


class ApprovalTests(unittest.TestCase):
    def setUp(self):
        self.pr, self.review, self.project, self.items = fixtures()

    def test_current_member_approval(self):
        self.assertTrue(sync.is_approved(self.pr, [self.review]))

    def test_old_commit_approval_is_not_enough(self):
        self.review["commit_id"] = "old-head"
        self.assertFalse(sync.is_approved(self.pr, [self.review]))

    def test_changes_requested_blocks_approval(self):
        other = dict(self.review, user={"login": "another"}, state="CHANGES_REQUESTED")
        self.assertFalse(sync.is_approved(self.pr, [self.review, other]))

    def test_dismissed_approval_is_not_enough(self):
        dismissed = dict(self.review, state="DISMISSED", submitted_at="2026-10-16T10:00:00Z")
        self.assertFalse(sync.is_approved(self.pr, [self.review, dismissed]))

    def test_comment_does_not_discard_approval(self):
        comment = dict(self.review, state="COMMENTED", submitted_at="2026-10-16T10:00:00Z")
        self.assertTrue(sync.is_approved(self.pr, [self.review, comment]))

    def test_untrusted_or_self_approval_is_not_enough(self):
        for changes in ({"author_association": "NONE"}, {"user": {"login": "author"}}):
            with self.subTest(changes=changes):
                self.assertFalse(sync.is_approved(self.pr, [dict(self.review, **changes)]))

    def test_draft_and_closed_unmerged_are_not_approved(self):
        for changes in ({"draft": True}, {"state": "closed"}):
            with self.subTest(changes=changes):
                self.assertFalse(sync.is_approved(dict(self.pr, **changes), [self.review]))

    def test_merged_pr_uses_final_state(self):
        self.assertTrue(sync.is_approved(dict(self.pr, merged=True, state="closed"), []))

    def test_unrelated_or_fork_pr_is_rejected(self):
        for head in (dict(self.pr["head"], ref="codex/unrelated"),
                     dict(self.pr["head"], repo={"full_name": "someone/fork"})):
            with self.subTest(head=head):
                with self.assertRaises(ValueError):
                    sync.release_version(dict(self.pr, head=head))

    def test_only_matching_final_section_is_extracted(self):
        text = "7.12.0\n========\n(Omnia 7.12.0)\n\n- Newer\n\n" + SECTION + "\n\n7.11.98\n========\n(Omnia 7.11.98)\n\n- Older"
        self.assertEqual(sync.extract_release(text, "7.11.99"), SECTION)

    def test_grouped_section_is_extracted_whole(self):
        grouped = ("7.11.99\n========================================\n(Omnia 7.11.99 / WCM 7.11.99)\n\n"
                   "**Page Rollup**\n\n- Page Rollup note (#59036)\n\n**Search**\n\n- Search note")
        text = grouped + "\n\n7.11.98\n========\n(Omnia 7.11.98)\n\n- Older"
        self.assertEqual(sync.extract_release(text, "7.11.99"), grouped)

    def test_missing_duplicate_or_empty_release_is_rejected(self):
        for text in ("Unrelated", SECTION + "\n\n" + SECTION, SECTION.split("- Final")[0]):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    sync.extract_release(text, "7.11.99")

    def test_plan_preserves_option_ids_other_columns_and_metadata(self):
        original = deepcopy(self.project)
        plan = sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)
        self.assertEqual(self.project, original)
        self.assertEqual(plan["options"][0], original["fields"]["nodes"][0]["options"][0])
        self.assertEqual(plan["options"][1], dict(original["fields"]["nodes"][0]["options"][1],
            name="Approved - Omnia 7.11.99 / WCM 7.11.99"))
        self.assertTrue(plan["rename"])
        self.assertTrue(plan["convert"])
        self.assertIn(SECTION, plan["body"])
        self.assertLess(plan["body"].index(SECTION), plan["body"].index("## Generated draft (recommendation)"))
        self.assertNotIn("DRAFT - NOT APPROVED", plan["body"].split("## Generated draft (recommendation)")[0])
        self.assertIn("publication still requires merging", plan["body"])
        self.assertEqual(plan["title"], "Release notes for Omnia 7.11.99 are approved")

    def test_already_approved_column_is_not_renamed(self):
        self.project["fields"]["nodes"][0]["options"][1]["name"] = "Approved - Omnia 7.11.99 / WCM 7.11.99"
        plan = sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)
        self.assertFalse(plan["rename"])

    def test_missing_duplicate_or_unlinked_notification_is_rejected(self):
        for items in ([], self.items * 2, [dict(self.items[0], content=dict(self.items[0]["content"], body="Different PR"))]):
            with self.subTest(items=items):
                with self.assertRaises(ValueError):
                    sync.plan_update(self.project, items, self.pr, "7.11.99", SECTION)

    def converted(self, repository="omniaintranet/OmniaMono"):
        self.items[0]["content"].update(__typename="Issue", id="issue", repository={"nameWithOwner": repository})

    def test_converted_issue_is_updated_without_converting_again(self):
        self.converted()
        plan = sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)
        self.assertFalse(plan["convert"])

    def test_issue_outside_omniamono_or_other_content_is_rejected(self):
        for content in ({"__typename": "Issue", "repository": {"nameWithOwner": "omniaintranet/OmniaDocsG2"}},
                        {"__typename": "PullRequest"}):
            with self.subTest(content=content):
                self.items[0]["content"].update(content)
                with self.assertRaises(ValueError):
                    sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)

    def test_wrong_release_column_is_rejected(self):
        self.project["fields"]["nodes"][0]["options"][1]["name"] = "Wait for RN - Omnia 7.11.98"
        with self.assertRaises(ValueError):
            sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)

    def test_waiting_for_rn_name_variants_are_renamed_to_approved(self):
        for name in ("Waiting for RN - Omnia 7.11.99 / WCM 7.11.99", "waiting for rn - Omnia 7.11.99 / WCM 7.11.99",
                     "Awaiting release notes - Omnia 7.11.99 / WCM 7.11.99", "Wait-for-RN - Omnia 7.11.99 / WCM 7.11.99",
                     "\u23f3 Waiting for RN - Omnia 7.11.99 / WCM 7.11.99", "[Wait for RN] Omnia 7.11.99 / WCM 7.11.99",
                     "Wait for RN: Omnia 7.11.99 / WCM 7.11.99", "Wait for RN / Omnia 7.11.99 / WCM 7.11.99",
                     "Wait for RN Omnia 7.11.99 / WCM 7.11.99"):
            with self.subTest(name=name):
                self.project["fields"]["nodes"][0]["options"][1]["name"] = name
                plan = sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)
                self.assertTrue(plan["rename"])
                self.assertEqual(plan["status"], "Approved - Omnia 7.11.99 / WCM 7.11.99")

    def test_unrelated_waiting_column_is_rejected(self):
        for name in ("Waiting for QA - Omnia 7.11.99", "Ready - Omnia 7.11.99", "Wait for RNA - Omnia 7.11.99"):
            with self.subTest(name=name):
                self.project["fields"]["nodes"][0]["options"][1]["name"] = name
                with self.assertRaises(ValueError):
                    sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)

    def test_separate_approved_column_is_not_overwritten(self):
        options = self.project["fields"]["nodes"][0]["options"]
        options.append(dict(options[1], id="duplicate", name="Approved - Omnia 7.11.99 / WCM 7.11.99"))
        with self.assertRaises(ValueError):
            sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)

    def exercise_sync(self, *, merged=False, change_head=False, approved=True, dry_run=False, withdraw=False, close_pr=False,
                      fail=None, repeat=True):
        """fail: a mutation name whose call raises gh's permission error (the call is still recorded)."""
        self.pr["merged"] = merged
        calls = []
        reads = []
        pulls = 0
        review_reads = 0

        def api(endpoint, *, query=None, variables=None, project=False):
            nonlocal pulls, review_reads
            reads.append(endpoint)
            if query and query.startswith("mutation"):
                calls.append((query, variables))
                if fail and fail in query:
                    raise sync.GitHubError(DENIED)
                if "updateProjectV2DraftIssue" in query or "updateIssue" in query:
                    self.items[0]["content"].update(title=variables["title"], body=variables["body"])
                elif "convertProjectV2DraftIssueItemToIssue" in query:
                    self.converted()
                else:
                    self.project["fields"]["nodes"][0]["options"] = deepcopy(variables["options"])
                return {}
            if query and "repository(" in query:
                reads.append(variables)
                return {"data": {"repository": {"id": "repo-omniamono"}}}
            if "/reviews?" in endpoint:
                review_reads += 1
                return [self.review] if approved and not (withdraw and review_reads > 1) else []
            if "/commits?" in endpoint:
                return [{"sha": "first123"}, {"sha": "head123"}]
            if "/contents/" in endpoint:
                notes = GENERATED if "ref=first123" in endpoint else SECTION
                return {"content": base64.b64encode((notes + "\n").encode()).decode()}
            pulls += 1
            result = deepcopy(self.pr)
            if change_head and pulls > 1:
                result["head"]["sha"] = "changed"
            if close_pr and pulls > 1:
                result["state"] = "closed"
            return result

        with patch.object(sync, "api", side_effect=api), patch.object(sync, "load_project", return_value=(self.project, self.items)):
            if change_head:
                with self.assertRaises(ValueError):
                    sync.sync("99")
            elif fail:
                with self.assertRaises(sync.SyncIncomplete) as failure:
                    sync.sync("99")
                return reads, calls, failure.exception
            else:
                sync.sync("99", dry_run=dry_run)
                if repeat and not dry_run and approved and not withdraw and not close_pr:
                    first_writes = len(calls)
                    sync.sync("99")
                    self.assertEqual(len(calls), first_writes, "Repeating synchronization must not rewrite the item or field")
        return reads, calls

    def test_approved_sync_updates_item_renames_column_and_converts_once(self):
        reads, calls = self.exercise_sync()
        self.assertEqual([next(m for m in ("updateProjectV2DraftIssue", "updateProjectV2Field", "convertProjectV2")
                               if m in query) for query, _ in calls],
                         ["updateProjectV2DraftIssue", "updateProjectV2Field", "convertProjectV2"],
                         "The draft must leave the Wait for RN column before it becomes an issue")
        self.assertEqual(calls[2][1], {"item": "item", "repository": "repo-omniamono"})
        self.assertIn({"owner": "omniaintranet", "name": "OmniaMono"}, reads)
        self.assertTrue(any("ref=head123" in endpoint for endpoint in reads))

    def test_merge_after_conversion_updates_the_issue(self):
        self.converted()
        self.project["fields"]["nodes"][0]["options"][1]["name"] = "Approved - Omnia 7.11.99 / WCM 7.11.99"
        _, calls = self.exercise_sync(merged=True)
        self.assertEqual(len(calls), 1)
        self.assertIn("updateIssue", calls[0][0])
        self.assertEqual(calls[0][1]["id"], "issue")
        self.assertIn("APPROVED AND MERGED", calls[0][1]["body"])

    def test_merge_sync_reads_merged_content(self):
        reads, calls = self.exercise_sync(merged=True)
        self.assertEqual(len(calls), 3)
        self.assertTrue(any("ref=merge123" in endpoint for endpoint in reads))
        self.assertIn("APPROVED AND MERGED", calls[0][1]["body"])

    def test_changed_pr_is_not_written(self):
        _, calls = self.exercise_sync(change_head=True)
        self.assertEqual(calls, [])

    def test_approval_withdrawn_during_sync_makes_no_mutations(self):
        _, calls = self.exercise_sync(withdraw=True)
        self.assertEqual(calls, [])

    def test_pr_closed_during_sync_makes_no_mutations(self):
        _, calls = self.exercise_sync(close_pr=True)
        self.assertEqual(calls, [])

    def test_no_approval_and_dry_run_make_no_mutations(self):
        for changes in ({"approved": False}, {"dry_run": True}):
            with self.subTest(changes=changes):
                _, calls = self.exercise_sync(**changes)
                self.assertEqual(calls, [])


class KeptDraftTests(unittest.TestCase):
    def setUp(self):
        self.pr, _, self.project, self.items = fixtures()

    def plan(self, **kwargs):
        return sync.plan_update(deepcopy(self.project), self.items, self.pr, "7.11.99", SECTION, **kwargs)

    def kept_section(self, body):
        approved, marker, draft = body.partition("## Generated draft (recommendation)")
        self.assertTrue(marker, "The body has no kept-draft section")
        return approved, draft

    def test_draft_is_kept_whole_below_the_approved_notes(self):
        plan = self.plan()
        approved, draft = self.kept_section(plan["body"])
        self.assertIn(SECTION, approved)
        self.assertNotIn(GENERATED, approved)
        self.assertIn(GENERATED, draft)
        # Christian, 2026-11-03: the security-review section stays as it is, with its suggested wording.
        self.assertIn("### Security-sensitive issues pending manual review", draft)
        self.assertIn("> - Improved security validation of URLs", draft)
        self.assertIn("### Issues not included in the draft", draft)
        self.assertIn("### Generated draft release notes", draft)
        self.assertNotIn("\n## ", draft, "The draft's headings sit one level below the kept-draft heading")
        self.assertEqual(plan["draft_source"], "kept from the notification")

    def test_repeated_sync_neither_nests_nor_duplicates_the_draft(self):
        body = self.plan()["body"]
        for merged in (False, True):
            self.items[0]["content"].update(body=body, title="Release notes for Omnia 7.11.99 are approved")
            self.pr["merged"] = merged
            again = self.plan()["body"]
            if not merged:
                self.assertEqual(again, body)
            for marker in (sync.DRAFT_START, sync.DRAFT_END, "## Generated draft (recommendation)", GENERATED):
                self.assertEqual(again.count(marker), 1, marker)
            self.assertEqual(self.kept_section(again)[1], self.kept_section(body)[1])
            body = again
        self.assertIn("APPROVED AND MERGED", body)

    def test_converted_issue_keeps_its_draft_section(self):
        body = self.plan()["body"]
        self.items[0]["content"].update(__typename="Issue", id="issue", body=body,
                                        repository={"nameWithOwner": "omniaintranet/OmniaMono"})
        self.pr["merged"] = True
        plan = self.plan()
        self.assertFalse(plan["convert"])
        self.assertEqual(self.kept_section(plan["body"])[1], self.kept_section(body)[1])

    def test_replaced_body_recovers_the_draft_from_the_pr(self):
        # 7.12.9: an older sync had already replaced the draft with the approved notes.
        self.items[0]["content"]["body"] = sync.approval_body(dict(self.pr, merged=True), SECTION)
        plan = self.plan(recover_draft=lambda: "Recovered draft")
        self.assertIn("Recovered draft", self.kept_section(plan["body"])[1])
        self.assertEqual(plan["draft_source"], "recovered from the documentation PR's first commit")
        self.assertNotIn("Generated draft (recommendation)", self.plan()["body"])

    def test_draft_from_pr_reads_the_first_commit(self):
        reads = []

        def api(endpoint, **_):
            reads.append(endpoint)
            if "/commits?" in endpoint:
                return [{"sha": "first123"}, {"sha": "fixup456"}]
            return {"content": base64.b64encode(("Intro\n\n" + GENERATED + "\n").encode()).decode()}

        with patch.object(sync, "api", side_effect=api):
            draft = sync.draft_from_pr("repos/x/pulls/99", "7.11.99")
        self.assertIn("ref=first123", reads[1])
        self.assertIn(f"```text\n{GENERATED}\n```", draft)
        self.assertIn(f"https://github.com/{sync.REPOSITORY}/commit/first123", draft)
        self.assertIn("not available", draft)

    def test_generator_markers_keep_the_whole_draft(self):
        # The markers, not the heading text, decide: a draft whose headings were edited is still kept whole.
        body = draft_body(markers=True).replace("## Generated draft release notes", "## Draft notes")
        self.items[0]["content"]["body"] = body
        _, draft = self.kept_section(self.plan()["body"])
        for part in ("### Draft notes", GENERATED, "### Issues not included in the draft",
                     "### Security-sensitive issues pending manual review", "Needs review",
                     "> - Improved security validation of URLs"):
            self.assertIn(part, draft)
        self.assertNotIn(sync.GENERATED_START, draft)
        self.assertNotIn(sync.GENERATED_END, draft)

    def test_long_notes_are_left_out_before_the_issue_lists(self):
        notes = GENERATED + "".join(f"\n- Generated bullet {n} " + "x" * 200 for n in range(400))
        self.items[0]["content"]["body"] = draft_body(notes, markers=True)
        body = self.plan()["body"]
        self.assertLessEqual(len(body), sync.MAX_BODY)
        self.assertIn(SECTION, body)
        _, draft = self.kept_section(body)
        self.assertEqual(draft.count(sync.NOTES_CUT), 1)
        self.assertNotIn("Generated bullet", draft)
        self.assertNotIn(sync.DRAFT_CUT, draft)
        for part in ("### Issues not included in the draft", "### Security-sensitive issues pending manual review",
                     "Needs review", "> - Improved security validation of URLs"):
            self.assertIn(part, draft)
        self.assertEqual(body.count("```") % 2, 0, "Every code fence is closed")
        self.items[0]["content"]["body"] = body
        self.assertEqual(self.plan()["body"], body, "A shortened draft is stable on the next sync")

    def long_lists(self):
        return "".join(f"\n- [omniaintranet/OmniaMono#{n}](https://github.com/omniaintranet/OmniaMono/issues/{n}) - "
                       + "Needs review " * 20 for n in range(70000, 70300))

    def test_long_lists_are_cut_within_the_body_limit(self):
        self.items[0]["content"]["body"] = draft_body(extra=self.long_lists())
        body = self.plan()["body"]
        self.assertLessEqual(len(body), sync.MAX_BODY)
        self.assertIn(SECTION, body)
        self.assertEqual(body.count(sync.NOTES_CUT), 1, "The notes go first")
        self.assertEqual(body.count(sync.DRAFT_CUT), 1)
        self.assertEqual(body.count("```") % 2, 0, "Every code fence is closed")
        self.assertTrue(body.endswith(sync.DRAFT_END + "\n"))
        self.items[0]["content"]["body"] = body
        self.assertEqual(self.plan()["body"], body, "A cut draft is stable on the next sync")

    def test_cut_draft_is_cut_again_without_a_second_note(self):
        self.items[0]["content"]["body"] = draft_body(extra=self.long_lists())
        self.items[0]["content"]["body"] = self.plan()["body"]
        longer = SECTION + "".join(f"\n- Approved bullet {n} " + "y" * 200 for n in range(50))
        body = sync.plan_update(deepcopy(self.project), self.items, self.pr, "7.11.99", longer)["body"]
        self.assertLessEqual(len(body), sync.MAX_BODY)
        self.assertEqual(body.count(sync.DRAFT_CUT), 1)

    def test_oversized_approved_notes_are_rejected(self):
        huge = SECTION + "\n- " + "z" * sync.MAX_BODY
        with self.assertRaises(ValueError):
            sync.plan_update(deepcopy(self.project), self.items, self.pr, "7.11.99", huge)


class FailureTests(unittest.TestCase):
    """Readable failures that say what is done, and a safe re-run."""
    setUp = ApprovalTests.setUp
    exercise_sync = ApprovalTests.exercise_sync
    converted = ApprovalTests.converted

    def test_denied_conversion_names_the_permission_and_what_is_pending(self):
        _, calls, failure = self.exercise_sync(fail="convertProjectV2")
        self.assertEqual(len(calls), 3, "Notes and column are written before the conversion is tried")
        self.assertIn(sync.TOKEN_SECRET, str(failure))
        self.assertIn("Issues: Read and write on omniaintranet/OmniaMono", str(failure))
        self.assertIn(DENIED, str(failure))
        self.assertIn("Up to date in Project 8: the approved release notes", failure.summary)
        self.assertIn("the release column `Approved - Omnia 7.11.99 / WCM 7.11.99`", failure.summary)
        self.assertIn("Still pending: the conversion to an omniaintranet/OmniaMono issue", failure.summary)
        self.assertIn("`pr_number` 99", failure.summary)
        _, calls = self.exercise_sync(repeat=False)
        self.assertEqual([("convertProjectV2" in query) for query, _ in calls], [True],
                         "A re-run after the token fix only converts")

    def test_denied_issue_update_names_the_permission(self):
        self.converted()
        self.project["fields"]["nodes"][0]["options"][1]["name"] = "Approved - Omnia 7.11.99 / WCM 7.11.99"
        _, _, failure = self.exercise_sync(merged=True, fail="updateIssue")
        self.assertIn(sync.ISSUE_ACCESS, str(failure))
        self.assertIn("Nothing was changed in Project 8.", failure.summary)

    def test_denied_column_rename_does_not_blame_issue_access(self):
        _, calls, failure = self.exercise_sync(fail="updateProjectV2Field")
        self.assertNotIn(sync.ISSUE_ACCESS, str(failure))
        self.assertIn("Still pending: the release column", failure.summary)
        self.assertNotIn("convertProjectV2", "".join(query for query, _ in calls))

    def test_gh_error_text_replaces_the_traceback(self):
        failed = sync.subprocess.CompletedProcess([], 1, stdout="", stderr=DENIED + "\n")
        with patch.object(sync.subprocess, "run", return_value=failed):
            with self.assertRaises(sync.GitHubError) as error:
                sync.api("graphql", query="mutation { x }")
        self.assertEqual(str(error.exception), DENIED)

    def test_summary_and_annotation(self):
        import os
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "summary.md"
            with patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(path)}):
                sync.write_summary("First")
                sync.write_summary("Second\n")
            self.assertEqual(path.read_text(encoding="utf-8"), "First\n\nSecond\n\n")
        with patch("builtins.print") as printed:
            sync.annotate("100% done\nnext")
        printed.assert_called_once_with("::error::100%25 done%0Anext")


if __name__ == "__main__":
    unittest.main()
