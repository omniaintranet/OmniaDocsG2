Secrets
=====================================

A number of settings are available under Secrets. Exactly what is available here depends on the implementation. Here's a common example: 

.. image:: tenant-secrets-v77.png

In Omnia 7.8 and later some options have been renamed and a few added:

.. image:: tenant-secrets-v78-new.png

System Account
------------------
System account is a standard extension for specialized implementations only, normally used by developers.

.. image:: tenant-secrets-system-account-v78.png

Connected tenants
------------------
This option is connected to the cross tenant publilshing functionality. The first list simply lists the other tenant this tenant is connected to, for example:

.. image:: secrets-connected-tenants.png

By clicking the pen, you can edit these settings:

.. image:: secrets-connected-tenants-edit.png

You have to communicate witth a tenant edmin to recieve the information you neeed for these two fields.

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

Azure OpenAI text completion configuration
--------------------------------------------
(Called AI features: OpenAI API in 7.8).

To be able to use AI text functionality within Omnia, the tenant feature "Text completion" must be activated. When that is done, an API key and an API base URL must be entered here

.. image:: azure-open-ai-secret-v77.png

AI features: AI search
------------------------
Available in Omnia 7.8 and later. In order for the "Semantic search" feature to work correctly, an Azure AI Search instance needs to be set up and it's read/write access credentials entered here.
 
.. image:: aifeatures-aisearch.png

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












