---
name: omnia-release-notes
description: Draft customer-facing Omnia hotfix release notes from the Omnia GitHub organization project. Use when finding cards in a "Wait for RN" or named approved release status, reviewing their customer references and QA outcomes, or revising an Omnia 7.11.x release-note draft.
---

# Omnia Release Notes

Create concise public release notes from organization project `omniaintranet/8` using the user's authenticated GitHub CLI environment.

## Retrieve the release

1. If the user names a complete project status, use it exactly. Otherwise inspect project item statuses and find unique values beginning with `Wait for RN`.
2. If one matching status exists, proceed with it. If several exist and the intended release cannot be inferred safely, show the matches and ask which release to prepare.
3. Retrieve every project item with that exact status. Record the GitHub repository, card number, title, labels, and URL for audit purposes.
4. Read the full body and relevant recent comments for every issue. Prefer the implemented and QA-verified behavior over the initial title, proposed solution, or AI investigation.
5. Do not change the project status or edit GitHub cards unless the user explicitly requests it.

The project may contain private data. Keep customer URLs, email addresses, environment details, screenshots, logs, and implementation details out of the public draft.

## Handle issue references correctly

- GitHub issue numbers are internal card identifiers and must never be used as the `#` reference in public release notes.
- Append a reference only when the card or its trusted discussion contains a Zendesk ticket URL such as `.../agent/tickets/59036` or an Omnia Issue Management URL ending in `/issues/166490`.
- Render those references as `(#59036)` or `(#59558, #59606)`.
- Do not invent, infer, or copy a number from a title. Trello and linked GitHub card numbers are not public release-note references.
- A clearly customer-originated change without a Zendesk/OIM number may still be included without a number when it is meaningful to communicate.

## Decide what belongs in the public notes

Include changes that are customer-reported, materially customer-visible, new functionality, important compatibility changes, or security/reliability improvements worth communicating.

Omit an unreferenced internal defect when it is suitable for silent delivery. Typical examples are narrow regressions found by QA, internal logging corrections, and low-level maintenance fixes. Do not omit a meaningful feature merely because it lacks a formal ticket.

For a security correction, use deliberately general wording that communicates improvement without exposing an exploitation path.

When an implementation was made for one customer's special case, describe it cautiously or omit it. Do not imply broad platform support unless QA and the implemented behavior justify that claim.

If two or more cards describe the same shipped correction, consolidate them into one bullet and combine distinct Zendesk/OIM references. Account for the consolidation when reporting card and bullet counts.

## Write in the established Omnia style

Use this format:

```text
# 7.11.x

(Omnia 7.11.x / Workplace 7.11.x / WCM 7.11.x / MS 7.11.x / Analytics x / Feed x)

- Release-note bullet
```

Derive the version line from the project status and remove the `Wait for RN - ` prefix.

Write short, customer-facing bullets in neutral English. Remove customer names unless essential. Name Omnia features consistently, such as Page Rollup, Document Bulk Update, Page Bulk Update, Quick Search, Semantic Search, Publishing App, and Controlled Documents.

Prefer concrete descriptions of the affected scenario:

- `Fixed an issue that could prevent document searches in Document Bulk Update from returning results in some scenarios (#59036)`
- `A–Z filtering in the Page Rollup now returns the correct results when users select a letter (#59558, #59606)`

Avoid vague claims such as `now returns the expected results`, which can imply the feature never worked. Avoid raw technical causes, internal configuration names, database details, and unsupported guarantees. Use phrases such as `Fixed an issue that could...`, `Improved...`, or `Added support for...` according to the actual scope.

When matching house style is uncertain, consult the published versions page:
`https://omnia-docs-g2.readthedocs.io/en/latest/release-notes/7.0/versions.html`.

## Deliver the draft

Return the finished notes as a `document` writing block. Keep the same writing-block ID when revising that release within a chat.

Outside the writing block, provide a compact audit summary:

- total matching GitHub cards;
- number of published bullets;
- any consolidated cards;
- omitted cards and the reason for omission.

When the user requests only a wording revision or an omitted-item list, answer only that focused request unless the full draft is needed for clarity.
