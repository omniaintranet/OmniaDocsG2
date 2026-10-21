#!/usr/bin/env bash
# Installs the pinned Vale and gitleaks versions that docs_review.py needs on a Linux runner
# and adds them to PATH for the following steps. Used by the workflows that publish
# generated documentation (latest-changes.yml, hotfix-release-notes.yml).
# docs-review.yml installs the same versions itself; change both together.

set -euo pipefail

VALE_VERSION="3.24.0"
VALE_SHA256="867534ddb678abca7f214bc4706ead0922bd5252ffe8035fc227013f66c8b214"
GITLEAKS_VERSION="8.30.1"
GITLEAKS_SHA256="551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb"

tmp="${RUNNER_TEMP:?RUNNER_TEMP is not set}"
bin="$tmp/bin"
mkdir -p "$bin"

curl -fsSL -o "$tmp/vale.tar.gz" \
  "https://github.com/errata-ai/vale/releases/download/v${VALE_VERSION}/vale_${VALE_VERSION}_Linux_64-bit.tar.gz"
echo "${VALE_SHA256}  $tmp/vale.tar.gz" | sha256sum -c -
tar -xzf "$tmp/vale.tar.gz" -C "$bin" vale

curl -fsSL -o "$tmp/gitleaks.tar.gz" \
  "https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/gitleaks_${GITLEAKS_VERSION}_linux_x64.tar.gz"
echo "${GITLEAKS_SHA256}  $tmp/gitleaks.tar.gz" | sha256sum -c -
tar -xzf "$tmp/gitleaks.tar.gz" -C "$bin" gitleaks

echo "$bin" >> "${GITHUB_PATH:?GITHUB_PATH is not set}"
