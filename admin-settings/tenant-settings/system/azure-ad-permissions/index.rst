Entra ID permissions
=====================================

Here, a Tenant Administrator can see lists of all consented permissions for Omnia in Entra ID.

.. image:: azure-ad-permissions-all-v78.png

+ **CONSENT PENDING/CONSENT LINK**: If a feature is activated, that requires new consent for the app, the button says CONSENT PENDING. When consent has been given, the button says CONSENT LINC. the button can then be clicked if any changes in the consent is needed.
+ **INVALIDATE ALL USER TOKENS**: When permissions for Omnia has been changed, users needs to log out and log in for the changes to take effect. You can click this button to force a log out from Omnia for all users. More information on this below.
+ **Microsoft Graph**: Select to see a list of Microsoft Graph consented permissions for Omnia.
+ **Office 365 Sharepoint online**: Select to see a list of the permissions Omnia requests in Microsoft 365.
+ **Viva Engage**: Select to see a list of the permissions Omnia requests in Viva Engage.

Here's an example of the MS Graph list:

.. image:: azure-ad-permissions-graph-v78.png

More on Invalidate all user tokens
******************************************
If the button INVALIDATE ALL USER TOKENS is clicked to force a log out from Omnia for all users, only Omnia is affected, not SharePoint, Office apps, mail or anything else outside Omnia.

If an editor or author is working on a page in Omnia, the user will be logged out but if content is added to a page, even if it's not published, is automatically saved quite often, to minimize content lost.

