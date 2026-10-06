Capabilities and operations
===========================

The connector can describe itself: which actions it has, what each one needs, and which blocks and layout templates it knows about. It can also tell you what happened to a change it made earlier in the conversation. You rarely need to ask for any of this directly - your client uses it to find the right action - but it is useful when you want to know what is possible before you start, or when a change ended without a clear answer.

.. TODO screenshot: Claude listing the connector's capabilities

What you can ask for
********************

+ List every action the connector has, optionally only the reading or the writing ones, or the ones for one area.
+ Describe one action - what it needs, what it changes, and whether that can be undone.
+ List the blocks the connector knows about, with their settings.
+ List the layout templates a new page collection or page type can be created from, optionally with a preview image.
+ Check what happened to an earlier change.

What can the connector do?
**************************

::

   What can the Omnia connector do with page collections?

::

   What does it take to publish a page through the connector?

The list gives every action with whether it reads or writes, which part of Omnia it works in, and what it needs. Describing one action adds its fields with their allowed values, an example, and its **effects**: whether it changes a draft or the live content, whether it removes something, whether it can be undone, and whether it reaches beyond one item.

Some things cannot be known in advance - for example whether you have the permission, or whether a feature is activated on your tenant. Those are reported as **unknown**, which means *not established*, not *no*.

Blocks and layout templates
***************************

::

   Which blocks can be added to a page?

::

   Show me the layout templates for page types, with previews

The block catalogue gives each block's title, category and a short description, and which of its settings can be changed. It lists the blocks **the connector knows about**, not the ones installed in your tenant, so a block in the catalogue can still be missing from your tenant's block picker.

The layout templates are the ones a new page collection or page type is created from. A layout is chosen **once, at creation** - no action changes it afterwards. For a page type, prefer the templates under the **Pages** category. See :doc:`/mcp/examples/page-collection/index` and :doc:`/mcp/examples/page-type/index`.

Approving high-impact changes
*****************************

Every write is approved in your client before it runs. A few changes reach so far that the connector adds a second safeguard: **publishing a page**, **publishing a page collection**, **archiving a page** and **changing an Html/Script block on a page type**.

1. The first request writes **nothing**. It returns a preview: what will change, how far it reaches, and whether and how it can be reversed.
2. Your client shows you the preview. Only when you approve it is the same request sent again, together with the approval.
3. Before writing, the connector checks that the approval still matches: **same user, same change, same target, and the target has not changed** since the preview.

An approval is valid for **10 minutes** and can be used **once**. If it has expired, has already been used, or the content was changed by someone else in between, nothing is written and you are shown a fresh preview to approve instead.

.. TODO screenshot: Claude showing a publish preview and asking for approval

When the result is uncertain
****************************

Sometimes a change is sent to Omnia but no clear answer comes back - the connection drops, Omnia does not answer in time, or you cancel the request while it is running. The connector then does not report a failure, because the change may well have happened. It says the outcome is **uncertain** and asks you to read the content back before trying again, since repeating the change could apply it twice.

::

   Did my last change to the travel policy page go through?

Every change is given an operation id, and the connector can look it up and tell you which steps were applied. A few things to know:

+ Operations are remembered for **24 hours**, by the connector instance that ran them, and are forgotten if it restarts. When there is no record, that does **not** mean the change did not happen - read the content back.
+ You only see your own operations.
+ Creating a page and activating a feature protect themselves against repeats: if an earlier attempt may still have gone through, the connector looks for the page or the running activation first and never creates a second one.

Cancelling a request **before** it reaches Omnia, or while it is only reading, changes nothing and can simply be repeated.

Actions
*******

+ ``Capabilities.List`` - every action, with whether it reads or writes, the context it needs and its required fields.
+ ``Capabilities.DescribeAction`` - one action in full: fields, example, effects and prerequisites.
+ ``BlockCatalog.List`` - the blocks the connector knows about, with their settings.
+ ``LayoutCatalog.List`` - the layout templates for new page collections and page types, optionally with preview images.
+ ``Operation.Get`` - what happened to an earlier change.
