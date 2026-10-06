Page layouts
============

Every page is built from sections, columns and blocks. Some of them belong to the **page itself**, and some are **inherited** - from the page type, or from the layout of the page collection. The connector can show you which part of a page comes from where, preview a change to the page's own layout, and apply it: change a block's settings, change the spacing or background of a section, column or block, add a block or remove one.

.. TODO screenshot: a page whose own blocks and inherited blocks are shown by the connector

What you can ask for
********************

+ See which parts of a page are the page's own and which are inherited, and from where.
+ See how many pages would be affected by a change to a layout.
+ Preview a change to a page's own layout before anything is written.
+ Change the settings of one of the page's own blocks.
+ Change the layout settings - such as padding or background - of one of the page's own sections, columns or blocks.
+ Add a block from the block catalogue, in an existing column or in a new section at the end of the page.
+ Remove one of the page's own blocks.

Who owns what
*************

::

   Which parts of https://contoso.omniacloud.net/sites/hr/travel-policy come
   from its page type, and which belong to the page?

You get every section, column and block the page renders, each marked with where it comes from: the **page itself**, the **page type**, the **page collection**, a parent page, or an **External Layout**. You can also see:

+ an inherited block the page has **overridden** with its own settings, where the page type allows it,
+ a block of the page's own that sits inside an **inherited column** - a change keeps it there,
+ which version was read - the checked-out draft if there is one, otherwise the published version. You can ask for either one explicitly.

The inherited part is always read from the **published** version of the page type or page collection, never from a draft. Reading never checks anything out.

.. TODO screenshot: Claude listing the page's own and inherited blocks

Previewing a change
*******************

::

   Add a Text block at the end of the travel policy page and give the
   intro section a light grey background - show me a preview first

A preview shows each setting that would change, with its value **before and after**, where a new block would be placed, and anything that would be refused. It also says **who renders the layout** being changed: a page's own layout is rendered on that page only. Nothing is written and nothing is checked out by a preview.

When a change targets something that is shared, the preview says how far it reaches:

+ For a **page type**, the number of published pages that use it is given as a **minimum** - drafts and pages you cannot see are not counted.
+ If the number cannot be found, it is reported as **unknown**, not as zero.
+ An **External Layout** is shared by every page collection that uses it, and that number cannot be counted.

Changing the page's own layout
******************************

::

   Apply that change

What a change can do:

+ **Change a block's settings.** Only the settings you name change; the rest are kept. A setting can also be removed.
+ **Change layout settings** of a section, column or block, such as padding or background.
+ **Add a block.** The block is named by its title from the block catalogue, for example *Text*. In a column you name, it is added at the end of that column. With no column named, it is added in a **new full-width section at the end of the page**, after the inherited sections as well.
+ **Remove a block** of the page's own, together with its settings and content.

The page is **checked out for you** if needed, the change is saved to the **draft**, and the result is read back. Nothing is published - publish the page to make the change visible, or discard the draft to throw it away, see :doc:`/mcp/examples/page/index`.

.. TODO screenshot: Claude applying a layout change and reporting the result

Good to know
************

+ Only a **plain page's own layout** is changed. A page type's layout is rendered by every page of that type, and a page collection's layout may be a shared External Layout, so neither is changed this way - and neither is any block the page inherits from them.
+ **All or nothing.** If any part of a change is refused, nothing is changed and you are told which part and why. A change can have at most 25 steps; split a bigger one in two.
+ **No scripts or styles.** HTML, CSS, JavaScript and markup are never written through a layout change. Html/Script blocks are added and changed with their own actions, see :doc:`/mcp/examples/html-script-block/index`; only their padding and background can be changed here.
+ Sections and blocks **cannot be moved or reordered**, and a section is only created as the home of a new block. Move things in the page editor if needed.
+ Whether a block is **locked or unlocked** between a page and its page type is managed by Omnia and is not changed.
+ If the page's own layout was changed by someone else **after your preview**, the change is refused and you are asked to look at a new preview. If **another user** has the page checked out, nothing is changed.
+ If Omnia places a new section somewhere other than at the end, you are told where it ended up so you can move it in the page editor.
+ The block catalogue lists the blocks the connector knows about. A block in it can still be missing from your tenant's block picker, see :doc:`/mcp/examples/capabilities/index`.

Actions
*******

+ ``Layout.GetOwnership`` - the page's own, inherited and resulting layout, with the source of every section, column and block.
+ ``Layout.PreviewPatch`` - preview a change to a page's own layout, with the pages it reaches. Writes nothing.
+ ``Page.ApplyLayoutPatch`` - apply a change to a plain page's own layout and save it to the draft.
