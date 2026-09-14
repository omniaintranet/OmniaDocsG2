#!/usr/bin/env bash

set -euo pipefail

ORG="omniaintranet"
PROJECT_NUMBER=8

INPUT_FILE="/tmp/release.json"
OUTPUT_FILE="/tmp/release-issues.json"

if [ ! -f "$INPUT_FILE" ]; then
  echo "Input file not found: $INPUT_FILE"
  exit 1
fi

found=$(jq -r '.found' "$INPUT_FILE")

if [ "$found" != "true" ]; then
  echo "No release waiting for release notes."

  jq -n \
    '{
      releases: []
    }' > "$OUTPUT_FILE"

  exit 0
fi

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
                  title
                  body
                  url
                  updatedAt
                  labels(first: 100) {
                    nodes {
                      name
                    }
                  }
                  comments(last: 50) {
                    nodes {
                      author {
                        login
                      }
                      body
                      createdAt
                    }
                  }
                  repository {
                    name
                    nameWithOwner
                  }
                }
              }
            }
          }
        }
      }
    }
  ' \
  -f org="$ORG" \
  -F projectNumber="$PROJECT_NUMBER"
)

releases='[]'

while IFS= read -r release; do
  status_id=$(echo "$release" | jq -r '.statusId')
  status_name=$(echo "$release" | jq -r '.statusName')

  issues=$(
    printf '%s\n' "$response" |
      jq -s -c --arg statusId "$status_id" '
        [
          .[]
          | .data.organization.projectV2.items.nodes[]
          | select(
              any(
                .fieldValues.nodes[];
                .field.name == "Status"
                and .optionId == $statusId
              )
            )
          | select(.content != null)
          | select(.content.number != null)
          | {
              number: .content.number,
              title: .content.title,
              body: (.content.body // ""),
              url: .content.url,
              updatedAt: .content.updatedAt,
              labels: [.content.labels.nodes[]?.name],
              comments: [
                .content.comments.nodes[]?
                | {
                    author: (.author.login // ""),
                    createdAt: .createdAt,
                    body: (.body // "")
                  }
              ],
              repository: .content.repository.name,
              repositoryWithOwner: .content.repository.nameWithOwner
            }
        ]
      '
  )

  release_result=$(
    jq -n \
      --arg statusId "$status_id" \
      --arg statusName "$status_name" \
      --argjson issues "$issues" \
      '{
        statusId: $statusId,
        statusName: $statusName,
        issues: $issues
      }'
  )

  releases=$(
    jq -n \
      --argjson existing "$releases" \
      --argjson newRelease "$release_result" \
      '$existing + [$newRelease]'
  )

done < <(jq -c '.releases[]' "$INPUT_FILE")

jq -n \
  --argjson releases "$releases" \
  '{
    releases: $releases
  }' > "$OUTPUT_FILE"

total_issue_count=$(jq '[.releases[].issues | length] | add // 0' "$OUTPUT_FILE")
echo "Retrieved $total_issue_count issue(s) for release-note generation."
jq -r '.releases[] | "- \(.statusName): \(.issues | length) issue(s)"' "$OUTPUT_FILE"
