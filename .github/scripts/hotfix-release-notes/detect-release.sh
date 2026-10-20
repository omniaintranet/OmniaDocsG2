#!/usr/bin/env bash

set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/wait-for-rn-lib.sh"

ORG="omniaintranet"
PROJECT_NUMBER=8
OUTPUT_FILE="/tmp/release.json"
REQUESTED_STATUS="${RELEASE_STATUS:-}"

response=$(
  gh api graphql --paginate -f query='
    query($org: String!, $projectNumber: Int!, $endCursor: String) {
      organization(login: $org) {
        projectV2(number: $projectNumber) {
          items(first: 100, after: $endCursor) {
            pageInfo {
              hasNextPage
              endCursor
            }
            nodes {
              fieldValues(first: 50) {
                nodes {
                  ... on ProjectV2ItemFieldSingleSelectValue {
                    name
                    optionId
                    field {
                      ... on ProjectV2SingleSelectField {
                        name
                      }
                    }
                  }
                }
              }
              content {
                ... on Issue {
                  number
                }
              }
            }
          }
        }
      }
    }
  ' -f org="$ORG" -F projectNumber="$PROJECT_NUMBER"
)

matches=$(
  printf '%s\n' "$response" |
    jq -s -c \
      --arg waitPattern "$WAIT_FOR_RN_PATTERN" \
      --arg requestedStatus "$REQUESTED_STATUS" '
      [
        .[]
        | .data.organization.projectV2.items.nodes[]
        | select(.content.number != null)
        | .fieldValues.nodes[]
        | select(.field.name == "Status")
        | select(
            if $requestedStatus == "" then
              (.name // "") | test($waitPattern; "i")
            else
              .name == $requestedStatus
            end
          )
        | {
            statusId: .optionId,
            statusName: .name
          }
      ]
      | sort_by(.statusName, .statusId)
      | group_by(.statusId)
      | map({
          statusId: .[0].statusId,
          statusName: .[0].statusName,
          issueCount: length
        })
    '
)

count=$(printf '%s\n' "$matches" | jq 'length')

if [ "$count" -eq 0 ]; then
  if [ -n "$REQUESTED_STATUS" ]; then
    echo "The requested status has no project issues: $REQUESTED_STATUS"
  else
    echo "No releases waiting for release notes."
    echo "Status columns seen on project items (none matched the Wait-for-RN pattern '$WAIT_FOR_RN_PATTERN'):"
    printf '%s\n' "$response" |
      jq -s -r '
        [
          .[]
          | .data.organization.projectV2.items.nodes[]
          | select(.content.number != null)
          | .fieldValues.nodes[]
          | select(.field.name == "Status")
          | .name
        ]
        | unique
        | if length == 0 then ["(none)"] else . end
        | .[]
        | "- \(.)"
      '
    echo "If the release column was renamed, extend .github/scripts/hotfix-release-notes/wait-for-rn-pattern.txt."
  fi

  if [ -n "${GITHUB_OUTPUT:-}" ]; then
    echo "found=false" >> "$GITHUB_OUTPUT"
  fi

  jq -n \
    --argjson found false \
    '{
      found: $found,
      releases: []
    }' > "$OUTPUT_FILE"

  exit 0
fi

if [ "$count" -gt 1 ]; then
  echo "More than one populated release is waiting for release notes:" >&2
  printf '%s\n' "$matches" |
    jq -r '.[] | "- \(.statusName): \(.issueCount) issue(s)"' >&2
  echo "Resolve the project statuses or dispatch the workflow with an exact release_status value." >&2

  if [ -n "${GITHUB_OUTPUT:-}" ]; then
    echo "found=false" >> "$GITHUB_OUTPUT"
  fi

  jq -n \
    --argjson found false \
    --argjson releases "$matches" \
    '{
      found: $found,
      releases: $releases
    }' > "$OUTPUT_FILE"

  exit 1
fi

status_name=$(printf '%s\n' "$matches" | jq -r '.[0].statusName')
issue_count=$(printf '%s\n' "$matches" | jq -r '.[0].issueCount')

if [[ ! "$status_name" =~ Omnia[[:space:]]+[0-9]+\.[0-9]+\.[0-9]+ ]]; then
  echo "The populated release status does not contain a concrete Omnia patch version:" >&2
  echo "$status_name" >&2
  echo "Rename the project status with the approved component versions before retrying." >&2

  if [ -n "${GITHUB_OUTPUT:-}" ]; then
    echo "found=false" >> "$GITHUB_OUTPUT"
  fi

  exit 1
fi

echo "Found one release waiting for release notes: $status_name ($issue_count issue(s))."

if [ -n "${GITHUB_OUTPUT:-}" ]; then
  echo "found=true" >> "$GITHUB_OUTPUT"
fi

jq -n \
  --argjson found true \
  --argjson releases "$matches" \
  '{
    found: $found,
    releases: $releases
  }' > "$OUTPUT_FILE"
