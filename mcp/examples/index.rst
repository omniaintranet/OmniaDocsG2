Omnia MCP examples
==================

When the Omnia connector is in place (see :doc:`/mcp/setup/index`) you work with Omnia by writing in plain language in your MCP client - for example the Claude app. The client turns what you ask for into calls to Omnia, shows you what it is about to do, and asks before it changes anything.

This section has one page per area of Omnia the connector can reach, with example prompts, walkthroughs and the things that are good to know before you start.

.. TODO screenshot: overview - a first conversation in Claude where the Omnia connector is used

How a conversation works
************************

A few things are true for every example in this section:

+ **Everything happens as you.** The connector never gives you more permission than you already have in Omnia. If you are not allowed to create an announcement in the Omnia interface, you cannot create one through the connector either.
+ **Two tools, many actions.** The connector exposes one tool for reading (**Read**) and one for writing (**Write**). Everything else is an action name in the form ``Entity.Operation``, such as ``SharedLink.Add``. You never have to type those names - they are listed on each page so you can see exactly what an area supports, and so you can recognise them when your client shows what it is doing.
+ **You will be asked which part of Omnia you mean.** Most actions need a scope: the whole tenant, one business profile, one Publishing App, one page collection or one page. You can save a round trip by pasting a URL into your prompt, or simply answer when you are asked.
+ **The connector asks instead of guessing.** When a value can only be one of a set - an announcement type, a page type, a layout, a language, publish now or keep as draft - the connector returns the valid choices and your client presents them as a list. Nothing is invented on your behalf.
+ **Reading is free, writing is confirmed.** Reading information out of Omnia happens as part of the conversation. Anything that creates, changes, archives or removes content is a write, and your client asks you to approve it first.
+ **Your tenant's own rules apply.** At the start of a chat the client reads the guidance your tenant administrator has written for the connector - see :doc:`mcp-tenant-context/index` - and follows it for the rest of the conversation.

Examples per area
*****************

.. toctree::
   :titlesonly:

   mcp-tenant-context/index
   search/index
   my-link/index
   shared-link/index
   announcement/index
   property/index
   language/index
   date-time-format/index
   theme/index
   business-profile/index
   publishing-app-template/index
   publishing-app/index
   page-collection/index
   page/index
   page-type/index
   feature/index
   azure-ad-permission/index
