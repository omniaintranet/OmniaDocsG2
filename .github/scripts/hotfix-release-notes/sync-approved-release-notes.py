"""Synchronize approved documentation PR content to the existing Prod release item."""
import base64
import json
import os
import re
import subprocess
from pathlib import Path

REPOSITORY = "omniaintranet/OmniaDocsG2"
NOTES_PATH = "release-notes/7.0/versions.rst"
PUBLISHED_URL = "https://omnia-docs-g2.readthedocs.io/en/latest/release-notes/7.0/versions.html"
# Approved notifications become issues here, where the other Project 8 issues live (private repo).
ISSUE_OWNER, ISSUE_REPO = "omniaintranet", "OmniaMono"
# Shared with the bash scripts: what counts as a "waiting for release notes" column.
# The lookahead is the same end boundary wait-for-rn-lib.sh adds ("Wait for RNA" is not the column).
WAIT_FOR_RN = re.compile(
    Path(__file__).with_name("wait-for-rn-pattern.txt").read_text(encoding="utf-8").strip() + r"(?![A-Za-z0-9])",
    re.IGNORECASE)


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
    return json.loads(subprocess.check_output(
        args, input=json.dumps(payload) if payload else None,
        text=True, encoding="utf-8", env=env))


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


def approval_body(pr, section):
    state = "APPROVED AND MERGED" if pr.get("merged") else "APPROVED"
    publication = ("The documentation PR has been merged." if pr.get("merged") else
                   "These notes are approved; publication still requires merging the documentation PR.")
    return (f"> **{state}.** {publication}\n\n"
            f"[Review the documentation pull request]({pr['html_url']}).\n\n"
            f"[View the published hotfix release notes]({PUBLISHED_URL}).\n\n"
            f"## Approved release notes\n\n```text\n{section}\n```\n")


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


def plan_update(project, items, pr, version, section):
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
    return {"item": item, "field_id": field["id"], "options": options, "rename": rename,
            "convert": kind == "DraftIssue",
            "title": f"Release notes for Omnia {version} are approved",
            "body": approval_body(pr, section), "status": approved_name}


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
    plan = plan_update(project, items, pr, version, section)
    latest = api(endpoint)
    if latest["head"]["sha"] != pr["head"]["sha"] or latest.get("merged") != pr.get("merged"):
        raise ValueError("PR changed during synchronization; no Project updates made")
    current_reviews = [] if latest.get("merged") else load_reviews(endpoint)
    if not is_approved(latest, current_reviews):
        print("Approval is no longer current; Prod is unchanged.")
        return
    if not dry_run:
        item = plan["item"]["content"]
        if item["title"] != plan["title"] or item["body"] != plan["body"]:
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
        if plan["rename"]:
            api("graphql", query="""mutation($field: ID!, $options: [ProjectV2SingleSelectFieldOptionInput!]!) {
              updateProjectV2Field(input: {fieldId: $field, singleSelectOptions: $options}) {
                projectV2Field { ... on ProjectV2SingleSelectField { id } }
              }
            }""", variables={"field": plan["field_id"], "options": plan["options"]}, project=True)
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
    converted = (f"; {'would convert' if dry_run else 'converted'} to an {ISSUE_OWNER}/{ISSUE_REPO} issue"
                 if plan["convert"] else "")
    print(("Dry run: would synchronize" if dry_run else "Synchronized") +
          f" Omnia {version}: {plan['title']}; Status: {plan['status']}{converted}")


if __name__ == "__main__":
    number = os.environ.get("PR_NUMBER", "")
    if not re.fullmatch(r"[1-9][0-9]*", number):
        raise SystemExit("PR_NUMBER must be a positive integer")
    sync(number, dry_run=os.environ.get("SYNC_DRY_RUN") == "true")
