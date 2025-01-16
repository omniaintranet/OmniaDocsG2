Model configuration (AI)
=============================================

This description applies to Omnia 7.8.

**(This page is being edited).**

The following settings are available here:

.. image:: settings-ai-engine-all.png

Text completion configuration
*******************************
The following options are available here:

.. image:: settings-ai-engine-config.png

+ **AI alias**: Add the label to be used in the UI here.
+ **Deployment name**: Add the name for the deployment you are using. 

Semantic search
*******************
The tenant feature "Semantic search" must be active for this functionality to be available.

To put it very simple, semantic search makes it possible to type search strings similar to the way you would ask a colleague. Even if you don't type the correct words, semantic search usually "understands" what you are looking for. The information must of course be available within Omnia.

**Very important!** The sesmantic search will soon be developed further in Omnia but for now it does not support security trimming. Therefore, use semantic search only for common information that anyone in the organization have permission to read. If semantic search should be used can be set at page collection level for pages, and in document types for controlled documents. Semantic search does not work for other types of documents yet.

These settings are available for semantic search:

.. image:: settings-ai-engine-semantic.png

+ **LLM deployment name**: (A description will added soon).
+ **Embeddings deployment name**: (A description will added soon)

**Comment**: This has to be tested further, but it looks like you don't have to add anything here for a defaul setup.

