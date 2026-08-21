Recommended AI models
===========================================

Omnia uses Azure OpenAI model deployments created in Microsoft Foundry (formerly Azure AI Foundry). This page lists the recommended model IDs for new or updated Omnia installations.

.. note::
   Model availability varies by Azure region, deployment type, subscription and quota. Check the `current Azure model availability <https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability>`_ for your subscription before creating a deployment.

   Azure lets you choose a custom deployment name. Omnia expects the **deployment name**, not the model display name, in its model configuration. We recommend using the model ID as the deployment name to make the configuration easy to identify.

Recommended models
-------------------------------------------

.. list-table::
   :widths: 24 28 48
   :header-rows: 1

   * - Omnia use case
     - Recommended model and deployment name
     - Guidance
   * - Semantic search (LLM)
     - GPT-5.6 Luna

       ``gpt-5.6-luna``
     - Optimized for efficient, high-volume workloads. Use this deployment in **LLM deployment name** for semantic search.
   * - Text completion and content analysis
     - GPT-5.6 Terra

       ``gpt-5.6-terra``
     - Balances intelligence and cost for more demanding generation and analysis tasks. Use this deployment in **Text completion configuration**.
   * - Image generation
     - GPT Image 2

       ``gpt-image-2``
     - The recommended image model for new deployments. Use this deployment in **GPT Image** configuration.
   * - Semantic search embeddings
     - Text Embedding 3 Small

       ``text-embedding-3-small``
     - Generates the 1,536-dimensional vectors used by the current Omnia semantic search index. Use this deployment in **Embeddings deployment name**.

.. important::
   GPT-4-series models are no longer recommended for new Omnia deployments. Before migrating an existing text-completion or semantic-search deployment, confirm GPT-5 reasoning-model support for your Omnia version and feature, then validate the change in a non-production environment.

Omnia version compatibility
-------------------------------------------

GPT-5.6 models are reasoning models and reject some generation parameters accepted by earlier chat models. Use them only after confirming that your Omnia version and the specific AI feature support GPT-5 reasoning models. This is especially important for semantic search.

Omnia 7.11.16 introduced support for GPT-5 models. Later model versions and individual AI features can have additional requirements, so check the release notes for your Omnia version or confirm compatibility with Omnia Support. Test custom prompts, content analysis and semantic-search answers before deploying the change to production.

Why GPT Image 1.5 is not recommended
-------------------------------------------

Omnia supports GPT Image 1.5 (``gpt-image-1.5``) and GPT Image 2 (``gpt-image-2``). GPT Image 1.5 requires limited-access registration in Azure, and availability varies by region and subscription. It is therefore **not recommended for new deployments**. Use GPT Image 2, which Azure lists as generally available.

With current Omnia image settings, select ``1024x1024`` for GPT Image 1.5 or GPT Image 2. The legacy ``512x512`` and ``256x256`` options are not valid for these deployments.

Embedding model compatibility
-------------------------------------------

Use ``text-embedding-3-small`` for Omnia semantic search. The current Omnia search index expects 1,536-dimensional vectors, which matches this model's default output.

Do not configure ``text-embedding-3-large`` with the current Omnia semantic-search implementation. Omnia requests the model's default vector size and expects 1,536 dimensions; ``text-embedding-3-large`` returns 3,072 dimensions by default. Supporting it requires an Omnia/index configuration change and a full reindex.

Changing an embedding model produces different vectors, even when the vector dimensions are the same. After changing the embeddings deployment, start a **Semantic Search Full Reindex** in Omnia Admin so all existing content is vectorized again.

Configure the deployments in Omnia
-------------------------------------------

After deploying the models in Azure:

1. Go to **Omnia Admin > Settings > AI features > Model configuration**.
2. Set **Text completion configuration** to the ``gpt-5.6-terra`` deployment.
3. Under **Semantic search**, set **LLM deployment name** to the ``gpt-5.6-luna`` deployment and **Embeddings deployment name** to the ``text-embedding-3-small`` deployment.
4. Set **GPT Image** to the ``gpt-image-2`` deployment.
5. Save the settings and validate each enabled AI feature.

For instructions on creating the Azure resources and deployments, see :doc:`Setup AI </setup/setup-ai/index>`.

Official model information
-------------------------------------------

Model names, availability and lifecycle status can change. See the following official documentation before deploying or upgrading a model:

* `Microsoft Foundry model catalog <https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure>`_
* `Azure OpenAI image generation models <https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/dall-e>`_
* `OpenAI model catalog <https://developers.openai.com/api/docs/models>`_
