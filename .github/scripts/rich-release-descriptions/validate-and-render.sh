#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 APPROVED_INPUT_JSON GENERATED_JSON OUTPUT_RST" >&2
  exit 1
fi

input_file="$1"
generated_json="$2"
output_file="$3"

for required_file in "$input_file" "$generated_json"; do
  if [ ! -s "$required_file" ]; then
    echo "Required validation input is missing or empty: $required_file" >&2
    exit 1
  fi
done

highlight_count=$(jq '.highlights | length' "$input_file")

if ! jq -e --argjson expectedCount "$highlight_count" '
  type == "object"
  and (keys == ["highlights"])
  and (.highlights | type == "array")
  and (.highlights | length == $expectedCount)
  and (([.highlights[].highlightId] | sort) == [range(1; $expectedCount + 1)])
  and ([.highlights[].title] | unique | length == $expectedCount)
  and all(.highlights[];
    (keys == ["businessValue", "highlightId", "limitations", "summary", "title", "useCases"])
    and
    (.highlightId | type == "number")
    and (.title | type == "string" and length >= 3 and length <= 120 and (contains("\n") | not))
    and (.summary | type == "string" and length >= 20 and length <= 1200 and (contains("\n") | not))
    and (.businessValue | type == "string" and length >= 20 and length <= 1200 and (contains("\n") | not))
    and (.useCases | type == "array" and length <= 3)
    and all(.useCases[]; type == "string" and length > 0 and length <= 300 and (contains("\n") | not))
    and (.limitations | type == "array" and length <= 3)
    and all(.limitations[]; type == "string" and length > 0 and length <= 300 and (contains("\n") | not))
  )
' "$generated_json" >/dev/null; then
  echo "Copilot output does not match the required release-highlight JSON schema." >&2
  exit 1
fi

generated_text_file=$(mktemp)
trap 'rm -f "$generated_text_file"' EXIT

jq -r '
  .highlights[]
  | .title,
    .summary,
    .businessValue,
    (.useCases[]?),
    (.limitations[]?)
' "$generated_json" > "$generated_text_file"

if grep -Eiq 'https?://|[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}|#[0-9]+' "$generated_text_file"; then
  echo "Generated release descriptions contain a URL, email address, or ticket-style reference." >&2
  exit 1
fi

if grep -Eq '(^|[[:space:]])\.\.[[:space:]]+(raw|include|literalinclude)::|```|[`|]' "$generated_text_file"; then
  echo "Generated release descriptions contain prohibited markup." >&2
  exit 1
fi

release_version=$(jq -r '.releaseVersion' "$input_file")

if [[ ! "$release_version" =~ ^[0-9]+\.[0-9]+$ ]]; then
  echo "The selected Feature candidates do not contain a valid major.minor release version." >&2
  exit 1
fi

: > "$output_file"

for ((highlight_id = 1; highlight_id <= highlight_count; highlight_id++)); do
  public_title=$(jq -r --argjson id "$highlight_id" '.highlights[] | select(.highlightId == $id) | .title' "$generated_json")
  summary=$(jq -r --argjson id "$highlight_id" '.highlights[] | select(.highlightId == $id) | .summary' "$generated_json")
  business_value=$(jq -r --argjson id "$highlight_id" '.highlights[] | select(.highlightId == $id) | .businessValue' "$generated_json")
  heading="(${release_version}) ${public_title}"

  printf '%s\n' "$heading" >> "$output_file"
  printf '%*s\n' "${#heading}" '' | tr ' ' '-' >> "$output_file"
  printf '%s\n\n' "$summary" >> "$output_file"
  printf '%s\n\n' "$business_value" >> "$output_file"

  use_case_count=$(jq --argjson id "$highlight_id" '.highlights[] | select(.highlightId == $id) | .useCases | length' "$generated_json")

  if [ "$use_case_count" -gt 0 ]; then
    printf 'Typical use cases:\n\n' >> "$output_file"
    jq -r --argjson id "$highlight_id" '.highlights[] | select(.highlightId == $id) | .useCases[] | "- " + .' "$generated_json" >> "$output_file"
    printf '\n' >> "$output_file"
  fi

  limitation_count=$(jq --argjson id "$highlight_id" '.highlights[] | select(.highlightId == $id) | .limitations | length' "$generated_json")

  if [ "$limitation_count" -gt 0 ]; then
    printf 'Requirements and limitations:\n\n' >> "$output_file"
    jq -r --argjson id "$highlight_id" '.highlights[] | select(.highlightId == $id) | .limitations[] | "- " + .' "$generated_json" >> "$output_file"
    printf '\n' >> "$output_file"
  fi

  screenshot_count=$(jq --argjson id "$highlight_id" '.highlights[] | select(.highlightId == $id) | .screenshots | length' "$input_file")

  for ((screenshot_index = 0; screenshot_index < screenshot_count; screenshot_index++)); do
    screenshot_file=$(jq -r --argjson id "$highlight_id" --argjson index "$screenshot_index" '.highlights[] | select(.highlightId == $id) | .screenshots[$index].file' "$input_file")
    screenshot_alt=$(jq -r --argjson id "$highlight_id" --argjson index "$screenshot_index" '.highlights[] | select(.highlightId == $id) | .screenshots[$index].alt' "$input_file")
    printf '.. image:: %s\n' "$screenshot_file" >> "$output_file"
    printf '   :alt: %s\n\n' "$screenshot_alt" >> "$output_file"
  done
done

echo "Rich release-description validation passed for Omnia $release_version."
