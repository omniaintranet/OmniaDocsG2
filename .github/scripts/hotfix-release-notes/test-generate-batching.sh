#!/usr/bin/env bash
# Offline test for generate-release-notes.sh: a release whose issues do not fit one prompt goes out in
# batches, each under the prompt budget, and the merged result passes the usual checks. A fake
# `copilot` stands in for the model; nothing is sent anywhere. Run from anywhere.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$repo_root"

test_dir=$(mktemp -d)
trap 'rm -rf "$test_dir"' EXIT

failures=0
fail() { echo "FAIL: $*" >&2; failures=$((failures + 1)); }
pass() { echo "ok: $*"; }

mkdir -p "$test_dir/bin"

# The fake model: logs the size of each prompt, then accounts for every issue named in the prompt with
# one bullet each. FAKE_DROP_ISSUE leaves one issue out of its first answer (not of a follow-up).
cat > "$test_dir/bin/copilot" <<'FAKE'
#!/usr/bin/env bash
prompt=$(cat)
printf '%s\n' "${#prompt}" >> "$FAKE_LOG"
case "$prompt" in
  *"Release-note bullets already written"*) printf 'context\n' >> "$FAKE_LOG.context" ;;
esac
list=$(printf '%s\n' "$prompt" | sed -n 's/^- The release data holds [0-9]* issue(s): \(.*\)\. Before returning.*/\1/p')
drop="${FAKE_DROP_ISSUE:-}"
case "$prompt" in *"did not account for"*) drop="" ;; esac
jq -n --arg list "$list" --arg drop "$drop" '
  ($list | split(", ") | map(select(. != $drop)))
  | map(capture("^(?<r>.+)#(?<n>[0-9]+)$"))
  | {
      bullets: map({
        text: "- Fixed problem \(.n) in the area.",
        category: "Other",
        sourceIssues: [{repositoryWithOwner: .r, number: (.n | tonumber)}]
      }),
      omittedIssues: [],
      pendingReviewIssues: []
    }'
FAKE
chmod +x "$test_dir/bin/copilot"

cat > "$test_dir/bin/rules" <<'FAKE'
#!/usr/bin/env bash
echo "Stand-in for the documentation review rules."
FAKE
chmod +x "$test_dir/bin/rules"

# make_release <count> <body words> <file>: <count> issues, each with a long body and long comments.
make_release() {
  jq -n --argjson count "$1" --argjson words "$2" '
    ([range(0; $words) | "word\(.)"] | join(" ")) as $text
    | {releases: [{
        statusId: "x",
        statusName: "Wait for RN - Omnia 7.99.1 / WCM 7.99.1",
        issues: [range(1; $count + 1) | {
          number: .,
          title: "Issue \(.)",
          body: $text,
          url: "https://github.com/omniaintranet/OmniaMono/issues/\(.)",
          updatedAt: "2026-11-12T00:00:00Z",
          labels: ["bug"],
          comments: [range(0; 4) | {author: "tester", createdAt: "2026-11-12T00:00:00Z", body: $text}],
          repository: "OmniaMono",
          repositoryWithOwner: "omniaintranet/OmniaMono"
        }]
      }]}
  ' > "$3"
}

# run_generate <name> <release file> [VAR=value ...]: runs the script in its own folder; sets
# $run_dir, $run_log and $run_status.
run_generate() {
  local name="$1" release="$2"
  shift 2
  run_dir="$test_dir/$name"
  mkdir -p "$run_dir"
  cp "$release" "$run_dir/release-issues.json"
  cp .github/skills/hotfix-release-notes/categories.txt "$run_dir/categories.txt"
  : > "$run_dir/prompts.log"
  run_log="$run_dir/output.log"
  run_status=0
  # The script keeps its files in /tmp; run a copy that keeps them in the run folder instead (the same
  # rewrite test-release-review.py does), so the test never touches a real /tmp/release-issues.json.
  sed "s#/tmp/#$run_dir/#g" .github/scripts/hotfix-release-notes/generate-release-notes.sh > "$run_dir/generate-release-notes.sh"
  cp .github/scripts/hotfix-release-notes/wait-for-rn-lib.sh .github/scripts/hotfix-release-notes/wait-for-rn-pattern.txt "$run_dir/"
  env "$@" \
    PATH="$test_dir/bin:$PATH" \
    CATEGORIES_FILE="$run_dir/categories.txt" \
    PYTHON="$test_dir/bin/rules" \
    FAKE_LOG="$run_dir/prompts.log" \
    bash "$run_dir/generate-release-notes.sh" > "$run_log" 2>&1 || run_status=$?
}

budget_chars() { echo $((PROMPT_TOKEN_BUDGET * CHARS_PER_TOKEN)); }
export PROMPT_TOKEN_BUDGET=90000 CHARS_PER_TOKEN=3
limit=$(budget_chars)

# 1. A release that fits one request: one request, no batch context, nothing about batches in the log.
make_release 3 200 "$test_dir/small.json"
run_generate small "$test_dir/small.json"
[ "$run_status" -eq 0 ] || { fail "small release failed"; cat "$run_log" >&2; }
[ "$(wc -l < "$run_dir/prompts.log")" -eq 1 ] && pass "small release: one request" || fail "small release: expected one request"
[ ! -e "$run_dir/prompts.log.context" ] && pass "small release: prompt carries no batch context" || fail "small release: unexpected batch context"
grep -q "does not take all" "$run_log" && fail "small release: batching message printed" || pass "small release: no batching message"
[ "$(grep -c '^- ' "$run_dir/generated-release-notes.rst")" -eq 3 ] && pass "small release: three bullets" || fail "small release: wrong bullet count"

# 2. A release over the budget (57 issues, as in the failed run): several requests, each under the budget.
make_release 57 300 "$test_dir/large.json"
single_prompt_estimate=$(jq -c . "$test_dir/large.json" | wc -m)
[ "$single_prompt_estimate" -gt "$limit" ] || fail "large fixture is not over the budget ($single_prompt_estimate <= $limit)"
run_generate large "$test_dir/large.json"
[ "$run_status" -eq 0 ] || { fail "large release failed"; tail -20 "$run_log" >&2; }
requests=$(wc -l < "$run_dir/prompts.log")
[ "$requests" -gt 1 ] && [ "$requests" -lt 10 ] && pass "large release: $requests requests" || fail "large release: expected a few requests, got $requests"
too_big=$(awk -v limit="$limit" '$1 > limit' "$run_dir/prompts.log" | wc -l)
[ "$too_big" -eq 0 ] && pass "large release: every prompt within $limit characters" || fail "large release: $too_big prompt(s) over $limit characters"
[ "$(grep -c '^- ' "$run_dir/generated-release-notes.rst")" -eq 57 ] && pass "large release: 57 bullets in the notes" || fail "large release: wrong bullet count"
jq -e '[.bullets[].sourceIssues[].number] | sort == [range(1; 58)]' "$run_dir/release-notes-audit.json" >/dev/null &&
  pass "large release: every issue accounted for once" || fail "large release: audit does not account for every issue"
grep -q "Generated release notes passed" "$run_log" && pass "large release: validation passed" || fail "large release: validation did not pass"
[ -e "$run_dir/prompts.log.context" ] && pass "large release: later batches carry the bullets already written" || fail "large release: no batch context"

# 3. A follow-up for a missing issue also works with batches (issue 5 missing from the first answer).
run_generate followup "$test_dir/large.json" FAKE_DROP_ISSUE=omniaintranet/OmniaMono#5
[ "$run_status" -eq 0 ] || { fail "follow-up run failed"; tail -20 "$run_log" >&2; }
grep -q "Asking Copilot about only those issues" "$run_log" && pass "follow-up: missing issue asked again" || fail "follow-up: no follow-up request"
[ "$(grep -c '^- ' "$run_dir/generated-release-notes.rst")" -eq 57 ] && pass "follow-up: 57 bullets in the notes" || fail "follow-up: wrong bullet count"

# 4. One issue larger than a whole request is shortened for the model; the run still succeeds.
make_release 1 120000 "$test_dir/huge.json"
run_generate huge "$test_dir/huge.json"
[ "$run_status" -eq 0 ] || { fail "huge issue run failed"; tail -20 "$run_log" >&2; }
[ "$(wc -l < "$run_dir/prompts.log")" -eq 1 ] && [ "$(head -n1 "$run_dir/prompts.log")" -le "$limit" ] &&
  pass "huge issue: shortened to fit one request" || fail "huge issue: prompt over the budget"

# 5. A smaller budget batches a small release too, and the batches are sized by the budget.
run_generate tight "$test_dir/small.json" PROMPT_TOKEN_BUDGET=6000
[ "$run_status" -eq 0 ] || { fail "tight budget run failed"; tail -20 "$run_log" >&2; }
[ "$(wc -l < "$run_dir/prompts.log")" -gt 1 ] && pass "tight budget: several requests" || fail "tight budget: expected several requests"

if [ "$failures" -gt 0 ]; then
  echo "$failures check(s) failed." >&2
  exit 1
fi

echo "All batching checks passed."
