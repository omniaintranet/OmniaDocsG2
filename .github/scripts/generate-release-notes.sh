#!/usr/bin/env bash

set -euo pipefail

INPUT_FILE="/tmp/release-issues.json"
OUTPUT_FILE="/tmp/generated-release-notes.rst"
SKILL_FILE=".github/skills/hotfix-release-notes/SKILL.md"

MODEL="${OPENAI_MODEL:-gpt-5.6}"

if [ ! -f "$INPUT_FILE" ]; then
  echo "Input file not found: $INPUT_FILE"
  exit 1
fi

if [ ! -f "$SKILL_FILE" ]; then
  echo "Skill file not found: $SKILL_FILE"
  exit 1
fi

if [ -z "${OPENAI_API_KEY:-}" ]; then
  echo "OPENAI_API_KEY is not configured."
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

status_name=$(jq -r '.releases[0].statusName' "$INPUT_FILE")
issue_count=$(jq '.releases[0].issues | length' "$INPUT_FILE")

if [ "$issue_count" -eq 0 ]; then
  echo "Release was found but contains no issues."
  exit 1
fi

echo "Generating release notes for:"
echo "$status_name"
echo "Issues: $issue_count"

skill_instructions=$(cat "$SKILL_FILE")

release_input=$(
  jq -c '
    {
      statusName: .releases[0].statusName,
      issues: .releases[0].issues
    }
  ' "$INPUT_FILE"
)

user_prompt=$(cat <<EOF
Generate the hotfix release notes for the following approved release.

Use the supplied status name to construct the release heading and component-version line.

Return ONLY the final RST release-note content.
Do not include markdown code fences.
Do not include explanations before or after the release notes.

Release data:
$release_input
EOF
)

request_body=$(
  jq -n \
    --arg model "$MODEL" \
    --arg instructions "$skill_instructions" \
    --arg input "$user_prompt" \
    '{
      model: $model,
      instructions: $instructions,
      input: $input
    }'
)

response=$(
  curl --fail-with-body --silent --show-error \
    https://api.openai.com/v1/responses \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$request_body"
)

generated_text=$(
  echo "$response" |
    jq -r '
      [
        .output[]?.content[]?
        | select(.type == "output_text")
        | .text
      ]
      | join("\n")
    '
)

if [ -z "$generated_text" ] || [ "$generated_text" = "null" ]; then
  echo "The model did not return release-note content."
  echo "$response" | jq .
  exit 1
fi

printf '%s\n' "$generated_text" > "$OUTPUT_FILE"

echo
echo "Generated release notes:"
echo "------------------------"
cat "$OUTPUT_FILE"