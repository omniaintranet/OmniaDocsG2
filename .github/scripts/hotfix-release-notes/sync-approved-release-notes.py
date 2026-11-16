"""Synchronize approved documentation PR content to the existing Prod release item, and close out the release.

The closeout replaces the earlier rename of the release column to "Approved - ...". It creates (or reuses) the
release milestone, sets it on the column's issues, closes them as completed and moves every item of the column,
the release notification included, to Status "Released". It writes item field values only and never edits the
Status field itself: updating that field resends every option and can wipe the Status of every item on the board.
"""
import base64
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPOSITORY = "omniaintranet/OmniaDocsG2"
NOTES_PATH = "release-notes/7.0/versions.rst"
PUBLISHED_URL = "https://omnia-docs-g2.readthedocs.io/en/latest/release-notes/7.0/versions.html"
# Approved notifications become issues here, where the other Project 8 issues live (private repo).
ISSUE_OWNER, ISSUE_REPO = "omniaintranet", "OmniaMono"
TOKEN_SECRET = "GH_PROJECT_TOKEN_HOTFIX_RELEASE_NOTES_WF"
ISSUE_REPOSITORY = f"{ISSUE_OWNER}/{ISSUE_REPO}"


def issue_access(repository):
    """What the token needs for issue and milestone writes in a repository."""
    return (f"The project token (secret {TOKEN_SECRET}) needs the repository permission "
            f"Issues: Read and write on {repository}.")


ISSUE_ACCESS = issue_access(ISSUE_REPOSITORY)
# The closeout's target column, looked up by this exact name and never created.
RELEASED = "Released"
# Columns renamed by the earlier version of this script ("Approved - Omnia ...") are still recognised.
APPROVED = re.compile(r"^Approved(?![A-Za-z0-9])")
# Component parts the milestone name leaves out ("Release Omnia 7.12.13 / Workplace 7.12.13 / ..." keeps Omnia,
# Analytics and Feed), as in the milestones of the manual closeouts (OmniaMono milestones #11-#33).
MILESTONE_DROPPED = re.compile(r"(?:Workplace|WCM|MS) \d+\.\d+\.\d+", re.IGNORECASE)
MILESTONE_PART = re.compile(r"[A-Za-z][A-Za-z0-9 .&-]* \d+\.\d+\.\d+")
# GitHub rejects issue and draft-issue bodies over 65,536 characters; keep a margin.
MAX_BODY = 65000
# The generated draft (the recommendation) is kept below the approved notes between these markers,
# so a repeated sync finds it again and neither nests nor duplicates it.
DRAFT_START = "<!-- hotfix-release-notes:generated-draft:start -->"
DRAFT_END = "<!-- hotfix-release-notes:generated-draft:end -->"
DRAFT_CUT = "<!-- hotfix-release-notes:generated-draft:cut -->"
NOTES_CUT = "<!-- hotfix-release-notes:generated-draft:notes-left-out -->"
# create-ready-project-item.sh writes the whole generated draft between these markers.
GENERATED_START = "<!-- hotfix-release-notes:draft:start -->"
GENERATED_END = "<!-- hotfix-release-notes:draft:end -->"
DRAFT_HEADING = ("## Generated draft (recommendation)\n\n"
                 "The automatically generated draft, kept for comparison with the approved release notes above. "
                 "It is not approved.\n\n")
# Shared with the bash scripts: what counts as a "waiting for release notes" column.
# The lookahead is the same end boundary wait-for-rn-lib.sh adds ("Wait for RNA" is not the column).
WAIT_FOR_RN = re.compile(
    Path(__file__).with_name("wait-for-rn-pattern.txt").read_text(encoding="utf-8").strip() + r"(?![A-Za-z0-9])",
    re.IGNORECASE)


class GitHubError(Exception):
    """A gh call failed; the message is gh's own error text."""


class SyncIncomplete(Exception):
    """A Project write failed after the PR checks passed; summary says what is done and what is pending."""

    def __init__(self, message, summary):
        super().__init__(message)
        self.summary = summary


def api(endpoint, *, query=None, variables=None, project=False, method=None, fields=None):
    """One gh api call: GraphQL (query), REST with a JSON body (method and fields) or a REST read."""
    args = ["gh", "api", endpoint]
    if method:
        args += ["--method", method]
    if query:
        payload = {"query": query, "variables": variables or {}}
    else:
        payload = fields
    if payload is not None:
        args += ["--input", "-"]
    env = dict(os.environ)
    if project and env.get("PROJECT_TOKEN"):
        env["GH_TOKEN"] = env["PROJECT_TOKEN"]
    result = subprocess.run(args, input=json.dumps(payload) if payload is not None else None, capture_output=True,
                            text=True, encoding="utf-8", env=env)
    if result.returncode:
        message = " ".join((result.stderr or result.stdout or "").split())
        raise GitHubError(message or f"gh api {endpoint} exited with {result.returncode}")
    return json.loads(result.stdout)


def release_version(pr):
    match = re.fullmatch(r"hotfix-release-notes-(\d+\.\d+\.\d+)", pr["head"]["ref"])
    if (not match or pr["base"]["ref"] != "master" or
            (pr["head"].get("repo") or {}).get("full_name") != REPOSITORY):
        raise ValueError("Expected a hotfix release-note PR from this repository into master")
    return match[1]


def is_approved(pr, reviews):
    if pr.get("merged"):
        return True
    if pr["state"] != "open" or pr.get("draft"):
        return False
    latest = {}
    for review in sorted(reviews, key=lambda review: review.get("submitted_at") or ""):
        if review["state"] in ("APPROVED", "CHANGES_REQUESTED", "DISMISSED"):
            latest[review["user"]["login"]] = review
    if any(review["state"] == "CHANGES_REQUESTED" for review in latest.values()):
        return False
    return any(review["state"] == "APPROVED" and
               review.get("commit_id") == pr["head"]["sha"] and
               review.get("author_association") in ("OWNER", "MEMBER", "COLLABORATOR") and
               review["user"]["login"] != pr["user"]["login"]
               for review in latest.values())


def extract_release(text, version):
    text = text.replace("\r\n", "\n")
    headings = list(re.finditer(r"(?m)^(\d+\.\d+\.\d+)\n=+\s*$", text))
    matches = [i for i, heading in enumerate(headings) if heading[1] == version]
    if len(matches) != 1:
        raise ValueError("Expected exactly one matching release section in the approved PR")
    index = matches[0]
    end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
    section = text[headings[index].start():end].strip()
    lines = section.splitlines()
    if len(lines) < 5 or not lines[2].startswith("(") or not lines[2].endswith(")"):
        raise ValueError("Approved release section is missing its component-version line")
    if not any(line.startswith("- ") for line in lines[3:]):
        raise ValueError("Approved release section contains no release-note bullets")
    if "```" in section:
        raise ValueError("Cannot safely embed release notes containing Markdown fences")
    return section


def demote_headings(text):
    """Move the draft's Markdown headings one level down, so they sit under the kept-draft heading."""
    lines, fenced = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and re.match(r"#{1,5} ", line):
            line = "#" + line
        lines.append(line)
    return "\n".join(lines)


def kept_draft(body):
    """The generated draft to keep, taken from the notification body, or None when the body no longer holds it.

    A body written by this sync carries the draft between its markers: it is reused as it is (idempotent).
    A body still as create-ready-project-item.sh wrote it is the whole draft, every section included:
    between the generator's markers, or (for drafts written before those markers) the body itself.
    """
    body = (body or "").replace("\r\n", "\n")
    start, end = body.find(DRAFT_START), body.rfind(DRAFT_END)
    if start != -1 and end > start:
        return body[start + len(DRAFT_START):end].strip("\n")
    start, end = body.find(GENERATED_START), body.rfind(GENERATED_END)
    if start != -1 and end > start:
        return demote_headings(body[start + len(GENERATED_START):end].strip("\n"))
    if "**DRAFT - NOT APPROVED.**" in body and "## Generated draft release notes" in body:
        return demote_headings(body.strip())
    return None


def leave_out_notes(draft, pr_url):
    """Replace the draft's release-notes block with a pointer to the PR, keeping every other section.

    The notes are the one part of the draft that is also in the documentation PR's first commit;
    the left-out issues and the security-review issues are only here.
    """
    match = re.search(r"(?ms)^```text\n.*?^```[ \t]*$", draft)
    if not match:
        return draft
    return (draft[:match.start()] + f"{NOTES_CUT}\n_The draft release notes are left out here to stay within GitHub's "
            f"size limit for issue descriptions. They are in the first commit of the "
            f"[documentation pull request]({pr_url})._" + draft[match.end():])


def fit_draft(draft, room, pr_url):
    """Make the draft take at most room characters: first leave out its release-notes block, then
    cut it at a line boundary, closing an open code fence."""
    if len(draft) <= room:
        return draft
    draft = leave_out_notes(draft, pr_url)
    if len(draft) <= room:
        return draft
    if DRAFT_CUT in draft:
        draft = draft[:draft.find(DRAFT_CUT)].rstrip("\n")
    note = (f"\n{DRAFT_CUT}\n_The draft was cut here to stay within GitHub's size limit for issue descriptions; "
            f"the rest of it is not shown. Its release notes are in the first commit of the "
            f"[documentation pull request]({pr_url})._")
    budget = room - len(note) - len("\n```")
    kept, size = [], 0
    for line in draft.split("\n"):
        if size + len(line) + 1 > budget:
            break
        kept.append(line)
        size += len(line) + 1
    if sum(line.startswith("```") for line in kept) % 2:
        kept.append("```")
    return "\n".join(kept) + note


def approval_body(pr, section, draft=None):
    state = "APPROVED AND MERGED" if pr.get("merged") else "APPROVED"
    publication = ("The documentation PR has been merged." if pr.get("merged") else
                   "These notes are approved; publication still requires merging the documentation PR.")
    body = (f"> **{state}.** {publication}\n\n"
            f"[Review the documentation pull request]({pr['html_url']}).\n\n"
            f"[View the published hotfix release notes]({PUBLISHED_URL}).\n\n"
            f"## Approved release notes\n\n```text\n{section}\n```\n")
    if len(body) > MAX_BODY:
        raise ValueError("The approved release notes alone exceed GitHub's size limit for issue descriptions")
    if draft is None:
        return body
    frame = "\n---\n\n" + DRAFT_HEADING + DRAFT_START + "\n{}\n" + DRAFT_END + "\n"
    draft = fit_draft(draft, MAX_BODY - len(body) - len(frame.format("")), pr["html_url"])
    return body + frame.format(draft)


def draft_from_pr(endpoint, version):
    """Rebuild the draft notes from the documentation PR's first commit, for a body an older sync replaced.

    create-pr.sh commits the same generated notes that create-ready-project-item.sh puts into the draft,
    so the first commit holds the recommendation; the omitted and security-review lists are not in it.
    """
    commits = api(f"{endpoint}/commits?per_page=100")
    if not commits:
        return "_The generated draft could not be recovered: the documentation pull request has no commits._"
    sha = commits[0]["sha"]
    content = api(f"repos/{REPOSITORY}/contents/{NOTES_PATH}?ref={sha}")
    try:
        section = extract_release(base64.b64decode(content["content"]).decode("utf-8-sig"), version)
    except ValueError as error:
        return f"_The generated draft could not be recovered from the documentation pull request: {error}._"
    return (f"_This notification's original draft had already been replaced, so the draft release notes below come "
            f"from the [first commit of the documentation pull request](https://github.com/{REPOSITORY}/commit/{sha}). "
            "Its lists of omitted issues and of issues held for security review are not available._\n\n"
            f"### Generated draft release notes\n\n```text\n{section}\n```")


PROJECT_QUERY = """query($cursor: String) {
  organization(login: "omniaintranet") { projectV2(number: 8) {
    id
    fields(first: 100) { nodes { ... on ProjectV2SingleSelectField {
      id name options { id name }
    } } }
    items(first: 100, after: $cursor) {
      pageInfo { hasNextPage endCursor }
      nodes {
        id
        status: fieldValueByName(name: "Status") {
          ... on ProjectV2ItemFieldSingleSelectValue { optionId name }
        }
        content {
          __typename
          ... on DraftIssue { id title body }
          ... on Issue {
            id number title body state
            repository { nameWithOwner }
            milestone { id number title state }
          }
          ... on PullRequest { id number title repository { nameWithOwner } }
        }
      }
    }
  } }
}"""


def load_project():
    cursor = None
    items = []
    while True:
        project = api("graphql", query=PROJECT_QUERY, variables={"cursor": cursor}, project=True)["data"]["organization"]["projectV2"]
        items.extend(project["items"]["nodes"])
        page = project["items"]["pageInfo"]
        if not page["hasNextPage"]:
            return project, items
        cursor = page["endCursor"]


def version_pattern(version):
    return re.compile(r"\bOmnia\s+" + re.escape(version) + r"(?=\s|/|\)|$)")


def column_label(name):
    """The Wait for RN label (or the legacy Approved label) at the start of a column name, or None."""
    return WAIT_FOR_RN.match(name) or APPROVED.match(name)


def is_release_column(name, version):
    return bool(column_label(name) and version_pattern(version).search(name))


def milestone_title(column_name, version):
    """The release milestone's name: the column's component line without its label and the Workplace, WCM and MS parts.

    "[Wait for RN] Release Omnia 7.12.13 / Workplace 7.12.13 / WCM 7.12.13 / MS 7.12.13 / Analytics 7.12.5 /
    Feed 7.11.6" gives "Release Omnia 7.12.13 / Analytics 7.12.5 / Feed 7.11.6".
    """
    name = column_name.strip()
    label = column_label(name)
    if label:
        name = re.sub(r"^[^A-Za-z0-9(]+", "", name[label.end():])
    name = name.strip()
    if name.startswith("(") and name.endswith(")"):
        name = name[1:-1]
    parts = [" ".join(part.split()) for part in name.split("/")]
    error = f"Cannot derive the release milestone's name from the column `{column_name}`"
    if not re.fullmatch(r"(?:Release )?Omnia " + re.escape(version), parts[0], re.IGNORECASE):
        raise ValueError(f"{error}: it does not start with Omnia {version}")
    kept = [part for part in parts[1:] if not MILESTONE_DROPPED.fullmatch(part)]
    if not all(MILESTONE_PART.fullmatch(part) for part in kept):
        raise ValueError(f"{error}: expected components such as `Analytics 7.12.5` between the slashes")
    return " / ".join([f"Release Omnia {version}"] + kept)


def repository_of(entry):
    return entry["content"]["repository"]["nameWithOwner"]


def describe(entry):
    """A Project item for the run log: owner/repo#number, or the draft's title."""
    content = entry.get("content") or {}
    if content.get("number"):
        return f"{repository_of(entry)}#{content['number']}"
    return f"draft `{content.get('title') or entry['id']}`"


def plan_update(project, items, pr, version, section, recover_draft=None):
    titles = {f"Release notes for Omnia {version} are now ready",
              f"Release notes for Omnia {version} are approved"}
    matches = [item for item in items if (item.get("content") or {}).get("title") in titles]
    if len(matches) != 1:
        raise ValueError("Expected exactly one existing release notification in Prod")
    item = matches[0]
    kind = item["content"].get("__typename")
    if kind not in ("DraftIssue", "Issue"):
        raise ValueError("The Prod notification is neither a draft nor an issue")
    if kind == "Issue" and (item["content"].get("repository") or {}).get("nameWithOwner") != ISSUE_REPOSITORY:
        raise ValueError(f"The Prod notification is an issue outside {ISSUE_REPOSITORY}")
    if not re.search(re.escape(pr["html_url"]) + r"(?=[)\s]|$)", item["content"]["body"]):
        raise ValueError("The Prod notification is not linked to this documentation PR")
    fields = [field for field in project["fields"]["nodes"] if field.get("name") == "Status"]
    if len(fields) != 1 or not item.get("status"):
        raise ValueError("Cannot identify the release notification's Status option")
    field = fields[0]
    options = field["options"]
    released = [option for option in options if option["name"] == RELEASED]
    if len(released) != 1:
        raise ValueError(f'Expected exactly one Status option named "{RELEASED}" in Prod; this workflow never creates '
                         "one, so add it in the board's UI")
    released = released[0]
    current = [option for option in options if option["id"] == item["status"]["optionId"]]
    if len(current) != 1:
        raise ValueError("Cannot identify the release column")
    current = current[0]
    columns = [option for option in options if is_release_column(option["name"], version)]
    if current["id"] == released["id"]:
        # Moved by an earlier run (a re-run, or the merge sync after the approval sync): the column is found by
        # its name, and Christian may already have deleted it.
        if len(columns) > 1:
            raise ValueError(f"More than one release column for Omnia {version}; manual reconciliation required")
        column = columns[0] if columns else None
    else:
        if not version_pattern(version).search(current["name"]):
            raise ValueError("The release column does not match the PR version")
        if not column_label(current["name"]):
            raise ValueError("Expected a Wait for RN or Approved release column")
        if len(columns) != 1:
            raise ValueError(f"More than one release column for Omnia {version}; manual reconciliation required")
        column = current
    draft = kept_draft(item["content"]["body"])
    draft_source = "kept from the notification" if draft is not None else "not available"
    if draft is None and recover_draft:
        draft = recover_draft()
        draft_source = "recovered from the documentation PR's first commit"
    return {"item": item, "project_id": project["id"], "field_id": field["id"], "released_id": released["id"],
            "move": current["id"] != released["id"], "column": column["name"] if column else None,
            "closeout": plan_closeout(items, item, column, version) if column else None,
            "convert": kind == "DraftIssue",
            "title": f"Release notes for Omnia {version} are approved",
            "body": approval_body(pr, section, draft), "draft_source": draft_source}


def plan_closeout(items, notification, column, version):
    """What the closeout does with the release column's other items. Milestones are looked up separately."""
    title = milestone_title(column["name"], version)
    in_column, issues, others = [], [], []
    for entry in items:
        if entry["id"] == notification["id"] or (entry.get("status") or {}).get("optionId") != column["id"]:
            continue
        content = entry.get("content") or {}
        kind = content.get("__typename")
        if kind in ("Issue", "PullRequest") and not (content.get("id") and content.get("number") and
                                                     (content.get("repository") or {}).get("nameWithOwner")):
            kind = f"{kind} without its id, number or repository"
        if kind == "Issue":
            if entry["content"].get("state") not in ("OPEN", "CLOSED"):
                raise ValueError(f"Cannot tell whether {describe(entry)} is open or closed")
            issues.append(entry)
        elif kind in ("PullRequest", "DraftIssue"):
            others.append(entry)
        else:
            raise ValueError(f"An item in the release column has no readable content ({kind or 'none'}); the project "
                             f"token (secret {TOKEN_SECRET}) may lack read access to its repository")
        in_column.append(entry)
    milestone = lambda entry: entry["content"].get("milestone")  # noqa: E731
    assign = [entry for entry in issues if not milestone(entry)]
    # An issue that already has another milestone (its own repository's, such as OmniaAnalytics#7) keeps it.
    kept = [entry for entry in issues if milestone(entry) and milestone(entry)["title"] != title]
    # The release notification gets the OmniaMono milestone and is closed too (Christian, 2026-11-16), once it is
    # an issue; a draft is converted first. A milestone it already has is kept, as for any other issue.
    note = notification["content"]
    note_milestone = note.get("milestone") if note["__typename"] == "Issue" else None
    note_assign = not note_milestone
    note_close = note["__typename"] == "DraftIssue" or note.get("state") == "OPEN"
    # OmniaMono always gets the milestone; another repository only for an issue without a milestone of its own.
    create = sorted({ISSUE_REPOSITORY} | {repository_of(entry) for entry in assign}) if in_column or note_assign else []
    # Repositories that already hold the milestone (an earlier run) are closed out too.
    holding = {repository_of(entry) for entry in items
               if (entry.get("content") or {}).get("__typename") == "Issue" and (milestone(entry) or {}).get("title") == title}
    return {"title": title, "items": in_column, "assign": assign, "kept": kept, "others": others,
            "note_assign": note_assign, "note_close": note_close,
            "note_kept": note_milestone["title"] if note_milestone and note_milestone["title"] != title else None,
            "close": [entry for entry in issues if entry["content"]["state"] == "OPEN"],
            "already_closed": [entry for entry in issues if entry["content"]["state"] == "CLOSED"],
            "create": create, "milestone_repos": sorted(set(create) | holding)}


def find_milestone(repository, title):
    """The repository's milestone with exactly this title (open or closed), or None."""
    found, page = [], 1
    while True:
        try:
            batch = api(f"repos/{repository}/milestones?state=all&per_page=100&page={page}", project=True)
        except GitHubError as error:
            raise GitHubError(f"Cannot read the milestones of {repository}: {error}. {issue_access(repository)}") from None
        found += [milestone for milestone in batch if milestone.get("title") == title]
        if len(batch) < 100:
            break
        page += 1
    if len(found) > 1:
        raise ValueError(f"{repository} has more than one milestone named `{title}`")
    return found[0] if found else None


def load_milestones(plan):
    closeout = plan["closeout"]
    if not closeout:
        return {}
    return {repository: find_milestone(repository, closeout["title"]) for repository in closeout["milestone_repos"]}


MOVE_ITEM = """mutation($project: ID!, $item: ID!, $field: ID!, $option: String!) {
  updateProjectV2ItemFieldValue(input: {projectId: $project, itemId: $item, fieldId: $field,
                                        value: {singleSelectOptionId: $option}}) {
    projectV2Item { id }
  }
}"""


def update_notification(plan):
    item = plan["item"]["content"]
    if item["__typename"] == "Issue":
        api("graphql", query="""mutation($id: ID!, $title: String!, $body: String!) {
          updateIssue(input: {id: $id, title: $title, body: $body}) { issue { id } }
        }""", variables={"id": item["id"], "title": plan["title"], "body": plan["body"]}, project=True)
    else:
        api("graphql", query="""mutation($id: ID!, $title: String!, $body: String!) {
          updateProjectV2DraftIssue(input: {draftIssueId: $id, title: $title, body: $body}) {
            draftIssue { id }
          }
        }""", variables={"id": item["id"], "title": plan["title"], "body": plan["body"]}, project=True)


def create_milestone(repository, title, milestones):
    milestones[repository] = api(f"repos/{repository}/milestones", method="POST", fields={"title": title}, project=True)


def set_milestone(entry, milestone):
    api("graphql", query="""mutation($id: ID!, $milestone: ID!) {
      updateIssue(input: {id: $id, milestoneId: $milestone}) { issue { id } }
    }""", variables={"id": entry["content"]["id"], "milestone": milestone["node_id"]}, project=True)


def close_issue(entry):
    api("graphql", query="""mutation($id: ID!) {
      closeIssue(input: {issueId: $id, stateReason: COMPLETED}) { issue { id } }
    }""", variables={"id": entry["content"]["id"]}, project=True)


def move_to_released(plan, entry):
    api("graphql", query=MOVE_ITEM, variables={"project": plan["project_id"], "item": entry["id"],
                                               "field": plan["field_id"], "option": plan["released_id"]}, project=True)


def convert_notification(plan):
    """Convert the draft; the item keeps its id and Status, and its content becomes the new OmniaMono issue."""
    repository = api("graphql", query="""query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) { id }
    }""", variables={"owner": ISSUE_OWNER, "name": ISSUE_REPO}, project=True)["data"]["repository"]["id"]
    result = api("graphql", query="""mutation($item: ID!, $repository: ID!) {
      convertProjectV2DraftIssueItemToIssue(input: {itemId: $item, repositoryId: $repository}) {
        item { id content { ... on Issue { id number } } }
      }
    }""", variables={"item": plan["item"]["id"], "repository": repository}, project=True)
    issue = ((((result.get("data") or {}).get("convertProjectV2DraftIssueItemToIssue") or {}).get("item") or {})
             .get("content") or {})
    if not issue.get("id"):
        raise ValueError("the conversion did not return the new issue")
    plan["item"]["content"] = dict(plan["item"]["content"], __typename="Issue", id=issue["id"],
                                   number=issue.get("number"), repository={"nameWithOwner": ISSUE_REPOSITORY})


def close_milestone(repository, milestones):
    """Close the milestone once every issue on it is closed; re-read first, so a re-run never writes twice."""
    milestone = api(f"repos/{repository}/milestones/{milestones[repository]['number']}", project=True)
    if milestone["state"] == "closed":
        return
    if milestone.get("open_issues"):
        raise ValueError(f"the milestone `{milestone['title']}` in {repository} still has {milestone['open_issues']} "
                         "open issue(s) that are not in the release column, so it was left open")
    api(f"repos/{repository}/milestones/{milestone['number']}", method="PATCH", fields={"state": "closed"}, project=True)


def plan_writes(plan, milestones):
    """Every write, in order: (description, repository whose Issues permission it needs or None, call).

    Order: the notes; the milestones; milestone on each issue; close each issue; move the column's items, then the
    notification, to Released; convert the notification (only after it left the Wait for RN column, because
    detect-release.sh reads the repository issues in such columns), set the milestone on it and close it; close the
    milestones.
    Whatever is already done (read from the current state) is left out, so a re-run only finishes what is pending.
    """
    writes = []
    note = plan["item"]["content"]
    if note["title"] != plan["title"] or note["body"] != plan["body"]:
        writes.append(("update the release notification with the approved release notes, the generated draft kept "
                       "below them", ISSUE_REPOSITORY if note["__typename"] == "Issue" else None,
                       lambda: update_notification(plan)))
    closeout = plan["closeout"]
    if closeout:
        title = closeout["title"]
        for repository in closeout["create"]:
            if milestones.get(repository) is None:
                writes.append((f"create the milestone `{title}` in {repository}", repository,
                               lambda repository=repository: create_milestone(repository, title, milestones)))
        for entry in closeout["assign"]:
            writes.append((f"set the milestone on {describe(entry)}", repository_of(entry),
                           lambda entry=entry: set_milestone(entry, milestones[repository_of(entry)])))
        for entry in closeout["close"]:
            writes.append((f"close {describe(entry)} as completed", repository_of(entry),
                           lambda entry=entry: close_issue(entry)))
        for entry in closeout["items"]:
            writes.append((f"move {describe(entry)} to {RELEASED}", None,
                           lambda entry=entry: move_to_released(plan, entry)))
    if plan["move"]:
        writes.append((f"move the release notification to {RELEASED}", None,
                       lambda: move_to_released(plan, plan["item"])))
    if plan["convert"]:
        writes.append((f"convert the release notification to an {ISSUE_REPOSITORY} issue", ISSUE_REPOSITORY,
                       lambda: convert_notification(plan)))
    if closeout and closeout["note_assign"]:
        writes.append(("set the milestone on the release notification", ISSUE_REPOSITORY,
                       lambda: set_milestone(plan["item"], milestones[ISSUE_REPOSITORY])))
    if closeout and closeout["note_close"]:
        writes.append(("close the release notification as completed", ISSUE_REPOSITORY,
                       lambda: close_issue(plan["item"])))
    if closeout:
        for repository in closeout["milestone_repos"]:
            milestone = milestones.get(repository)
            if (milestone is None and repository in closeout["create"]) or (milestone or {}).get("state") == "open":
                writes.append((f"close the milestone `{title}` in {repository}", repository,
                               lambda repository=repository: close_milestone(repository, milestones)))
    return writes


def closeout_notes(plan, version):
    """What the closeout leaves as it is, for the run log and the job summary."""
    closeout = plan["closeout"]
    if not closeout:
        return [f"The release column for Omnia {version} is no longer on the board; there is nothing more to close out."]
    notes = [f"Release column: `{plan['column']}`. Milestone: `{closeout['title']}`."]
    notes += [f"Kept its own milestone `{entry['content']['milestone']['title']}`: {describe(entry)}"
              for entry in closeout["kept"]]
    notes += [f"Moved to {RELEASED} only (not an issue: no milestone, not closed): {describe(entry)}"
              for entry in closeout["others"]]
    if closeout["already_closed"]:
        notes.append("Already closed, left as they are: " + ", ".join(map(describe, closeout["already_closed"])))
    if closeout["note_kept"]:
        notes.append(f"The release notification kept its own milestone `{closeout['note_kept']}`.")
    return notes


def run_writes(writes, version, number):
    """Make the writes in order; a failed write stops the ones after it and says what is done and what is pending."""
    done = []
    for description, repository, call in writes:
        try:
            call()
        except (GitHubError, ValueError) as error:
            denied = isinstance(error, GitHubError) and re.search(r"not accessible|forbidden|permission|\b403\b",
                                                                  str(error), re.IGNORECASE)
            # Issue and milestone writes need Issues access on their repository; the Project writes need only the
            # project permission the token already uses.
            hint = issue_access(repository) if repository and denied else ""
            answer = f"GitHub answered: `{error}`." if isinstance(error, GitHubError) else f"Stopped: {error}."
            summary = [f"### Omnia {version}: hotfix release notes sync incomplete",
                       ("Done in this run:\n\n" + "\n".join(f"- {line}" for line in done)) if done else
                       "Nothing was changed in Project 8 in this run.",
                       f"Still pending: {description}. {answer}"]
            if hint:
                summary.append(hint)
            summary.append(f"After fixing the cause, run this workflow again with `pr_number` {number}; "
                           "steps that are already done are skipped.")
            raise SyncIncomplete(f"Omnia {version}: {description} failed: {error}. {hint}".strip(),
                                 "\n\n".join(summary)) from None
        done.append(description)
    return done


def load_reviews(endpoint):
    reviews = []
    page = 1
    while True:
        batch = api(f"{endpoint}/reviews?per_page=100&page={page}")
        reviews.extend(batch)
        if len(batch) < 100:
            return reviews
        page += 1


def prepare(endpoint, pr, version, section):
    project, items = load_project()
    plan = plan_update(project, items, pr, version, section, recover_draft=lambda: draft_from_pr(endpoint, version))
    return plan, load_milestones(plan)


def sync(number, *, dry_run=False):
    endpoint = f"repos/{REPOSITORY}/pulls/{number}"
    pr = api(endpoint)
    version = release_version(pr)
    reviews = [] if pr.get("merged") else load_reviews(endpoint)
    if not is_approved(pr, reviews):
        print("No current approval to synchronize; Prod is unchanged.")
        return
    ref = pr["merge_commit_sha"] if pr.get("merged") else pr["head"]["sha"]
    content = api(f"repos/{REPOSITORY}/contents/{NOTES_PATH}?ref={ref}")
    section = extract_release(base64.b64decode(content["content"]).decode("utf-8-sig"), version)
    plan, milestones = prepare(endpoint, pr, version, section)
    latest = api(endpoint)
    if latest["head"]["sha"] != pr["head"]["sha"] or latest.get("merged") != pr.get("merged"):
        raise ValueError("PR changed during synchronization; no Project updates made")
    current_reviews = [] if latest.get("merged") else load_reviews(endpoint)
    if not is_approved(latest, current_reviews):
        print("Approval is no longer current; Prod is unchanged.")
        return
    if not dry_run:
        # Re-read the board and the milestones right before writing, so the writes follow the current state.
        plan, milestones = prepare(endpoint, pr, version, section)
    writes = plan_writes(plan, milestones)
    notes = closeout_notes(plan, version)
    if dry_run:
        print(f"Dry run for Omnia {version}: {len(writes)} planned write(s), none made.")
        for description, _, _ in writes:
            print(f"- would {description}")
        for note in notes:
            print(note)
        return
    done = run_writes(writes, version, number)
    converted = f"; converted to an {ISSUE_REPOSITORY} issue" if plan["convert"] else ""
    message = (f"Synchronized Omnia {version}: {plan['title']}; Status: {RELEASED}{converted}; "
               f"generated draft: {plan['draft_source']}")
    print(message)
    lines = [f"- {line}" for line in done] or ["- Nothing to write: Prod was already up to date."]
    for line in lines + notes:
        print(line)
    write_summary("\n\n".join([message, "Done in this run:\n\n" + "\n".join(lines), "\n\n".join(notes)]))


def write_summary(text):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as summary:
            summary.write(text.rstrip("\n") + "\n\n")


def annotate(message):
    """One GitHub Actions error annotation; the workflow-command format needs these characters escaped."""
    print("::error::" + message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A"))


if __name__ == "__main__":
    number = os.environ.get("PR_NUMBER", "")
    if not re.fullmatch(r"[1-9][0-9]*", number):
        raise SystemExit("PR_NUMBER must be a positive integer")
    try:
        sync(number, dry_run=os.environ.get("SYNC_DRY_RUN") == "true")
    except SyncIncomplete as failure:
        annotate(str(failure))
        write_summary(failure.summary)
        sys.exit(1)
    except (GitHubError, ValueError) as error:
        message = f"Release notes for PR #{number} were not synchronized: {error}"
        annotate(message)
        write_summary(message)
        sys.exit(1)
