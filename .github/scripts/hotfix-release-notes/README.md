# Approved hotfix release closeout

`sync-approved-release-notes.py` runs from `sync-approved-hotfix-release-notes.yml`
on approval or merge of a release-note PR from this repository into `master`.
It keeps the approved notes and generated draft in the release notification,
creates or reuses the release milestone, assigns it to issues without a milestone,
closes the issues, moves the column to Released, converts the notification into
an issue, milestones and closes it, and closes the release milestones.
Existing different milestones are preserved.

In that closeout, issues receiving the release milestone also receive the board 8
NUMBER field `Release order`. The notification receives it too. The value is the
Omnia version encoded as `major * 1000000 + minor * 1000 + patch`, for example
`7.12.12` becomes `7012012`. The PR version must match the Omnia part of the
release column and derived milestone; Analytics and Feed versions are not used.
Issues retaining a different milestone, pull requests, and other drafts keep
their existing Release order values.

The field is looked up by exact name and must have type NUMBER. Missing or
incorrect field definitions and conflicting item values stop planning before
any writes. Correct values are skipped. Missing values are set before the items
leave the release column, so reruns can finish after an interrupted closeout,
including after a milestone assignment succeeded. Only item field values are
written, never field definitions. If the notification is moved manually and the
release column is deleted after a failed write, a rerun cannot finish its pending
Release order, milestone assignment, or closure. There is no historical backfill.

For a read-only plan, set `PR_NUMBER` and `SYNC_DRY_RUN=true` when invoking the
script. Its output lists the number and items it would update. Offline tests:

```sh
python .github/scripts/hotfix-release-notes/test-approved-release-sync.py
```
