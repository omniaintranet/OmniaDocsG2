Newsletter implementation example
==============================================

Here's a newsletter implementation example. First an example of a newsletter archive:

.. image:: newsletter-archive-new.png

The page type is set up with three blocks: a text block for the heading, an action button block for the newsletter editor to use when creating a newslettter page, and finally a page rollup block to list the newsletter pages. The same page type is used when en editor creates a newsletter, but then works slightly different.

The action button block has the following general settings:

.. image:: newsletter-archive-button-settings-1-new.png

And the following style settings:

.. image:: newsletter-archive-button-style-1-new-frame.png

The page rollup block has the following settings for Query:

.. image:: newsletter-archive-page-query-new.png

The settings for Display are the following:

.. image:: newsletter-archive-page-display-1-new.png

and these:

.. image:: newsletter-archive-page-display-2-new.png

Regarding the Filter settings, the following is set:

.. image:: newsletter-archive-page-filter.png

No settings are made for Time period.

Newsletters from the editor's point of view
----------------------------------------------
When a newsletter editor creates a newsletter, the first step is to create a new page for the newsletter, in this example by clicking the button CREATE NEWSLETTER, as seen in the image above:

.. image:: cerate-newsletter-1-new.png

The new page can look something like this:

.. image:: create-newsletter-2-new.png

The editor can now use the blocks set up on the page type, in Write mode, or in Design mode. In this implementation example, a text block for the newsletter heading and another text block for the newsletter text is available, as well as a page rollup block (that's "Pick pages".)

He or she enters some text for the newsletter, and picks the news pages to be sent in the newsletter, for example:

.. image:: newsletter-editor-page-picking.png

More information about how to use the page picker is found here: :doc:`The Page picker </general-assets/page-picker/index>`

If it's set up that way, some edits to properties may be needed, and the Email recipients must be added, everything available through Write mode and Design mode. The editor just clicks NEXT to cycle through the steps.

.. image:: create-newsletter-3-new.png

When it's time to publish and send, the editor can preview the newsletter before publishing. The editor can also send the newsletter to someone for a last check before sending to the recipients.

.. image:: newsletter-editor-send.png

When all is done, the editor then publishes to send the newsletter. If needed, the newsletter can be saved as a draft, as all other pages, and be sent later. If scheduled publishing is set up, it can be used for newsletters as well.

You can find more information about publishing a page here: :doc:`Publish page changes </pages/publish-page-changes/index>`

Here's an example of a newsletter:

.. image:: newsletter-example-new.png

