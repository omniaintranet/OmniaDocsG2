Edit permissions for a page
=============================

Default settings is that the same edit permissions apply to all pages, including variations, but that can be changed if needed. If you change permissions for a page that has sub pages, all the sub pages gets the new permissions (they inherit the permissions settings from the "parent"). Also note that permissions for variations works a bit differentlt, see below.

Do the following:

1. Open Edit mode.
2. Select the page where you need to edit permissions.
3. Open the menu and select "Permissions".

.. image:: page-select-permissions-new.png

Omnia works with inheritance, just as Sharepoint does, so the first thing you have to do is:

4. Click to break permission inheritance.

.. image:: page-select-permissions-inheritance-new.png

You can now set the following permissions, for this page and all sub pages (options in Omnia 7.8 and earlier, see below for Omnia 7.9 and later):

+ **Editor**: Can create, delete and move pages and nodes, can use both Design mode and Write mode and can edit permissions here.
+ **Author**: Can create pages and can use Write mode to edit contents in some blocks.

For more information on the people picker, see: :doc:`Using the people picker </general-assets/using-people-picker/index>`

**Note!** Page collection administrators and publishing app administrators are always permitted to work with pages (Editor permissions). They don't need to be added here.

5. To add an editor or an author, just open the list and select the user.

.. image:: page-permissions-select-user-new.png

You can also search for users the same way as in other people lists.

6. To remove a user from one of the list, click the x. 

.. image:: page-permissions-remove-user-new.png

7. Click "SAVE" when you're done. (If you don't want to save, just close the window to ignore the changes.

Permissions for variations
***************************
A variation page is simply a copy of a source page, with some sort of alternative content, for example in another language.

An author can be assigned to a specific variation (in Omnia 7.9 and later several authors). If that is not done, permission for the source page apply to the variations as well. Also note that page collection administrators always can edit variations if needed.

Read more about variation authors on this page: :doc:`Publishing app settings </pages/page-settings/index>`

If needed, specific permissions for certain variations and varition pages can be set up, see: :doc:`Permissions for variation pages </pages/permissions-for-variations/index>`

