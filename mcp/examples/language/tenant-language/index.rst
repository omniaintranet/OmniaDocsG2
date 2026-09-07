Tenant languages
================

The tenant languages are the full set of languages available anywhere in the tenant. One of them is the default, which is the language Omnia falls back to when a text has no value for the language a reader is using.

.. TODO screenshot: language settings in Omnia admin, for reference

What you can ask for
********************

+ Read the languages enabled for the tenant and which one is the default.
+ Add one or more languages.
+ Remove one or more languages.
+ Change which language is the default.
+ Change whether the country part of a language name is shown.

Example
*******

::

   Which languages are enabled on this tenant?

::

   Add Swedish and Norwegian to the tenant languages

If you do not name a language, the ones that can still be added are returned as a list to pick from:

::

   Add another tenant language

.. TODO screenshot: Claude offering the languages that can be added

::

   Make Swedish the default tenant language

Good to know
************

+ The **default language cannot be removed**. Make another language the default first.
+ Only languages Omnia supports are accepted; anything else is rejected by name so you can correct it.
+ Removing a language does not delete the translations already stored for it - but readers no longer get that language, and it can no longer be given a value.
+ **Exclude country** controls whether a language is presented as *English* or *English (United States)*.
+ These settings are **tenant-wide** and need the tenant administrator role.

Actions
*******

+ ``TenantLanguage.Get`` - the enabled languages and the default.
+ ``TenantLanguage.Add`` - enable one or more languages.
+ ``TenantLanguage.Remove`` - disable one or more languages.
+ ``TenantLanguage.SetDefault`` - change the default language.
+ ``TenantLanguage.SetExcludeCountry`` - show languages with or without their country.
