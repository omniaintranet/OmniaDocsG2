#!/usr/bin/env bash

set -euo pipefail

INPUT_FILE="/tmp/release-issues.json"
GENERATED_FILE="/tmp/generated-release-notes.rst"

if [ ! -f "$INPUT_FILE" ]; then
  echo "Input file not found: $INPUT_FILE"
  exit 1
fi

if [ ! -f "$GENERATED_FILE" ]; then
  echo "Generated release notes not found: $GENERATED_FILE"
  exit 1
fi

if [ -z "${RELEASE_NOTES_FILE:-}" ]; then
  echo "RELEASE_NOTES_FILE is not configured."
  exit 1
fi

status_name=$(jq -r '.releases[0].statusName' "$INPUT_FILE")

omnia_version=$(
  echo "$status_name" |
    sed -n 's/^Wait for RN Omnia \([^ /]*\).*/\1/p'
)

if [ -z "$omnia_version" ]; then
  echo "Could not extract the Omnia version from:"
  echo "$status_name"
  exit 1
fi

branch_name="hotfix-release-notes-${omnia_version}"
pr_title="Release notes ${omnia_version}"

echo "Version: $omnia_version"
echo "Branch: $branch_name"
echo "Release notes file: $RELEASE_NOTES_FILE"

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

git checkout -b "$branch_name"

if [ ! -f "$RELEASE_NOTES_FILE" ]; then
  echo "Target release notes file does not exist:"
  echo "$RELEASE_NOTES_FILE"
  exit 1
fi

temp_file=$(mktemp)

cat "$GENERATED_FILE" > "$temp_file"
printf '\n\n' >> "$temp_file"
cat "$RELEASE_NOTES_FILE" >> "$temp_file"

mv "$temp_file" "$RELEASE_NOTES_FILE"

git add "$RELEASE_NOTES_FILE"

if git diff --cached --quiet; then
  echo "No release-note changes detected."
  exit 0
fi

git commit -m "Add release notes for ${omnia_version}"

git push --set-upstream origin "$branch_name"

existing_pr=$(
  gh pr list \
    --head "$branch_name" \
    --state open \
    --json number \
    --jq '.[0].number // empty'
)

if [ -n "$existing_pr" ]; then
  echo "Draft PR already exists: #$existing_pr"
  exit 0
fi

gh pr create \
  --draft \
  --title "$pr_title" \
  --body "Automatically generated draft release notes for Omnia ${omnia_version}." \
  --head "$branch_name"

echo "Draft PR created successfully."