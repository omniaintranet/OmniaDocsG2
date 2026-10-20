:orphan:

Release 7.13 (draft)
================================================

.. REVIEW NOTE: Built from the existing 7.13 draft plus the commits that are in the dev branch but not in 7.12 (preview/main), as of 20 Oct 2026. Items marked "REVIEW" in rst comments need a fact check and are not rendered. Bug fixes, build and internal changes are left out on purpose. Each section lists the key selling points only; smaller details are folded in or left out.

AI
------------------------------------------------
- Omnia Skills and Agent Studio: build Omnia Agents with their own skills, guardrails and audiences, including Ask Omnia, which uses Omnia MCP tools
- Responsible AI: answers respect each user's permissions, guardrails check messages and answers, AI use is recorded, and content disclaimers can be shown
- AI Insights in Page Rollup, Analytics Report, Metrics and Target Reach
- Credit-based AI usage and subscription
- Your choice of AI provider, including Microsoft AI Foundry with Azure RBAC authentication
- Better AI context from object descriptions, and AI prompts that can be set per business profile

.. REVIEW: Upgrade notes to decide. Agent Studio needs the feature activated, existing Ask Omnia and chat settings are migrated, and direct OpenAI organization-key chat is retired as a chat provider. Customized Content Builder AI prompts must be saved again in each business profile.

.. REVIEW: Removed "Full undo/redo support on pages and page types": no such code in dev, and the backlog item is still open.

.. REVIEW: Possibly missing (dev-only, before 5 Oct): Text Completion renamed to "Omnia AI suite" (#2786) and the Activity Hub Reach dashboard (#2770).

Semantic Search
------------------------------------------------
- Answers only from content each user is allowed to see
- Choose what is searchable per page type, document type, page collection and authoring site, or include all pages and documents

Smart Properties
------------------------------------------------
- Smart properties for documents, app instances and users, filled in automatically
- Smart property rules without AI for users, page types and document types

.. REVIEW: Removed "Deprecation of Auto-summary and Auto-tagging": "Enable Automatic Summary" is unchanged in dev and no deprecation commit was found. Restore it if the deprecation is announced without a code change.

Free form views
------------------------------------------------
- Design rollups, search results and the high priority announcements banner with your own HTML and CSS templates
- An editor with live preview, tokens, conditions and multilingual labels, so templates show exactly the information each audience needs

.. REVIEW: Free form covers Page, People, Document, Process, App instance, Calendar, Media, Channel, Team News, Sign-off request, Form, Teamwork and List rollups, the RSS reader, Quick links, Announcements, Quick search, Advanced search and semantic search answers. Anyone who can edit a block's settings can author templates; confirm before saying more about authoring rights.

Activity Hub
------------------------------------------------
- One place for activities, tasks and chat, in the mega menu, the left panel and the Omnia mobile app
- Secure chat with encrypted messages, image attachments and emoji
- Reach the right people: channel collections, targeting personas, default and enforced subscriptions
- Never miss what matters: digests of missed activities, review reminders for documents and pages, and rich push and Microsoft Teams notifications
- Bring Activity Hub to any page with the Activity Panel and Activity Feed blocks
- Omnia mobile app: create pages, edit your profile, sign up for events and watch videos without leaving the app
- Administrators get a scoped Activity Hub administrator role, and page views are reported to Matomo

.. REVIEW: The mobile app is released separately (app stores and over-the-air updates), and several of its source issues are still in scenario test. Decide whether the mobile bullet stays in the 7.13 notes.

.. REVIEW (security, pending approval): A new permission role for publishing activities (#4345). Suggested wording: "New permission role for publishing activities". Not rendered until reviewed.

Web Content Management
------------------------------------------------
- Compare variations side by side in the editor
- Readers can translate comments and replies on request
- A "Do not translate" list keeps product names and company terms in the original language when content is machine translated
- An alert when viewing a draft that has never been published

.. REVIEW: Left out as details: alternate layouts for publishing app layouts, Page Rollup Calendar "Open on" and List "Show total row", and page creation action buttons that copy several properties (#4339). Add back if any of them is a selling point.

.. REVIEW (security, pending approval): Share to LinkedIn with a public page preview in the External Share action button (#4465). Suggested wording: "External Share action button: share pages to LinkedIn with a preview". Not rendered until reviewed.

Event Management
------------------------------------------------
- All-day events, in-person or online (Teams) attendance, and Outlook busy status
- Your own questions in event sign-up forms

Navigation and Layout
------------------------------------------------
- Single header layout with header settings
- User menu in the left panel
- Faster navigation: quick links, menus and footer links open without reloading the page

.. REVIEW: Removed "Quick access drawer for the left panel on mobile": it shipped in 7.12 (#3919).

Miscellaneous
------------------------------------------------
- FAQ blocks can look the same as accordion sections
- Unread news can be highlighted in more views
- A font picker in the admin font settings

.. REVIEW (security, pending approval): External OpenID Connect sign-in (#4542, #4735). Suggested wording: "Users can sign in with the organization's OpenID Connect identity provider, also when they sign up through self-service". Not rendered until reviewed.
