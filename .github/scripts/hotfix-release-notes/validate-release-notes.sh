#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 RELEASE_DATA_JSON GENERATED_RST" >&2
  exit 1
fi

input_file="$1"
generated_file="$2"

if [ ! -s "$input_file" ]; then
  echo "Release data is missing or empty: $input_file" >&2
  exit 1
fi

if [ ! -s "$generated_file" ]; then
  echo "Generated release notes are missing or empty: $generated_file" >&2
  exit 1
fi

release_count=$(jq '.releases | length' "$input_file")

if [ "$release_count" -ne 1 ]; then
  echo "Expected exactly one release in $input_file; found $release_count." >&2
  exit 1
fi

status_name=$(jq -r '.releases[0].statusName' "$input_file")

if [[ "$status_name" =~ Omnia[[:space:]]+([0-9]+\.[0-9]+\.[0-9]+) ]]; then
  omnia_version="${BASH_REMATCH[1]}"
else
  echo "Could not extract an Omnia version from status: $status_name" >&2
  exit 1
fi

component_versions=$(
  printf '%s\n' "$status_name" |
    sed -E 's/^Wait for RN([[:space:]]*-[[:space:]]*|[[:space:]]+)//; s/^[[:space:]]+//; s/[[:space:]]+$//'
)

if [ -z "$component_versions" ]; then
  echo "Could not extract the component-version line from status: $status_name" >&2
  exit 1
fi

if [[ "$component_versions" == \(*\) ]]; then
  expected_component_line="$component_versions"
else
  expected_component_line="($component_versions)"
fi

first_line=$(sed -n '1p' "$generated_file")
first_line="${first_line#$'\xEF\xBB\xBF'}"
second_line=$(sed -n '2p' "$generated_file")
third_line=$(sed -n '3p' "$generated_file")
fourth_line=$(sed -n '4p' "$generated_file")

if [ "$first_line" != "$omnia_version" ]; then
  echo "Generated heading '$first_line' does not match expected version '$omnia_version'." >&2
  exit 1
fi

if [ "$second_line" != "========================================" ]; then
  echo "Generated release heading does not use the required RST underline." >&2
  exit 1
fi

if [ "$third_line" != "$expected_component_line" ]; then
  echo "Generated component-version line does not match the project status." >&2
  exit 1
fi

if [ -n "$fourth_line" ]; then
  echo "Expected a blank line before the release-note bullets." >&2
  exit 1
fi

if ! tail -n +5 "$generated_file" | grep -q '^- '; then
  echo "Generated release notes contain no bullets." >&2
  exit 1
fi

if ! tail -n +5 "$generated_file" | awk 'NF && $0 !~ /^- / { exit 1 }'; then
  echo "Every release-note bullet must occupy one physical line." >&2
  exit 1
fi

if grep -Eq '(^|[[:space:]])\.\.[[:space:]]+(raw|include|literalinclude)::|```|^# ' "$generated_file"; then
  echo "Generated release notes contain prohibited markup." >&2
  exit 1
fi

if grep -Eiq 'https?://' "$generated_file"; then
  echo "Generated release notes contain a URL; refusing to publish potentially private links." >&2
  exit 1
fi

if grep -Eiq '[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}' "$generated_file"; then
  echo "Generated release notes contain an email address." >&2
  exit 1
fi

source_text_file=$(mktemp)
source_urls_file=$(mktemp)
allowed_references_file=$(mktemp)
generated_references_file=$(mktemp)
trap 'rm -f "$source_text_file" "$source_urls_file" "$allowed_references_file" "$generated_references_file"' EXIT

jq -r '
  .releases[0].issues[]
  | .body, (.comments[]?.body // "")
' "$input_file" > "$source_text_file"

grep -Eo 'https?://[^[:space:]<>()"]+' "$source_text_file" > "$source_urls_file" || true

while IFS= read -r source_url; do
  if [[ "$source_url" =~ /agent/tickets/([0-9]+) ]]; then
    printf '%s\n' "${BASH_REMATCH[1]}" >> "$allowed_references_file"
  elif [[ ! "$source_url" =~ github\.com/ ]] && [[ "$source_url" =~ /issues/([0-9]+) ]]; then
    printf '%s\n' "${BASH_REMATCH[1]}" >> "$allowed_references_file"
  fi
done < "$source_urls_file"

sort -u -o "$allowed_references_file" "$allowed_references_file"

grep -Eo '#[0-9]+' "$generated_file" |
  tr -d '#' |
  sort -u > "$generated_references_file" || true

while IFS= read -r reference; do
  [ -z "$reference" ] && continue

  if ! grep -Fxq "$reference" "$allowed_references_file"; then
    echo "Generated customer reference #$reference is not supported by a trusted source URL." >&2
    exit 1
  fi
done < "$generated_references_file"

while IFS= read -r bullet; do
  if [[ "$bullet" == *"#"* ]] && ! printf '%s\n' "$bullet" | grep -Eq '\(#[0-9]+(, #[0-9]+)*\)$'; then
    echo "Customer references must be formatted at the end of a bullet, for example (#59036, #59606)." >&2
    exit 1
  fi
done < <(grep '^- ' "$generated_file")

echo "Release-note validation passed for Omnia $omnia_version."
