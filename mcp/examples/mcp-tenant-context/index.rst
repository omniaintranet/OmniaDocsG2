MCP context for the tenant
==========================

The MCP context is a piece of free text your tenant administrator writes once and that every chat session reads before it does anything else. Use it for the things a person joining your intranet team would need to be told: naming conventions, tone of voice, which languages content must be written in, who owns what, what must never be published without review.

Because the context is read at the start of every session, the guidance in it shapes everything that follows in the conversation - the wording of an announcement, the category a link ends up in, whether something is published straight away or left as a draft.

.. TODO screenshot: the MCP context settings page in Omnia admin

What you can ask for
********************

+ Read the guidance currently saved for the tenant.
+ Replace it with new guidance (tenant administrators only).

Example
*******

Ask for the current context at any time:

::

   Show me the Omnia MCP context for this tenant

To change it, describe the rules you want in place. This is a write, so you are asked to confirm before it is saved:

::

   Update the Omnia MCP context: announcements must always be written in
   both English and Swedish, link categories must reuse the existing ones,
   and pages are never published without review - always leave them as drafts.

.. TODO screenshot: Claude reading the tenant context at the start of a session

Good to know
************

+ The context is **tenant-wide**. There is no separate context per business profile.
+ Saving it requires the **tenant administrator** role. Everyone else can read it.
+ Saving **replaces** the whole text rather than appending to it. Ask for the current context first if you want to add to what is already there.
+ It is plain guidance, not a rule the platform enforces. It steers the conversation; permissions and validation in Omnia still decide what actually gets through.
+ Do not put secrets in it. The text is sent to the model as part of the conversation.

Actions
*******

+ ``McpTenantContext.Get`` - read the saved guidance.
+ ``McpTenantContext.Save`` - replace the saved guidance.
