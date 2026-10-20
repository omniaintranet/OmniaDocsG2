#!/usr/bin/env bash
# Offline test for the shared Wait-for-RN status matcher (bash, jq and sed paths).
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/wait-for-rn-lib.sh"

failures=0
fail() { echo "FAIL: $*" >&2; failures=$((failures + 1)); }

matching=(
  "Wait for RN - Omnia 7.11.99 / WCM 7.11.99"
  "Waiting for RN - Omnia 7.11.99 / WCM 7.11.99"
  "waiting for rn - Omnia 7.11.99"
  "WAIT FOR RN - Omnia 7.11.99"
  "Wait for RNs - Omnia 7.11.99"
  "Wait for RN: Omnia 7.11.99"
  "Wait for RN – Omnia 7.11.99"
  "Wait for RN — Omnia 7.11.99"
  "Wait for RN-Omnia 7.11.99"
  "Wait  for   RN  -  Omnia 7.11.99"
  "  Wait for RN - Omnia 7.11.99"
  "Wait RN - Omnia 7.11.99"
  "Waiting RN - Omnia 7.11.99"
  "Wait on RN - Omnia 7.11.99"
  "Waiting on RN - Omnia 7.11.99"
  "Awaiting RN - Omnia 7.11.99"
  "Awaiting for RN - Omnia 7.11.99"
  "Wait for Release Notes - Omnia 7.11.99"
  "Waiting for release note - Omnia 7.11.99"
  "Waiting for Release-Notes - Omnia 7.11.99"
  "Wait-for-RN - Omnia 7.11.99"
  "Wait_for_RN - Omnia 7.11.99"
  "WaitForRN - Omnia 7.11.99"
  "⏳ Waiting for RN - Omnia 7.11.99"
  "[Wait for RN] Omnia 7.11.99"
  "Wait for RN / Omnia 7.11.99"
  "Wait for RN | Omnia 7.11.99"
  "Wait for RN"
)
not_matching=(
  "Approved - Omnia 7.11.99 / WCM 7.11.99"
  "Waiting for QA"
  "Wait for QA - Omnia 7.11.99"
  "Waiting for customer"
  "Ready for release"
  "Investigation"
  "Done"
  "Omnia 7.11.99 - Wait for RN"
  "RN waiting"
  "Wait for RNA - Omnia 7.11.99"
  "Waiting for release notesx - Omnia 7.11.99"
  ""
)

for name in "${matching[@]}"; do
  is_wait_for_rn_status "$name" || fail "bash should match: '$name'"
  jq -en --arg p "$WAIT_FOR_RN_PATTERN" --arg n "$name" '$n | test($p; "i")' > /dev/null ||
    fail "jq should match: '$name'"
  [ "$name" = "Wait for RN" ] && continue
  stripped=$(strip_wait_for_rn_prefix "$name")
  case "$stripped" in
    *Omnia\ 7.11.99*) ;;
    *) fail "strip lost the version for '$name' -> '$stripped'" ;;
  esac
  case "$stripped" in
    Omnia*) ;;
    *) fail "strip left a prefix for '$name' -> '$stripped'" ;;
  esac
done

for name in "${not_matching[@]}"; do
  if is_wait_for_rn_status "$name"; then fail "bash should not match: '$name'"; fi
  if jq -en --arg p "$WAIT_FOR_RN_PATTERN" --arg n "$name" '$n | test($p; "i")' > /dev/null; then
    fail "jq should not match: '$name'"
  fi
done

expected="Omnia 7.11.99 / WCM 7.11.99"
for name in "Wait for RN - $expected" "Waiting for RN - $expected" "Wait for RN: $expected" "Awaiting release notes – $expected" "[Wait for RN] $expected" "Wait for RN / $expected"; do
  [ "$(strip_wait_for_rn_prefix "$name")" = "$expected" ] ||
    fail "strip of '$name' gave '$(strip_wait_for_rn_prefix "$name")'"
done

# A bracketed component line keeps its brackets; names without the label are only trimmed.
for pair in "Wait for RN - ($expected)|($expected)" "Waiting for RN ($expected)|($expected)" \
  "Approved - $expected|Approved - $expected" "Wait for RNA - $expected|Wait for RNA - $expected" \
  "  Approved - $expected  |Approved - $expected"; do
  name="${pair%%|*}"
  [ "$(strip_wait_for_rn_prefix "$name")" = "${pair#*|}" ] ||
    fail "strip of '$name' gave '$(strip_wait_for_rn_prefix "$name")', expected '${pair#*|}'"
done

if [ "$failures" -ne 0 ]; then
  echo "$failures failure(s)." >&2
  exit 1
fi
echo "All Wait-for-RN status matcher tests passed."
