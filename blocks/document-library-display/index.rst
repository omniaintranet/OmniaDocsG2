Document library display
==========================

Available in Omnia 7.12 and later.

**This is a preliminary description. Will be edited soon.**

Use this block to display the folder structure for a document library in SharePoint.

Settings
*********
The following settings are available:

.. image:: document-library-settings.png

Pick one document library

Pick it in the same way as we pick lists/document libraries.

Use CSOM

Support folders and all SharePoint views.

Support picking individual columns (to be consistent with the list rollup)

Prompt:

I am creating a new block in the legacy project for management system. This block will render a document library that the user selects in the settings panel.

For the settings form we should have a similar structure as other blocks. (Query, Display, Filter, Export)
- Picking the library should be built similar to the list rollups pick single list.

When picking, only show document libraries (should be easy to identify)

For display, we should show all SharePoint views that are available on the picked library.

We should support all sorts of views and settings that SharePoint provides.