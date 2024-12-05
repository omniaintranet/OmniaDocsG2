Controlled documents library settings
=======================================

You must be administrator (the permission group is often called "Owners") of the teamsite - there can be one or more - to be able to edit the settings for the three lists in the controlled documents library, and to edit permissions.

Settings for the tabs
***********************
To access the settings, go to the controlled documents library and click "Edit".

.. image:: edit-controlled-library-77.png

Here, the following settings are available:

.. image:: edit-controlled-library-settings-all-77.png

General
-----------
Here you can use the following settings:

.. image:: edit-controlled-library-general-77.png

+ **Title**: You can edit or add a title for the library here. 
+ **Open in client app**: Per default, documents are opened in the online Microsoft 365 application. If documents should be opened in the locally installed application instead, select this option. 

Display
----------
Here you can set the following:

.. image:: edit-controlled-library-display-77.png

+ **Default tab**: Decide which tab will be shown when an author enters the controlled documents library.
+ **Paging**: Select paging for the lists here; “No paging”, “Classic” or “Scroll”.
+ **Page size**: Set the number of rows to display. **Important note**: If more documents or tasks are available than the page size set, a navigation to the next page is shown when paging is set to "Classic". If paging is set to either "No paging" or "Scroll", page size is the maximum number of documents or tasks that can be shown in the lists, regardless of how many are available.
+ **Padding**: Set some padding around the lists, if needed.
+ **Hide Tasks tab**: If the Tasks tab should not be displayed for authors, select this option.

Drafts
--------
The following settings are available for the Drafts tab:

.. image:: edit-controlled-library-drafts-77.png

+ **Default ordering field**: Select the column for default sort order for the list.
+ **Sort direction**: Select Descending or Ascending here.
+ **Show search box**: If authors should be able to search for draft documents in the library, select this option.
+ **Column**: Use this option to add a column to be shown. Open the list, select the column and click "ADD".
+ **Display columns in draft view**: Here the selected columns are listed. To remove a column, click the dust bin. If no dust bin is shown for a column it's mandatory, and therefore can't be removed. You can set the order of the columns, from left to right, by grabbing the equal-to-icon for the column and drag it to another place in the list.

Published
------------
The same type of settings as for drafts are available here. See above for a description.

.. image:: edit-controlled-library-published-77.png

Default document types
------------------------
Use this setting to select one or more document types to be suggested when an author creates a new draft document in this controlled documents library.

As an example, these settings:

.. image:: default-types-example-77.png

Will result in the following:

.. image:: default-types-example-wizard-77.png

A user can always click ALL to see all available document types. More information about how the document wizard works is found here: :doc:`Using the create new document wizard </working-with-documents/using-the-document-wizard/index>`

To add a document type, do the following:

1. Click in the field.

.. image:: document-type-add-1-77.png

2. Use the list to select one or more document types. 

.. image:: document-type-add-2-77.png

If the document types are grouped (as Organization, Office, Project and Product are in the image above) you may need to expand a group to select a document type there. 

Also note that you can deselect document types as well using this list.

For more information about document types, see this page: :doc:`Document types </admin-settings/tenant-settings/document-management/document-types/index>`

Permissions
************
If Document management is set up for using permission groups, an administrator (Owner) of the teamsite, can edit these permissions.

**Important note!** Only SharePoint users can be added here (not Omnia only users). Also note that a user or a group must be permissions enabled to show up in the lists.

Do the following:

1. Click PERMISSION in the controlled documents library.

.. image:: click-permissions-77.png

Something like the following is shown:

.. image:: controlled-permissions-2-77.png

How this works depends on settings for document management at tenant level. In this example, authors of controlled documents are set as "Group owner and members", and additionally an approvers permission group will be used. Other settings for "Authors" will result in a "normal" people picker field, just as the "Readers" field in this example.

In this example, the settings for authors works as follows:

You can add/remove groups and/or users for readers and approvers the usual way.

To add authors, that's a bit different:

1. Click the link "Group owner and members".

.. image:: click-owners-77.png

2. Add owners and members for the site, as needed.

.. image:: click-owners-listed-77.png

3. Read the description carefully once you have clicked "Add members".

.. image:: click-owners-read-77.png

Note that external users that has been invited in Entra ID can be added here as well. Users invited this way can log in with their own Microsoft 365 account.

Settings for Document management is found under that heading in Omnia admin. See this part of the documentation for more information: :doc:`Document management </admin-settings/tenant-settings/document-management/index>`

