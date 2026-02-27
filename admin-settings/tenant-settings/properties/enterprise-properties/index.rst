Enterprise properties
=============================

Here you add ALL properties that should be used within the tenant. The list displays all existing properties organized after category, for example:

.. image:: enterprise-properties-list-v711.png

To find a property for editing, you can either search (note the search field at the top), or browse by category.

**Note!** In Omnia on-prem there is no support for Microsoft Search mappings.

Open a category to see the list of properties. Here's an example:

.. image:: enterprise-properties-list-example-v711.png

Click the pen to edit a property. See below for editable settings. If it's possible to delete a property (meaning move it to the Property recycle bin) a dust bin is displayed.

**Note!** Term sets to be used as properties for targeting in Omnia, must be set to "Available for tagging" in SharePoint, but we recommend that you set this for all SharePoint term sets.

Adding a property
*********************
To add a property, click the plus and use the following settings:

.. image:: tenant-properties-settings-v711.png

+ **Title**: Add a title (name) for the property. Default language is mandatory. Add titles in other tenant languages as needed.
+ **Internal name**: An internal name can, or should in some instances, be used instead of the title, for example as a place holder. The first character of an internal name can't be a number, and the name can't contain spaces. Note that the internal name can not be edited once the prroperty is created.
+ **Category**: Select category for the property here. 
+ **Type**: The property type can be Data, Datetime, Enterprise Keywords, Language, Media, Number, Person, Process, Rich text, Tags, Taxonomy, Text or Yes/No. Most of the types are self explanatory. "Data" is a system field that users never enter anything to. "Rich text" can be formatted by the editor. "Text" is plain text that the editor can't format. Note that the type can not be edited once the prroperty is created.

**Note!** Properties used for targeting must be of the "Taxonomy" type.

Some, but not all properties, can be selected as SharePoint Searchable and/or Microsoft Searchable. Then, open the option and select it, for example:

.. image:: tenant-properties-settings-more-v7.png

Editing a property
************************
When you edit a property, you can't change the internal name or the type, but you can change settings for SharePoint searchable and Microsoft searchable if needed.

**Note!** If you change settings for SharePoint Searchable it's only valid for new pages created from here on. If you want this setting to be active for all existing pages as well, you must execute Reindex for all publishing apps using this property, in the publishing app settings.

