#!/usr/bin/env bash

set -euo pipefail

INPUT_FILE="/tmp/release-issues.json"
OUTPUT_FILE="/tmp/generated-release-notes.rst"
SKILL_FILE=".github/skills/hotfix-release-notes/SKILL.md"

if [ ! -f "$INPUT_FILE" ]; then
  echo "Input file not found: $INPUT_FILE"
  exit 1
fi

if [ ! -f "$SKILL_FILE" ]; then
  echo "Skill file not found: $SKILL_FILE"
  exit 1
fi

release_count=$(jq '.releases | length' "$INPUT_FILE")

if [ "$release_count" -eq 0 ]; then
  echo "No releases waiting for release notes."
  exit 0
fi

if [ "$release_count" -gt 1 ]; then
  echo "More than one release is waiting for release notes."
  echo "This first version only supports one release at a time."
  exit 1
fi

issue_count=$(jq '.releases[0].issues | length' "$INPUT_FILE")

if [ "$issue_count" -eq 0 ]; then
  echo "Release was found but contains no issues."
  exit 1
fi

status_name=$(jq -r '.releases[0].statusName' "$INPUT_FILE")

echo "Generating release notes for:"
echo "$status_name"
echo "Issues: $issue_count"

skill_instructions=$(cat "$SKILL_FILE")
release_data=$(cat "$INPUT_FILE")

prompt=$(cat <<EOF
You are generating customer-facing Omnia hotfix release notes.

Follow these release-note instructions exactly:

$skill_instructions

Release data:

$release_data

Requirements:
- Generate release notes only for the release in the supplied JSON.
- Use the status name to construct the release heading and component-version line.
- Use the supplied GitHub issue information as the source of truth.
- Do not invent functionality or ticket numbers.
- Return only the final RST release-note content.
- Do not use Markdown code fences.
- Do not include explanations, commentary, or introductory text.
EOF
)

copilot \
  -p "$prompt" \
  -s \
  --no-ask-user \
  > "$OUTPUT_FILE"

if [ ! -s "$OUTPUT_FILE" ]; then
  echo "Copilot returned an empty response."
  exit 1
fi

echo
echo "Generated release notes:"
echo "------------------------"
cat "$OUTPUT_FILE"