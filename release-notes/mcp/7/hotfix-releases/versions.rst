Release 7.11
============

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
