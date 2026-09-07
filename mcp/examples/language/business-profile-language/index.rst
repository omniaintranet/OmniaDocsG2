Business profile languages
==========================

A business profile can either use the tenant's languages as they are, or keep its own shorter list - useful when one part of the organisation works in two languages and the tenant supports five.

What you can ask for
********************

+ Read the languages for this business profile, its default, and whether it inherits from the tenant.
+ Turn inheritance from the tenant on or off.
+ Add one or more languages to the profile.
+ Remove one or more languages from the profile.
+ Change the profile's default language.

Example
*******

::

   Which languages does https://contoso.omniacloud.net/sites/hr use?

A profile that inherits from the tenant has no list of its own, so inheritance has to be turned off before anything can be changed. If you try it the other way round you are told so rather than left guessing:

::

   Stop inheriting languages from the tenant for the HR site,
   then keep only English and Swedish

.. TODO screenshot: Claude turning off inheritance and setting the profile languages

Good to know
************

+ While the profile **inherits from the tenant**, adding and removing languages is rejected - turn inheritance off first.
+ A profile can only use languages that are enabled on the tenant. Add the language to the tenant first if it is missing - see :doc:`../tenant-language/index`.
+ The profile's **default language cannot be removed**. Change the default first.
+ These settings need the permission to manage the business profile.

Actions
*******

+ ``BusinessProfileLanguage.Get`` - the profile's languages, default and inheritance.
+ ``BusinessProfileLanguage.SetInheritFromTenant`` - turn inheritance on or off.
+ ``BusinessProfileLanguage.Add`` - add one or more languages.
+ ``BusinessProfileLanguage.Remove`` - remove one or more languages.
+ ``BusinessProfileLanguage.SetDefault`` - change the profile's default language.
