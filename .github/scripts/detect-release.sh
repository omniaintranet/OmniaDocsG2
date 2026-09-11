#!/usr/bin/env bash

set -euo pipefail

ORG="omniaintranet"
PROJECT_NUMBER=8
STATUS_PREFIX="Wait for RN"

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
    jq -r --arg prefix "$STATUS_PREFIX" '
      .data.organization.projectV2.fields.nodes[]
      | select(.name == "Status")
      | .options[]
      | select(.name | startswith($prefix))
      | .name
    '
)

if [ -z "$matches" ]; then
  echo "No releases waiting for release notes."
  exit 0
fi

echo "Found release(s) waiting for release notes:"
echo "$matches"