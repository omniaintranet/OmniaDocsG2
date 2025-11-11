Permissions for the tenant
============================

The following settings are found here:

.. image:: security-tenant-v78.png

Users and groups
******************* 
Use this setting to add and remove tenant administrators and separate administrators for some areas, if needed. Only tenant administrators can use this setting. A tenant administrator can also edit all the settings for all business profiles within the tenant. (Image from Omnia 7.11).

.. image:: tenant-permissions-v711.png

To delete an administrator in any of the lists, just click the x. To add an administrator, add the name the same way as in other name fields.

**Note!** There must always be at least one tenant administrator. If there is only one, that administrator can not be removed until an additional administrator has been added.

In the field "Directory reader" all users that should be able to list users in Omnia must be added. Users not added here can't use the people picker or see a list of users in the People rollup block. Groups can be added here as well, for example "Internal users", for all internal users. This can be a way of making sure external users, or some other type of users, can't list all users.

If you see a field called "Username", as in the image above, it's a special case that can be necessary to handle when setting up a new tenant. As the user sync can't be executed until the tenant has been setup, you may need to add a tenant administrator in this field, in this special circumstance.

In the "Block gallery editor" field you can add additional users that should be able edit the block gallery. Available in Omnia 7.11 and later.

For more information on the people picker, see: :doc:`Using the people picker </general-assets/using-people-picker/index>`

The semantic search reader setting
--------------------------------------
Semantic search is an AI feature that can be available in Omnia 7.8 and later (if semantic search is activated in the tenant). Add the colleagues and groups that should be able to use semantic search. 
If a search block is set up with semantic search and certain users are not allowed to use the feature, they get empty search result if trying to use this search block. Also note that other permissions apply as usual. 

If pages or documents should be available for semantic search can be set at page collection level for pages, and in document types for controlled documents. Semantic search does not work for other types of documents yet.

**Very important!** The semantic search will soon be developed further in Omnia but for now it does **not support security trimming**. Therefore, semantic search should only be used for common information that anyone in the organization have permission to read, for now. 

This permission settings can be another way of restricting who can read information gathered by semantic search.

Secrets
********
A number of settings are available under Secrets. Exactly what is available here depends on the implementation. Here's an example from Omnia 7.11: 

.. image:: tenant-secrets-v711.png

Here are descriptions of some common secrets:

System account
------------------
System account is a standard extension for specialized implementations only, normally used by developers.

.. image:: tenant-secrets-system-account-v78.png

Connected tenants
------------------
This option has to do with to the cross tenant publishing functionality. The list simply displays the other tenants this tenant is connected to, for example:

.. image:: secrets-connected-tenants.png

By clicking the pen, you can edit these settings:

.. image:: secrets-connected-tenants-edit.png

Event Management service account
----------------------------------
If you will be using Event Management with a connection to calendars in Outlook, you must add the service account that will be used to read and write from the calendars in the tenant. (Don't forget that this account needs permissions to that calendar.)

.. image:: tenant-secrets-event-url-v78.png

Draftable account
---------------------
If you're using Draftable's solution for comparing changes in controlled documents, you may have to edit the information here.

.. image:: secrets-draftable-v78.png

A default base URL is added but can be edited if needed. 

SharePoint user profiles sync app-only
-----------------------------------------
In the process of enabling SharePoint app-only, Client ID and Client secret must to be added here.

.. image:: sharepoint-sync-app-v78.png

AI features: OpenAI API
--------------------------------------------
To be able to use AI text functionality within Omnia, the tenant feature "Text completion" must be activated. When that is done, an API key and an API base URL must be entered here

.. image:: azure-open-ai-secret-v711.png

AI features: AI search
------------------------
Available in Omnia 7.8 and later. In order for the "Semantic search" feature to work correctly, an Azure AI Search instance needs to be set up and it's read/write access credentials entered here.
 
.. image:: aifeatures-aisearch-711.png

Azure OpenAI Dall-E configuration
------------------------------------
(Called AI features: Dall-E in 7.8 and earlier).

To be able to use the Dall-E functionality within Omnia, the tenant feature "Dall-E" must be activated. When that is done, an API key and an API base URL must be entered here.

.. image:: dall-e-secret-v878-frame.png

**Important note!** The model version should be dall-e-3 and the deployment name needs to be “Dalle3” in Omnia 7.7, when setting up Dall-E.

Unsplash
----------
If your organization will use images from Unsplash, Application ID and Client ID received from Unsplash, must be entered here.

.. image:: unsplash-settings.png

reCAPTCHA
-----------
If you would like to use reCAPTCHA, you must enable it here and add a site key and a secret key.

.. image:: recaptch-v78.png

