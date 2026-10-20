#!/usr/bin/env bash
# Shared helpers for recognising the "waiting for release notes" Project 8 status column.
#
# The column name is typed by people, so it drifts ("Wait for RN", "Waiting for RN",
# "Awaiting release notes", ...). The one regular expression that defines what counts
# as that column lives in wait-for-rn-pattern.txt and is shared with the Python sync
# script. It is written in the subset that bash/grep/sed -E, jq (Oniguruma) and
# Python's re all read identically, and is always applied case-insensitively.
# The label must not run on into a word ("Wait for RNA" is not the column), so
# matching adds an end boundary; the Python script adds the same as a lookahead.
#
# Source this file; do not execute it.

_WAIT_FOR_RN_LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WAIT_FOR_RN_LABEL="$(tr -d '\r\n' < "${_WAIT_FOR_RN_LIB_DIR}/wait-for-rn-pattern.txt")"

if [ -z "$WAIT_FOR_RN_LABEL" ]; then
  echo "wait-for-rn-pattern.txt is missing or empty." >&2
  return 1 2>/dev/null || exit 1
fi

# For bash and jq matching: the label followed by a non-alphanumeric character or the end.
WAIT_FOR_RN_PATTERN="${WAIT_FOR_RN_LABEL}([^A-Za-z0-9]|\$)"

# True when the status name starts with a "waiting for release notes" label.
is_wait_for_rn_status() {
  printf '%s\n' "$1" | grep -Eiq -- "$WAIT_FOR_RN_PATTERN"
}

# Prints the status name without the waiting label and the separator after it
# ("Waiting for RN - Omnia 7.11.99" -> "Omnia 7.11.99", "[Wait for RN] Omnia 7.11.99" -> "Omnia 7.11.99").
# The separator is everything up to the first letter, digit or "(" (a bracketed component line).
# Names without the label are only trimmed.
strip_wait_for_rn_prefix() {
  if is_wait_for_rn_status "$1"; then
    printf '%s\n' "$1" |
      sed -E "s/${WAIT_FOR_RN_LABEL}//I; s/^[^A-Za-z0-9(]+//; s/[[:space:]]+\$//"
  else
    printf '%s\n' "$1" | sed -E 's/^[[:space:]]+//; s/[[:space:]]+$//'
  fi
}
