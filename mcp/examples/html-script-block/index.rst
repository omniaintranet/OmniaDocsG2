Html/Script blocks
==================

An Html/Script block holds custom HTML, CSS and JavaScript that runs on a page. The connector can add one and patch an existing one, on three kinds of target: a **page**, a **page collection's own landing page**, and a **page type**.

This is the only way the connector writes executable content. A block's script is always written by a named action against one block, never as part of building a layout.

.. TODO screenshot: an Html/Script block on a page in Omnia, for reference

What you can ask for
********************

+ Add an Html/Script block to a page, a page collection or a page type.
+ Change the HTML, CSS or JavaScript of a block that is already there.
+ Read the script API contract - what ``Vue``, ``omniaScriptApi`` and ``omnia`` actually are inside a block.

Adding a block
**************

::

   Add an Html/Script block to this page that shows a countdown to 1 January

The block is placed in a **new full-width section at the bottom** of the page. That is deliberate rather than a limitation: the first section of most built-in layouts is a hero band, not the content area, so anything placed there lands inside the banner. Moving the section afterwards in the Omnia interface is easy; diagnosing a block inside a hero band is not.

Only the **JavaScript field runs**. A ``<script>`` tag written inside the HTML field is inert.

Changing a block
****************

Changes are patches - anything you do not mention is left exactly as it is:

::

   Change the styling of the countdown block so the numbers are larger

If the page has more than one Html/Script block you are shown each one with a preview of its HTML and script, and asked which you mean.

The script API
**************

Before writing a script that talks to Omnia, Microsoft Graph or SharePoint, ask for the contract:

::

   What can a script in an Html/Script block call?

You get the execution model, what exists in each global, and the mistakes that are easiest to make. The two that come up most often: the ``Vue`` global is **Vue 2**, so ``new Vue({ ... })`` and not ``Vue.createApp``; and the Graph and SharePoint clients are **axios-based promises** that have to be awaited before use, with the response body on ``.data``.

Running in an iframe
********************

A block runs **in an iframe by default**, and none of the Omnia globals exist inside it. A script that uses ``Vue``, ``omniaScriptApi`` or ``omnia`` therefore has to run outside the iframe, and the connector refuses such a script rather than writing one that could never work. Say so in the request if the script needs the page globals:

::

   The block needs the Omnia globals, so do not run it in an iframe

Adding a block to a page type
*****************************

A page does not carry its own copy of its page type's layout - it refers to it. A script block added to a **page type** therefore runs on **every page of that type at once**.

Because of that, the connector asks first. The first request changes nothing and reports how many published pages use the page type:

::

   Add an Html/Script block to the News article page type

The count is a **lower bound**: it covers published pages you are allowed to see, so drafts and pages outside your permissions are not in it. Only after you confirm is the block written.

Good to know
************

+ Changes are saved to the **draft**. A page or page type has to be published afterwards for anyone to see the block.
+ A **page collection** has to be checked out first, and there is no connector action that publishes an existing page collection - it has to be published from the Omnia interface. Until it is, the page collection stays checked out to you and other editors cannot change it.
+ A page collection's block goes on **its own landing page**, not on the pages inside it. Those inherit their layout from their page type instead.
+ The script does **not run while a page is being edited**, only when the page is rendered.
+ Wrap a script in ``(function(){ ... })();`` or ``(async () => { ... })();``. The script runs in the page's global scope, so top-level declarations collide with other blocks on the page.
+ An empty value **clears** a field. To change only the script, ask only for the script - resending the HTML and CSS unchanged is how their content gets quietly reworded.

Actions
*******

+ ``HtmlScriptBlock.GetScriptApi`` - the globals contract for a block's script.
+ ``Page.AddHtmlScriptBlock`` / ``Page.UpdateHtmlScriptBlock`` - add and patch a block on a page.
+ ``PageCollection.AddHtmlScriptBlock`` / ``PageCollection.UpdateHtmlScriptBlock`` - add and patch a block on a page collection's own landing page.
+ ``TenantPageType.AddHtmlScriptBlock`` / ``TenantPageType.UpdateHtmlScriptBlock`` - add and patch a block on a page type, with an affected-page confirmation.
