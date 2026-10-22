---
name: omnia-release-notes
description: Draft customer-facing Omnia hotfix release notes from the Omnia GitHub organization project. Use when finding cards in a "Wait for RN" (or close variant such as "Waiting for RN") or named approved release status, reviewing their customer references and QA outcomes, or revising an Omnia 7.11.x release-note draft.
---

# Omnia Release Notes

Create concise public release notes from organization project `omniaintranet/8` using the user's authenticated GitHub CLI environment.

## Retrieve the release

1. If the user names a complete project status, use it exactly. Otherwise inspect project item statuses and find unique values beginning with `Wait for RN` or a close variant such as `Waiting for RN` or `Awaiting release notes` (the automation matches these through `.github/scripts/hotfix-release-notes/wait-for-rn-pattern.txt`).
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

### Verify customer references before delivery

Keep source issue identity separate from customer references. In automation, `sourceIssues[].number` identifies the internal GitHub card for audit accounting; it does not authorize appending that number to the public bullet's `text`.

Before drafting each bullet, collect only the Zendesk/OIM numbers extracted from supported URLs in that bullet's source card bodies or trusted discussion. Treat no matching URLs as an empty customer-reference list. A GitHub URL ending in `/issues/4331` is never an OIM reference.

- If a GitHub source card is numbered `4331` and has no supported Zendesk/OIM URL, an otherwise eligible bullet must have no reference suffix. Do not append `(#4331)` as a fallback.
- If that same card contains a supported Zendesk URL ending in `/agent/tickets/59036`, use `(#59036)` and retain `4331` only in the internal source accounting.
- For consolidated bullets, use only the union of verified customer references from the associated source cards. Do not borrow a reference from an unrelated card in the release.

**Before finalizing, check every public `#` reference against a supported URL on an associated source card. Remove any reference without that evidence; do not replace it with the GitHub card number or remove an otherwise eligible bullet merely because it has no customer reference.** If automation rejects an unsupported reference, correct the reference while preserving source accounting and rerun validation; do not bypass the validator.

## Decide what belongs in the public notes

Include changes that are customer-reported, materially customer-visible, new functionality, important compatibility changes, or security/reliability improvements worth communicating.

Omit an unreferenced internal defect when it is suitable for silent delivery. Typical examples are narrow regressions found by QA, internal logging corrections, and low-level maintenance fixes. Do not omit a meaningful feature merely because it lacks a formal ticket.

When an implementation was made for one customer's special case, describe it cautiously or omit it. Do not imply broad platform support unless QA and the implemented behavior justify that claim.

If two or more cards describe the same shipped correction, consolidate them into one bullet and combine distinct Zendesk/OIM references. Account for the consolidation when reporting card and bullet counts.

### Security-sensitive changes

Review changes involving authentication, authorization, account recovery, permissions, tokens, and other security-sensitive functionality before including them in public release notes.

- Flag potentially security-sensitive entries for manual review rather than automatically publishing or excluding them. Keep pending entries separate from the public draft until that review determines how to communicate them.
- Avoid technical details that could help identify, reproduce, or exploit a security weakness.
- Prefer high-level, customer-focused descriptions of security-related improvements.
- Make security-related suggested wording deliberately general, even in pending-review drafts. Describe only a broad improvement category, such as URL validation. Omit the specific workflow, vulnerable component, trigger, attack method, and prevented exploit; do not describe where or how the weakness can be used. For example, prefer `Improved security validation of URLs to fix a possible security issue (#60130)` over wording that identifies login redirects, domain checks, or unauthorized redirection. Use a reference only when verified for the associated source card. Review the suggestion specifically for clues that could direct a reader toward the weakness, and generalize them before delivery.
- For every pending entry, include both a high-level reason for manual review and suggested customer-facing release-note wording. Keep the suggestion concise, factual, and free of technical details that could identify, reproduce, or exploit a weakness. Apply the same verified customer-reference rules. Label it as pending approval and keep it outside public release-note bullets until a reviewer approves inclusion. In structured automation output, put this wording in `suggestedText` on the pending entry.
- During manual review, omit security-sensitive fixes when public disclosure is unnecessary, unless a security disclosure policy or customer communication requirement applies.

## Write in the established Omnia style

Use this format:

```rst
7.11.x
========================================
(Omnia 7.11.x / Workplace 7.11.x / WCM 7.11.x / MS 7.11.x / Analytics x / Feed x)

- Release-note bullet
```

Derive the version line from the project status and remove the waiting label and its separator (for example `Wait for RN - ` or `Waiting for RN - `).

Write short, customer-facing bullets in neutral English. Remove customer names unless essential. Name Omnia features consistently, such as Page Rollup, Document Bulk Update, Page Bulk Update, Quick Search, Semantic Search, Publishing App, and Controlled Documents.

Make the affected product or functional scope explicit whenever the wording could apply to more than one Omnia area. Use the implementation and QA evidence to identify whether the change concerns documents, pages, processes, or a named product such as ODM or OPM; do not rely on readers to infer the scope from generic terms such as `publishing process` or `workflow history`. Prefer the clearest customer-facing wording, for example:

- `Workflow history now correctly reflects when a document publishing process has been canceled (#55468)`
- `Workflow history now correctly reflects when a publishing process in ODM has been canceled (#55468)`

Prefer the first form when the affected object communicates the scope clearly; use a product name or acronym when it removes ambiguity more effectively.

Prefer concrete descriptions of the affected scenario:

- `Fixed an issue that could prevent document searches in Document Bulk Update from returning results in some scenarios (#59036)`
- `A–Z filtering in the Page Rollup now returns the correct results when users select a letter (#59558, #59606)`

Avoid vague claims such as `now returns the expected results`, which can imply the feature never worked. Identify the affected action and scenario when saying it now works as expected. Avoid raw technical causes, internal configuration names, database details, and unsupported guarantees.

### Sentence variation and readability

- Prefer describing the corrected behavior or customer-visible result rather than explaining what was previously broken.
- Avoid repetitive sentence openings, particularly `Fixed an issue where...`, `Fixed an issue in...`, and `Improved...`. Vary sentence structure naturally across consecutive entries.
- Use a mix of formulations as appropriate to the actual scope:
  - `[Feature] now correctly handles...`
  - `[Feature] now supports...`
  - `Users can now...`
  - `[Action] now works as expected...`
  - `Corrected an issue preventing...`
  - `Improved [feature] to ensure...`
  - `Resolved an issue affecting...`
- Do not force variation at the expense of clarity or technical accuracy. Keep entries concise, factual, and customer-focused; avoid unnecessary verbosity.
- **Before finalizing, review all entries together and rewrite repetitive sentence openings.** As a guideline, avoid starting more than two consecutive entries with the same phrase or sentence pattern.

Published text must also pass the documentation review (`.github/docs-review/README.md`): no internal or sales language, unfinished text, superlatives, promises about future releases, or confidential data. Automation adds the current rules to its prompt (`python .github/scripts/docs-review/docs_review.py --prompt-rules`) and gives flagged bullets back for rewording; in an interactive chat, run that command and follow its output.

When matching house style is uncertain, consult the published versions page:
`https://omnia-docs-g2.readthedocs.io/en/latest/release-notes/7.0/versions.html`.

## Deliver the draft

Choose the output wrapper requested by the caller:

- In an interactive chat, return the finished notes as a `document` writing block. Keep the same writing-block ID when revising that release within a chat.
- In automation that explicitly requests raw RST, return only the RST content without a writing block, code fence, audit summary, or commentary. Put every bullet on one physical line. If the caller says it constructs the heading separately, return only the requested RST bullet lines.

When automation requests structured JSON, follow its schema and record security-sensitive entries separately as pending manual review, outside public bullets.

For interactive delivery, provide a compact audit summary outside the writing block:

- total matching GitHub cards;
- number of published bullets;
- any consolidated cards;
- omitted cards and the reason for omission;
- potentially security-sensitive cards pending manual review, with a high-level reason and suggested release-note wording marked as pending approval; keep sensitive details out of the public notes.

When the user requests only a wording revision or an omitted-item list, answer only that focused request unless the full draft is needed for clarity.
