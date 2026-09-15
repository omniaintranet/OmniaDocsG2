Promoted search results
=======================

A promoted search result is the entry a Quick Search block shows above the ordinary hits when someone searches for a particular word - the HR policy you always want at the top when a user types "holiday". The connector can list, create, change and delete the promoted results of a business profile.

.. TODO screenshot: promoted search results in Omnia admin, for reference

What you can ask for
********************

+ List the promoted search results of a business profile.
+ Add a promoted result for one or more keywords.
+ Change an existing one - its title, description, address, keywords, status or date window.
+ Delete one.

Listing what is there
*********************

::

   List the promoted search results for this business profile

The list includes results that are **on hold** and results whose date window has passed, not just the ones currently showing. That is deliberate: it is how you find the one you want to change. Each entry also tells you whether it carries an **image** and whether it has a **targeting filter**.

::

   Show me only the promoted results that are active right now

Adding a promoted result
************************

::

   Add a promoted search result for the keyword "holiday" pointing at
   https://contoso.omniacloud.net/sites/hr/holiday-policy, titled "Holiday policy"

A **title** and an **address** are required. The title is what the keyword is matched against, so it can be given per language. A new result is created **on hold** unless you say otherwise, so nothing appears in search until someone activates it:

::

   Activate it

You can also give it a description, more keywords, and a start and end date.

Changing and deleting
*********************

Changes are merges. Titles and descriptions merge per language, keywords replace the whole list, and anything you do not mention is left as it is:

::

   Add the keywords "vacation" and "annual leave" to the holiday policy promoted result

Deleting is **permanent**. Unlike a page, a promoted search result has no archive and no restore path, so you are asked to confirm first.

Good to know
************

+ Promoted search results need a **business profile** scope and the business profile administrator or search administrator role. The connector does not work around Omnia's permission model - without the role you get Omnia's own refusal.
+ **Matching is exact**, case-insensitive and ignores surrounding spaces. It matches a result's title in any language, or one of its keywords. A result keyed on ``benefits`` is not found by someone searching for ``benefit``, so add both if you need both. This is the same rule the search box itself uses.
+ A new result is **on hold by default** and has to be activated before it appears.
+ An **end date earlier than the start date** closes the window, and a closed window silently stops the result ever matching. The connector refuses it rather than saving it.
+ **Images cannot be set** through the connector. A promoted result created here renders in its text-only form. An image added in the Omnia interface is never removed by a later change made here, so the way to add one is to create the result here and add the image in Omnia afterwards.
+ **Targeting cannot be set** either, and is never removed by a change made here. A result that is in the list but never appears in search usually has a targeting filter on it.
+ Promoted result **ids are numbers** and are not shown anywhere else in Omnia. Ask for the list to get them.

Actions
*******

+ ``PromotedSearchResult.List`` - the promoted search results of the business profile.
+ ``PromotedSearchResult.Add`` - add a promoted search result.
+ ``PromotedSearchResult.Update`` - change an existing one.
+ ``PromotedSearchResult.Delete`` - delete one permanently.
