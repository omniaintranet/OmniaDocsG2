Release 7.11
============

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
