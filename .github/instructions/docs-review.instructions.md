---
applyTo: "**/*.rst"
excludeAgent: "cloud-agent"
---

# Reviewing Omnia documentation changes

These pages are published to customers at https://omnia-docs-g2.readthedocs.io/. Review every changed `.rst`
file as the customer who will read it. Comment only on the lines the pull request changes.

The workflow "Documentation review" already blocks fixed phrase lists (sales words such as "key selling point",
TODO/TBD, superlatives, "coming soon"), email addresses, tenant host names, GUIDs, IP addresses, internal ticket
numbers, secrets, broken references and new build warnings. Do not repeat its findings. Look for what fixed rules
cannot see.

## What to look for

1. **Wrong reader.** Check that the text fits the audience of its section:
   - Administrators: `admin-settings/`, `setup/`, `switch-site-selected/`, the SharePoint policy pages.
     Settings, permissions and setup steps. Technical terms from Microsoft 365 and Azure are fine.
   - Editors: `pages/`, `blocks/`, `working-with-documents/`, `working-with-processes-v7/`, `working-with-events/`,
     `general-assets/`. How to create and publish content. No developer or infrastructure terms.
   - End users: `user-options/`, `using-communities/`, `using-newsletters/`, `using-omnia-feed/`.
     Plain language, task first, no admin settings unless the user must ask an admin.
   - Developers: `mcp/`, `mcp-context/`. Precise technical language is expected.
   - Release notes (`release-notes/`): every customer reads them. Short, neutral bullets that say what changed for
     the reader and in which feature. No code names, class names, configuration keys, database or API details.
   Flag developer jargon (component, API, endpoint, payload, flag, refactor, backend, regression, hotfix branch,
   class or property names) on editor and end-user pages, and suggest the words a reader of that page would use.
2. **Internal-sounding text the rules miss.** Sales or positioning language in other words ("this sets us apart",
   "customers have asked for this for years", "this will help close"), notes to colleagues, names of internal
   teams, people, customers or projects, internal processes (QA, sprint, board, card, Slack/Teams channel), and
   wording copied from tickets.
3. **Promises and uncertainty.** Indirect promises about future releases or dates, and unsupported guarantees
   ("always", "never fails", "fully secure"). Describe what is available now.
4. **Confidentiality in text.** Customer names, real people, real tenant or site names written without a URL,
   details of security fixes that could help an attacker (keep these general, as the release-note skill in
   `.github/skills/hotfix-release-notes/SKILL.md` requires).
5. **Clarity for this reader.** Ambiguous scope (which product or feature is meant), steps out of order, UI labels
   that do not match the product, sentences that are hard to follow.

## How to comment

- One comment per problem, on the changed line, with a concrete suggested rewrite (use a suggestion block when the
  fix is a replacement of the line).
- Explain in one sentence why the reader would be confused or why the text must not be published.
- Keep the existing terminology, heading style and structure of the section.
- Do not comment on rst markup, spelling style preferences or anything outside the changed lines.
- If the change is fine, say so briefly instead of inventing problems.
