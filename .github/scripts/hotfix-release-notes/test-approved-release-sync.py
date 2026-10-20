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
    items = [{"id": "item", "status": {"optionId": "release"}, "content": {"id": "draft",
              "title": "Release notes for Omnia 7.11.99 are now ready",
              "body": "Stale draft with pending wording\n[PR](" + pr["html_url"] + ")"}}]
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
        self.assertIn(SECTION, plan["body"])
        self.assertNotIn("Stale draft", plan["body"])
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

    def exercise_sync(self, *, merged=False, change_head=False, approved=True, dry_run=False, withdraw=False, close_pr=False):
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
                if "updateProjectV2DraftIssue" in query:
                    self.items[0]["content"].update(title=variables["title"], body=variables["body"])
                else:
                    self.project["fields"]["nodes"][0]["options"] = deepcopy(variables["options"])
                return {}
            if "/reviews?" in endpoint:
                review_reads += 1
                return [self.review] if approved and not (withdraw and review_reads > 1) else []
            if "/contents/" in endpoint:
                return {"content": base64.b64encode((SECTION + "\n").encode()).decode()}
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
            else:
                sync.sync("99", dry_run=dry_run)
                if not dry_run and approved and not withdraw and not close_pr:
                    first_writes = len(calls)
                    sync.sync("99")
                    self.assertEqual(len(calls), first_writes, "Repeating synchronization must not rewrite the item or field")
        return reads, calls

    def test_approved_sync_updates_item_and_renames_column_once(self):
        reads, calls = self.exercise_sync()
        self.assertEqual(len(calls), 2)
        self.assertTrue(any("ref=head123" in endpoint for endpoint in reads))

    def test_merge_sync_reads_merged_content(self):
        reads, calls = self.exercise_sync(merged=True)
        self.assertEqual(len(calls), 2)
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


if __name__ == "__main__":
    unittest.main()
