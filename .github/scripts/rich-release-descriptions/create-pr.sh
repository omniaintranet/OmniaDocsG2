#!/usr/bin/env bash

set -euo pipefail

INPUT_FILE="/tmp/release-highlights-with-assets.json"
GENERATED_FILE="/tmp/generated-release-highlights.rst"
GENERATED_JSON="/tmp/generated-release-highlights.json"
ASSET_MANIFEST="/tmp/release-highlight-assets.txt"

for required_file in "$INPUT_FILE" "$GENERATED_FILE" "$GENERATED_JSON" "$ASSET_MANIFEST"; do
  if [ ! -e "$required_file" ]; then
    echo "Required release-highlight artifact is missing: $required_file" >&2
    exit 1
  fi
done

if [ -z "${RELEASE_DESCRIPTION_FILE:-}" ] || [ ! -f "$RELEASE_DESCRIPTION_FILE" ]; then
  echo "RELEASE_DESCRIPTION_FILE must identify the existing Release 7 overview file." >&2
  exit 1
fi

if [ "$(sed -n '1p' "$RELEASE_DESCRIPTION_FILE")" != "Release 7" ] || \
   [ "$(sed -n '2p' "$RELEASE_DESCRIPTION_FILE")" != "========================================" ] || \
   [ -n "$(sed -n '3p' "$RELEASE_DESCRIPTION_FILE")" ]; then
  echo "The Release 7 overview preamble is not in the expected RST format." >&2
  exit 1
fi

release_version=$(jq -r '.releaseVersion' "$INPUT_FILE")

if [[ ! "$release_version" =~ ^[0-9]+\.[0-9]+$ ]]; then
  echo "The selected Feature candidates do not contain a valid major.minor release version." >&2
  exit 1
fi

while IFS= read -r public_title; do
  heading="(${release_version}) ${public_title}"

  if grep -Fxq "$heading" "$RELEASE_DESCRIPTION_FILE"; then
    echo "A generated release-highlight heading already exists on the default branch." >&2
    exit 1
  fi
done < <(jq -r '.highlights[].title' "$GENERATED_JSON")

branch_name="rich-release-descriptions-${release_version}"
pr_title="Release highlights ${release_version}"
bot_email="41898282+github-actions[bot]@users.noreply.github.com"
existing_pr=$(
  gh pr list \
    --head "$branch_name" \
    --state open \
    --json number \
    --jq '.[0].number // empty'
)

git config user.name "github-actions[bot]"
git config user.email "$bot_email"

base_sha=$(git rev-parse HEAD)
remote_sha=""

if [ -n "$existing_pr" ]; then
  echo "Updating existing rich release-description PR #$existing_pr."
  git fetch --no-tags origin \
    "refs/heads/${branch_name}:refs/remotes/origin/${branch_name}"
  remote_sha=$(git rev-parse "refs/remotes/origin/${branch_name}")
  remote_author_email=$(git show -s --format='%ae' "$remote_sha")

  if [ "$remote_author_email" != "$bot_email" ]; then
    echo "The existing draft branch contains reviewer-authored changes." >&2
    echo "Preserving those changes instead of regenerating the branch." >&2
    exit 1
  fi

  git checkout -B "$branch_name" "$base_sha"
else
  if git ls-remote --exit-code --heads origin "$branch_name" >/dev/null 2>&1; then
    echo "Remote branch $branch_name exists without an open PR." >&2
    echo "Refusing to overwrite a closed or abandoned release-description branch." >&2
    exit 1
  fi

  git checkout -b "$branch_name"
fi

temporary_file=$(mktemp)
head -n 3 "$RELEASE_DESCRIPTION_FILE" > "$temporary_file"
cat "$GENERATED_FILE" >> "$temporary_file"
printf '\n' >> "$temporary_file"
tail -n +4 "$RELEASE_DESCRIPTION_FILE" >> "$temporary_file"
mv "$temporary_file" "$RELEASE_DESCRIPTION_FILE"

git add -- "$RELEASE_DESCRIPTION_FILE"

while IFS= read -r asset_path; do
  [ -z "$asset_path" ] && continue

  if [ ! -f "$asset_path" ]; then
    echo "Prepared release asset is missing: $asset_path" >&2
    exit 1
  fi

  git add -- "$asset_path"
done < "$ASSET_MANIFEST"

if git diff --cached --quiet; then
  echo "No rich release-description changes detected."
  exit 0
fi

git commit -m "Add release highlights for ${release_version}"

if [ -n "$existing_pr" ]; then
  git push \
    --force-with-lease="refs/heads/${branch_name}:${remote_sha}" \
    --set-upstream origin "$branch_name"
  echo "Rich release-description PR #$existing_pr updated successfully."
  exit 0
fi

git push --set-upstream origin "$branch_name"

gh pr create \
  --draft \
  --title "$pr_title" \
  --body "Automatically generated rich release highlights for Omnia ${release_version}. Before marking this PR ready, verify every claim, screenshot, alt text, limitation, and business-value statement against the selected Feature issues." \
  --head "$branch_name" \
  --reviewer ChristianHDegn

echo "Draft rich release-description PR created successfully."
