#!/usr/bin/env bash

set -euo pipefail

INPUT_FILE="/tmp/release-highlights.json"
OUTPUT_FILE="/tmp/release-highlights-with-assets.json"
ASSET_MANIFEST="/tmp/release-highlight-assets.txt"

if [ ! -s "$INPUT_FILE" ]; then
  echo "Selected Feature data is missing or empty: $INPUT_FILE" >&2
  exit 1
fi

if [ -z "${RELEASE_ASSET_DIRECTORY:-}" ] || [ ! -d "$RELEASE_ASSET_DIRECTORY" ]; then
  echo "RELEASE_ASSET_DIRECTORY must identify an existing documentation directory." >&2
  exit 1
fi

if [ -z "${GH_TOKEN:-}" ]; then
  echo "GH_TOKEN is required to retrieve developer-provided public issue attachments." >&2
  exit 1
fi

release_version=$(jq -r '.releaseVersion' "$INPUT_FILE")

if [[ ! "$release_version" =~ ^[0-9]+\.[0-9]+$ ]]; then
  echo "The selected Feature candidates do not contain a valid major.minor release version." >&2
  exit 1
fi

jq '.highlights |= map(. + {screenshots: []})' "$INPUT_FILE" > "$OUTPUT_FILE"
: > "$ASSET_MANIFEST"

highlight_count=$(jq '.highlights | length' "$OUTPUT_FILE")
downloaded_count=0
image_line_pattern='^[[:space:]]*!\[([^][]+)\]\((https://github\.com/user-attachments/assets/[[:alnum:]-]+)\)[[:space:]]*$'

for ((highlight_index = 0; highlight_index < highlight_count; highlight_index++)); do
  source_title=$(jq -r --argjson index "$highlight_index" '.highlights[$index].sourceTitle' "$OUTPUT_FILE")
  title_hash=$(printf '%s' "$source_title" | sha256sum | cut -c1-12)
  screenshot_markdown=$(jq -r --argjson index "$highlight_index" '.highlights[$index].screenshotMarkdown // ""' "$OUTPUT_FILE")
  approved_count=0

  while IFS= read -r declaration; do
    declaration="${declaration%$'\r'}"

    if [[ ! "$declaration" =~ [^[:space:]] ]]; then
      continue
    fi

    if [[ ! "$declaration" =~ $image_line_pattern ]]; then
      echo "A Public screenshot section contains unsupported content." >&2
      echo "Use one GitHub user-attachment Markdown image per line." >&2
      exit 1
    fi

    alt_text="${BASH_REMATCH[1]}"
    attachment_url="${BASH_REMATCH[2]}"
    approved_count=$((approved_count + 1))

    if [ "$approved_count" -gt 3 ]; then
      echo "A release highlight declares more than three screenshots." >&2
      exit 1
    fi

    if [ -z "$alt_text" ] || [ "${#alt_text}" -gt 160 ]; then
      echo "Every approved screenshot needs concise alt text." >&2
      exit 1
    fi

    if printf '%s\n' "$alt_text" | grep -Eiq 'https?://|[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}'; then
      echo "Screenshot alt text contains a URL or email address." >&2
      exit 1
    fi

    temporary_image=$(mktemp)
    curl \
      --fail \
      --location \
      --silent \
      --show-error \
      --retry 3 \
      --connect-timeout 10 \
      --max-time 60 \
      --max-filesize 5242880 \
      --proto '=https' \
      --tlsv1.2 \
      --header "Authorization: Bearer ${GH_TOKEN}" \
      --output "$temporary_image" \
      "$attachment_url"

    image_size=$(stat -c '%s' "$temporary_image")

    if [ "$image_size" -le 0 ] || [ "$image_size" -gt 5242880 ]; then
      rm -f "$temporary_image"
      echo "An approved screenshot is empty or larger than 5 MB." >&2
      exit 1
    fi

    mime_type=$(file --brief --mime-type "$temporary_image")

    case "$mime_type" in
      image/png)
        extension="png"
        ;;
      image/jpeg)
        extension="jpg"
        ;;
      image/webp)
        extension="webp"
        ;;
      *)
        rm -f "$temporary_image"
        echo "Approved release screenshots must be PNG, JPEG, or WebP files." >&2
        exit 1
        ;;
    esac

    asset_name="${release_version}-highlight-${title_hash}-${approved_count}.${extension}"
    asset_path="${RELEASE_ASSET_DIRECTORY}/${asset_name}"
    mv "$temporary_image" "$asset_path"
    printf '%s\n' "$asset_path" >> "$ASSET_MANIFEST"

    updated_file=$(mktemp)
    jq \
      --argjson index "$highlight_index" \
      --arg file "$asset_name" \
      --arg alt "$alt_text" \
      '.highlights[$index].screenshots += [{file: $file, alt: $alt}]' \
      "$OUTPUT_FILE" > "$updated_file"
    mv "$updated_file" "$OUTPUT_FILE"

    downloaded_count=$((downloaded_count + 1))
  done <<< "$screenshot_markdown"
done

updated_file=$(mktemp)
jq 'del(.highlights[].screenshotMarkdown)' "$OUTPUT_FILE" > "$updated_file"
mv "$updated_file" "$OUTPUT_FILE"

echo "Fetched $downloaded_count developer-provided public screenshot(s)."
