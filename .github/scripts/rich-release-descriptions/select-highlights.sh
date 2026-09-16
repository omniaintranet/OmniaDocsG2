#!/usr/bin/env bash

set -euo pipefail

ORG="omniaintranet"
PROJECT_NUMBER=18
OUTPUT_FILE="/tmp/release-highlights.json"
REQUESTED_VERSION="${RELEASE_VERSION:-}"

if [ -z "${GH_TOKEN:-}" ]; then
  echo "GH_TOKEN is required to read the Omnia preproduction project." >&2
  exit 1
fi

if [ -n "$REQUESTED_VERSION" ] && [[ ! "$REQUESTED_VERSION" =~ ^[0-9]+\.[0-9]+$ ]]; then
  echo "RELEASE_VERSION must use the major.minor format, for example 7.12." >&2
  exit 1
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
                    field {
                      ... on ProjectV2SingleSelectField {
                        name
                      }
                    }
                  }
                }
              }
              content {
                __typename
                ... on Issue {
                  title
                  body
                  issueType {
                    name
                  }
                  labels(first: 100) {
                    nodes {
                      name
                    }
                  }
                  comments(last: 10) {
                    nodes {
                      body
                      createdAt
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  ' -f org="$ORG" -F projectNumber="$PROJECT_NUMBER"
)

records=$(
  printf '%s\n' "$response" |
    jq -s -c '
      [
        .[]
        | .data.organization.projectV2.items.nodes[]
        | ([
            .fieldValues.nodes[]?
            | select(.field.name == "Status")
            | .name
          ][0] // "") as $statusName
        | ($statusName
            | capture("^(?<state>Approved|Done) (?<version>[0-9]+\\.[0-9]+) Sprint (?<sprint>[0-9]+)$"; "i")) as $status
        | select(.content.__typename == "Issue")
        | select(
            (((.content.issueType.name // "") | ascii_downcase) == "feature")
            or any(
              .content.labels.nodes[]?;
              (((.name // "") | ascii_downcase) == "feature")
              or (((.name // "") | ascii_downcase) == "features")
            )
          )
        | {
            releaseVersion: $status.version,
            sprintNumber: ($status.sprint | tonumber),
            statusName: $statusName,
            sourceTitle: (.content.title // ""),
            sourceBody: ((.content.body // "")[0:20000]),
            comments: [
              .content.comments.nodes[]?
              | {
                  createdAt: .createdAt,
                  body: ((.body // "")[0:4000])
                }
            ]
          }
      ]
    '
)

available_versions=$(jq -c '[.[].releaseVersion] | unique' <<< "$records")
available_version_count=$(jq 'length' <<< "$available_versions")

if [ -n "$REQUESTED_VERSION" ]; then
  if ! jq -e --arg requestedVersion "$REQUESTED_VERSION" \
      'any(.[]; .releaseVersion == $requestedVersion)' <<< "$records" >/dev/null; then
    echo "No Feature issues were found for release $REQUESTED_VERSION in matching Approved or Done sprint statuses." >&2
    exit 1
  fi

  release_version="$REQUESTED_VERSION"
elif [ "$available_version_count" -eq 0 ]; then
  echo "No Feature issues were found in Approved or Done versioned sprint statuses."
  echo "found=false" >> "${GITHUB_OUTPUT:-/dev/null}"
  jq -n '{releaseVersion: "", statuses: [], highlights: []}' > "$OUTPUT_FILE"
  exit 0
elif [ "$available_version_count" -gt 1 ]; then
  echo "Feature issues exist for more than one release version:" >&2
  jq -r '.[] | "- " + .' <<< "$available_versions" >&2
  echo "Dispatch the workflow again with an exact major.minor release_version." >&2
  exit 1
else
  release_version=$(jq -r '.[0]' <<< "$available_versions")
fi

selected_records=$(
  jq -c \
    --arg releaseVersion "$release_version" '
      [
        .[]
        | select(.releaseVersion == $releaseVersion)
      ]
      | sort_by([.sprintNumber, .statusName, .sourceTitle])
      | to_entries
      | map(.value + {highlightId: (.key + 1)})
    ' <<< "$records"
)

highlight_count=$(jq 'length' <<< "$selected_records")

if [ "$highlight_count" -gt 25 ]; then
  echo "Release $release_version contains $highlight_count Feature candidates; the safe automation limit is 25." >&2
  exit 1
fi

body_file=$(mktemp)
candidate_file=$(mktemp)
highlights_file=$(mktemp)
sanitized_body_file=$(mktemp)
screenshot_file=$(mktemp)
updated_file=$(mktemp)
statuses_file=$(mktemp)
trap 'rm -f "$body_file" "$candidate_file" "$highlights_file" "$sanitized_body_file" "$screenshot_file" "$updated_file" "$statuses_file"' EXIT

extract_screenshot_section() {
  awk '
    {
      line = $0
      sub(/\r$/, "", line)
      sub(/[[:space:]]+$/, "", line)
      normalized = tolower(line)

      if (normalized ~ /^##[[:space:]]+public screenshots?$/) {
        capture = 1
        next
      }

      if (capture && line ~ /^##[[:space:]]+/) {
        exit
      }

      if (capture) {
        print line
      }
    }
  ' "$body_file"
}

strip_screenshot_section() {
  awk '
    {
      line = $0
      sub(/\r$/, "", line)
      comparison = line
      sub(/[[:space:]]+$/, "", comparison)
      normalized = tolower(comparison)

      if (normalized ~ /^##[[:space:]]+public screenshots?$/) {
        skip = 1
        next
      }

      if (skip && comparison ~ /^##[[:space:]]+/) {
        skip = 0
      }

      if (!skip) {
        print line
      }
    }
  ' "$body_file"
}

printf '[]\n' > "$highlights_file"

for ((candidate_index = 0; candidate_index < highlight_count; candidate_index++)); do
  candidate=$(jq -c --argjson index "$candidate_index" '.[$index]' <<< "$selected_records")
  jq -r '.sourceBody' <<< "$candidate" > "$body_file"

  screenshot_section_count=$(grep -Eic '^##[[:space:]]+public screenshots?[[:space:]]*$' "$body_file" || true)

  if [ "$screenshot_section_count" -gt 1 ]; then
    echo "A Feature issue contains more than one Public screenshot section." >&2
    exit 1
  fi

  extract_screenshot_section > "$screenshot_file"

  if [ "$screenshot_section_count" -eq 1 ] && \
     ! grep -q '[^[:space:]]' "$screenshot_file"; then
    echo "A declared Public screenshot section does not contain an image." >&2
    exit 1
  fi

  strip_screenshot_section > "$sanitized_body_file"

  candidate=$(
    jq -c \
      --rawfile sourceBody "$sanitized_body_file" \
      --rawfile screenshots "$screenshot_file" \
      '.sourceBody = $sourceBody | . + {screenshotMarkdown: $screenshots}' \
      <<< "$candidate"
  )
  printf '%s\n' "$candidate" > "$candidate_file"
  jq -s '.[0] + [.[1]]' "$highlights_file" "$candidate_file" > "$updated_file"
  mv "$updated_file" "$highlights_file"
done

jq '[.[].statusName] | unique' "$highlights_file" > "$statuses_file"

jq -n \
  --arg releaseVersion "$release_version" \
  --slurpfile statuses "$statuses_file" \
  --slurpfile highlights "$highlights_file" \
  '{
    releaseVersion: $releaseVersion,
    statuses: $statuses[0],
    highlights: $highlights[0]
  }' > "$OUTPUT_FILE"

echo "found=true" >> "${GITHUB_OUTPUT:-/dev/null}"
echo "Selected $highlight_count Feature candidate(s) for release $release_version from $(jq 'length' "$statuses_file") Approved/Done sprint status(es)."
