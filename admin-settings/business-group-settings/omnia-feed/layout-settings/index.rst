Layout settings
===========================================

**We are still working on this description. More will be added soon.**

In Omnia 7.11 and later, there is a new way of working with the views for the Omnia Feed tabs. You can now set up a number of layouts for views (Tab view and Detail view). The possibilities are almost endless. 
To speed up the process, you can base a new layout on a template or on an existing (exported) layout file.

You must decide for each business profile, if you would like to work with the views the new way, or the legacy way. You can't use both. To be clear, you can take different decisions for the business profiles in your tenant, but note that once you have chosen to go for the new way for a business profile, it can't be reversed.

**Note!** Working with layouts for the tabs in Omnia Feed is suitable for advanced administrators and developers. Also, if you plan to continue using the "old" way, the legacy way, of working with the tabs for this business profile, you don't need to do anything here.

The following settings are available here:

.. image:: layout-settings.png
   
This is how you are meant to work with these options:

1. Add one or more previewers if you like some comments along the way.
2. Create one or more layout drafts. The draft(s) are now listed.
3. Collect comments from the previewers, if any.
4. Do final changes and publish the layouts.
5. Activate the layout engine migration.

Before the migration, previewers can see the new layout(s) in their unit, for others the legacay display is used. After the migration, previewers can select the different versions of a layout available, other users can only see the last one published.

**Note!** The layout engine migration can not be reversed for this business profile, once started, as stated in the text above the button. When the migration is completed, the Display settings for the tabs work differently. Now you select a layout there.

You can also share layouts between business profiles if you wish, to make sure the tabs look the same for some, or all, business profiles within the tenant - or simply use already created layouts as starting points for new layouts.

Creating new layouts
**********************
To create one or more new layouts, click the plus and use the following settings:

.. image:: new-layout.png

You can import a layout or select a layout template as a starting point, see below. One layout template is always available.

Layout settings
-----------------
Use these settings to create a new layout or edit a template or an imported layout:

+ **Title**: The title will be used in the list of layouts, and as the base for the file name, if the layout is exported.
+ **Page Types**: You can add one or more page types.
+ **Tab view settings**: Here you set up the tab view settings for the tab.
+ **Detail view settings**: Here you set up the detail view setting for the tab.
+ **Version history**: Each time you edit a layout and save or publish it, a new version is created. Published editions are noted with an integer, work in progress with a decimal. When there's more than one version, you can continue working on any version. 

When all settings are done, don't forget to click CREATE to create a draft of the new layout. When the layout is finalized, you can publish the layout.

Edit a layout
*****************
When you have created a layout draft, it's shown in the list and you can edit or delete it. Click here to edit:

.. image:: edit-layout-edit.png

The settings are shown:

.. image:: edit-layout-edit-preview.png

If you click the EDIT button you can edit all settings as shown above. If there are more than one version of this layout available, you can choose the version to work with.

When all edits are done, and saved, you use the PUBLISH button to finalize the layout.

Create a draft from a published version
*****************************************
When you have opened a published version of a layout, you can create a new draft from that layout:

.. image:: layout-create-draft.png

When a new draft is created, you work with it as described above.

Export a layout
*****************
You can export a published layout so it can be used as a starting point, or as is, in another business profile.

Click this button to export the layout:

.. image:: layout-export-layout.png

A file is now created as a json file in your computer's Downloads folder, using the title of the layout as the file name. This file can be copied or moved anywhere you need.

Import a layout
****************
If there are a layout that have been exported available, you can import it, but note that you must know the file name. Here's how:

1. Click this icon.

.. image:: import-layout-icon.png

2. Click "Choose file" to browse and find the layout file.

.. image:: import-layout-choose.png

3. When you have selected a file, click IMPORT.

You can now edit the imported layout if you wish, and publish a new version. Note that the title is not imported, you always have to add a  new title.

Use a template
******************
To use a template as a starting point, do the following:

1. Click this icon.

.. image:: layout-template-icon.png

2. Select a layout.

.. image:: layout-template-select.png

3. Click IMPORT.
4. Edit the template if you wish, and publish a new version.

Editing layout settings
**************************
When creating a new or editing a layout, you can add a great number of settings for both Tab view settings and Detail view settings. You work the same way with both.

The work order is roughly:

1. Add one or more page types (mandatory).
2. Select a block and click ADD.

Additional settings for the block are now shown - different settings depending on type of block. Here's an example for the Heading block:

.. image:: layout-heading-block.png

For several blocks you choose properties the get information from. For most blocks you can also add a custom style sheet if needed, if you now how to use Text style syntax for React Native: https://reactnative.dev/docs/text-style-props

For a few blocks, you can select a number of child blocks to be displayed. Here's an example from the template with blocks and a custom style sheet:

.. image:: layout-heading-block-example-1.png

To edit child blocks, click the pen. Now you can edit one or more child blocks and decide the view order, for example:

.. image:: layout-heading-block-example-2.png

As you can see, in this work view you can delete child blocks, and you can add new ones.

You can edit any settings for a child block (settings differ between blocks). Here's an example of settings for a Heading child block:

.. image:: layout-heading-block-example-3.png

