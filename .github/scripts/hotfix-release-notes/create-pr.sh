#!/usr/bin/env bash

set -euo pipefail

INPUT_FILE="/tmp/release-issues.json"
GENERATED_FILE="/tmp/generated-release-notes.rst"
VALIDATOR_FILE=".github/scripts/hotfix-release-notes/validate-release-notes.sh"

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

if [ ! -f "$VALIDATOR_FILE" ]; then
  echo "Release-note validator not found: $VALIDATOR_FILE"
  exit 1
fi

bash "$VALIDATOR_FILE" "$INPUT_FILE" "$GENERATED_FILE"

status_name=$(jq -r '.releases[0].statusName' "$INPUT_FILE")

if [[ "$status_name" =~ Omnia[[:space:]]+([0-9]+\.[0-9]+\.[0-9]+) ]]; then
  omnia_version="${BASH_REMATCH[1]}"
else
  omnia_version=""
fi

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

if [ ! -f "$RELEASE_NOTES_FILE" ]; then
  echo "Target release notes file does not exist:"
  echo "$RELEASE_NOTES_FILE"
  exit 1
fi

if grep -Fxq "$omnia_version" "$RELEASE_NOTES_FILE"; then
  echo "Release notes for $omnia_version already exist on the default branch."
  exit 0
fi

existing_pr=$(
  gh pr list \
    --head "$branch_name" \
    --state open \
    --json number \
    --jq '.[0].number // empty'
)

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

base_sha=$(git rev-parse HEAD)
remote_sha=""

if [ -n "$existing_pr" ]; then
  echo "Updating existing release-note PR #$existing_pr."
  git fetch --no-tags origin \
    "refs/heads/${branch_name}:refs/remotes/origin/${branch_name}"
  remote_sha=$(git rev-parse "refs/remotes/origin/${branch_name}")
  git checkout -B "$branch_name" "$base_sha"
else
  if git ls-remote --exit-code --heads origin "$branch_name" >/dev/null 2>&1; then
    echo "Remote branch $branch_name exists without an open PR." >&2
    echo "Refusing to overwrite a closed or abandoned release-note branch." >&2
    exit 1
  fi

  git checkout -b "$branch_name"
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

if [ -n "$existing_pr" ]; then
  git push \
    --force-with-lease="refs/heads/${branch_name}:${remote_sha}" \
    --set-upstream origin "$branch_name"
  echo "Draft PR #$existing_pr updated successfully."
  exit 0
fi

git push --set-upstream origin "$branch_name"

gh pr create \
  --draft \
  --title "$pr_title" \
  --body "Automatically generated draft release notes for Omnia ${omnia_version}. Before marking this PR ready, verify the wording, included issues, customer references, and absence of private customer information." \
  --head "$branch_name" \
  --reviewer ChristianHDegn

echo "Draft PR created successfully."
