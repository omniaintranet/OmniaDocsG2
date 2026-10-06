SharePoint sync
================

The following can be set here:

.. image:: web-content-sharepoint-sync-v712.png

General
***********
Use these settings to configure the sync from publishing apps in Omnia to SharePoint site pages. What you do is map properties to specific fields in SharePoint. (Image from Omnia 7.12).

.. image:: sharepoint-sync-v712.png

+ **Max number of versions to sync**: If there are several versions of start pages in Omnia, you can set this value to only sync the latest versions to SharePoint. The sync creates a backup in SharePoint. Start page versions that are not synced are still present in Omnia.
+ **Enable redirect to Omnia page**: Select this option (default) to redirect site pages links to the Omnia page instead of the backend communication site page, when applicable. These synced pages will be picked up by and displayed by Microsoft search. When the user clicks on an item in the search result, the user will be redirected to the correct Omnia page. 
+ **Enable full page view**: Available in Omnia 7.12 and later. Select to activate the full page experience. Note that the tenant feature "Omnia full page experience" must be active for this functionality to be available. For more information, see: :doc:`The full page experince </use-omnia-in-sharepoint/full-page-experience/index>`
+ **Enable enhanced Copilot integration. Available in Omnia 7.12 and later. This option must be activated to make the Omnia metadata avaiable to co-pilot. 
+ **Page Image etc**: Open the list for a field and select the property to map to.

**Note!** An administrator can override these sync settings for a specific page type, see the heading "Override SharePoint Sync Settings" on this page for more information: :doc:`Page Type Settings </pages/page-types/page-type-settings/index>`

Search
*********
By default, all normal text in blocks is searchable in full text search, but for example hidden properties are not. If you would like one or more properties to be searchable for full text search, add them here. One example is if you want to use a Keywbords property to make certain terms are searchable even if they are not present as text on the page.

To add properties to the full text search, do the following:

1. Click the plus.
2. Open the list and select a property.
3. Click ADD.

The property is now added to the list, for example:

.. image:: sharepoint-sync-search-list-v7.png

To additional properties, repeat these steps. To remove a property from the list, click the X.

4. Click SAVE when you're done.
