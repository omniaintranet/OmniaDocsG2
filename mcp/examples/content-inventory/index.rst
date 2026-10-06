Content inventory
=================

Before changing a Publishing App it helps to know what is in it. The connector can list the content of a Publishing App, show the version history of a page, page collection or page type, and show what a page refers to - its layout, its properties, and the links, images and pages it points at. All of it is reading only; nothing is checked out.

.. TODO screenshot: Claude listing the content of a Publishing App

What you can ask for
********************

+ List the pages, page collections and page types of a Publishing App, or of one page collection.
+ See the state of each one: published, published with a draft, draft only or never published, and who has it checked out.
+ Show the versions of a page, page collection or page type.
+ Show what a page depends on: where its layout comes from, its property values, and the links, images and pages it refers to.

Listing the content
*******************

::

   List everything in https://contoso.omniacloud.net/sites/hr

::

   Which pages in the Policies page collection have a draft that is not published yet?

Each entry has its title, address, kind, page type, languages, state, and who has it checked out. Every language version is its own entry. The list comes 25 entries at a time - up to 50 if you ask - and you can ask for the next part. Listing without page types is faster when you do not need them.

The list also tells you **how complete it is**. Pages you are not allowed to read are counted but not described, and some content is never in the list:

+ pages that are not in the navigation, such as archived pages,
+ link and heading entries in the navigation,
+ the content of the pages - the list is about the pages, not what is on them.

A page that appears in the navigation more than once is listed once.

Versions
********

::

   Show the version history of the travel policy page

You get the current state - the live version, and whether there is a draft and who has it - and every version, newest first, with its number, when and by whom it was changed, and whether it is the live version, an earlier published version, a draft or the checked-out draft. To see what a version contains, read the page, page collection or page type itself.

Viewing the version history needs an **author, editor or admin** role on the content.

Dependencies
************

::

   What does the travel policy page link to, and where does its layout come from?

You get:

+ where the page's **layout** comes from - its own, its page type's, its page collection's, or an External Layout, see :doc:`/mcp/examples/page-layout/index`,
+ its **property values**, and which properties are empty,
+ the **links**, **images and files**, and **other pages** it refers to, and where each one is found. For a page you are not allowed to read, only the reference is shown.

The published version is read by default; ask for the draft to see a version that is not published yet. At most 200 references are listed.

A dependency list shows only what the page itself **points at**. It cannot show what points **at the page** - other pages linking to it, menus, search and query blocks, scripts, external sites - or links built while the page renders. An empty list is therefore not proof that nothing depends on a page.

Good to know
************

+ Listing needs a **Publishing App**; versions and dependencies need the **page**, **page collection** or **page type**.
+ The list is ordered so that asking for the next part keeps working while pages are being added or removed. A continuation belongs to one Publishing App and one page collection - start again if you change either.
+ A page that has never been published shows no page type in the list. Read the page itself to see its draft.
+ To find content by words in it, use search instead, see :doc:`/mcp/examples/search/index`.

Actions
*******

+ ``Content.ListInventory`` - the pages, page collections and page types of a Publishing App, with their state.
+ ``Content.GetVersions`` - the version history of a page, page collection or page type.
+ ``Content.GetDependencies`` - the layout, properties and outgoing references of a page.
