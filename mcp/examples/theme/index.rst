Theme colours
=============

Each business profile has a primary and a secondary theme colour, used for headers, buttons, links and accents in that part of the intranet. The connector can read the current pair and set new ones.

.. TODO screenshot: theme settings for a business profile, for reference

What you can ask for
********************

+ Read the theme colours of this business profile.
+ Change the primary colour, the secondary colour, or both.

Example
*******

::

   What are the theme colours for https://contoso.omniacloud.net/sites/hr?

::

   Set the primary colour to #0057B8 and the secondary colour to #FFB81C
   for the HR site

.. TODO screenshot: Claude confirming the new theme colours

.. TODO screenshot: the business profile with the new colours applied

Good to know
************

+ Colours are given as hex values - either ``#RGB`` or ``#RRGGBB``. Anything else is rejected with the expected format named, so a colour is never approximated for you.
+ You can change one colour without touching the other.
+ Theme colours are **per business profile**, and changing them needs the permission to manage that profile.
+ The change applies to everyone in that part of the intranet as soon as it is saved, so it is worth agreeing the pair before you set it.

Actions
*******

+ ``BusinessProfileTheme.Get`` - the profile's primary and secondary colours.
+ ``BusinessProfileTheme.Update`` - set the primary colour, the secondary colour, or both.
