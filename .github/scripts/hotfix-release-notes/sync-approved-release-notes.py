"""Synchronize approved documentation PR content to the existing Prod release item."""
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
ISSUE_ACCESS = (f"The project token (secret {TOKEN_SECRET}) needs the repository permission "
                f"Issues: Read and write on {ISSUE_OWNER}/{ISSUE_REPO}.")
# GitHub rejects issue and draft-issue bodies over 65,536 characters; keep a margin.
MAX_BODY = 65000
# The generated draft (the recommendation) is kept below the approved notes between these markers,
# so a repeated sync finds it again and neither nests nor duplicates it.
DRAFT_START = "<!-- hotfix-release-notes:generated-draft:start -->"
DRAFT_END = "<!-- hotfix-release-notes:generated-draft:end -->"
DRAFT_CUT = "<!-- hotfix-release-notes:generated-draft:cut -->"
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


def api(endpoint, *, query=None, variables=None, project=False):
    args = ["gh", "api", endpoint]
    if query:
        payload = {"query": query, "variables": variables or {}}
        args += ["--input", "-"]
    else:
        payload = None
    env = dict(os.environ)
    if project and env.get("PROJECT_TOKEN"):
        env["GH_TOKEN"] = env["PROJECT_TOKEN"]
    result = subprocess.run(args, input=json.dumps(payload) if payload else None, capture_output=True,
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

    A body written by this sync carries the draft between markers: it is reused as it is (idempotent).
    A body still as create-ready-project-item.sh wrote it is the draft itself.
    """
    body = (body or "").replace("\r\n", "\n")
    start, end = body.find(DRAFT_START), body.rfind(DRAFT_END)
    if start != -1 and end > start:
        return body[start + len(DRAFT_START):end].strip("\n")
    if "**DRAFT - NOT APPROVED.**" in body and "## Generated draft release notes" in body:
        return demote_headings(body.strip())
    return None


def fit_draft(draft, room, pr_url):
    """Cut the draft at a line boundary so it takes at most room characters, closing an open code fence."""
    if len(draft) <= room:
        return draft
    if DRAFT_CUT in draft:
        draft = draft[:draft.find(DRAFT_CUT)].rstrip("\n")
    note = (f"\n{DRAFT_CUT}\n_The draft was cut here to stay within GitHub's size limit for issue descriptions. "
            f"The full draft release notes are in the first commit of the [documentation pull request]({pr_url})._")
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
      id name options { id name color description }
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
          ... on Issue { id title body repository { nameWithOwner } }
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
    if kind == "Issue" and (item["content"].get("repository") or {}).get("nameWithOwner") != f"{ISSUE_OWNER}/{ISSUE_REPO}":
        raise ValueError(f"The Prod notification is an issue outside {ISSUE_OWNER}/{ISSUE_REPO}")
    if not re.search(re.escape(pr["html_url"]) + r"(?=[)\s]|$)", item["content"]["body"]):
        raise ValueError("The Prod notification is not linked to this documentation PR")
    fields = [field for field in project["fields"]["nodes"] if field.get("name") == "Status"]
    if len(fields) != 1 or not item.get("status"):
        raise ValueError("Cannot identify the release notification's Status option")
    field = fields[0]
    option_id = item["status"]["optionId"]
    options = [dict(option) for option in field["options"]]
    matching = [option for option in options if option["id"] == option_id]
    if len(matching) != 1:
        raise ValueError("Cannot identify the release column")
    option = matching[0]
    if not re.search(r"\bOmnia\s+" + re.escape(version) + r"(?=\s|/|$)", option["name"]):
        raise ValueError("The release column does not match the PR version")
    approved_name = option["name"]
    label = WAIT_FOR_RN.match(approved_name)
    if label:
        # Same separator rule as strip_wait_for_rn_prefix, so "[Wait for RN] X" becomes "Approved - X".
        approved_name = "Approved - " + re.sub(r"^[^A-Za-z0-9(]+", "", approved_name[label.end():]).rstrip()
    if not re.match(r"^Approved(?![A-Za-z0-9])", approved_name):
        raise ValueError("Expected a Wait for RN or Approved release column")
    if any(other["id"] != option_id and other["name"] == approved_name for other in options):
        raise ValueError("An Approved column already exists separately; manual reconciliation required")
    rename = option["name"] != approved_name
    option["name"] = approved_name
    draft = kept_draft(item["content"]["body"])
    draft_source = "kept from the notification" if draft is not None else "not available"
    if draft is None and recover_draft:
        draft = recover_draft()
        draft_source = "recovered from the documentation PR's first commit"
    return {"item": item, "field_id": field["id"], "options": options, "rename": rename,
            "convert": kind == "DraftIssue",
            "title": f"Release notes for Omnia {version} are approved",
            "body": approval_body(pr, section, draft), "status": approved_name, "draft_source": draft_source}


def load_reviews(endpoint):
    reviews = []
    page = 1
    while True:
        batch = api(f"{endpoint}/reviews?per_page=100&page={page}")
        reviews.extend(batch)
        if len(batch) < 100:
            return reviews
        page += 1


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
    project, items = load_project()
    plan = plan_update(project, items, pr, version, section, recover_draft=lambda: draft_from_pr(endpoint, version))
    latest = api(endpoint)
    if latest["head"]["sha"] != pr["head"]["sha"] or latest.get("merged") != pr.get("merged"):
        raise ValueError("PR changed during synchronization; no Project updates made")
    current_reviews = [] if latest.get("merged") else load_reviews(endpoint)
    if not is_approved(latest, current_reviews):
        print("Approval is no longer current; Prod is unchanged.")
        return
    if not dry_run:
        write_project(plan, version, number)
    converted = (f"; {'would convert' if dry_run else 'converted'} to an {ISSUE_OWNER}/{ISSUE_REPO} issue"
                 if plan["convert"] else "")
    message = (("Dry run: would synchronize" if dry_run else "Synchronized") +
               f" Omnia {version}: {plan['title']}; Status: {plan['status']}{converted}; "
               f"generated draft: {plan['draft_source']}")
    print(message)
    if not dry_run:
        write_summary(message)


def write_project(plan, version, number):
    """Update the notes, then rename the column, then convert; a failed step stops the ones after it."""
    item = plan["item"]["content"]
    is_issue = item["__typename"] == "Issue"
    steps = [("update", "the approved release notes, with the generated draft kept below them"),
             ("rename", f"the release column `{plan['status']}`"),
             ("convert", f"the conversion to an {ISSUE_OWNER}/{ISSUE_REPO} issue")]
    current = 0
    try:
        if item["title"] != plan["title"] or item["body"] != plan["body"]:
            if is_issue:
                api("graphql", query="""mutation($id: ID!, $title: String!, $body: String!) {
                  updateIssue(input: {id: $id, title: $title, body: $body}) { issue { id } }
                }""", variables={"id": item["id"], "title": plan["title"], "body": plan["body"]}, project=True)
            else:
                api("graphql", query="""mutation($id: ID!, $title: String!, $body: String!) {
                  updateProjectV2DraftIssue(input: {draftIssueId: $id, title: $title, body: $body}) {
                    draftIssue { id }
                  }
                }""", variables={"id": item["id"], "title": plan["title"], "body": plan["body"]}, project=True)
        current = 1
        if plan["rename"]:
            api("graphql", query="""mutation($field: ID!, $options: [ProjectV2SingleSelectFieldOptionInput!]!) {
              updateProjectV2Field(input: {fieldId: $field, singleSelectOptions: $options}) {
                projectV2Field { ... on ProjectV2SingleSelectField { id } }
              }
            }""", variables={"field": plan["field_id"], "options": plan["options"]}, project=True)
        current = 2
        # Convert only after the column is Approved: detect-release.sh reads repository issues
        # in Wait for RN columns, so the notification must never be an issue while it sits there.
        if plan["convert"]:
            repository = api("graphql", query="""query($owner: String!, $name: String!) {
              repository(owner: $owner, name: $name) { id }
            }""", variables={"owner": ISSUE_OWNER, "name": ISSUE_REPO}, project=True)["data"]["repository"]["id"]
            api("graphql", query="""mutation($item: ID!, $repository: ID!) {
              convertProjectV2DraftIssueItemToIssue(input: {itemId: $item, repositoryId: $repository}) {
                item { id }
              }
            }""", variables={"item": plan["item"]["id"], "repository": repository}, project=True)
    except GitHubError as error:
        name, pending = steps[current]
        done = [description for _, description in steps[:current]]
        # Writing an OmniaMono issue (the conversion, or updating a notification that is already an issue)
        # needs Issues access on OmniaMono; the Project writes need only the project permission.
        issue_write = name == "convert" or (name == "update" and is_issue)
        denied = re.search(r"not accessible|forbidden|permission|\b403\b", str(error), re.IGNORECASE)
        hint = ISSUE_ACCESS if issue_write and denied else ""
        summary = [f"### Omnia {version}: hotfix release notes sync incomplete",
                   ("Up to date in Project 8: " + "; ".join(done) + ".") if done else "Nothing was changed in Project 8.",
                   f"Still pending: {pending}. GitHub answered: `{error}`."]
        if hint:
            summary.append(hint)
        summary.append(f"After fixing the cause, run this workflow again with `pr_number` {number}; "
                       "steps that are already done are skipped.")
        raise SyncIncomplete(f"Omnia {version}: {pending} failed: {error}. {hint}".strip(),
                             "\n\n".join(summary)) from None


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
