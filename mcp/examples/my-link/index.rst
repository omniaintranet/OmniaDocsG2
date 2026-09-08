My Links
========

My Links are your own shortcuts in the intranet - the ones you see in your personal links panel. Through the connector you can list them, add new ones, change or remove the ones you own, and pick up a link that has been shared in your part of the intranet and keep it among your own.

.. TODO screenshot: the My Links panel in Omnia, for reference

What you can ask for
********************

+ List the links you have.
+ List everything available to you - your own links plus the shared links published in this part of the intranet.
+ Add a link of your own.
+ Change the title, address, category, description or open-in-new-window setting of a link you own.
+ Remove one of your own links.
+ Add an existing shared link to your own links.

Example
*******

Start by looking at what you have:

::

   List my links in https://contoso.omniacloud.net/sites/hr

Then add one. A My Link needs a title, an address, a category and a short description - if you leave one out you are asked for it rather than having something invented for you:

::

   Add a my link called Payroll pointing to https://payroll.contoso.com,
   category Tools, description "Report absence and view payslips",
   and open it in a new window

.. TODO screenshot: Claude confirming the new My Link

Changing or removing one works from the list. If you do not say which link you mean, the connector returns your links as a list to choose from:

::

   Change the category of my Payroll link to HR

::

   Remove one of my links

.. TODO screenshot: Claude presenting the list of My Links to pick from

To keep a link someone else has published:

::

   Add the IT support shared link to my links

Good to know
************

+ My Links are **personal and per business profile**. Ask in the part of the intranet where the links belong.
+ You can only change or remove links **you own**. Shared links published for everyone are managed under :doc:`../shared-link/index`.
+ Listing your links shows what your links panel shows, including any mandatory shared links pushed to you. Listing everything available shows the full set you can pick from.
+ Links you cannot see because of targeting are not returned - the same rules as in the interface.
+ An update changes only the fields you mention; everything else stays as it was.

Actions
*******

+ ``MyLink.List`` - the links in your own links panel.
+ ``MyLink.GetAll`` - your own links plus the shared links available to you.
+ ``MyLink.Add`` - add a link of your own.
+ ``MyLink.Update`` - change a link you own.
+ ``MyLink.Delete`` - remove a link you own.
+ ``MyLink.AddSharedLinkAsMyLink`` - add an existing shared link to your own links.
