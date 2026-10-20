:orphan:

Release 7.13 (draft)
================================================

.. REVIEW NOTE: Built from the existing 7.13 draft plus the commits that are in the dev branch but not in 7.12 (preview/main), as of 20 Oct 2026. Items marked "REVIEW" in rst comments need a fact check and are not rendered. Bug fixes, build and internal changes are left out on purpose.

AI
------------------------------------------------
- Credit-based AI usage and subscription
- AI Insights added to Page Rollup, Analytics Report, and Metrics blocks, with rich text responses
- AI action and prompts added to Target Reach
- AI respects each user's permissions
- Omnia Skills and Omnia Agents
- Agent Studio: configure Omnia Agents, skills, guardrails and chat configurations for selected audiences
- Guardrails for Omnia chat: predefined and custom rules that check messages and answers
- Chat skills from OpenAI and Anthropic, and Omnia MCP tools in chat
- Ask Omnia: a system agent that uses Omnia MCP tools
- Object descriptions to improve AI context knowledge (Enterprise properties, page types, blocks, document types)
- Consistent prompt editors for the AI prompts administrators can customize
- Content Builder AI prompts are set per business profile
- AI use is recorded, and content disclaimers can be shown
- AI settings are hidden when no AI provider is configured
- AI providers: support for Microsoft AI Foundry
- AI providers: Azure RBAC authentication
- AI providers: maximum input and output tokens, separate switches for custom sampling parameters, and guided endpoint URL entry

.. REVIEW: Pre- and post-prompts. Semantic Search pre- and post-prompts shipped in 7.11.x/7.12. The 7.13 code change found is the standardized prompt editors (#2142), so the bullet now says that. Confirm whether other new pre-/post-prompts belong here.

.. REVIEW: "AI respects each user's permissions" comes from the RBAC user-context work (#1056). Confirm it is the same as permission-trimmed Semantic Search below, or keep both.

.. REVIEW: Rich text AI responses were found only as rich text in AI Insights (2176), so they are merged into the AI Insights bullet.

.. REVIEW: "Full undo/redo support on pages and page types" was removed. No such code is in dev; the related backlog item is still open.

.. REVIEW: Agent Studio is the admin area; Omnia Agents are what it manages. Upgrade note candidate: Agent Studio needs the feature activated (version 2), existing Ask Omnia and chat settings are migrated, and direct OpenAI organization-key chat is retired as a chat provider. Confirm and decide whether this belongs in "Before you upgrade".

.. REVIEW: Content Builder AI prompts per business profile: customized prompts are not inherited from the earlier tenant-wide setting and must be saved again in each business profile. Consider an upgrade note.

.. REVIEW: "Azure RBAC authentication" replaces "Support for RBAC over OAuth" from the earlier draft. The code has the AI provider authentication modes "Omnia App (Azure RBAC)" and "Signed-in user (Azure RBAC)". Confirm this is what was meant.

.. REVIEW: Possibly missing from the draft (dev-only, before 5 Oct, not checked further): Text Completion renamed to "Omnia AI suite" (#2786); Activity Hub Reach dashboard (#2770). Decide whether to add.

Semantic Search
------------------------------------------------
- Permission-trimmed semantic search results
- Alignment of semantic search functionality (Page types/Document types, Page collections/Authoring sites)
- Option to include all pages and documents

.. REVIEW: "Include all" - confirm the wording (#2975).

.. REVIEW: Developer change, not listed: extensions can add their own Semantic Search content and document indexes, and the direct vector index client in Omnia.Fx is removed (breaking for extensions, #4495). Decide whether a developer note is needed.

Smart Properties
------------------------------------------------
- Smart properties for documents and app instances
- Automatic smart properties for users
- Smart property rules without AI for users, page types and document types

.. REVIEW: "Deprecation of Auto-summary and Auto-tagging" was removed. "Enable Automatic Summary" is unchanged in dev and no deprecation commit was found. Restore it if the deprecation is announced without a code change.

Free form views
------------------------------------------------
- Free form view with your own HTML and CSS templates for Page Rollup, People Rollup, Document Rollup, Process Rollup, App instance rollup, Calendar, Media, Channel, Team News, Sign-off request, Form, Teamwork and List rollups, the RSS reader, Quick links and Announcements
- Free form editor with item and container templates, CSS, multilingual labels, a token picker, conditions and a live preview
- Free form templates and layouts for Quick search, Advanced search and semantic search answers
- Free form view for the high priority announcements banner in the header and on digital signage
- Page statistics and due-date tokens ("Overdue", "Due in 2 days") for Free form templates

.. REVIEW: Free form view was called "Custom view" during development; that name never shipped. Check the rollup names against the published block names.

.. REVIEW: Templates are sanitized when rendered, and anyone who can edit the block settings can author them. Confirm with the team before saying anything about who may author templates.

Activity Hub
------------------------------------------------
- Activity Hub in the mega menu and left panel
- Chat: encrypted messages and image attachments, delete messages and conversations, emoji, chat notifications
- Content Builder pages display in Activity Hub (web and mobile)
- Notification links open in the configured panes
- Configurable navigation content, panes and badges
- Channel collections for tabs, menus and navigation panes; the Activity Feed block can use a channel collection
- Channels can be subscribed by default for the users who can see them
- Activity Hub administrator role with scoped access
- Targeting personas in the Activity Hub feed
- New Activity Panel block
- Block height settings for feeds and chats
- Digest of missed activities, sent daily, weekly or every other week
- Several activity templates, selected by activity key, and new templates can start from a copy of an existing one
- Review reminder and review overdue activities for documents and pages
- Activity tasks can be marked as done, with a To do / Done filter in the Tasks tab
- Activity info can be sent to an entire channel
- Push notifications show the activity title, summary and image
- Microsoft Teams notifications open the activity in Teams
- Feed images can show videos from a media property and several images from a multi-select image property
- Activity Hub page views are reported to Matomo as page reads
- WCAG improvements on web and mobile
- Re-worked sign-in flow in the Omnia mobile app

**Omnia mobile app**

- Create pages from the app: choose a publish location, fill in the page fields, then publish, schedule or send for approval
- Edit your own profile in the app, with the properties administrators choose per user type
- Sign-up information for events, task filters, reactions and translation of comments
- Videos from SharePoint, Stream and Clipchamp play inside the app
- Tab icons from the admin settings, a business profile picker and redesigned settings
- Faster and more reliable push notifications, and the app icon badge is cleared when the app is opened

.. REVIEW: The mobile app is built and released separately (app stores and over-the-air updates), and several of its source issues are still in scenario test. Decide whether the mobile bullets stay in the 7.13 notes or go to separate mobile notes. The admin settings they need (publish locations, mobile user profiles, tab icons) ship with the platform.

.. REVIEW: Mobile user profiles come with a new SharePoint user profile synchronization under User management. Consider a separate bullet for it outside Activity Hub.

.. REVIEW (security, pending approval): A new permission role for publishing activities ("Activity Hub Publishers", #4345). Suggested wording: "New permission role for publishing activities". Not rendered until reviewed.

Web Content Management
------------------------------------------------
- Variation comparison dialog in the editor
- Alert when viewing a draft that has never been published
- Alternate layouts for publishing app layouts, as on the workspace home page
- Comments and replies can be translated on request (Page comments and likes block, announcements and Activity Hub)
- Page Rollup: the Calendar view can open on today, the latest or the first item, and the List view can show a total row
- Page creation action buttons can copy several properties from the current page

.. REVIEW: The Page Rollup and action button items come from #4339 (e2590248d), which also keeps taxonomy-connected terms in sync when a page is renamed, unpublished or republished. Confirm the wording and whether the term sync is worth a bullet.

.. REVIEW (security, pending approval): Share to LinkedIn with a public page preview in the External Share action button (#4465). It adds an anonymous preview of published pages. Suggested wording: "External Share action button: share pages to LinkedIn with a preview". Not rendered until reviewed; also confirm whether the External Share button already shipped in 7.12 (it exists in the modern client there).

Event Management
------------------------------------------------
- All-day events
- Outlook busy status for events
- Attendance mode: in person or online (Teams), for events with a Teams meeting
- Own questions in event sign-up forms

Navigation and Layout
------------------------------------------------
- Single header layout with header settings
- User menu action in the left panel
- Quick links, the left menu, footer links and process links open without reloading the whole page

.. REVIEW: "Quick access drawer for the left panel on mobile" was removed. It shipped in 7.12 (#3919 is on preview and main).

Miscellaneous
------------------------------------------------
- It is now possible to make a FAQ block look the same as accordion sections.
- The highlight of unread news can be applied to more views.
- "Force to everyone" option for channel enforced subscriptions
- "Do not translate" list: words and phrases that machine translation keeps in the original language
- Font picker in the admin font settings

.. REVIEW: FAQ/accordion (#1046), unread news (#1052) and the "Do not translate" list (#2151, formerly "No translation dictionary") were found in dev and are not in 7.12. "Support for Microsoft Foundry" and "Support for RBAC over OAuth" moved to the AI section.

.. REVIEW (security, pending approval): External OpenID Connect sign-in (#4542, #4735). Suggested wording: "Users can sign in with the organization's OpenID Connect identity provider, also when they sign up through self-service". Not rendered until reviewed.
