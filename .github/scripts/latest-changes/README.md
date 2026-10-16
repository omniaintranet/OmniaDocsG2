# Documentation updates

`latest-changes.yml` runs daily at 07:00 Europe/Copenhagen and can also be run
manually. It updates `documentation-updates/index.rst` on the repository default branch.
Read the Docs publishes this page through the existing repository integration.

The report contains only linked documentation titles, a classification, and a
short reader-facing description, grouped by the date changes reach the publishing
branch, in Copenhagen time.
It retains the last 90 calendar days and combines each page's changes on a day.
Navigation-only updates are excluded from the reader digest. They remain in
internal state to avoid repeated classification. Changes that also update page
content are included under the applicable content classification.
It covers **all documentation changes on the default branch**, including direct
commits, browser edits, uploaded screenshots, and merged PRs, for every author.
It follows the checked-out branch's first-parent history and compares each commit
with its first parent. This counts merged changes once rather than reporting
every feature-branch commit again. Unmerged branches are excluded.

The first run backfills the same 90-day period. Upgrading from the PR-only version
preserves existing entries and seeds their processed merge SHAs, then backfills
previously missed direct commits. Direct and merged changes affecting the same
page/date are combined into one entry. Repeated edits use a complete net diff.

Text changes are classified by GitHub Copilot CLI using the repository's existing
workflow-token authentication pattern (`copilot-requests: write`). New pages and
image-only updates have deterministic classifications. Commit content is untrusted
data: the classifier is denied file, shell, web, and memory tools, has built-in
MCP servers disabled, uses no repository instructions, and
must return validated JSON. Invalid responses are retried up to three times.
It never receives GitHub credentials in its prompt.
Classifications describe documentation changes, not changes to product behavior.

Internal state records processed commit SHAs and per-entry source SHAs. It is never
included in the public page. Failed classification, incomplete API results,
missing build targets, or a concurrent branch update prevent publication. Each
run classifies up to 60 page/date groups, newest first, with at most three
independent classifiers running concurrently. All selected results must validate
before either generated file is written. Larger backfills resume
on subsequent runs without duplicating entries or reclassifying finished pages,
even when a single commit changes more than 60 pages. Each run reports remaining
groups in its log and `remaining_groups` step output. Manually rerun the workflow
until that count reaches zero to complete an immediate backfill. Otherwise the
daily schedule continues it. Failed work is retried inside the 90-day window. Deleted
pages are removed from the report; renamed pages' earlier links are migrated.
Changes to the digest itself, automation, root navigation, and build settings
are excluded and do not advance commit tracking. This prevents the generated
digest/state commit from causing another commit on a quiet day. Images and
shared includes are mapped to their referencing pages.

## Activation

Merge the workflow, scripts, navigation entry, and page into the default branch.
GitHub Actions must allow workflow-token writes and Copilot requests. The default
branch must allow this workflow to push its two generated files. Branch rules
are respected: if writes are blocked, the workflow fails without overwriting
anything. Read the Docs must build the default branch for its `latest` version.
Use **Actions → Documentation updates → Run workflow** for the initial
backfill. No new repository secret is required by this implementation.

## Local validation

```sh
python -m unittest discover -s .github/scripts/latest-changes -p 'test_*.py'
python -m sphinx -b html . _build/html
python .github/scripts/latest-changes/update.py --check-build _build/html
```

For a live local run, use a clean checkout of the default branch, authenticated
`gh`, and `copilot`, with `GITHUB_REPOSITORY=omniaintranet/OmniaDocsG2` and
`DOCS_BRANCH` set to the publishing branch. The script only writes local files;
the workflow separately builds and commits them. It does not push from Python.
