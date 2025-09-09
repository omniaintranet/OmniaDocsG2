Document types
================

When creating a new controlled document an author selects a document type. Document types can be grouped. In that case the author first selects group and then document type within that group.

The settings displays all existing document types, and groups, for example:

.. image:: document-types-start-v78.png

The i icon can show information on syncronization of new or edited document types.

.. image:: document-types-i-icon-v78.png

Here's an example from a test environment:

.. image:: document-types-info-v78.png

Creating a new group
**********************
To create a new a group, do the following:

1. Click any existing group.
2. Click the plus and select "Create Group".

.. image:: doctype-select-group-v78.png
 
3. Add a title. A title in the default language in the tenant is mandatory.

.. image:: doctype-group-title-v78.png

4. Save.

Creating a document type
*****************************
To create a new document dype, do the following:

1. Click the group to create a document type in.
2. Click the plus and select "Create Document Type".

.. image:: doctype-new-type-v78.png
 
2. Set all necessary settings and save.

The same settings are available when creating a document type and when editing one. See *Settings for document types* below for detailed information.

Sort document types
***********************
You can sort if you want to present the list in a specific order to the editors.

1. Select the group or document type to move and use the arrows.

.. image:: document-types-move-v78.png

Move a document type
*************************
You can move a document type to another group when editing the document type.

1. Click MOVE.

.. image:: move-image-type-1-v78.png

2. Select the group to move to and save.

.. image:: move-image-type-2-v78.png

Edit or delete a document type or group
******************************************
To edit a group or a document type, do the following:

1. Select the type or group.
2. Edit available settings (see below for detailed information about the settings).
3. Save.

To delete a group or document type, do the following:

1. Select the type or group.
2. Available settings are now shown.
3. Click the dust bin.

.. image:: doctype-delete-v78.png

**Note!** If a group contains any document types, it can't deleted (the delete icon is not shown). You must delete or move any document type(s) from the group first.

Settings for document types
****************************
The settings are organized into five tabs, see the sections below.

General
--------
The General tab contains the following settings (image from Omnia 7.8).

.. image:: document-type-general-v78-1.png

and these:

.. image:: document-type-general-v78-2.png

+ **Title**: Add a title for the document type. Note that a title in the default language is mandatory.
+ **Description**: A description is not mandatory but can be useful if your organization uses a lot of different document types.
+ **Property set**: Property sets is a way of grouping a number of properties into a set, which makes it easier to use properties in several document types. Select a property set for the document type. When you have done so you can click the cogwheel to see the properties that belong to the set. You will also see information about, and can sometimes edit, placeholder shortname and default value for the properties in the set.
+ **Document templates**: Select one or more of the available templates. You must always do this even if there’s just one template available.
+ **Default document template**: Use this option to select one of the templates for this document type as the default template. When an author selects the document type, this template is preselected.
+ **Enable appendices**: Check this option to allow for appendices. Authors can then tie other documents as appendices to the main documents. This option must be checked to make it possible for this document type.
+ **Enable signed copy**: If it should be possible to handle a signed copy for documents of this type, select this option. For more information on signed copies, see this page: :doc:`Working with published documents </working-with-documents/authoring-controlled-documents/working-with-published-documents/index>`
+ **Enable read receipts**: If it should be possible to send read receipts when a new controlled document is published, select this option. It's then up to the document editor to decide to use it or not each time a document is published (also see *Enable sign-off requests* below as an alternative way).
+ **Is record**: Some controlled documents may not need to be updated, just to be used as is. To set that for this document type, select this option. See below for more information.
+ **Enable sign-off request**: If it should be posible for published controlled documents of this type to be added to sign-off requests, select this option. See this page for more information: :doc:`Sign-off requests </admin-settings/tenant-settings/sign-off-requests-613/index>`
+ **Enable Create document feature in document rollup**: In the document rollup the “Create document icon” column can be added. A document can be created using this option only if it belongs to a document type that has this option selected. if not, the option is not shown.
+ **Enable track changes when sending for comments**: Microsoft Word's options for tracking changes can be really useful when sending a document for comments. Select this option to automatically enable these options in Word.
+ **Enable 'Show changes' button to document authors**: If the Draftable feature is activated, this option is available here. Select to enable the button "Show changes" for Draftable. See this page for more information about Draftable: :doc:`See changes in a controlled document </user-options/see-changes-in-controlled-document/index>`
+ **Enable 'Show changes' button in a document rollup**: If the Draftable feature is activated, this option can be made available in a document rollup. For more info about Draftable, see link above. For more information about document rollups, see: :doc:`The document rollup block</blocks/document-rollup/index>`

Don't forget to save when you're done.

Options for Is record
----------------------
The following options are available when you select "Is record":

.. image:: document-type-is-record-v78.png

+ **Disable create draft**: When you select this option, documents of this document type can only exist in one edition. Creating a draft from a published edition is not possible.
+ **Disable move**: When this is selected, the Move option in a controlled documents library, can't be used for a document of this type.
+ **Disable unpublish**: If this option is selected, a document of this type can't be unpublished. Once published, it's always available.

You can select any combination of options here. Be careful, this can not be changed for existing, published documents created from a document type with these settings, just for new document editions after the document type has been edited.

Publish
---------
On the Publish tab you can set the following (image from Omnia 7.10):

.. image:: document-types-publish-v710.png

+ **Replace tokens inside document on publishing**: When a document is published, the placeholders (tokens) will be replaced with metadata, but for a document that will be used as a template, you will probably not want that to happen. If you are creating a document type to be used for templates, deselect this option.
+ **Allow revisions**: Selecting this option you can allow authors to publish a revision of a document that does not require approval, for example for correcting typing errors. If this option is active, it's up to the author to decide if approval is needed or not. Approval is still needed for publication of a new edition of a document.
+ **Publishing approval**: Select if approval is to be used for this document type. If this option is NOT active, a document will be published immediately when an author clicks "Publish". If publishing approval is selected, you must also choose how approval will take place, see below.
+ **Allow scheduled publishing**: Available in Omnia 7.10. To allow scheduled publishing for this document type, select this.
+ **Conversion**: Select if conversion to PDF will be available, and then choose how.
+ **Semantic search**: Can be available in Omnia 7.8 and later. If semantic search should be possible for this document type, select the option and the choose how, see below.
+ **Do not allow the publishing of a document with unaccepted changes**: If you select this option, all unaccepted changes, added with the "Review" options, must be accepted/not accepted before a document can be published.

Don't forget to save your changes.

**Important note!** How publish will work is set when document management is activated for a site. If the settings here are changed, it does not change the setting in existing sites. If you want that to happen, you must update the document management feature in each site. See the heading "Features" on this page for more information: :doc:`App settings </admin-settings/app-settings/index>`

Options for publishing approval
--------------------------------
If you selected that publishing approval is needed for this document type, you mus also select how:

.. image:: document-types-publish-approval-v78.png

+ **Anyone**: The author can select any user of the portal as approver, when the document is published.
+ **Limited list of users**: Authors can select approvers from a defined list only. You create the list here.
+ **Term-driven**: Authors can select approvers from a defined list only. Available approvers depend on the properties selected for the documents. You select the term(s) here. When you have selected one or more terms you can use the cogwheel to set approvers for individual terms in the set.
+ **Based on person property**: You select one of the person properties defined, for example document owner.
+ **Group**: This setting will use the permission group for approvers in the teamsite. Needs "Approvers group" to be selected in settings for document management.

Option for scheduled publishing
-------------------------------
When you have selected to allow secheduled publishing för this document type, choose the property to bas that on.

.. image:: doc-scheduled.png

Options for semantic search
------------------------------
For semantic search to be available in the tenant, the feature "Semantic search" must be active.

When you select Semantic search, you also select one of these options:

.. image:: document-types-publish-semantic-v78.png

+ **Allow to be included in semantic search. Unchecked by default.**: An author can choose that a document of this type should be available for semantic search, in the publishing process. With this option, the default is that it's not (unchecked).
+ **Allow to be included in semantic search. Checked by default.**: A document of this type is available for semantic search by default, in the publishing process. With this option an author can choose that it should not be, by unchecking the option.
+ **Always include in semantic search. Unchecked by default.**: All documents of this type are always available for semantic search. No option is shown when publishing.The tenant feature "Semantic search" must be active for this functionality to be available.

**Very important!** The semantic search will soon be developed further in Omnia but for now it does **not support security trimming**. 

For more information, see: :doc:`About semantic search </general-assets/about-semantic-search/index>`

Review
---------
On this tab you handle settings for feedback and review for this document type. When a document of this type has passed it's review date, a link to the document is placed in the list "Expired review".

At first, just these options are available:

.. image:: document-types-review-v78.png

+ **Feedback recipients**: Select feedback recipient(s) in the list. 
+ **Review reminder**: Select this option to activate review reminders.

When review reminders are activated you can set the following:

.. image:: document-types-review-reminder-v78.png

+ **Review interval**: Set number of days, months or years for the review interval. 
+ **Property**: Another way is to select a property for review. An example could be if you want authors to be able to set a specific date for review, which could be needed for a supplier agreement, for example. A date property must then have been set up for this to work.
+ **Send reminder in advance**: Set the number of days, months or years that a reminder should be sent, before the review date.
+ **Review reminder recipients**: Select review reminder recipient(s) in the list.
+ **Create task**: If a review task should be created, select this option. For more information, see below.

When you choose to create a task, this is shown:

.. image:: doctype-review-create-task-v78.png

1. Use the list to select who the task should be sent to, for example document owner.
2. Select when the task will expire.
3. Add a custom text for the review button, if needed.
4. Save when you're done with all settings. 

**Important note!** The review reminder task works this way: If a new edition/revision of a controlled document is published or the published document is deleted, any associated review reminder task will be automatically completed. If the review is completed, the review comment will be added to the document history and a new review date will be calculated based on the review reminder rule set on the document type.

Archive
----------
Use this tab to decide if documents of this type should be archived or not. If the document type should be archived, you can set archive to be used, by adding the URL. You don't have to add a URL to use the default archive.

.. image:: document-types-archive-v78.png

Retention
------------
If retention is activated, this tab is shown for all document types:

.. image:: document-types-retention-v78.png

Use this tab to set up a retention policy.

+ **Limit Retention**: Select this option if a retention policy should be set for this document type.

Then you can set the following:

.. image:: document-types-retention-settings-v78.png

+ **Calculated**: You can select to calculate the number of days, months or years from when the document was first published or when it was last published.
+ **Property**: Another way is to select a property for retention (if any are availble). Could for example be Retention date.

When the set retention time has passed, the retention manager will receive an Email. The Email includes a link to a page where the document can be terminated (completely removed from the system), if needed. 

