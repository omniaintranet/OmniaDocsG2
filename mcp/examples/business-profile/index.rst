Business profile
================

A business profile is a top-level part of the intranet - a country, a division, a brand - with its own languages, theme, links, announcements and apps. The connector can list the business profiles in the tenant, and create a new one in a single step that also sets up its workspace and makes you its administrator.

What you can ask for
********************

+ List the business profiles in the tenant, with their addresses.
+ Find out which business profile an address belongs to.
+ Create a business profile.

Listing business profiles
*************************

::

   List the business profiles in this tenant

::

   Which business profile is /_wp/sales?

Each business profile in the list comes with its title in every language it has, a short name, every address mapped to it and its default URL. The first address is the profile's primary one, and the short name is the last part of that address - ``/_wp/sales`` gives ``sales``.

The list is a convenient way to find the business profile you want to work in next. Once it is found, you can carry on in the same conversation without pasting its URL.

.. TODO screenshot: Claude listing the business profiles of the tenant

Creating a business profile
***************************

A business profile needs a title, and the title must have a value in the tenant's default language, because the profile's address is generated from it:

::

   Create a business profile called "Human Resources" in English
   and "Personal" in Swedish

.. TODO screenshot: Claude confirming the new business profile, its alias and its administrator

What you get back is the created profile, the address it was given, and the identity that was made its administrator - you.

.. TODO screenshot: the new business profile in the Omnia interface

Good to know
************

+ Listing business profiles needs no particular scope, only the tenant. The list only includes the business profiles **you are allowed to see** - a profile you cannot see is simply left out.
+ A profile's **default URL can be missing** from the list when the profile has none or you are not allowed to read it. The rest of the entry is still correct.
+ The **short name** in the list is worked out from the primary address. It is not a separate setting in Omnia, and a profile whose only address is the root of the tenant has none.
+ Creating a business profile needs the **tenant administrator** role.
+ The **address is generated from the title** in the tenant default language. If a profile already uses that address, or the address is reserved, the creation is refused and you are told why - pick a different title.
+ Creating a profile also provisions its **workspace app** and assigns you as the profile's administrator. If any part of that fails, the profile that was just created is rolled back, so a half-finished profile is not left behind.
+ Adding more administrators, and changing or removing a profile, is done in the Omnia interface - the connector only lists and creates.
+ Once the profile exists, you can continue in the same conversation to set its :doc:`languages <../language/business-profile-language/index>` and :doc:`theme colours <../theme/index>`.

Actions
*******

+ ``BusinessProfile.List`` - the business profiles you can see, with their titles, addresses and default URLs.
+ ``BusinessProfile.Create`` - create a business profile, its workspace and its first administrator.
