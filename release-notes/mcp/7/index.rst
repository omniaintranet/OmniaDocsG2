Release 7
========================================

- Compatible with Omnia release 7.
- Work with Omnia in plain language from an AI assistant, using the Model Context Protocol (MCP).
- Supported MCP clients are the Claude app and Microsoft Copilot Studio, which makes it possible to publish an agent to Microsoft Teams and Microsoft 365 Copilot.
- MCP clients are connected from Omnia admin System / OAuth2 Credentials, where administrators generate the client ID and secret needed by the client.
- Omnia MCP acts on behalf of the signed-in user and never grants more permission than the user already has in Omnia.
- Reading information from Omnia happens as part of the conversation, while any action that creates, changes, archives or removes content must be approved in the MCP client first.
- Tenant administrators can save an MCP context with the guidance every MCP session should follow, such as naming conventions, languages and publishing rules.
- Supported areas are search and promoted search results, My Links, Shared Links, announcements, pages, page types, page collections, Html/Script blocks, Publishing Apps and templates, business profiles, enterprise properties, languages, date and time formats, theme colours, features and Azure AD permissions.
- Requires the OmniaMCP extension to be installed on the tenant.


Hotfix releases
---------------

The hotfix releases for Omnia MCP version 7 are available here: :doc:`Hotfix releases </release-notes/mcp/7/hotfix-releases/index>`.
