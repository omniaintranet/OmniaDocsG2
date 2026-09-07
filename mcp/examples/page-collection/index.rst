Page collection
===============

A page collection is the container pages live in inside a Publishing App - the news archive, the policy library, the project area. The connector can create one and read and change its settings.

.. TODO screenshot: a page collection and its settings in the Omnia interface, for reference

What you can ask for
********************

+ Create a page collection in this Publishing App.
+ Read a page collection's settings in one go.
+ Check out a page collection so its settings can be changed.
+ Add or remove the page types that may be used inside it.
+ Change its page creation, scheduling, collaboration, notification, distribution and AI settings.

Creating one
************

::

   Create a page collection called "Policies" in
   https://contoso.omniacloud.net/sites/hr

You are asked for the things that cannot be guessed: the **structure** (hierarchical or flat), the **layout** from the built-in catalogue, which **page types** may be used inside it, and whether to **publish it now or leave it as a draft**.

.. TODO screenshot: Claude asking for structure, layout and page types

Changing the settings
*********************

Reading the settings needs nothing special:

::

   Show me the settings of the Policies page collection

Changing them does. A page collection has to be **checked out** first, and every change is saved to the draft:

::

   Check out the Policies page collection, then turn on scheduling
   using the Publish date property and let editors co-author pages

.. TODO screenshot: Claude checking out the page collection and applying settings

The settings are grouped the same way as in the Omnia interface:

+ **Page creation** - auto publish, show properties, show URL.
+ **Scheduling** - whether pages are scheduled, and which date property drives it.
+ **Collaboration** - co-authoring and related options.
+ **Notification** - what editors and readers are notified about.
+ **Distribution** - publishing to channels, and whether channels are mandatory.
+ **AI** - the OpenAI-backed features and semantic search, and the properties they read.
+ **Available page types** - added and removed one call at a time, so you never resend the whole list.

Good to know
************

+ Creating needs a **Publishing App** scope; changing settings needs the **page collection** itself, which you are offered as a list if you do not name it.
+ A page collection **cannot be nested inside another page collection**.
+ The **structure** is chosen at creation and cannot be changed safely afterwards.
+ The **layout** can only be chosen at creation. Changing an existing page collection's layout has to be done in the Omnia interface.
+ **The settings actions never publish.** They save to the draft, so the changes stay invisible to readers until the page collection is published in the Omnia interface.
+ Settings are applied as **patches** - only what you mention changes, so you can turn one thing on without resending the rest.
+ **Scheduling** needs a date-and-time property, and the eligible ones are offered if the one you name will not do.
+ **Mandatory channels** cannot be turned on unless publishing to channels is on. Turning publishing to channels off also turns mandatory channels off.
+ **Semantic search** can only be turned on when the tenant's AI Engine feature is activated - see :doc:`../feature/index`. The OpenAI features need an image property and two text properties named in the same breath.

Actions
*******

+ ``PageCollection.Create`` - create a page collection.
+ ``PageCollection.GetSettings`` - read every setting in one call, no checkout needed.
+ ``PageCollection.CheckOut`` - check the page collection out for editing.
+ ``PageCollection.AddAvailablePageType`` / ``PageCollection.RemoveAvailablePageType`` - manage the page types allowed inside it.
+ ``PageCollection.SetPageCreationSettings``
+ ``PageCollection.SetSchedulingSettings``
+ ``PageCollection.SetCollaborationSettings``
+ ``PageCollection.SetNotificationSettings``
+ ``PageCollection.SetDistributionSettings``
+ ``PageCollection.SetAiSettings``
