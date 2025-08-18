Model configuration (AI)
=============================================

This description applies to Omnia 7.8 and later.

See this page for important information on how to set up AI in your tenant: :doc:`Setup AI </setup/setup-ai/index>`

The following settings are available here in Omnia 7.8:

.. image:: settings-ai-engine-all-78.png

In Omnia 7.9 settings for Dall-E are also available:

.. image:: settings-ai-engine-all-79.png

Text completion configuration
*******************************
The following options are available here:

.. image:: settings-ai-engine-config.png

+ **AI alias**: Add the label to be used in the UI here.
+ **Deployment name**: Add the name for the deployment you are using. 

Semantic search
*******************
The tenant feature "Semantic search" must be active for this functionality to be available.

**Very important!** The semantic search will soon be developed further in Omnia but for now it does **not support security trimming**. 

These settings are available for semantic search:

.. image:: settings-ai-engine-semantic.png

When you have created the services you need in Azure Open AI, you add services here.

+ **LLM deployment name**: Add the Large Language Model you will use in Omnia.
+ **Embeddings deployment name**: Add the name of the embeddings employment you have created.

For more information about semantic search, see: :doc:`About semantic search </general-assets/about-semantic-search/index>`

Dall-E
*******
Add the name of the Dall-E depolyment you're using here:

.. image:: dall-e-settings-tenant.png

Note, additional settings för Dall-E are available in business profile settings, see: :doc:`Dall-E settings (business profile) </admin-settings/business-group-settings/settings/dall-e/index>`




