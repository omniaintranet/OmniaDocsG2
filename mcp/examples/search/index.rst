Search
======

Search lets you look for content in the intranet from the conversation, and then keep working with what comes back - summarise it, compare it, or use it as the source for a new announcement or page.

The search runs the **Quick Search configuration of the business profile you are working in**. That means you get the same categories, the same sources and the same result types as the search box in that part of the intranet, and results are trimmed to what you personally have access to.

.. TODO screenshot: asking Claude to search the intranet and getting results back

What you can ask for
********************

+ Search the intranet for a keyword.
+ Ask follow-up questions about the results - summarise them, group them, pick out the relevant one.
+ Use a result as input for something else, such as drafting an announcement from a news article.

Depending on how the profile's Quick Search is configured, results can come from:

+ Omnia content - pages, news, events and other workplace content
+ Shared links
+ Comments
+ SharePoint search and Microsoft Search
+ Semantic search, when the AI Engine feature is activated on the tenant

Example
*******

::

   Search the intranet for parental leave

::

   Find news about the office move in https://contoso.omniacloud.net/sites/hr
   and summarise the three most recent ones

.. TODO screenshot: search results in the conversation

Good to know
************

+ Search needs a **business profile** scope. If you have not said which part of the intranet you mean, you will be asked.
+ Only what is configured in that profile's Quick Search is searched. If a source is missing from the results, the place to fix it is the Quick Search settings, not the prompt.
+ Results are **security trimmed** - you only ever see what you are allowed to see in Omnia.
+ One keyword per search. Ask again to search for something else.
+ If a single source fails - a SharePoint query that times out, for example - the other sources still return, and the failure is reported alongside the results.

Actions
*******

+ ``Search.Execute`` - search the current business profile with one keyword.
