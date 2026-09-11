#!/usr/bin/env bash

set -euo pipefail

ORG="omniaintranet"
PROJECT_NUMBER=8
STATUS_PREFIX="Wait for RN"
OUTPUT_FILE="/tmp/release.json"

response=$(
  gh api graphql -f query='
    query($org: String!, $projectNumber: Int!) {
      organization(login: $org) {
        projectV2(number: $projectNumber) {
          id
          title
          number
          fields(first: 50) {
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
        }
      }
    }
  ' -f org="$ORG" -F projectNumber="$PROJECT_NUMBER"
)

matches=$(
  echo "$response" |
    jq -c --arg prefix "$STATUS_PREFIX" '
      [
        .data.organization.projectV2.fields.nodes[]
        | select(.name == "Status")
        | .options[]
        | select(.name | startswith($prefix))
        | {
            statusId: .id,
            statusName: .name
          }
      ]
    '
)

count=$(echo "$matches" | jq 'length')

if [ "$count" -eq 0 ]; then
  echo "No releases waiting for release notes."

  jq -n \
    --argjson found false \
    '{
      found: $found,
      releases: []
    }' > "$OUTPUT_FILE"

  exit 0
fi

echo "Found $count release(s) waiting for release notes."

jq -n \
  --argjson found true \
  --argjson releases "$matches" \
  '{
    found: $found,
    releases: $releases
  }' > "$OUTPUT_FILE"

cat "$OUTPUT_FILE"