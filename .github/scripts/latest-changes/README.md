# Latest documentation changes

`latest-changes.yml` runs daily at 07:00 Europe/Copenhagen and can also be run
manually. It updates `latest-changes/index.rst` on the repository default branch.
Read the Docs publishes this page through the existing repository integration.

The report contains only linked documentation titles, a classification, and a
short reader-facing description, grouped by the merge date in Copenhagen time.
It retains the last 90 calendar days and combines each page's changes on a day.
The first run backfills that same period. It processes only merged PRs targeting
the default branch whose merge commit is present in the checkout. Direct commits
are outside the PR-based scope.

Text changes are classified by GitHub Copilot CLI using the repository's existing
workflow-token authentication pattern (`copilot-requests: write`). New pages and
image-only updates have deterministic classifications. PR content is untrusted
data: the classifier is denied file, shell, web, and memory tools, has built-in
MCP servers disabled, uses no repository instructions, and
must return validated JSON. Invalid responses are retried up to three times.
It never receives GitHub credentials in its prompt.
Classifications describe documentation changes, not changes to product behavior.

Internal state records processed PR numbers and reader entries. It is never
included in the public page. Failed classification, incomplete API results,
missing build targets, or a concurrent branch update prevent publication. The
next run retries unprocessed changes still inside the 90-day window. Deleted
pages are removed from the report; renamed pages' earlier links are migrated.
Changes to the digest itself, automation, root navigation, and build settings
are excluded. Images and shared includes are mapped to their referencing pages.

## Activation

Merge the workflow, scripts, navigation entry, and page into the default branch.
GitHub Actions must allow workflow-token writes and Copilot requests. The default
branch must allow this workflow to push its two generated files. Branch rules
are respected: if writes are blocked, the workflow fails without overwriting
anything. Read the Docs must build the default branch for its `latest` version.
Use **Actions → Latest documentation changes → Run workflow** for the initial
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
