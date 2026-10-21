#!/usr/bin/env bash
# Runs the documentation review (.github/docs-review/README.md) on the release notes as
# create-pr.sh will commit them: the generated notes above the current release-notes file.
#
# Findings never stop the run. create-pr.sh adds the summary to the pull request, which
# people review before it is marked ready, and marks blocking findings at the top.
# The release-notes file is restored afterwards, so create-pr.sh starts from the default branch.

set -euo pipefail

GENERATED_FILE="/tmp/generated-release-notes.rst"
REVIEW_DIR="/tmp/docs-review-release-notes"
REVIEW_SCRIPT=".github/scripts/docs-review/docs_review.py"
PYTHON="${PYTHON:-python}"

if [ ! -f "$GENERATED_FILE" ]; then
  echo "Generated release notes not found: $GENERATED_FILE"
  exit 1
fi

if [ -z "${RELEASE_NOTES_FILE:-}" ] || [ ! -f "$RELEASE_NOTES_FILE" ]; then
  echo "RELEASE_NOTES_FILE is not configured or does not exist: ${RELEASE_NOTES_FILE:-}"
  exit 1
fi

if ! git diff --quiet HEAD -- "$RELEASE_NOTES_FILE"; then
  echo "$RELEASE_NOTES_FILE has uncommitted changes; refusing to review over them." >&2
  exit 1
fi

rm -rf "$REVIEW_DIR"
mkdir -p "$REVIEW_DIR"
trap 'git checkout -- "$RELEASE_NOTES_FILE"' EXIT

# Same composition as create-pr.sh, so line numbers match the pull request.
temp_file=$(mktemp)
cat "$GENERATED_FILE" > "$temp_file"
printf '\n\n' >> "$temp_file"
cat "$RELEASE_NOTES_FILE" >> "$temp_file"
mv "$temp_file" "$RELEASE_NOTES_FILE"

# The validator already allows no links or markup beyond headings and bullets,
# so the Sphinx build comparison and the link check add nothing here.
status=0
"$PYTHON" "$REVIEW_SCRIPT" \
  --base HEAD \
  --build never \
  --linkcheck never \
  --no-fail \
  --out "$REVIEW_DIR" \
  --annotations \
  --step-summary \
  --subject "the generated release notes" || status=$?

if [ "$status" -ne 0 ] || [ ! -s "$REVIEW_DIR/findings.json" ]; then
  echo "::warning title=Documentation review::The review of the generated release notes could not finish (exit $status)."
  printf '%s\n## ⚠️ Documentation review could not finish\n\nThe automatic review of the generated release notes stopped before it produced a result. Check the wording, customer references and confidentiality by hand.\n' \
    '<!-- docs-review-summary -->' > "$REVIEW_DIR/summary.md"
  printf 'errors=unknown\n' >> "${GITHUB_OUTPUT:-/dev/null}"
  exit 0
fi

errors=$(jq '[.[] | select(.severity == "error")] | length' "$REVIEW_DIR/findings.json")
printf 'errors=%s\n' "$errors" >> "${GITHUB_OUTPUT:-/dev/null}"

if [ "$errors" -gt 0 ]; then
  echo "::warning title=Documentation review::$errors problem(s) in the generated release notes must be fixed before the pull request is marked ready."
fi
