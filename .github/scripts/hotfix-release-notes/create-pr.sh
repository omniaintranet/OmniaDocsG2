#!/usr/bin/env bash

set -euo pipefail

INPUT_FILE="/tmp/release-issues.json"
GENERATED_FILE="/tmp/generated-release-notes.rst"
VALIDATOR_FILE=".github/scripts/hotfix-release-notes/validate-release-notes.sh"
CATEGORIES_FILE="${CATEGORIES_FILE:-.github/skills/hotfix-release-notes/categories.txt}"
# Written by generate-release-notes.sh: categories it added to CATEGORIES_FILE.
NEW_CATEGORIES_FILE="/tmp/release-notes-new-categories.txt"
# Written by review-release-notes.sh in the step before this one.
REVIEW_DIR="/tmp/docs-review-release-notes"
REVIEW_MARKER="<!-- release-notes-review -->"

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

# The pull request body: the instructions for the reviewer, then the documentation review.
# Everything from REVIEW_MARKER on is replaced when the pull request is updated.
write_review_section() {
  printf '%s\n\n' "$REVIEW_MARKER"
  if [ -s "$NEW_CATEGORIES_FILE" ]; then
    printf '> [!NOTE]\n> New category headers, added to `%s`: %s. Keep them for later releases, or rename them to a listed category in both files.\n\n' \
      "$CATEGORIES_FILE" "$(paste -sd ',' "$NEW_CATEGORIES_FILE" | sed 's/,/, /g')"
  fi
  if [ ! -s "$REVIEW_DIR/summary.md" ]; then
    printf '> [!WARNING]\n> The documentation review did not run for these release notes. Check the wording, customer references and confidentiality by hand.\n'
    return
  fi
  local errors=0
  if [ -s "$REVIEW_DIR/findings.json" ]; then
    errors=$(jq '[.[] | select(.severity == "error")] | length' "$REVIEW_DIR/findings.json")
  fi
  if [ "$errors" -gt 0 ]; then
    printf '> [!CAUTION]\n> The documentation review found **%s problem(s) that must be fixed** before this pull request is marked ready. See "Must fix" below.\n\n' "$errors"
  fi
  cat "$REVIEW_DIR/summary.md"
}

write_pr_body() {
  printf '%s\n\n' "Automatically generated draft release notes for Omnia ${omnia_version}. Before marking this PR ready, verify the wording, included issues, customer references, and absence of private customer information."
  write_review_section
}

report_pr_url() {
  local pr_url
  pr_url=$(gh pr view "$branch_name" --json url --jq '.url')
  if [ -n "${GITHUB_OUTPUT:-}" ]; then
    printf 'pr_url=%s\n' "$pr_url" >> "$GITHUB_OUTPUT"
  fi
}

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
if [ -s "$NEW_CATEGORIES_FILE" ]; then
  git add "$CATEGORIES_FILE"
fi

if git diff --cached --quiet; then
  echo "No release-note changes detected."
  if [ -n "$existing_pr" ]; then
    report_pr_url
  fi
  exit 0
fi

git commit -m "Add release notes for ${omnia_version}"

if [ -n "$existing_pr" ]; then
  git push \
    --force-with-lease="refs/heads/${branch_name}:${remote_sha}" \
    --set-upstream origin "$branch_name"
  # Keep what people wrote above the review section; replace the review itself.
  body_file=$(mktemp)
  current_body=$(gh pr view "$branch_name" --json body --jq '.body')
  if [[ "$current_body" == *"$REVIEW_MARKER"* ]]; then
    printf '%s' "${current_body%%"$REVIEW_MARKER"*}" > "$body_file"
  else
    printf '%s\n\n' "$current_body" > "$body_file"
  fi
  write_review_section >> "$body_file"
  gh pr edit "$branch_name" --body-file "$body_file" > /dev/null
  report_pr_url
  echo "Draft PR #$existing_pr updated successfully."
  exit 0
fi

git push --set-upstream origin "$branch_name"

body_file=$(mktemp)
write_pr_body > "$body_file"

gh pr create \
  --draft \
  --title "$pr_title" \
  --body-file "$body_file" \
  --head "$branch_name" \
  --reviewer ChristianHDegn

report_pr_url
echo "Draft PR created successfully."
