Editing text with the RTF editor
=====================================

When editing text in Omnia, a RTF editor can be available. What is available in the editor is set up in Omnia admin, and in a few cases in the block itself. In a Text block, the mode must be Limited rich text, Rich text or Custom rich text for the RTF editor to be available. When editing text in a Text block it's done using Write mode.

**Note!** Options available in the RTF editor can differ a lot, depending on how it's set up. Not all options described below may be available.

For more information about the settings, see: :doc:`RTF editor settings </admin-settings/tenant-settings/settings/rtf-editor/index>`

Using the RTF editor
**********************
Here's a common example of available options in the editor:

.. image:: rtf-editor-all-options-76.png

There are two lists and a number of icons available. You point at an icon for a tool tip. Here's an example:

.. image:: rtf-editor-all-tooltip-76.png

Some options are also available as a floating toolbar, when text is selected, for example "Add link", "Keep text only", "OpenAI" (if available) and "Keep text only":

.. image:: rtf-editor-all-floating-76.png

Se below for more information.

Add style
---------------
A number of styles can be available. To add a style, do the following:

1. Select the text.
2. Open the "Styles" list and select style.

.. image:: rtf-editor-all-style-76.png

This example only shows headings, but there are other styles available below. Any style can be added to this list in Omnia admin (see link above).

Add link
----------
To add a link, do the following.

1. Click where the link should be added, or select some text that should be the clickable text for the link.
2. Click the icon in the toolbar at the top, or in the floating toolbar.

.. image:: rtf-editor-all-link-76.png

The Add link general asset is shown. If you selected text, it's added to the title field:

.. image:: rtf-editor-all-link-title-76.png

See this page for more information: :doc:`Add link </general-assets/add-link/index>`

To edit or remove a link:

1. Select some of the clickable text for the link.
2. Use the icons in the floating toolbar.

Add link to an enterprise term
-------------------------------
You may be able to add a link to an enterprise term, and by that use the enterprise glossary functionality.

Here's how to add such a link:

1. Type the text as usual and when you type something that match a term in the enterprise glossary, it's highlighted.

.. image:: rtf-editor-glossary-aware-highlight-76.png

2. To add a link to that term (you don't have to), click the term and the following is shown:

.. image:: rtf-editor-glossary-aware-highlight-icons-76.png

3. Click the left icon to create the link (the one to the right to remove it).

For more information about glossary terms, see: :doc:`Enterprise glossary </admin-settings/tenant-settings/properties/enterprise-glossary/index>`

Add and edit media
--------------------
You can add an image or a video to the text. This is how:

1. Click where the image or video should be added.
2. Click the media icon.

.. image:: rtf-add-image-76.png

3. Use the media picker to add the image or video.

.. image:: rtf-add-image-media-picker-76.png

Available image or video suppliers will differ depending on setup. This is an example.

See this page for more information: :doc:`Media picker </general-assets/media-picker/index>`

The image/video area fills up the whole width (same width as the text), the height/width ratio intact. Some tools also becomes available. Here's an example for a photo:

.. image:: what-the-heck-76.png

From left to right:

+ To create a clickable link on the image.
+ To edit the image in Media Picker.
+ To remove the image.
+ To set the width of the image.

For a video, it's not possible to create a clickable link. The other three tools are availble for a video as well.

To create a clickable link, click the link tool shown on the image and use the Add link general asset to add the link, see: :doc:`Add link </general-assets/add-link/index>`

When you click the tool to set the image width, the following is available:

.. image:: rtf-add-image-tools-width-1-76.png

The following is shown:

.. image:: rtf-add-image-tools-width-2-76.png

Responsive width is the default, meaning the image fills the whole width of the RTF area in the block, with the height/width ratio intact. (This works the same for a video).

You can also set an exact width in pixels by selecting "Fixed width". 

Add an animated GIF
---------------------
It can be possible to add an animated GIF to the RTF editor, if settings allow it, using this icon:

.. image:: rtf-animated-gif-icon-76.png

1. click where the animated GIF should be placed.
2. Click the icon.

Something like the following is now shown:

.. image:: rtf-animated-gif-select-76.png

3. Use the search field or just browse to find an animated GIF.
4. Click the GIF to add it.
5. Click the GIF in the RTF editor, for editing options.

To remove an animated GIF, click it and click the dust bin shown.

You can also add a clickable link to the GIF, using the normal link tool, see above under the heading "Add and edit media". 

Add an emoji
---------------------
It can be possible to add an emoji to the RTF editor, if settings allow it, using this icon:

.. image:: rtf-emoticon-icon-76.png

1. click where the emoji should be placed.
2. Click the icon.

Something like the following is now shown:

.. image:: rtf-emoticon-select-76.png

3. Use the search field or just browse to find the emoji you want.
4. Click the emoji to add it. (You can add more than one if you want to).
5. Click outside the emoji window to close it.

Add a table
------------
To add a table, do the following:

1. Click where the table should be placed.
2. Click the table icon.

.. image:: rtf-editor-table-76.png

3. Click somewhere in the table for more options.

The following options for tables are available:

.. image:: rtf-editor-table-edits-76.png

Most of these option you recognize from other applications, for example Microsoft Word.

In the Table styles list, a number of ready-to-use styles are available:

.. image:: rtf-editor-table-edits-table-styles-76.png

You can also style an individual cell using the icon to the far right.

.. image:: rtf-editor-table-edits-cell-style-76.png

Pasting text only
-------------------
A well known problem when pasting text from other sources into an HTML environment is that styles and the like from the original text does not work - or is not wanted. To make that problem go away, you can paste the text as text only.

All style tags are removed. Default HTML styles is kept.

1. Paste the text.
2. Select the pasted text.
3. Click the Keep text only icon.

.. image:: rtf-editor-test-only-76.png

You can also use this option on text you already have in the block. Just select the text and the option becomes available.

Pasting contents from Microsoft Word
-------------------------------------
When pasting contents from a Microsoft Word document into a rich text field, some of the text formats can also be pasted. Headings are also regocnized and the RTF editor settings for these headings are applied. 

Note that bold, underscore and headings are considered default HTML styles and will be kept, with the RTF editor settings, even when pasting text only is selected.

Images from the Word document are also pasted, if you select them. Note that this apply to Rich text fields (blocks) only. It does not work for plain text.

Add an anchor (bookmark)
---------------------------
Anchors can be used in the Add link general asset and when creating a link button using the Action button block. So, if you add an anchor (bookmark) to the text, links can be created to that anchor. Another use is to create an anchor navigation.

Here's how to add an anchor:

1. Type the text.
2. Select the text where the anchor should be placed.
3. Click the anchor icon.

.. image:: anchor-icon-76.png

4. Edit the suggested anchor name, or keep it as is, and save.

.. image:: anchor-name-76.png

For more information about Add link, see: :doc:`Add link </general-assets/add-link/index>`

For more information about the action button block, see: :doc:`Action button block </blocks/button-link/index>`

For more information about anchor navigation, see: :doc:`Anchor navigation block </blocks/anchor-navigation/index>` 

Using machine translation
---------------------------
If the option is available you can machine translate the text in a block. The whole text in the block is translated in one go. It's just a suggestion and you can edit it to finish the translation. 

Here's how:

1. Click the icon.

.. image:: rtf-editor-machine-translation-76.png

2. Select the language to translate to.

.. image:: machine-translation-select-language-76.png

Any language can be selected here. The languages set up in Omnia admin are shown at the top of the list. To select another language, select "Show all Languages" at the bottom of the list.

.. image:: machine-translation-select-language-all-76.png

**Note!** You can use Ctrl-Z or just discard changes if you change your mind.

Using OpenAI
-----------------
If available, you can use OpenAI to suggest changes to the text, or maybe even to suggest some text for you.

In Omnia 7.8, the AI functionality is called The AI Engine and is generally updated and somewhat extended. You work with the options for text suggestions the same way in Omnia 7.8, as is described here.

If OpenAI is available, you use the following icon to start the option:

.. image:: openai-icon-76.png

If you select a part of the text, it's also available on the floating toolbar:

.. image:: openai-icon-floating-76.png

Here's how to use it:

1. Click the icon to process the whole text, or select part of the text and then click the icon to only process that part.
2. Choose what to do.

What is available here can differ greatly, if available at all. It's fully up to administrators to set up in Omnia admin. Here's an example:

.. image:: openai-options-76.png

3. Select option.
4. Check OpenAI:s suggestion and edit if needed (or cancel the whole suggestions with Ctrl-Z).

If a Custom option is available (can be named something else) you can ask OpenAI to do more or less anything you like (with text that is).

The chat window, which can be called something else ("Alameda Bot" in this example), can look this way:

.. image:: openai-chat-76.png

You can ask OpenAI to do any changes to the text, or create new text, by using "normal" conversation. Just try it out, what will be saved is totally up to you.

In this example the author wanted to write some text about how relaxing fishing can be and wanted some suggestions. 

.. image:: openai-chat-example-76.png

The author then copied bits and pieces of the text and edited it to the description he or she wanted.

HTML
------
If it's available, you can work with the HTML code, if you know how. When you click the icon a separate window is opened, where you do your HTML work.

.. image:: rtf-editor-html-76-new.png

The window where you can edit the HTML code can look something like this:

.. image:: rtf-editor-edit-html-76.png

Just save when you're done and you will be returned to the RTF editor.

