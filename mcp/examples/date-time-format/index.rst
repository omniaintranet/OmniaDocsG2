Date and time format
====================

The date and time format decides how Omnia writes dates and times across the tenant, and which day a week starts on in calendars and date pickers.

.. TODO screenshot: regional settings in Omnia admin, for reference

What you can ask for
********************

+ Read the current date format, time format and first day of the week.
+ Change any of the three.

The available values are:

+ **Date format** - ``YYYY-MM-DD`` for 2026-09-07, or ``LL`` for the long, language-dependent form such as *September 7, 2026*.
+ **First day of week** - Monday or Sunday.
+ **Time format** - 24 hours or 12 hours.

Example
*******

::

   What date and time format does this tenant use?

::

   Use the YYYY-MM-DD date format, 24 hour time, and start weeks on Monday

If you ask for something that is not one of the supported values, the valid ones are returned as a list to pick from instead of the change being guessed at:

::

   Change the date format

.. TODO screenshot: Claude offering the available date formats

Good to know
************

+ These settings are **tenant-wide** and need the tenant administrator role.
+ You can change one of the three without touching the other two.
+ The long date form (``LL``) is rendered per language, so it follows each reader's language rather than one fixed pattern.

Actions
*******

+ ``DateTimeFormat.Get`` - the current date format, time format and first day of week.
+ ``DateTimeFormat.Update`` - change one or more of them.
