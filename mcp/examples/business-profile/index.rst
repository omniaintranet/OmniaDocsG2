Business profile
================

A business profile is a top-level part of the intranet - a country, a division, a brand - with its own languages, theme, links, announcements and apps. The connector can create one, in a single step that also sets up its workspace and makes you its administrator.

What you can ask for
********************

+ Create a business profile.

Example
*******

A business profile needs a title, and the title must have a value in the tenant's default language, because the profile's address is generated from it:

::

   Create a business profile called "Human Resources" in English
   and "Personal" in Swedish

.. TODO screenshot: Claude confirming the new business profile, its alias and its administrator

What you get back is the created profile, the address it was given, and the identity that was made its administrator - you.

.. TODO screenshot: the new business profile in the Omnia interface

Good to know
************

+ Creating a business profile needs the **tenant administrator** role.
+ The **address is generated from the title** in the tenant default language. If a profile already uses that address, or the address is reserved, the creation is refused and you are told why - pick a different title.
+ Creating a profile also provisions its **workspace app** and assigns you as the profile's administrator. If any part of that fails, the profile that was just created is rolled back, so a half-finished profile is not left behind.
+ Adding more administrators, and changing or removing a profile, is done in the Omnia interface - the connector only creates.
+ Once the profile exists, you can continue in the same conversation to set its :doc:`languages <../language/business-profile-language/index>` and :doc:`theme colours <../theme/index>`.

Actions
*******

+ ``BusinessProfile.Create`` - create a business profile, its workspace and its first administrator.
