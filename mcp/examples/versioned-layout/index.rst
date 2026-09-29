Layouts
=======

Layouts are the frame around the content in Omnia - the header, the mega menu, the home layout, the layout of a workspace, the login and status pages. Each layout is versioned: you check it out, change the draft, and publish it when it is ready, just as in the layout editor in the Omnia interface. The connector can list the layouts of the tenant, a business profile or a Publishing App, read one of them, and - for business profile and Publishing App layouts - check it out, change the draft, publish it or discard the draft.

.. TODO screenshot: a layout changed through the connector, seen in the Omnia interface

What you can ask for
********************

+ List the layouts of the tenant, of a business profile or of a Publishing App.
+ Narrow the list to one kind of layout, for example the mega menus.
+ Look at one layout - its title, its kind, whether it is published and whether someone has it checked out.
+ Read the published version of a layout, or a draft that has not been published yet.
+ Check out a business profile or Publishing App layout.
+ Change the checked-out draft, as many times as you need.
+ Publish the draft, or discard it and go back to the published version.

Listing layouts
***************

Which layouts are listed depends on the part of Omnia you are working in. With no business profile or app in the conversation, the tenant's layouts are listed:

::

   List the layouts in the tenant

Name a business profile or a Publishing App, or paste its URL, to list its own layouts instead:

::

   Which layouts does https://contoso.omniacloud.net/sites/hr have?

Each layout in the list comes with its title in your language, what kind of layout it is - such as **MegaMenu**, **Home**, **System** or **Authentication** - which layout it inherits from, whether it has been published, and whether someone has it checked out - you or another user.

.. TODO screenshot: Claude listing the layouts of a business profile

Looking at one layout
*********************

::

   Show me the mega menu layout of the HR business profile

You get the layout and its **definition** - the sections, section items and blocks it is built from, with the settings of each block. By default the **published version** is read. A layout that has never been published has no published version, and you are told so; ask for the draft instead:

::

   Show me the draft of that layout

The definition is the layout's own composition only. What a visitor sees can also include what the layout inherits from a parent layout, which is not merged into the answer.

Changing a layout
*****************

Changing a layout follows the same steps as in the layout editor: **check out**, **change the draft**, then **publish** or **discard**.

::

   Check out the mega menu layout of the HR business profile, add a link
   to the new travel portal in the Services column, and publish it

1. **Checking out** gives you the current draft to work on. If you already have the layout checked out, your existing draft is returned. If **another user** has it checked out, nothing happens unless you ask to take it over - and then their saved draft becomes yours, so only do it when they agree.
2. **Changing the draft** saves the whole changed definition back to your checkout. You can save as many times as you like; nothing is visible to visitors yet.
3. **Publishing** makes your draft the published version, and you are told the new version and the one it replaced. **Discarding** throws your draft away and the layout falls back to the version before it - the published version is never touched.

.. TODO screenshot: Claude checking out, changing and publishing a layout

Good to know
************

+ Reading needs only the tenant; the context decides which layouts you get - a Publishing App's own, a business profile's own, or the tenant's.
+ **Tenant layouts are read only.** They affect every business profile, so the connector refuses to check out, change, publish or discard them. Only business profile and Publishing App layouts can be changed.
+ A layout can only be changed **in the context that owns it**. A Publishing App layout is changed while working in that app, a business profile layout while working in that profile; otherwise nothing is written and you are told which context to use.
+ The draft you change must be **your own checkout**. Changing, publishing or discarding a layout that you have not checked out, or that someone else has checked out, is refused.
+ A layout's **kind cannot be changed**, and everything in the definition you did not ask to change - block ids, block settings, blocks of any type - is saved back exactly as it was.
+ **No scripts or styles through layouts.** A change that adds or alters JavaScript or CSS anywhere in the layout, or changes the content of an Html/Script block, is refused before anything is saved. Scripts and styles already in the layout are kept as they are. Html/Script blocks are managed on pages, page collections and page types instead, see :doc:`/mcp/examples/html-script-block/index`.
+ Business profile layouts are looked up **one kind at a time**, because that is how Omnia offers them. The kinds that were looked up are reported back, so a profile layout of an unusual kind is not silently missed.
+ **No layouts are created or deleted** through the connector. Choosing a layout for a new page collection or page type is done from the built-in templates, see :doc:`/mcp/examples/page-collection/index` and :doc:`/mcp/examples/page-type/index`.

Actions
*******

+ ``VersionedLayout.List`` - the layouts of the tenant, a business profile or a Publishing App, optionally of one kind.
+ ``VersionedLayout.Get`` - one layout and the definition of its published version or of a given draft.
+ ``VersionedLayout.CheckOut`` - check out a business profile or Publishing App layout, optionally taking over another user's checkout.
+ ``VersionedLayout.UpdateDraft`` - save a changed definition to your checkout.
+ ``VersionedLayout.Publish`` - publish your checkout.
+ ``VersionedLayout.Discard`` - discard your checkout.
