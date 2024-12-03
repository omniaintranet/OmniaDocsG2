Sections and blocks in a page type
=================================================

This describes how to work with sections and blocks for a page type. You work the same way with local page types and tenant page types.

For the very first steps when creating a new page type, see: :doc:`Create new page type </pages/page-types/create-new-page-type/index>`

For information on the settings: :doc:`Section settings </pages/page-types/section-settings/index>`

Create a section in a column
******************************
If needed, you can create a section in a column and then select a layout for the column and set all other section settings. Here's how:

1. Click the plus for the column.

.. image:: column-layout-click-plus-new.png

Note that it's the same dialog for sections and blocks you can add to a page or a page layout. The sections are found under "Layout".

2. Open the Layout list.

.. image:: column-layout-list-77.png

3. Select layout for the column.

.. image:: column-layout-list-open-77.png

4. Set the section's settings.

For a description of available settings for the section, see: :doc:`Settings for sections </pages/page-types/section-settings/index>`

If needed, you can even go a step further and create a new section in one of the new columns.

**A tip!** The stepper section is useful when organizing information in steps. It's also used with the forms functionality. See below for more information.

Using the stepper section
***************************
A stepper section is one of the sections you can use.

.. image:: stepper-section.png

A stepper section makes it possible to organize content in a layout in a wizard-like style. It is possible to configure the stepper to allow for an author to add new steps in Write mode.

.. image:: working-with-stepper-77.png

Here's an example where a stepper section is used:

.. image:: working-with-stepper-example.png

All settings for sections are available for the stepper section.

Decide to show a section on a device or not
**********************************************
When you're working on a section you can select if it should be show on different devices.

Click this icon:

.. image:: device-support-section-77.png

You can now use the following settings:

.. image:: select-device-section-77.png

To hide a section for a device, do the following:

1. Select the device.
2. Click the pen for "Visibility".
3. Select "Hide Section".

To add some padding for the section, for a specific device, do the following:

1. Select the device.
2. Click the pen for "Section padding".
3. Set the padding.

Delete a section
*****************
If you need to delete a section, here's how to do it:

1. Click in the section (not on any plus).

.. image:: delete-section-1-77.png

2. Click the dust bin for the section.

.. image:: delete-section-2-77.png

3. Click OK to delete the section.

Move a section
***************
Do the following to move a section to another place on the page.

1. Click the section.
2. Click the Move icon.

.. image:: move-icon-section-77.png

Icons now show where you can move the section, for example:

.. image:: can-be-moved-section-77.png

3. Click the icon where you want the section and it's moved there.

Copy a section
***************
If you need a section with roughly the same settings somewhere else on the page, you can copy a section and place the copy where you want it, and then edit the settings. Do the following:

1. Click the section.
2. Click the Copy icon.

.. image:: copy-icon-section-77.png

Note that you can also copy blocks this way. Sections are indicated with a green color and blocks with a blue color, so you can see what is what.

Icons now show where you can add the new section, the same way as when you move a section, for example:

.. image:: section-can-be-copied-77.png

3. Click the icon where you want the copied section and it's placed there.
4. Edit the settings that you want to change for the copy.

Copy a section from the clipboard
-----------------------------------
There's also a clipboard available, that can be used to copy sections between pages or page types, see: :doc:`Clipboard for sections and blocks </general-assets/layout-explorer/clipboard-sections-blocks/index>`

Adding blocks to a section
***************************
Here's how to add a block to a section:

1. Click the plus for the section.

.. image:: addblock-1-77.png

2. Select block to add.

.. image:: section-add-block-77.png

Here's an example with a block added:

.. image:: section-block-added-77.png

You add additional blocks, work with the settings, move or delete blocks the same way as editors do when editing a page, see: :doc:`Working with blocks </blocks/working-with-blocks/index>`

**Note!** When editing a page, blocks that belong to the page type may be locked, meaning they can not be moved or deleted, and settings for those blocks can't be edited. But content can be edited, if applicable, using Write mode. For more information on this, see *Lock a block or not*, below.

Copy a block from the clipboard
---------------------------------------------
There's also a clipboard available, that can be used to copy blocks between pages or page types, see: :doc:`Clipboard for sections and blocks </general-assets/layout-explorer/clipboard-sections-blocks/index>`

Lock a block or not
************************
Additional settings for locking of blocks are available, under "Lock" in the LAYOUT menu:

.. image:: lock-menu-77.png

You can decide if it should be possible to unlock the settings for a block. The block can still not be moved and can not be deleted.

The following options are available here:

.. image:: lock-menu-options-77-frame.png

+ **Locked by default**: If this option is selected, and not the following, it works as before; settings for the block can not be changed but content can be edited using Write mode. If this option is NOT selected and the next is, the block's settings are simply not locked. Design permission is still needed to be able to change settings.
+ **Lock can be edited**: If this option is selected, editors (Design permission) can unlock or lock the settings for the block - and if unlocked, can edit the block's settings.

