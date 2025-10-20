Page collection settings
===============================

A number of settings can be edited for the page collection, this way:

1. Edit a page in the publishing app and open the page menu.
2. Click the main navigation node for the page collection.

In this example, three page collections has been added in the publishing app, besides Start and News, and "Start" is selected:

.. image:: page-collection-general-news2.png

3. Click "Settings".

.. image:: page-collection-click-settings-new2.png

4. Click "Edit" at the bottom to edit the settings.

.. image:: page-collection-click-edit-new2.png

4. Use the following settings (image from an existing page collection):

.. image:: page-collection-settings-79.png

All settings are not shown in the image above, but listed below.

Use the settings this way:

+ **Navigation structure/Flat**: Here you can see what was selected when the page collection was created. If you want to change from navigation structure to flat in an existing page collection, you need to first manually flatten the page structure (move sub pages so they all become main pages, or remove them) and then use the option here. You can always change from flat to navigation structure.
+ **Title**: The title for the page collection is shown here. It can be edited if needed. It's updated everywhere it's shown when the changes here are published.
+ **Layout**: Here a layout can be selected. Layouts are created in Omnia admin.
+ **Create page dialog**: You can set the title for the dialog displayed when an editor has selected to create a new page. If you leave this field blank, the dialog title will be "Create new page".
+ **Show URL**: If the URL for the new page should be shown for the editor when creating a page, select this option. The URL can then be edited.
+ **Show properties**: If available page properties should be shown for the editor when creating a page, select this option. The properties can then be edited in that stage. Page properties can always be edited after the page has been created.
+ **Auto publish**: This is a setting probably most relevant for communities, but can ofcourse be used for any types of pages. If this option is selected a new page is always published automatically. It's only applicable when a new page is created, not when it's updated.
+ **Page types**: Select which of the page types that should be available for an editor to select when creating a page in this page collection. It can be local page types or tenant page types. Tenant page types are indicated by the text "(Tenant)". For more information, see this page: :doc:`Tenant page types </admin-settings/tenant-settings/webcontent-managament/page-types/index>`. 
+ **Publishing policies**: Available in Omnia 7.8 and later. Prompts set up under "AI features" in Omnia admin can be available for page authors to use, to let AI review a page before publishing. 
+ **Automatic page creation**: A copy of a page can be published automatically to another page collection or another tenant, when certain rules are met. For more information, see this page: :doc:`Automatic page creation </pages/automatic-page-creation/index>`
+ **Promotion channels**: You can configure promotion channels to send teasers to Microsoft Teams, Viva Engage, and via Email - for example to use in a publishing campaign. For details, see below.
+ **Viva Engage integration**: When Viva Engage (former Yammer) integration is setup, a post will be created in the selected Viva Engage community whenever a new page, matching the selected criteria, is created. See below for more information.
+ **Taxonomy connection**: When this option is activated, it's possible to connect the page collection to a taxonomy. Whenever a page is created in the page collection, a term will be created in the connected taxonomy and the page will automatically be tagged with the newly created term. This can, for example, be useful in different rollups. For more information, see below.
+ **Approval**: (Called Publishing approval in Omnia 7.10 and later). If approval should be needed for publication of pages (new pages and updates), enable this. If not enabled, editors can publish directly. See more info about approval settings below.
+ **Deletion approval**: Available in Omnia 7.10. Works the same and has almost the same settings as publishing approval (see below), but for page deletion. The only difference is that multistep approval is not availble for deletion approval. When a page deletion has been approved, the page is also removed from the archive.
+ **Activities**: For a community, activity tracking can be activated. See the heading *Settings for activity points* on this page, for more information: :doc:`Setting up a community </using-communities/settings/index>` 
+ **Notifications**: This setting defines when a notification that a page is new should be shown for users, for example in the Notification panel. Normally it's only when the page is created, not when it's updated. If this option is activated the page is considered to be new every time it's updated and a new version is published. Therefore it's probably more relevant for pages in communities than for publishing pages.
+ **Send as Email**: Select "Enable send page as Email" if pages in the page collection should be available to send through Email. One example of when this is needed is in a Newsletter inplementation. If this option is activated, authors can decide to send the new or edited page by email, or decide not to, each time the page is published.
+ **Scheduling**: If scheduling should be available in this page collection, select this option and select the property to be used. The author can then set a scheduled start date and time, using the PROPERTIES tab for the page. Note that scheduled publishing never is mandatory, an author can always choose to publish without using scheduling. 
+ **Break permission inheritance by default**: Select this option if inheritance should be broken when a new page is created within the page collection. This could, for example, be useful for communities. When this option is active, the colleague creating the page will be the page owner, meaning that he or she has full control over who can edit. The new option "Invite co-authors" can then be used to easily add authors for the page, see below.
+ **Allow invitation of co-authors**: If this option is selected, authors can invite co-authors. 
+ **Channel**: If you enable "Enabel publishing to channels", it will be possible for an author to select channels the page should be published to. Publication to a channel may require approval from the channel administrator. See more information below.
+ **AI generated content**Open AI**: (This option is called "Open AI" in Omnia 7.7 and earlier). When you activate this option, if available, you can set properties for what the AI should be able to work with, see below. Also note that tenant features must be activated for this option to be available and settings for AI have to be made in Omnia Admin.
+ **Semantic search**: Can be available in Omnia 7.8 and later (a tenant feature must be activated). It's applicable for all pages in the page collection, but note that if there are existing pages when you activate this option, these pages have to be re-published to be indexed for semantic search. 
+ **Enable page checker**: Available in Omnia 7.10 and later. This is a validation for accessibility you can select. When you preview the page (Preview mode), you can receive a warning if there are any accessibility issues. See this page for more information: :doc:`Accessibility check when editing pages </pages/accessibility-check/index>`

**Note!** A prerequisite for semantic search is SharePoint sync. It's needed to be able to index page collections. Also see *Important notes about semantic search* below.

Set default values for a page type
--------------------------------------
You can set default values for the page types that has been added to the page collection. Any changes you do applies to the active page collection only.

1. Click the pen for the page type.

.. image:: page-type-default-pen.png

The default setting is that the settings are inherited from the tenant setting.

2. Deselect a settings to change it.

.. image:: page-type-default-deselect.png

3. Set a new default value for the page type, using the field that becomes available.

.. image:: page-type-default-setnew.png

Don't forget to save your changes.

Setup a promotion channel
-----------------------------
**Important note!** When using scheduled publishing for a page, a post from a promotion channel can not be published to Microsoft Teams or to Viva Engage.

Do the following to set up a promotion channel:

1. Click the plus.
2. Use the following settings:

.. image:: publishing-channels.png

+ **Name**: Add a name for the promotion channel here.
+ **Posting rule**: You can choose that a teaser for a new page in this page collection should always be published in this promotion channel, or you can set up rules for publishing. More information about this below.
+ **Type**: Can be Microsoft Teams, Viva Engage or Email.
+ **Group**: Select which group the promotion channel is tied to. If you selected Microsoft Teams, it's a list of Teams groups and so on.
+ **Channel**: For a Microsoft Teams group, several Teams channels can exist. Select channel here. (Not available for Viva Engage or Email).
+ **Property mapping**: The properties used for the teaser are listed here (properties in the image above is an example). Map properties you use for these purposes.

3. To set a posting rule, first select "Only post if".
4. Then select property, make other choices if necessary, and click ADD.

.. image:: promotion-property-add.png

In this simple example, a teaser should only be published to this promotion channel if the news type is Product News.

You can add several posting rules if needed, to further limit what will be published.

(Don't forget to save when you're done).

Setup Viva Engage integration for the page collection
-------------------------------------------------------
The Viva Engage (former Yammer) integration you can set up here is a one way integration; from Omnia to Viva Engage. A prerequisite is that the Feature "Viva Engage integration" is activated in Omnia admin (Tenant level).

To set up Viva Engage integration, do the following:

1. Select "Edit" to edit the settings.
2. Click the cogwheel for "Viva Engage integration".

.. image:: viva-integration-cogwheel.png

3. Use these settings:

.. image:: viva-integration-settings.png

+ **Viva Engage group**: Select a Viva Engage group to intergrate this page collection with.
+ **Initial properties**: Select the properties used on pages for Title, Summary and Content.
+ **Page creation rule**: Select if a Viva Engage post should always be created when a page is added, or only according to certain rules.

4. Save when you're done.

To set up rules, do the following:

1. Select "Only create if*.
2. Click ADD to add a rule.
3. Select a property.

.. image:: viva-integration-property.png

4. Add settings for that property as needed.

By using settings in the Page likes and comments block, you can set up a two way Viva Engage integration. Note that you must set up the integration here first.

For more information, see: :doc:`Page likes and comments block </blocks/page-likes-and-comments/index>`

Enable taxonomy connection
---------------------------
When you enable taxonomy connection, select a taxonomy from the list.

.. image:: page-collection-settings-taxonomy.png

When you have done that every new page in the page collection creates a term in the selected taxonomy, based on the title of the page. The newly created page is automatically tagged with the new term.

**Note!** If you change a title of a page, the term for the page is NOT changed automatically. If you would like to change the term as well, you have to do that in the term set manually.

**Also Note!** You must see to that the editors/authors that will create pages in this page collection has permissions to create terms in the selected term set.

Settings for approval
----------------------
When approval is activated, the following settings are available:

.. image:: page-collection-approval-settings-v79.png

+ **Apply to authors only**: If you select this, editors never need approval, they can always publish directly. When an author publishes, approval is needed.
+ **Apply to new pages only**: When this option is selected, only creating new pages needs approval, not when updating an existing page.
+ **Multi step approval**: Normally, when this option is not used, only one colleague can approve a page. When this option is used, a number of steps for approval can be set up, meaning several coleagues can need to approve a page. For more information, see below.

When approval is activated, you can select who can approve the creation of a page this way (also used in the multi step approval settings, see below):

+ **Anyone**: The author can select any colleague as approver when a page is published. See below for more information.
+ **Limited list of people**: You define the approvers using the field shown (see below). You can define one or more approvers but only one approval is needed each time, from any of the approvers.
+ **Based on person property**: You select property from the list shown (see below).
+ **Term driven**: Authors can select approvers from a defined list only. Which approvers will be available depends on the properties selected for the documents. You select the term(s) here. When you have selected one or more terms you can use the cogwheel to set approvers for individual terms in the set.

When "Anyone" is selected the following is shown when an editor sends the page for approval:

.. image:: approval-anyone-new.png

The author adds the approver to the field "Approver", types a message and sends the approval request.

When selecting "Limited list of people", you add approvers by typing their names in the field displayed:

.. image:: limited-list-79.png

Authors can then only choose between the colleagues in the list when selecting approver.

When you select "Based on person property", you open the list and select property. Normally just one or two properties are available. Page contact is an example of a field that can be relevant, if such a property is set up.

.. image:: based-on-person-new.png

Based on person property can result in more colleagues being available for approval. Authors can only choose between these colleagues when selecting approver.

For more information, see this page: :doc:`Properties </admin-settings/tenant-settings/properties/index>` 

For Term driven, you first select a term, then click the cogwheel.

.. image:: term-driven-cogwheel.png

Then select the colleague or group that should be available for approval for the term.

In this exeample Robert Johnson is set as approver for all object types (the parent). If you would like to select someone else to be avaialable as approval for, let's say News article, deselect "Inherit parent settings" and select colleague or group there.

.. image:: term-driven-cogwheel-approver.png

Setting up multi step approval
---------------------------------
When Multi step approval is selected, you set it up this way:

1. Click ADD STEP and set the following:

.. image:: multi-step-1-new.png

2. Add a description of the step in any tenant language.
3. Select who should be able for approval in this step. See above for information about the options.
4. Set the following:

+ **Use custom message**: Use this to customize texts, see below.
+ **Allow edit**: If this option is selected the "approver" can edit the page with the changes he or she sees as necessary and then approve for publishing, or send back with a comment (if send back is activated for that step). 
+ **Enable reject**: Select this option if publication could be rejected in this step.
+ **Enable send back**: If it should be possible to send back to previous approval step from here, select this option.

When you select "Use custom message" you can set the following:

.. image:: multi-step-custom.png

What you can use the fields for should be self explanatory. Also note that you can add button labels, and text for the Email, for different languages by clicking the flag.

5. Continue adding the needed approval steps the same way.

When you're finished it can look something like this:

.. image:: multi-step-2.png

To edit a step, just expand it and use the settings as described above. To adjust the order of the steps, use drag and drop. To delete a step, click the dust bin.

Don't forget to to publish to save your settings.

Allow invitation of co-authors
------------------------------------
If "Allow invitation of co-authors" is selected, an author can use this menu option to invite one or more co-authors:

.. image:: co-author-meny-79.png

(Available options in the menu depend on the settings for the page collection).

Note that this is not temporary, the co-authors will be added to the page permissions as authors.

For more information about inviting co-authors, see: :doc:`Invite co-authors </pages/invite-co-authors/index>`

Channel settings
-------------------
When you enable publishing to channels you can also choose that at least one publishing channel is required:

.. image:: channel-settings.png

I you select this there must be at least one channel selected when a new page is created in the page collection, or the the new page can not be saved.

Options for AI
-----------------------
When activating the AI option, the following settings are available for this page collection:

.. image:: open-ai-page-collection-79.png

+ **Summary**: To activate AI functionality for page summary, select the appropriate summary property here.
+ **Text**: Likewise for text fields, select property to activate AI functionality.
+ **Image**: Dall-E is an AI option that can be activated (a tenant feature) and is then available as an image provider in the image picker. Select the image property used to activate the functionality.
+ **Image ratio**: In Omnia 7.9 and later, you also select image ratio for the Dall-E image, when clicking the cig wheel. Here you can alos choose to use the image as background.

See the bottom of this page for information about how AI can be used in the RTF editor: :doc:`Editing text with the RTF Editor </general-assets/rtf-editor/index>`

Important notes about semantic search
---------------------------------------
To put it very simple, semantic search makes it possible to type search strings similar to the way you would ask a colleague. Even if you don't type the correct words, semantic search usually "understands" what you are looking for. The information must of course be available within Omnia. At the moment, semantic search can be available for pages (settings per page collection) and controlled documents (settings per document type). Other types of documents are not available for semantic search in Omnia, for now.

**Very important!** The semantic search will soon be developed further in Omnia but for now it does **not support security trimming**. Therefore, use semantic search only in page collections containing common information that anyone in the organization have permission to read. 

An additional way of restricting access to information gathered by semantic search, is to use the permission group available for tenant permissions. For more information, see: :doc:`Permissions for the tenant </admin-settings/tenant-settings/permissions/index>`

Saving page collection settings
********************************
To save the changes to the page collection settings, you need to publish. You can't save a draft, even if that option is present. 










