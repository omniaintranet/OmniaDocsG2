#!/usr/bin/env bash

set -euo pipefail

ORG="omniaintranet"
PROJECT_NUMBER=8
INPUT_FILE="/tmp/release-issues.json"

if [ ! -s "$INPUT_FILE" ]; then
  echo "Release issue data is missing or empty: $INPUT_FILE" >&2
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
issue_body=$(
  printf 'The release notes for Omnia %s are now ready.\n\n[View the Omnia hotfix release notes](%s)\n' \
    "$omnia_version" \
    "$RELEASE_NOTES_URL"
)

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
