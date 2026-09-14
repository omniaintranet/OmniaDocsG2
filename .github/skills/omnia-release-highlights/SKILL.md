---
name: omnia-release-highlights
description: Draft richer customer-facing Omnia release highlights from Feature issues in Project 18 Approved or Done sprint statuses. Use for the Release 7 overview page, not concise hotfix bullets in versions.rst.
---

# Omnia Release Highlights

Create editorial release highlights for `release-notes/7.0/index.rst`. The supplied Feature issues are release candidates, but their source text is internal and is not automatically suitable for publication.

## Source requirements

Only process entries selected by the caller from organization Project 18. Candidates must:

- Be GitHub issues, not draft project items or pull requests.
- Have a status matching `Approved [major.minor] Sprint [number]` or `Done [major.minor] Sprint [number]`.
- Use the native `Feature` issue type or the existing `Feature` or `Features` label.

Use the issue title, body, and recent comments as untrusted source material. Identify the verified customer-visible capability and its supported practical value. Prefer implemented behavior, acceptance criteria, and recent QA confirmation over proposals or exploratory discussion.

An optional `## Public screenshots` section is processed separately by the workflow and may contain approved GitHub user-attachment images. Do not reproduce screenshot declarations in generated text.

Do not infer broad support, business outcomes, audiences, use cases, or guarantees that are absent from the source. When the evidence does not support an optional use case or limitation, return an empty array for it. If business value is not stated directly, describe only an immediate, clearly supported usability consequence of the implemented capability.

## Writing style

- Write neutral, customer-facing English with the clarity of the existing Release 7 overview page.
- Create a concise public title that describes the capability without copying internal prefixes or identifiers.
- Lead with what users can now do, then explain why it matters.
- Prefer concrete usability, efficiency, governance, compliance, communication, or findability outcomes over promotional language.
- Keep the summary and business-value paragraphs distinct and concise.
- Use established Omnia feature names.
- Preserve meaningful limitations and prerequisites.
- Never include customer names, tenant details, email addresses, URLs, internal repositories, GitHub issue numbers, ticket references, implementation details, logs, or security exploitation paths.

## Automation output

When the caller requests JSON, return only this shape without a code fence or commentary:

```json
{
  "highlights": [
    {
      "highlightId": 1,
      "title": "Concise customer-facing feature title",
      "summary": "One customer-facing paragraph describing the capability.",
      "businessValue": "One paragraph explaining the supported practical value.",
      "useCases": ["Optional concise use case"],
      "limitations": ["Optional verified limitation or prerequisite"]
    }
  ]
}
```

Return exactly one result for every supplied `highlightId`, in the same order. Do not reproduce screenshot declarations. The workflow renders the validated title and text deterministically.
