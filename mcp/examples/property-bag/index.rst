Property bag
============

The property bag is where Omnia keeps a lot of its settings behind the scenes - the tenant's languages and regional settings, a business profile's theme, and settings that belong to a single Publishing App. Each setting is stored as a named model owned by one Omnia service. The connector can show you what is in the property bag of the tenant, of a business profile or of a Publishing App, exactly as Omnia stores it.

This is mainly useful to administrators and support - to check what a setting really holds, or to compare two business profiles. For everyday settings the dedicated pages, such as :doc:`languages <../language/index>`, :doc:`date and time format <../date-time-format/index>` and :doc:`theme colours <../theme/index>`, give a friendlier answer.

What you can ask for
********************

+ Show everything in the tenant's property bag.
+ Show everything in a business profile's property bag.
+ Show everything in a Publishing App's property bag.
+ Show one named model only, for example the theme of a business profile.

Examples
********

Which property bag is read depends on the part of Omnia you are working in. With no business profile or app in the conversation, it is the tenant's:

::

   Show me the tenant property bag

Name a business profile, or paste its URL, to read that profile's bag instead:

::

   Show me the property bag of https://contoso.omniacloud.net/sites/hr

And a Publishing App to read the bag of the app's route:

::

   What is in the property bag of https://contoso.omniacloud.net/_/team-news?

.. TODO screenshot: Claude showing the models in a business profile property bag

If you only want one model, name it:

::

   Show me only the themingV2 model in the property bag of this business profile

Each model comes back with its name, the Omnia service that owns it, and its content.

Good to know
************

+ **Read only.** The connector cannot change the property bag. Settings that can be changed have their own pages and actions.
+ **The scope decides which bag is read.** A Publishing App reads the app's bag, a business profile reads that profile's bag, and anything else reads the tenant's. When a Publishing App is in the conversation its bag wins over its business profile's, so leave the app out if you want the profile's.
+ The content is shown **exactly as Omnia stores it** - names, nesting and values are not interpreted or tidied up, and models the connector knows nothing about are included too.
+ The bag is **read fresh** on every request, so a change just made in the Omnia interface shows up straight away.
+ A model name has to match **exactly, including upper and lower case**. ``themingv2`` does not find ``themingV2``. Ask for the whole bag first if you are unsure of the name.
+ A Publishing App that is still being created may not have a route yet, and then its bag cannot be read. Check the app's status on the :doc:`Publishing App <../publishing-app/index>` page, or read the business profile's bag instead.
+ Nothing is hidden or masked in the result. Omnia does not mark any property bag value as secret.

Actions
*******

+ ``PropertyBag.Get`` - the models in the property bag of the tenant, a business profile or a Publishing App, optionally filtered to one model.
