#!/usr/bin/env bash

set -euo pipefail

ORG="omniaintranet"
PROJECT_NUMBER=8
INPUT_FILE="/tmp/release-issues.json"
GENERATED_FILE="/tmp/generated-release-notes.rst"
AUDIT_FILE="/tmp/release-notes-audit.json"

if [ ! -s "$INPUT_FILE" ]; then
  echo "Release issue data is missing or empty: $INPUT_FILE" >&2
  exit 1
fi

if [ ! -s "$GENERATED_FILE" ]; then
  echo "Generated release notes are missing or empty: $GENERATED_FILE" >&2
  exit 1
fi

if [ ! -s "$AUDIT_FILE" ]; then
  echo "Release-note audit data is missing or empty: $AUDIT_FILE" >&2
  exit 1
fi

if [ -z "${GH_TOKEN:-}" ]; then
  echo "GH_TOKEN is required to create the Project 8 notification." >&2
  exit 1
fi

if [[ ! "${RELEASE_NOTES_URL:-}" =~ ^https://omnia-docs-g2\.readthedocs\.io/ ]]; then
  echo "RELEASE_NOTES_URL must use the Omnia documentation site." >&2
  exit 1
fi

release_count=$(jq '.releases | length' "$INPUT_FILE")

if [ "$release_count" -ne 1 ]; then
  echo "Expected exactly one selected release; found $release_count." >&2
  exit 1
fi

status_name=$(jq -r '.releases[0].statusName' "$INPUT_FILE")

if [[ ! "$status_name" =~ ^Wait[[:space:]]+for[[:space:]]+RN ]]; then
  echo "The selected release is not a Wait for RN status." >&2
  exit 1
fi

if [[ "$status_name" =~ Omnia[[:space:]]+([0-9]+\.[0-9]+\.[0-9]+) ]]; then
  omnia_version="${BASH_REMATCH[1]}"
else
  echo "The selected Wait for RN status does not contain a concrete Omnia version." >&2
  exit 1
fi

issue_title="Release notes for Omnia ${omnia_version} are now ready"

source_issue_count=$(jq '.releases[0].issues | length' "$INPUT_FILE")
included_issue_count=$(jq '[.bullets[].sourceIssues[]] | length' "$AUDIT_FILE")
bullet_count=$(jq '.bullets | length' "$AUDIT_FILE")
omitted_issue_count=$(jq '.omittedIssues | length' "$AUDIT_FILE")

issue_body_file=$(mktemp)
trap 'rm -f "$issue_body_file"' EXIT

{
  printf '> [!WARNING]\n'
  printf '> **DRAFT - NOT APPROVED.** These release notes were generated automatically and must be reviewed before publication.\n\n'
  printf 'Generated from **%s** source issues: **%s** represented in **%s** draft bullets and **%s** omitted.\n\n' \
    "$source_issue_count" \
    "$included_issue_count" \
    "$bullet_count" \
    "$omitted_issue_count"
  printf '[View the currently published Omnia hotfix release notes](%s). The draft below will not appear there until its pull request is approved and merged.\n\n' \
    "$RELEASE_NOTES_URL"
  printf '## Generated draft release notes\n\n'
  printf '```text\n'
  cat "$GENERATED_FILE"
  printf '\n```\n\n'
  printf '## Issues not included in the draft\n\n'

  if [ "$omitted_issue_count" -eq 0 ]; then
    printf -- '- None. Every source issue is represented in the generated draft.\n'
  else
    jq -r --slurpfile releaseData "$INPUT_FILE" '
      .omittedIssues[] as $omitted
      | $releaseData[0].releases[0].issues[]
      | select(
          .repositoryWithOwner == $omitted.repositoryWithOwner
          and .number == $omitted.number
        )
      | "- [\(.repositoryWithOwner)#\(.number)](\(.url)) - \($omitted.reason)"
    ' "$AUDIT_FILE"
  fi
} > "$issue_body_file"

if [ "$(wc -c < "$issue_body_file")" -gt 60000 ]; then
  echo "The generated Project notification exceeds the safe GitHub body size." >&2
  exit 1
fi

issue_body=$(cat "$issue_body_file")

# Use a Project draft issue so this notification cannot be selected as release-note
# source material: detect-release.sh intentionally processes repository issues only.
project_response=$(
  gh api graphql --paginate -f query='
    query($org: String!, $projectNumber: Int!, $endCursor: String) {
      organization(login: $org) {
        projectV2(number: $projectNumber) {
          id
          fields(first: 100) {
            nodes {
              ... on ProjectV2SingleSelectField {
                id
                name
                options {
                  id
                  name
                }
              }
            }
          }
          items(first: 100, after: $endCursor) {
            pageInfo {
              hasNextPage
              endCursor
            }
            nodes {
              id
              content {
                __typename
                ... on DraftIssue {
                  id
                  title
                }
              }
            }
          }
        }
      }
    }
  ' -f org="$ORG" -F projectNumber="$PROJECT_NUMBER"
)

project_id=$(printf '%s\n' "$project_response" | jq -s -r '.[0].data.organization.projectV2.id // empty')
status_field_id=$(
  printf '%s\n' "$project_response" |
    jq -s -r '
      .[0].data.organization.projectV2.fields.nodes[]
      | select(.name == "Status")
      | .id
    '
)
status_option_id=$(
  printf '%s\n' "$project_response" |
    jq -s -r --arg statusName "$status_name" '
      .[0].data.organization.projectV2.fields.nodes[]
      | select(.name == "Status")
      | .options[]
      | select(.name == $statusName)
      | .id
    '
)

if [ -z "$project_id" ] || [ -z "$status_field_id" ] || [ -z "$status_option_id" ]; then
  echo "Could not resolve Project 8 and the exact selected status option." >&2
  exit 1
fi

existing_items=$(
  printf '%s\n' "$project_response" |
    jq -s -c --arg issueTitle "$issue_title" '
      [
        .[]
        | .data.organization.projectV2.items.nodes[]
        | select(.content.__typename == "DraftIssue")
        | select(.content.title == $issueTitle)
        | {
            itemId: .id,
            draftIssueId: .content.id
          }
      ]
    '
)
existing_count=$(jq 'length' <<< "$existing_items")

if [ "$existing_count" -gt 1 ]; then
  echo "Project 8 contains duplicate release-ready notifications for Omnia $omnia_version." >&2
  exit 1
fi

if [ "$existing_count" -eq 1 ]; then
  item_id=$(jq -r '.[0].itemId' <<< "$existing_items")
  draft_issue_id=$(jq -r '.[0].draftIssueId' <<< "$existing_items")

  gh api graphql \
    -f query='
      mutation($draftIssueId: ID!, $title: String!, $body: String!) {
        updateProjectV2DraftIssue(
          input: {
            draftIssueId: $draftIssueId
            title: $title
            body: $body
          }
        ) {
          draftIssue {
            id
          }
        }
      }
    ' \
    -f draftIssueId="$draft_issue_id" \
    -f title="$issue_title" \
    -f body="$issue_body" \
    >/dev/null

  action="Updated"
else
  create_response=$(
    gh api graphql \
      -f query='
        mutation($projectId: ID!, $title: String!, $body: String!) {
          addProjectV2DraftIssue(
            input: {
              projectId: $projectId
              title: $title
              body: $body
            }
          ) {
            projectItem {
              id
            }
          }
        }
      ' \
      -f projectId="$project_id" \
      -f title="$issue_title" \
      -f body="$issue_body"
  )

  item_id=$(printf '%s\n' "$create_response" | jq -r '.data.addProjectV2DraftIssue.projectItem.id // empty')

  if [ -z "$item_id" ]; then
    echo "GitHub did not return the created Project 8 item ID." >&2
    exit 1
  fi

  action="Created"
fi

gh api graphql \
  -f query='
    mutation(
      $projectId: ID!
      $itemId: ID!
      $fieldId: ID!
      $optionId: String!
    ) {
      updateProjectV2ItemFieldValue(
        input: {
          projectId: $projectId
          itemId: $itemId
          fieldId: $fieldId
          value: {
            singleSelectOptionId: $optionId
          }
        }
      ) {
        projectV2Item {
          id
        }
      }
    }
  ' \
  -f projectId="$project_id" \
  -f itemId="$item_id" \
  -f fieldId="$status_field_id" \
  -f optionId="$status_option_id" \
  >/dev/null

gh api graphql \
  -f query='
    mutation($projectId: ID!, $itemId: ID!) {
      updateProjectV2ItemPosition(
        input: {
          projectId: $projectId
          itemId: $itemId
          afterId: null
        }
      ) {
        items(first: 1) {
          nodes {
            id
          }
        }
      }
    }
  ' \
  -f projectId="$project_id" \
  -f itemId="$item_id" \
  >/dev/null

echo "$action Project 8 notification for Omnia $omnia_version in status: $status_name"
