Using tokens in Omnia
=============================================

**This page is being edited.**

Here you will find a list of tokens that can be used in Omnia for various purposes. Note that tokens must not be translated.

Tokens in search query
***********************
Tokens can be used in the search category queries. Tokens will be replaced with values in context when the query is executed. This makes it possible to create context dependent queries based on the underlying SharePoint site, app instance or user properties.

Examples of tokens that can be used:

+ {User.Id} - Logged in user's login id (usually email).
+ {User.Name} - Logged in user's display name.
+ {User.Email} - Logged in user's email.
+ {User.Language} - User selected language as ISO language code.
+ {SPSite.Id} - SharePoint id for the current site.
+ {SPSite.FullUrl} - Communication URL of the current Omnia page.
+ {Page.Id} - Id of the SharePoint folder.
+ {Page.SPPath} - Full URL to the folder where the page is located in Site Pages. Example: (Path:{Page.SPPath}).
+ {Variation.Segment} - URL segment of the current variation.
+ {TargetingProperty.InternalName} - TermID of matching property of current user.
+ {AppInstance.InternalName} - TermID of matching property of current user.

Some examples of how the tokens can be used:

To search this site: Path:{SPSite.FullUrl}*

To search PDF:s in my department: FileType:pdf AND RefinableString110:{TargetingProperty.Department}

To search pages in my language: FileType:aspx AND OmniaVariationSegmentOWSTEXT:{Variation.Segment}

Tokens used with action buttons
************************************
The following tokens can be used in text fields when using action buttons:

+ AppInstance tokens like {{AppInstance.Title}} etc.
+ {{Action.Type}}: The type of the button that is clicked.
+ {{Action.Title}}: The title from the button that is clicked.

If possible (WCM dependent), the following placeholders may be used as well:

+ {{Page.Id}}
+ {{Page.Title}}

Tokens in document rollup
***************************
The following tokens cam be used in document rollups:

+ Document.FullUrl
+ Document.RelativeUrl
+ Document.FileName
+ Document.Title
+ Document.[InternalName]: Any enterprise property internal name. (Note! Empty value if the data is not available in the result set).

Tokens in e-mails
*******************
For tokens used in e-mails within Omnia, se this page: :doc:`Tokens in Omnia e-mails </admin-settings/tenant-settings/system/tokens-in-emails/index>`

Text field tokens and tokens for Matomo event trackning
********************************************************
These tokens can be used in text fields in WCM and can also be used for Matomo event tracking:

+ {{Appinstance.Title}}
+ {{Appinstance.Description}}
+ {{Appinstance.Url}}
+ {{Page.Id}}
+ {{Page.Title}}
+ {{PublishingApp.PageCollections["UrlSegment"]}}

Using placeholders in Process management
*****************************************
Placeholders are a special kind of tokens. They are properties added between double brackets. When you print, the placeholders are replaced by by actual data, for example the title for the process or a date.

You can use these placeholders in the cover page, the header or the footer. Short information about them is available through the i icon.

+ [[OPMProcessTitle]]	- adds the titel of the process printed.
+ [[OPMEdition]] - adds the edition number of the process printed.
+ [[OPMPublished]] - adds the date for when the edition printed was published.
+ [[Comment]]	 - if the publisher of the process added any comments, they can be displayed using this placeholder.
+ [[OPMProcessIdNumber]] - adds the id number for the process.
+ [[OPMApprovedBy]]	- adds the name of the approver (if any) when the process was published.
+ [[OPMProcessType]] - adds the name of the process type used for this process.
+ [[OPMRevision]]	- adds the revision number for the process.
+ [[EnterpriseInternalName]] - displays the internal name for the process.

Using placeholders in Document Management
******************************************
For tokens (placeholders) that can be used in Document Management, see this page: :doc:`Creating a Document Template with Place Holders </admin-settings/tenant-settings/document-management/document-template-with-placeholders/index>`

