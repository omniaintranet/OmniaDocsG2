Recommended AI models
===========================================

Omnia uses Azure OpenAI model deployments created in Microsoft Foundry (formerly Azure AI Foundry). This page lists the recommended models and capability levels for new or updated Omnia installations.

.. note::
   Model availability varies by Azure region, deployment type, subscription and quota. Check the `current Azure model availability <https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability>`_ for your subscription before creating a deployment.

   Azure lets you choose a custom deployment name. Omnia expects the **deployment name**, not the model display name, in its model configuration. Use the deployment name you chose in Microsoft Foundry when configuring Omnia.

Recommended models
-------------------------------------------

.. list-table::
   :widths: 24 28 12 36
   :header-rows: 1

   * - Omnia use case
     - Recommended model
     - Capability level
     - Guidance
   * - Semantic search (LLM)
     - GPT 6 Luna
     - Efficient
     - Use this deployment in **LLM deployment name** for semantic search.
   * - Text completion and content analysis
     - GPT 6 Sol
     - Powerful
     - Use this deployment in **Text completion configuration**.
   * - Image generation
     - GPT Image 2.5 Flare
     - Powerful
     - Use this deployment in **GPT Image** configuration.
   * - Semantic search embeddings
     - Text Embedding Ada 002

       ``text-embedding-ada-002``
     - Capable
     - Generates the 1,536-dimensional vectors used by the current Omnia semantic search index. Use this deployment in **Embeddings deployment name**.

.. important::
   GPT-4-series models are no longer recommended for new Omnia deployments. Before migrating an existing text-completion or semantic-search deployment, confirm support for the recommended model in your Omnia version and feature, then validate the change in a non-production environment.

Omnia version compatibility
-------------------------------------------

Before using GPT 6 Luna or GPT 6 Sol, confirm that your Omnia version and the specific AI feature support the selected model and its generation parameters. This is especially important for semantic search.

Omnia 7.11.16 introduced support for GPT-5 models. Later model versions and individual AI features can have additional requirements, so check the release notes for your Omnia version or confirm compatibility with Omnia Support. Test custom prompts, content analysis and semantic-search answers before deploying the change to production.

Image model compatibility
-------------------------------------------

Use GPT Image 2.5 Flare for new image-generation deployments. Confirm that your Omnia version supports the model and select an image size supported by the deployment.

Embedding model compatibility
-------------------------------------------

Use Text Embedding Ada 002 (``text-embedding-ada-002``) for Omnia semantic search. The current Omnia search index expects 1,536-dimensional vectors, which matches this model's output.

Do not configure ``text-embedding-3-large`` with the current Omnia semantic-search implementation. Omnia requests the model's default vector size and expects 1,536 dimensions; ``text-embedding-3-large`` returns 3,072 dimensions by default. Supporting it requires an Omnia/index configuration change and a full reindex.

Changing an embedding model produces different vectors, even when the vector dimensions are the same. After changing the embeddings deployment, start a **Semantic Search Full Reindex** in Omnia Admin so all existing content is vectorized again.

Configure the deployments in Omnia
-------------------------------------------

After deploying the models in Azure:

1. Go to **Omnia Admin > Settings > AI features > Model configuration**.
2. Set **Text completion configuration** to the deployment name for GPT 6 Sol.
3. Under **Semantic search**, set **LLM deployment name** to the deployment name for GPT 6 Luna and **Embeddings deployment name** to the deployment name for Text Embedding Ada 002.
4. Set **GPT Image** to the deployment name for GPT Image 2.5 Flare.
5. Save the settings and validate each enabled AI feature.

For instructions on creating the Azure resources and deployments, see :doc:`Setup AI </setup/setup-ai/index>`.

Official model information
-------------------------------------------

Model names, availability and lifecycle status can change. See the following official documentation before deploying or upgrading a model:

* `Microsoft Foundry model catalog <https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure>`_
* `Azure OpenAI image generation models <https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/dall-e>`_
* `OpenAI model catalog <https://developers.openai.com/api/docs/models>`_
