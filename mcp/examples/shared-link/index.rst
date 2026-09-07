Shared Links
============

Shared Links are the links an editor publishes for everyone in a part of the intranet. They are grouped in categories, and a shared link can be made mandatory so that it appears in everyone's My Links panel and cannot be removed by the individual user.

.. TODO screenshot: shared links as end users see them

What you can ask for
********************

+ List the shared links in this part of the intranet.
+ List the categories already in use, so a new link ends up in an existing category instead of a new one.
+ Look at one link in detail.
+ Add a shared link.
+ Change an existing shared link.
+ Remove a shared link.

Example
*******

Look at the categories first - reusing them keeps the link panel tidy:

::

   Which shared link categories exist in https://contoso.omniacloud.net/sites/hr?

Then add the link. Title, address and category are required; a description, open in new window and mandatory are optional:

::

   Add a shared link called Travel policy pointing to
   https://contoso.omniacloud.net/sites/hr/travel, category Policies,
   description "Rules for booking and expensing business travel"

.. TODO screenshot: Claude confirming the new shared link

Make a link mandatory when everyone must have it:

::

   Make the Travel policy shared link mandatory

.. TODO screenshot: the new shared link in the Omnia interface

Good to know
************

+ Shared links are **per business profile**, and publishing them requires the permission to manage links in that part of the intranet.
+ **Mandatory** means the link is pushed into every user's My Links panel and cannot be removed by them. Use it sparingly.
+ An update changes only the fields you mention. To change a link you must be working in the same business profile the link belongs to.
+ Removing a shared link also removes it from the users who have it in their panel.

Actions
*******

+ ``SharedLink.List`` - the shared links in this business profile.
+ ``SharedLink.GetById`` - one shared link in detail.
+ ``SharedLink.GetCategories`` - the categories currently in use.
+ ``SharedLink.Add`` - publish a new shared link.
+ ``SharedLink.Update`` - change an existing shared link.
+ ``SharedLink.Delete`` - remove a shared link.
