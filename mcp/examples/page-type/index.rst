Page types
==========

A page type defines what a page of that kind looks like and what metadata it carries - the layout, and the content properties every page created from it gets. The connector works with **tenant-wide** page types, the ones available to every Publishing App in the tenant.

.. TODO screenshot: page types in Omnia admin, for reference

What you can ask for
********************

+ List the tenant's page types.
+ Read one page type - its title per language, address, properties with their data types, defaults and required flags, its checkout state and version, and its archiving and SharePoint sync settings.
+ Create a page type.
+ Change a page type's title or content properties.
+ Publish the current draft.
+ Discard the current draft.

Creating a page type
********************

::

   List the tenant page types

::

   Create a tenant page type called "News article" in English and Swedish

You are asked for the **layout** from the built-in catalogue - prefer the ones under the Pages category for a page type - and for the **content properties** the page type should carry. **None** is a valid answer if the page type should carry no properties.

.. TODO screenshot: Claude offering the layout catalogue

Each property can be given a **default value** applied to new pages, either a literal or one of the tokens ``[CurrentUser]``, ``[Today]`` or a relative date such as ``[Today][1][year]``:

::

   Add the Contact property with default [CurrentUser]
   and the Review date property with default [Today][1][year]

Three further decisions have to be made rather than left out, and each is put to you as a choice:

+ **Publish it or leave it as a draft.** A page type that is never published cannot be used to create pages.
+ **Automatic archiving** - whether pages of this type are archived on a date. If yes, you name which of the page type's own date properties drives it.
+ **SharePoint sync override** - whether this page type overrides the tenant's SharePoint sync settings. If yes, you also decide which properties represent the page's image, summary, content and related links; each one is either a property of this page type or explicitly left unmapped.

.. TODO screenshot: Claude asking about publishing, automatic archiving and SharePoint sync

Changing a page type
********************

Changes are patches. Only the languages you mention in the title change, and only the properties you mention are affected - adding one that is not on the page type yet, or updating its default if it is. Everything configured in the Omnia interface that the connector does not expose - required flags, labels, categories, visibility - is left alone rather than silently reset.

::

   Add the Department property to the News article page type
   and remove the Campaign property, then publish it

Good to know
************

+ Page types are **tenant-wide** and need the tenant administrator role. Page types scoped to a single Publishing App are not supported by the connector yet.
+ A page type's **address is generated** by the platform and cannot be chosen.
+ **The layout can never be changed** by an update. Pages refer to their page type rather than copying its layout, so swapping it would restyle every existing page of that type at once - that has to be done in the Omnia interface.
+ Removing a content property that automatic archiving or SharePoint sync still points at is **refused** rather than silently blanking the setting. Turn the setting off, or point it somewhere else, in the same request.
+ Turning the SharePoint sync override on **seeds the page type from the tenant's sync settings** first, exactly as the Omnia interface does. This matters: without it, enterprise property values would silently stop being indexed for search.
+ **Publishing sends no notification**, and publishing twice with nothing changed in between is refused. Discarding a draft needs a draft, and needs the page type to have been published at least once.
+ Page review rules and analytics settings on a page type are not exposed by the connector.

Actions
*******

+ ``TenantPageType.List`` - the tenant's page types.
+ ``TenantPageType.Get`` - read one page type in full.
+ ``TenantPageType.Create`` - create a tenant-wide page type.
+ ``TenantPageType.Save`` - change a page type's title or content properties.
+ ``TenantPageType.Publish`` - publish the current draft.
+ ``TenantPageType.Undo`` - discard the current draft.
