:orphan:

Release 7.13 (draft)
================================================

.. REVIEW NOTE: Built from the existing 7.13 draft plus the commits that are in the dev branch but not in 7.12 (preview/main), as of 5 Oct 2026. Items marked "REVIEW" in rst comments need a fact check and are not rendered. Bug fixes, build and internal changes are left out on purpose.

AI
------------------------------------------------
- Credit-based AI usage and subscription
- AI Insights added to Page Rollup, Analytics Report, and Metrics blocks
- AI action and prompts added to Target Reach
- AI respects each user's permissions
- Omnia Skills and Omnia Agents
- Ask Omnia: a system agent that uses Omnia MCP tools
- Object descriptions to improve AI context knowledge (Enterprise properties, page types, blocks, document types)
- Admin customization of AI prompts (pre- and post-prompts), with consistent prompt editors
- AI use is recorded, and content disclaimers can be shown
- AI settings are hidden when no AI provider is configured
- Rich text AI responses
- Full undo/redo support on pages and page types

.. REVIEW: Pre- and post-prompts. The 7.12 notes list Semantic Search pre- and post-prompts as already announced in 7.11.x. Confirm whether the 7.13 item is the same or an extension (for example prompts for other AI features).

.. REVIEW: "AI respects each user's permissions" comes from the RBAC user-context work (#1056). Confirm it is the same as permission-trimmed Semantic Search below, or keep both.

.. REVIEW: Rich text AI responses and undo/redo come from the earlier draft. They were not found in the dev commits, so confirm they are in 7.13.

Semantic Search
------------------------------------------------
- Permission-trimmed semantic search results
- Alignment of semantic search functionality (Page types/Document types, Page collections/Authoring sites)
- Option to include all pages and documents

.. REVIEW: "Include all" - confirm the wording (#2975).

Smart Properties
------------------------------------------------
- Smart properties for documents and app instances
- Automatic smart properties for users
- Deprecation of:

  - Auto-summary
  - Auto-tagging

Activity Hub
------------------------------------------------
- Activity Hub in the mega menu and left panel
- Chat: encrypted messages and image attachments, delete messages and conversations, emoji, chat notifications
- Content Builder pages display in Activity Hub (web and mobile)
- Notification links open in the configured panes
- Configurable navigation content, panes and badges
- Activity Hub administrator role with scoped access
- Targeting personas in the Activity Hub feed
- New Activity Panel block
- Block height settings for feeds and chats
- Activity Hub page views are reported to Matomo as page reads
- WCAG improvements on web and mobile
- Re-worked sign-in flow in the Omnia mobile app

Web Content Management
------------------------------------------------
- Variation comparison dialog in the editor
- Alert when viewing a draft that has never been published
- Alternate layouts for publishing app layouts, as on the workspace home page

Event Management
------------------------------------------------
- All-day events
- Outlook busy status for events
- Attendance mode (in person or online)
- Own questions in event sign-up forms

.. REVIEW: Attendance mode - confirm the options (in person / Microsoft Teams) from #1014.

Navigation and Layout
------------------------------------------------
- Single header layout with header settings
- User menu action in the left panel
- Quick access drawer for the left panel on mobile

.. REVIEW: The left panel (Everywhere Panel) shipped in 7.12. Confirm the user menu action and the mobile drawer are new in 7.13 and not already part of 7.12.

Miscellaneous
------------------------------------------------
- It is now possible to make a FAQ block look the same as accordion sections.
- The highlight of unread news can be applied to more views.
- "Force to everyone" option for channel enforced subscriptions
- Support for Microsoft Foundry
- Support for RBAC over OAuth
- No translation dictionary

.. REVIEW: FAQ/accordion, unread news, Microsoft Foundry, RBAC over OAuth and No translation dictionary come from the earlier draft and were not found in the dev commits. Confirm they are in 7.13.
