"""Offline tests for approval-to-Prod synchronization and the release closeout; GitHub is faked, nothing is written."""
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
GENERATED = ("7.11.99\n========================================\n(Omnia 7.11.99 / WCM 7.11.99)\n\n"
             "- Generated release note (#59036)\n- General performance and security improvements")
PR_URL = "https://github.com/omniaintranet/OmniaDocsG2/pull/99"
DENIED = "gh: Resource not accessible by personal access token"


def draft_body(notes=GENERATED, *, extra="", markers=False):
    """The notification body as create-ready-project-item.sh writes it (markers: as it does since they exist)."""
    body = ("> [!WARNING]\n> **DRAFT - NOT APPROVED.** These release notes were generated automatically and must be "
            "reviewed before publication.\n\n"
            "Generated from **2** source issues: **1** represented in **2** draft bullets, **0** omitted, and **1** "
            "pending manual security review.\n\n"
            f"[Review the documentation pull request]({PR_URL}).\n\n"
            f"## Generated draft release notes\n\n```text\n{notes}\n```\n\n"
            "## Issues not included in the draft\n\n- None. No issues were finally omitted.\n\n"
            "## Security-sensitive issues pending manual review\n\n"
            "These issues are held outside the public draft. The draft covers them with one general bullet, "
            "\"General performance and security improvements\"; no per-issue release note is published for them. "
            "Review whether that is enough for each issue, or whether an issue needs its own wording, under the "
            "applicable disclosure policy.\n\n"
            "- [omniaintranet/OmniaMono#60001](https://github.com/omniaintranet/OmniaMono/issues/60001) - Needs review" + extra)
    return f"{sync.GENERATED_START}\n{body}\n{sync.GENERATED_END}\n" if markers else body


def fixtures():
    pr = {"head": {"ref": "hotfix-release-notes-7.11.99", "sha": "head123", "repo": {"full_name": sync.REPOSITORY}},
          "base": {"ref": "master"}, "merged": False, "state": "open", "draft": False,
          "user": {"login": "author"}, "html_url": "https://github.com/omniaintranet/OmniaDocsG2/pull/99",
          "merge_commit_sha": "merge123"}
    review = {"user": {"login": "reviewer"}, "state": "APPROVED", "commit_id": "head123",
              "author_association": "MEMBER", "submitted_at": "2026-10-16T09:00:00Z"}
    options = [{"id": "unrelated", "name": "Investigation"},
               {"id": "release", "name": "Wait for RN - Omnia 7.11.99 / WCM 7.11.99"},
               {"id": "released", "name": "Released"}]
    project = {"id": "project", "fields": {"nodes": [{"id": "field", "name": "Status", "options": options}]}}
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

    def test_plan_moves_the_notification_to_released_without_touching_the_field(self):
        original = deepcopy(self.project)
        plan = sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)
        self.assertEqual(self.project, original)
        self.assertNotIn("options", plan, "The plan never carries Status options to resend")
        self.assertEqual(plan["released_id"], "released")
        self.assertEqual(plan["column"], "Wait for RN - Omnia 7.11.99 / WCM 7.11.99")
        self.assertTrue(plan["move"])
        self.assertTrue(plan["convert"])
        self.assertEqual(plan["closeout"]["title"], "Release Omnia 7.11.99")
        self.assertIn(SECTION, plan["body"])
        self.assertLess(plan["body"].index(SECTION), plan["body"].index("## Generated draft (recommendation)"))
        self.assertNotIn("DRAFT - NOT APPROVED", plan["body"].split("## Generated draft (recommendation)")[0])
        self.assertIn("publication still requires merging", plan["body"])
        self.assertEqual(plan["title"], "Release notes for Omnia 7.11.99 are approved")

    def test_legacy_approved_column_is_still_recognised(self):
        self.options()[1]["name"] = "Approved - Omnia 7.11.99 / WCM 7.11.99"
        plan = sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)
        self.assertEqual(plan["closeout"]["title"], "Release Omnia 7.11.99")

    def test_missing_duplicate_or_unlinked_notification_is_rejected(self):
        for items in ([], self.items * 2, [dict(self.items[0], content=dict(self.items[0]["content"], body="Different PR"))]):
            with self.subTest(items=items):
                with self.assertRaises(ValueError):
                    sync.plan_update(self.project, items, self.pr, "7.11.99", SECTION)

    def options(self):
        return self.project["fields"]["nodes"][0]["options"]

    def converted(self, repository="omniaintranet/OmniaMono"):
        self.items[0]["content"].update(__typename="Issue", id="issue", number=500, state="OPEN", milestone=None,
                                        repository={"nameWithOwner": repository})

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
        self.options()[1]["name"] = "Wait for RN - Omnia 7.11.98"
        with self.assertRaises(ValueError):
            sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)

    def test_waiting_for_rn_name_variants_are_recognised(self):
        for name in ("Waiting for RN - Omnia 7.11.99 / WCM 7.11.99", "waiting for rn - Omnia 7.11.99 / WCM 7.11.99",
                     "Awaiting release notes - Omnia 7.11.99 / WCM 7.11.99", "Wait-for-RN - Omnia 7.11.99 / WCM 7.11.99",
                     "⏳ Waiting for RN - Omnia 7.11.99 / WCM 7.11.99", "[Wait for RN] Omnia 7.11.99 / WCM 7.11.99",
                     "Wait for RN: Omnia 7.11.99 / WCM 7.11.99", "Wait for RN / Omnia 7.11.99 / WCM 7.11.99",
                     "Wait for RN Omnia 7.11.99 / WCM 7.11.99", "Wait for RN - (Omnia 7.11.99 / WCM 7.11.99)"):
            with self.subTest(name=name):
                self.options()[1]["name"] = name
                plan = sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)
                self.assertEqual(plan["column"], name)
                self.assertEqual(plan["closeout"]["title"], "Release Omnia 7.11.99")

    def test_unrelated_waiting_column_is_rejected(self):
        for name in ("Waiting for QA - Omnia 7.11.99", "Ready - Omnia 7.11.99", "Wait for RNA - Omnia 7.11.99"):
            with self.subTest(name=name):
                self.options()[1]["name"] = name
                with self.assertRaises(ValueError):
                    sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)

    def test_second_column_for_the_release_is_rejected(self):
        self.options().append(dict(self.options()[1], id="duplicate", name="Approved - Omnia 7.11.99 / WCM 7.11.99"))
        with self.assertRaises(ValueError):
            sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)

    def test_missing_or_duplicate_released_option_is_rejected_never_created(self):
        for options in ([option for option in self.options() if option["name"] != "Released"],
                        self.options() + [{"id": "released-2", "name": "Released"}]):
            with self.subTest(count=len(options)):
                self.project["fields"]["nodes"][0]["options"] = options
                with self.assertRaisesRegex(ValueError, "Released"):
                    sync.plan_update(self.project, self.items, self.pr, "7.11.99", SECTION)

    def exercise_sync(self, *, merged=False, change_head=False, approved=True, dry_run=False, withdraw=False, close_pr=False,
                      fail=None, repeat=True):
        """fail: a write name (see FakeGitHub.write) whose call raises gh's permission error (the call is still recorded)."""
        self.pr["merged"] = merged
        fake = FakeGitHub(self, fail=fail, withdraw=withdraw, change_head=change_head, close_pr=close_pr, approved=approved)
        with fake.patched():
            if change_head:
                with self.assertRaises(ValueError):
                    sync.sync("99")
            elif fail:
                with self.assertRaises(sync.SyncIncomplete) as failure:
                    sync.sync("99")
                return fake.reads, fake.calls, failure.exception
            else:
                sync.sync("99", dry_run=dry_run)
                if repeat and not dry_run and approved and not withdraw and not close_pr:
                    first_writes = len(fake.calls)
                    sync.sync("99")
                    self.assertEqual(fake.calls[first_writes:], [], "Repeating synchronization must write nothing")
        return fake.reads, fake.calls

    def test_approved_sync_updates_moves_converts_and_closes_the_notification_once(self):
        reads, calls = self.exercise_sync()
        self.assertEqual([name for name, _ in calls],
                         ["updateProjectV2DraftIssue", "create-milestone", "updateProjectV2ItemFieldValue",
                          "convertProjectV2DraftIssueItemToIssue", "set-milestone", "closeIssue", "close-milestone"],
                         "The draft must leave the Wait for RN column before it becomes an issue")
        self.assertEqual(calls[3][1], {"item": "item", "repository": "repo-omniamono"})
        self.assertEqual(calls[4][1]["id"], "converted-issue", "The milestone goes on the new issue")
        self.assertEqual(calls[5][1]["id"], "converted-issue")
        self.assertIn({"owner": "omniaintranet", "name": "OmniaMono"}, reads)
        self.assertTrue(any("ref=head123" in endpoint for endpoint in reads))

    def test_merge_after_closeout_only_updates_the_issue(self):
        self.exercise_sync()
        _, calls = self.exercise_sync(merged=True)
        self.assertEqual([name for name, _ in calls], ["updateIssue"])
        self.assertEqual(calls[0][1]["id"], "converted-issue")
        self.assertIn("APPROVED AND MERGED", calls[0][1]["body"])

    def test_merge_after_the_column_was_deleted_only_updates_the_issue(self):
        self.exercise_sync()
        self.project["fields"]["nodes"][0]["options"] = [option for option in self.options() if option["id"] != "release"]
        _, calls = self.exercise_sync(merged=True)
        self.assertEqual([name for name, _ in calls], ["updateIssue"])

    def test_merge_sync_reads_merged_content(self):
        reads, calls = self.exercise_sync(merged=True)
        self.assertEqual(len(calls), 7)
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
                self.setUp()
                _, calls = self.exercise_sync(**changes)
                self.assertEqual(calls, [])


class FakeGitHub:
    """GitHub as the sync sees it: the PR, Project 8 (the test's project and items) and repository milestones.

    Writes change the fake state, so a second sync reads what the first one wrote. calls lists every write as
    (name, variables or fields); reads lists every read endpoint (and the repository lookup's variables).
    """

    def __init__(self, test, *, fail=None, withdraw=False, change_head=False, close_pr=False, approved=True):
        self.test, self.fail = test, fail
        self.withdraw, self.change_head, self.close_pr, self.approved = withdraw, change_head, close_pr, approved
        self.calls, self.reads = [], []
        self.pulls = self.review_reads = 0
        if not hasattr(test, "milestones"):
            test.milestones = {}

    def patched(self):
        from contextlib import ExitStack
        stack = ExitStack()
        stack.enter_context(patch.object(sync, "api", side_effect=self.api))
        stack.enter_context(patch.object(sync, "load_project",
                                         side_effect=lambda: deepcopy((self.test.project, self.test.items))))
        stack.enter_context(patch("builtins.print"))
        return stack

    def item(self, item_id):
        return next(item for item in self.test.items if item["id"] == item_id)

    def issue(self, issue_id):
        return next(item["content"] for item in self.test.items if (item.get("content") or {}).get("id") == issue_id)

    def write(self, name, details):
        self.calls.append((name, details))
        if self.fail and (self.fail == name or (callable(self.fail) and self.fail(name, details))):
            raise sync.GitHubError(DENIED)

    def api(self, endpoint, *, query=None, variables=None, project=False, method=None, fields=None):
        self.reads.append(endpoint)
        if query and query.lstrip().startswith("mutation"):
            return self.mutation(query, variables)
        if query and "repository(" in query:
            self.reads.append(variables)
            return {"data": {"repository": {"id": "repo-omniamono"}}}
        if "/milestones" in endpoint:
            return self.milestone_call(endpoint, method, fields)
        if "/reviews?" in endpoint:
            self.review_reads += 1
            return [self.test.review] if self.approved and not (self.withdraw and self.review_reads > 1) else []
        if "/commits?" in endpoint:
            return [{"sha": "first123"}, {"sha": "head123"}]
        if "/contents/" in endpoint:
            notes = GENERATED if "ref=first123" in endpoint else SECTION
            return {"content": base64.b64encode((notes + "\n").encode()).decode()}
        self.pulls += 1
        result = deepcopy(self.test.pr)
        if self.change_head and self.pulls > 1:
            result["head"]["sha"] = "changed"
        if self.close_pr and self.pulls > 1:
            result["state"] = "closed"
        return result

    def mutation(self, query, variables):
        name = next(name for name in ("updateProjectV2DraftIssue", "updateProjectV2ItemFieldValue", "updateProjectV2Field",
                                      "convertProjectV2DraftIssueItemToIssue", "closeIssue", "updateIssue")
                    if name in query)
        if name == "updateIssue" and "milestoneId" in query:
            name = "set-milestone"
        self.write(name, variables)
        if name in ("updateProjectV2DraftIssue", "updateIssue"):
            self.issue(variables["id"]).update(title=variables["title"], body=variables["body"])
        elif name == "updateProjectV2ItemFieldValue":
            self.item(variables["item"])["status"] = {"optionId": variables["option"]}
        elif name == "convertProjectV2DraftIssueItemToIssue":
            self.item(variables["item"])["content"].update(
                __typename="Issue", id="converted-issue", number=500, state="OPEN", milestone=None,
                repository={"nameWithOwner": "omniaintranet/OmniaMono"})
            return {"data": {name: {"item": {"id": variables["item"],
                                             "content": {"id": "converted-issue", "number": 500}}}}}
        elif name == "closeIssue":
            self.issue(variables["id"])["state"] = "CLOSED"
        elif name == "set-milestone":
            milestone = next(m for ms in self.test.milestones.values() for m in ms if m["node_id"] == variables["milestone"])
            self.issue(variables["id"])["milestone"] = {"id": milestone["node_id"], "number": milestone["number"],
                                                        "title": milestone["title"], "state": milestone["state"].upper()}
        else:
            raise AssertionError("updateProjectV2Field must never be called")
        return {}

    def milestone_call(self, endpoint, method, fields):
        repository = endpoint.split("/milestones")[0].removeprefix("repos/")
        milestones = self.test.milestones.setdefault(repository, [])
        if method == "POST":
            self.write("create-milestone", dict(fields, repository=repository))
            if any(m["title"] == fields["title"] for m in milestones):
                raise AssertionError("A milestone with this title already exists (GitHub answers 422)")
            milestone = {"number": len(milestones) + 1, "node_id": f"ms-{repository}-{len(milestones) + 1}",
                         "title": fields["title"], "state": "open"}
            milestones.append(milestone)
            return dict(milestone, open_issues=0)
        if "?" in endpoint:
            return [dict(m, open_issues=self.open_issues(repository, m)) for m in milestones]
        number = int(endpoint.rsplit("/", 1)[1])
        milestone = next(m for m in milestones if m["number"] == number)
        if method == "PATCH":
            self.write("close-milestone", dict(fields, repository=repository, number=number))
            milestone.update(fields)
        return dict(milestone, open_issues=self.open_issues(repository, milestone))

    def open_issues(self, repository, milestone):
        return sum(1 for item in self.test.items
                   if (item.get("content") or {}).get("__typename") == "Issue" and item["content"].get("state") == "OPEN"
                   and (item["content"].get("repository") or {}).get("nameWithOwner") == repository
                   and (item["content"].get("milestone") or {}).get("id") == milestone["node_id"])


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
        # Christian, 2026-11-03/2026-11-12: the security-review section stays, now covered by the general bullet.
        self.assertIn("### Security-sensitive issues pending manual review", draft)
        self.assertIn("covers them with one general bullet", draft)
        self.assertIn("- General performance and security improvements", draft)
        self.assertNotIn("Suggested release note", draft)
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
                     "covers them with one general bullet"):
            self.assertIn(part, draft)
        self.assertNotIn("Suggested release note", draft)
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
                     "Needs review", "covers them with one general bullet"):
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
    options = ApprovalTests.options

    def test_denied_conversion_names_the_permission_and_what_is_pending(self):
        _, calls, failure = self.exercise_sync(fail="convertProjectV2DraftIssueItemToIssue")
        self.assertEqual([name for name, _ in calls][-2:],
                         ["updateProjectV2ItemFieldValue", "convertProjectV2DraftIssueItemToIssue"],
                         "The notification is moved to Released before the conversion is tried")
        self.assertIn(sync.TOKEN_SECRET, str(failure))
        self.assertIn("Issues: Read and write on omniaintranet/OmniaMono", str(failure))
        self.assertIn(DENIED, str(failure))
        self.assertIn("Done in this run:", failure.summary)
        self.assertIn("- update the release notification with the approved release notes", failure.summary)
        self.assertIn("- move the release notification to Released", failure.summary)
        self.assertIn("Still pending: convert the release notification to an omniaintranet/OmniaMono issue", failure.summary)
        self.assertIn("`pr_number` 99", failure.summary)
        _, calls = self.exercise_sync(repeat=False)
        self.assertEqual([name for name, _ in calls],
                         ["convertProjectV2DraftIssueItemToIssue", "set-milestone", "closeIssue", "close-milestone"],
                         "A re-run after the token fix only finishes what is pending")

    def test_denied_issue_update_names_the_permission(self):
        self.converted()
        _, _, failure = self.exercise_sync(merged=True, fail="updateIssue")
        self.assertIn(sync.ISSUE_ACCESS, str(failure))
        self.assertIn("Nothing was changed in Project 8 in this run.", failure.summary)

    def test_denied_move_does_not_blame_issue_access(self):
        _, calls, failure = self.exercise_sync(fail="updateProjectV2ItemFieldValue")
        self.assertNotIn(sync.ISSUE_ACCESS, str(failure))
        self.assertIn("Still pending: move the release notification to Released", failure.summary)
        self.assertNotIn("convertProjectV2DraftIssueItemToIssue", [name for name, _ in calls])

    def test_gh_error_text_replaces_the_traceback(self):
        failed = sync.subprocess.CompletedProcess([], 1, stdout="", stderr=DENIED + "\n")
        with patch.object(sync.subprocess, "run", return_value=failed):
            with self.assertRaises(sync.GitHubError) as error:
                sync.api("graphql", query="mutation { x }")
        self.assertEqual(str(error.exception), DENIED)

    def test_rest_writes_send_a_json_body(self):
        done = sync.subprocess.CompletedProcess([], 0, stdout='{"number": 7}', stderr="")
        with patch.object(sync.subprocess, "run", return_value=done) as run:
            sync.api("repos/o/r/milestones", method="POST", fields={"title": "Release Omnia 7.11.99"})
        args, kwargs = run.call_args
        self.assertEqual(args[0], ["gh", "api", "repos/o/r/milestones", "--method", "POST", "--input", "-"])
        self.assertEqual(kwargs["input"], '{"title": "Release Omnia 7.11.99"}')

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


COLUMN = ("[Wait for RN] Release Omnia 7.11.99 / Workplace 7.11.99 / WCM 7.11.99 / MS 7.11.99 / "
          "Analytics 7.11.5 / Feed 7.11.6")
MILESTONE = "Release Omnia 7.11.99 / Analytics 7.11.5 / Feed 7.11.6"


def issue_item(item_id, repository, number, *, state="OPEN", milestone=None, status="release"):
    content = {"__typename": "Issue", "id": f"issue-{item_id}", "number": number, "title": f"Issue {number}",
               "body": "", "state": state, "repository": {"nameWithOwner": repository},
               "milestone": milestone and {"id": f"other-{milestone}", "number": 1, "title": milestone, "state": "OPEN"}}
    return {"id": item_id, "status": {"optionId": status}, "content": content}


class MilestoneTitleTests(unittest.TestCase):
    def test_column_names_give_the_short_milestone_name(self):
        cases = {
            COLUMN: MILESTONE,
            "Release Omnia 7.12.13 / Workplace 7.12.13 / WCM 7.12.13 / MS 7.12.13 / Analytics 7.12.5 / Feed 7.11.6":
                "Release Omnia 7.12.13 / Analytics 7.12.5 / Feed 7.11.6",
            "Wait for RN - Omnia 7.12.13 / WCM 7.12.13": "Release Omnia 7.12.13",
            "Approved - Release Omnia 7.12.13 / wcm 7.12.13 / Feed 7.11.6": "Release Omnia 7.12.13 / Feed 7.11.6",
            "Waiting for RN - (Omnia 7.12.13 /  Analytics   7.12.5)": "Release Omnia 7.12.13 / Analytics 7.12.5",
        }
        for column, title in cases.items():
            version = "7.12.13" if "7.12.13" in column else "7.11.99"
            with self.subTest(column=column):
                self.assertEqual(sync.milestone_title(column, version), title)

    def test_unexpected_column_names_stop(self):
        for column in ("[Wait for RN] Release Omnia 7.11.98 / Feed 7.11.6", "[Wait for RN] Omnia 7.11.99 / Feed",
                       "[Wait for RN] Omnia 7.11.99 // Feed 7.11.6", "[Wait for RN] Feed 7.11.6 / Omnia 7.11.99"):
            with self.subTest(column=column):
                with self.assertRaises(ValueError):
                    sync.milestone_title(column, "7.11.99")


class CloseoutTests(unittest.TestCase):
    """The release closeout with a full column: milestones, closed issues and every item in Released."""
    exercise_sync = ApprovalTests.exercise_sync
    options = ApprovalTests.options

    def setUp(self):
        self.pr, self.review, self.project, self.items = fixtures()
        self.options()[1]["name"] = COLUMN
        mono, analytics, feed = "omniaintranet/OmniaMono", "omniaintranet/OmniaAnalytics", "omniaintranet/OmniaFeed"
        self.items += [
            issue_item("open", mono, 101),
            issue_item("closed", mono, 102, state="CLOSED"),
            issue_item("other-milestone", mono, 103, milestone="Release 7.12"),
            issue_item("analytics", analytics, 7, milestone="7.11.4"),
            issue_item("feed", feed, 5),
            {"id": "pr", "status": {"optionId": "release"},
             "content": {"__typename": "PullRequest", "id": "pr-content", "number": 200, "title": "Fix",
                         "repository": {"nameWithOwner": mono}}},
            {"id": "draft-item", "status": {"optionId": "release"},
             "content": {"__typename": "DraftIssue", "id": "draft-content", "title": "Check with QA", "body": ""}},
            issue_item("unrelated", mono, 300, status="unrelated"),
        ]
        # OmniaMono already has the release milestone (created by hand, or by an earlier run): it is reused.
        self.milestones = {mono: [{"number": 40, "node_id": "ms-mono", "title": MILESTONE, "state": "open"}]}

    def content(self, item_id):
        return next(item["content"] for item in self.items if item["id"] == item_id)

    def status(self, item_id):
        return next(item["status"]["optionId"] for item in self.items if item["id"] == item_id)

    def test_closeout_writes(self):
        _, calls = self.exercise_sync()
        names = [name for name, _ in calls]
        self.assertNotIn("updateProjectV2Field", names, "The Status field itself is never written")
        creates = [details for name, details in calls if name == "create-milestone"]
        self.assertEqual(creates, [{"title": MILESTONE, "repository": "omniaintranet/OmniaFeed"}],
                         "OmniaMono's milestone is reused; OmniaAnalytics#7 keeps its own, so none is created there")
        assigned = [details["id"] for name, details in calls if name == "set-milestone"]
        self.assertEqual(assigned, ["issue-open", "issue-closed", "issue-feed", "converted-issue"])
        self.assertEqual(self.content("open")["milestone"]["title"], MILESTONE)
        self.assertEqual(self.content("feed")["milestone"]["id"], "ms-omniaintranet/OmniaFeed-1")
        self.assertEqual(self.content("other-milestone")["milestone"]["title"], "Release 7.12", "A different milestone is kept")
        self.assertEqual(self.content("analytics")["milestone"]["title"], "7.11.4")
        closed = [details["id"] for name, details in calls if name == "closeIssue"]
        self.assertEqual(closed, ["issue-open", "issue-other-milestone", "issue-analytics", "issue-feed", "converted-issue"],
                         "Every open issue is closed; the already closed one is not touched")
        self.assertNotIn("reopenIssue", " ".join(names))
        moved = [details["item"] for name, details in calls if name == "updateProjectV2ItemFieldValue"]
        self.assertEqual(moved, ["open", "closed", "other-milestone", "analytics", "feed", "pr", "draft-item", "item"],
                         "Every item of the column moves, the notification last")
        self.assertTrue(all(details["option"] == "released" and details["field"] == "field" and details["project"] == "project"
                            for name, details in calls if name == "updateProjectV2ItemFieldValue"))
        for item in self.items:
            with self.subTest(item=item["id"]):
                self.assertEqual(item["status"]["optionId"], "unrelated" if item["id"] == "unrelated" else "released")
        self.assertEqual(self.content("unrelated")["state"], "OPEN")
        self.assertEqual(self.content("pr")["number"], 200)
        self.assertNotIn("state", self.content("pr"), "A pull request is never closed")
        closes = [details for name, details in calls if name == "close-milestone"]
        self.assertEqual(sorted(details["repository"] for details in closes),
                         ["omniaintranet/OmniaFeed", "omniaintranet/OmniaMono"])
        self.assertTrue(all(m["state"] == "closed" for ms in self.milestones.values() for m in ms))
        self.assertLess(names.index("updateProjectV2ItemFieldValue"), names.index("convertProjectV2DraftIssueItemToIssue"))
        self.assertLess(max(i for i, name in enumerate(names) if name == "closeIssue"), names.index("close-milestone"))

    def test_rerun_after_a_failure_finishes_without_doubling(self):
        _, calls, failure = self.exercise_sync(fail=lambda name, details: name == "closeIssue" and details["id"] == "issue-feed")
        self.assertIn("Still pending: close omniaintranet/OmniaFeed#5 as completed", failure.summary)
        self.assertIn("Issues: Read and write on omniaintranet/OmniaFeed", str(failure))
        self.assertEqual(self.content("open")["state"], "CLOSED")
        self.assertEqual(self.status("open"), "release", "Nothing moved yet")
        _, calls = self.exercise_sync()
        names = [name for name, _ in calls]
        self.assertNotIn("create-milestone", names, "The milestone the failed run created is reused")
        self.assertEqual([details["id"] for name, details in calls if name == "set-milestone"], ["converted-issue"])
        self.assertEqual([details["id"] for name, details in calls if name == "closeIssue"], ["issue-feed", "converted-issue"])
        self.assertEqual(len(self.milestones["omniaintranet/OmniaFeed"]), 1)
        self.assertTrue(all(item["status"]["optionId"] == "released" for item in self.items if item["id"] != "unrelated"))

    def test_open_issue_outside_the_release_keeps_the_milestone_open(self):
        mono = "omniaintranet/OmniaMono"
        stray = issue_item("stray", mono, 400, status="unrelated")
        stray["content"]["milestone"] = {"id": "ms-mono", "number": 40, "title": MILESTONE, "state": "OPEN"}
        self.items.append(stray)
        _, calls, failure = self.exercise_sync(fail="never")
        self.assertIn("still has 1 open issue(s)", str(failure))
        self.assertEqual(self.milestones[mono][0]["state"], "open")
        self.assertEqual(self.content("stray")["state"], "OPEN", "Issues outside the column are never touched")

    def test_dry_run_lists_every_write_and_makes_none(self):
        with patch("builtins.print") as printed:
            fake = FakeGitHub(self)
            with patch.object(sync, "api", side_effect=fake.api), \
                    patch.object(sync, "load_project", side_effect=lambda: deepcopy((self.project, self.items))):
                sync.sync("99", dry_run=True)
        self.assertEqual(fake.calls, [])
        output = "\n".join(str(call.args[0]) for call in printed.call_args_list)
        for line in ("- would create the milestone `" + MILESTONE + "` in omniaintranet/OmniaFeed",
                     "- would set the milestone on omniaintranet/OmniaMono#101",
                     "- would close omniaintranet/OmniaMono#103 as completed",
                     "- would move omniaintranet/OmniaMono#200 to Released",
                     "- would move draft `Check with QA` to Released",
                     "- would move the release notification to Released",
                     "- would convert the release notification to an omniaintranet/OmniaMono issue",
                     "- would set the milestone on the release notification",
                     "- would close the release notification as completed",
                     "- would close the milestone `" + MILESTONE + "` in omniaintranet/OmniaMono",
                     "Kept its own milestone `Release 7.12`: omniaintranet/OmniaMono#103",
                     "Kept its own milestone `7.11.4`: omniaintranet/OmniaAnalytics#7",
                     "Moved to Released only (not an issue: no milestone, not closed): omniaintranet/OmniaMono#200",
                     "Already closed, left as they are: omniaintranet/OmniaMono#102"):
            self.assertIn(line, output)
        self.assertNotIn("would close omniaintranet/OmniaMono#102", output)
        self.assertNotIn("would create the milestone `" + MILESTONE + "` in omniaintranet/OmniaMono", output)
        self.assertNotIn("OmniaAnalytics", "\n".join(line for line in output.splitlines() if "milestone `" + MILESTONE in line))

    def test_unreadable_item_in_the_column_stops_before_any_write(self):
        for content in (None, {"__typename": "Issue", "id": None, "number": None, "repository": None}):
            with self.subTest(content=content):
                self.setUp()
                self.items.append({"id": "hidden", "status": {"optionId": "release"}, "content": content})
                _, calls = self.exercise_sync_expecting(ValueError, "no readable content")
                self.assertEqual(calls, [])

    def exercise_sync_expecting(self, error, text):
        fake = FakeGitHub(self)
        with fake.patched():
            with self.assertRaisesRegex(error, text):
                sync.sync("99")
        return fake.reads, fake.calls

    def test_unreadable_milestones_name_the_permission(self):
        fake = FakeGitHub(self)
        original = fake.milestone_call

        def denied(endpoint, method, fields):
            if "OmniaFeed" in endpoint:
                raise sync.GitHubError("gh: Not Found (HTTP 404)")
            return original(endpoint, method, fields)

        fake.milestone_call = denied
        with fake.patched():
            with self.assertRaisesRegex(sync.GitHubError, "Issues: Read and write on omniaintranet/OmniaFeed"):
                sync.sync("99")
        self.assertEqual(fake.calls, [])


if __name__ == "__main__":
    unittest.main()
