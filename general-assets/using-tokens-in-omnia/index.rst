Using tokens in Omnia
=====================

Omnia supports tokens in several areas. Tokens are replaced with contextual values at runtime.

The lists below are examples and are not guaranteed to include every token available in all solutions or modules. Additional tokens can be added for specific scenarios.

.. note::
	Tokens and placeholders should not be translated.

Tokens in search queries
************************
You can use tokens in search category queries. At execution time, each token is replaced with a value from the current context (for example site, app instance, variation, or current user).

Examples of supported tokens:

- ``{User.Id}`` - Logged-in user login ID (usually email).
- ``{User.Name}`` - Logged-in user display name.
- ``{User.Email}`` - Logged-in user email.
- ``{User.Language}`` - User-selected language as ISO language code.
- ``{SPSite.Id}`` - SharePoint ID for the current site.
- ``{SPSite.FullUrl}`` - URL of the current Omnia page site.
- ``{Page.Id}`` - ID of the SharePoint folder.
- ``{Page.SPPath}`` - Full URL to the folder where the page is located in Site Pages.
- ``{Variation.Segment}`` - URL segment of the current variation.
- ``{TargetingProperty.PropertyTitle}`` - Targeting value(s) for the current user based on targeting property title (for example ``{TargetingProperty.Department}``).
- ``{AppInstance.InternalName}`` - App instance enterprise property value by internal name.

Example queries:

- Search only this site: ``Path:{SPSite.FullUrl}*``
- Search PDFs in my department: ``FileType:pdf AND RefinableString110:{TargetingProperty.Department}``
- Search pages in my language: ``FileType:aspx AND OmniaVariationSegmentOWSTEXT:{Variation.Segment}``
- Search current app instance property: ``RefinableString120:{AppInstance.YourPropertyInternalName}``

Tokens used with action buttons
********************************
You can use tokens in text fields for action buttons.

- App instance tokens, for example ``{{AppInstance.Title}}``
- ``{{Action.Type}}`` - Type of the button that was clicked.
- ``{{Action.Title}}`` - Title of the button that was clicked.

If supported by your WCM configuration, the following placeholders may also be available:

- ``{{Page.Id}}``
- ``{{Page.Title}}``

In document-based sign-off request scenarios, ``{{Document.Title}}`` is also supported.

Tokens in document rollups
**************************
Examples of tokens for document rollups:

- ``{{Document.FullUrl}}``
- ``{{Document.RelativeUrl}}``
- ``{{Document.FileName}}``
- ``{{Document.Title}}``
- ``{{Document.[InternalName]}}`` - Any enterprise property internal name (empty if the property is not included in the result set).

Tokens in emails
****************
For email tokens in Omnia, see: :doc:`Tokens in Omnia e-mails </admin-settings/tenant-settings/system/tokens-in-emails/index>`

Text field tokens and tokens for Matomo event tracking
*******************************************************
These tokens can be used in WCM text fields and for Matomo event tracking. Examples:

- ``{{AppInstance.Id}}``
- ``{{AppInstance.Title}}``
- ``{{AppInstance.Description}}``
- ``{{AppInstance.Url}}``
- ``{{User.Username}}``
- ``{{Page.Id}}``
- ``{{Page.Title}}``
- ``{{PublishingApp.PageCollections["UrlSegment"]}}``

Using placeholders in process management
****************************************
Placeholders are a special kind of token. They are properties wrapped in double brackets. When you print, placeholders are replaced with actual values, such as process title or date.

You can use these placeholders in the cover page, header, or footer. Short descriptions are available from the info icon in the UI.

- ``[[OPMProcessTitle]]`` - Adds the title of the printed process.
- ``[[OPMEdition]]`` - Adds the edition number of the printed process.
- ``[[OPMPublished]]`` - Adds the publication date of the printed edition.
- ``[[Comment]]`` - Adds publisher comments (if any).
- ``[[OPMProcessIdNumber]]`` - Adds the process ID number.
- ``[[OPMApprovedBy]]`` - Adds the approver name (if any) when published.
- ``[[OPMProcessType]]`` - Adds the process type name.
- ``[[OPMRevision]]`` - Adds the process revision number.
- ``[[EnterpriseInternalName]]`` - Adds the internal enterprise name for the process.

Using placeholders in document management
*****************************************
For document management placeholders, see: :doc:`Creating a document template with placeholders </admin-settings/tenant-settings/document-management/document-template-with-placeholders/index>`



