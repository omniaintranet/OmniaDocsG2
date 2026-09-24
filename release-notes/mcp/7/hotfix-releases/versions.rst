Release 7.11
============

Release 7.11.31
---------------------------------------

- Added support for listing the business profiles in the tenant, with their titles, addresses and default URLs
- Added support for listing the Publishing Apps of a business profile in every state, including apps that are still being created or that failed, and other kinds of app such as workspaces and communities
- Added support for reading one Publishing App's status, address, administrators and template, and for checking whether a new app is ready
- Added support for listing the Publishing App templates of a business profile, and the kinds of app registered in the tenant
- Added support for reading the property bag of the tenant, a business profile or a Publishing App, optionally filtered to one model
- Added support for listing the Management System processes the user can read, filtered by library or title with drafts on request, and for reading a process and its step tree
- Added support for listing, creating and configuring document types, reading their settings and checking whether a new document type has finished syncing to SharePoint
- Added support for listing and creating document templates and template categories, and for downloading an uploaded template's file
- Added support for creating Teamwork app templates and Teamwork apps, listing and activating their features, and activating the controlled document library on a Teamwork app
- Added support for finding, reading and downloading controlled documents, and for listing a site's drafts, published documents and tasks
- Added support for creating controlled documents from a document type and a template, and for starting a revision, uploading an edited file, changing properties and previewing the draft
- Added support for publishing controlled document drafts directly or through approval. The choice must always be given explicitly, and approval requires an approver and a due date
- Added support for republishing and unpublishing controlled documents, and for recovering documents whose publishing failed
- Added support for approving, rejecting and cancelling approval workflows, and for sending documents to review and managing reviewers and review tasks
- Added support for listing and terminating document retention
- Added support for updating a property, such as the review date, on many published documents at once and republishing them
- Search can now return diagnostics on request (the categories used, their queries and the unprocessed results). Diagnostics are no longer included in every answer
- Fixed Quick Search category names showing a technical type name instead of the category title in the user's language
- Fixed SharePoint search results showing raw user claims. The author and last editor are now shown by name and email, and empty property values are left out
- Fixed the list of business profiles, Publishing Apps, page collections or pages offered as a scope being silently limited to five. It now shows up to 50 and says when there are more
- Fixed the question asking which part of Omnia is meant being shown twice

Release 7.11.29
---------------------------------------

- Added support for adding and changing Html/Script blocks on pages, page collections and page types
- A new block is placed in its own section at the bottom of the page, and can be moved from there in the Omnia interface
- Adding an Html/Script block to a page type reports how many published pages use that page type and requires a confirmation before the block is added, since the block runs on every page of the type
- Added an action that returns the script API contract for an Html/Script block, describing the globals a block script can use
- A block script that uses the Omnia page globals is rejected while the block is set to run in an iframe, where those globals do not exist

Release 7.11.28
---------------------------------------

- Added support for listing, adding, changing and deleting promoted search results in a business profile
- Search results now include the promoted search results a Quick Search block would show for the same keyword, with an explanation when there are none
- Promoted search results are created on hold, so a new result does not appear in search until it is activated
- Images and targeting on a promoted search result are not changed by the connector and are preserved when a result is updated

Release 7.11.27
---------------------------------------

Initial release of Omnia MCP.

- Added Omnia MCP client integration, which lets AI assistants work with Omnia in plain language, with support for the Claude app and Microsoft Copilot Studio
- MCP clients are connected from Omnia admin System / OAuth2 Credentials, where administrators generate the client ID and secret needed by the client
- Omnia MCP acts on behalf of the signed-in user and never grants more permission than the user already has in Omnia
- Reading information from Omnia happens as part of the conversation, while any action that creates, changes, archives or removes content must be approved in the MCP client first
- Tenant administrators can save an MCP context with the guidance every MCP session should follow, such as naming conventions, languages and publishing rules
- Omnia MCP supports search, My Links, Shared Links, announcements, pages, page types, page collections, Publishing Apps and templates, business profiles, enterprise properties, languages, date and time formats, theme colours, features and Azure AD permissions
- The OmniaMCP extension must be installed on the tenant before the integration can be set up
