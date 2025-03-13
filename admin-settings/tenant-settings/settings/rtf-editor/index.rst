RTF editor settings
====================

Use these settings to decide which default options should be available for the rich text editor and the limited rich text editor, in the tenant. 

.. image:: rtf-editor-78.png

**Note!** For some blocks a custom RTF editor can be created. If that is done it will override these settings.

Both lists are handled the same way.

1. Select and deselect options to be available in the editor and save when you're done.

.. image:: rtf-editor-options-78.png

(All options are not shown in the image above, there's a lot more.)

At the top you will see a preview of what the RTF editor will look like with the selected options.

Most options should be self explanatory, but some options may need a description, see below.

**Language**:
**Important note!** This option should normally NOT be added to the RTF editor here. It's used in special cases only and will, for example, be added automatically to multi language fields.

**Activate machine translation (Text translator)**:
Text translator is the option for machine translations editors can use where the RTF editor is available. 

**Note!** Machine translation is not available in Omnia on-prem.

The text translator is always available in the tenant, no need to activated a feature, but there are two different translators to choose from per default, and more can be installed. More information about this is found here: :doc:`Services - Text translator </dmin-settings/tenant-settings/system/services-612/text-translator/index>`

Note that a machine translation is a suggestion - the text can always be edited and all suggestions by the machine translation can be discarded, if needed. It's always up to the person editing the text in the block to use a machine translation, or not, and to edit the translation before it's published.

Information on how to use machine translation is found under the heading "Using machine translation" on this page: :doc:`Editing text with the RTF editor </general-assets/rtf-editor/index>`

If you are working with language variations, a translator for the variations are always available there. See this page for more information: :doc:`Edit page variations </pages/edit-page-variations/index>`

Make the RTF editor enterprise glossary aware
------------------------------------------------
You can select "Enterprise glossary suggestion" to make the RTF editor enterprise glossary aware.

This means that whenever an author writes something in an RTF editor that match a term in the enterprise glossary, it will be highlighted. The author can click on the highlighted text and decide whether to create a link or not to the enterprise glossary term. If a link to the term is created, it will be possible for the end user to click on it and get detailed information about the term.

When a term is highlighted, it can look like this:

.. image:: rtf-editor-glossary-aware-highlight.png

When the author clicks the highlighted term, these two icons are shown:

.. image:: rtf-editor-glossary-aware-highlight-icons.png

The icon to the left is used to create a link, the other one to remove the link.

Animated GIF and emojis
-----------------------------
The possibility to add an animated GIF and/or to add emojis, can be available in the RTF editor. You can choose this by selecting "Gif" and/or "Emoji picker".

See the headings "Add an animated GIF" and "Add an emoji" on this page for information about how it works: :doc:`Editing text with the RTF editor </general-assets/rtf-editor/index>`

Settings for Styles
--------------------
To edit the settings for styles, click the cog wheel.

.. image:: tenant-settings-styles-76.png

Expand the list and select the styles that should be available.

.. image:: tenant-settings-styles-select-76.png

**Note!** You can use Text styles (option in the Settings menu) to configure styles. The enabled styles from Text styles are those shown in the above list. 

OpenAI
---------
OpenAI can be made available here, according to Omnia admin settings. 

The tenant feature "Text completion" must be activated for this functionality to be available throughout the tenant. Then, the feature can be added to the rich text editor or the limited rich text editor, or both. 

See this page for more information about the settings: :doc:`OpenAI (Admin settings) </admin-settings/tenant-settings/settings/open-ai/index>`

See the bottom of this page for information about how OpenAI can be used in the RTF editor: :doc:`Editing text with the RTF Editor </general-assets/rtf-editor/index>`

Reorder the options
---------------------
If you would like to reorder the options in the editor, use the icons to drag and drop:

.. image:: rtf-editor-reorder-76.png
