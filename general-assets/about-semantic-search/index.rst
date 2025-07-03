About semantic search
===================================

Semantic search can be available in Omnia 7.8 and later, depending on settings in Omnia admin. 

For users
**********
Semantic search is fundamentally different from classic search. To put it very simple, when searching, you can type a "question" similar to the way you would ask a colleague. Another important difference from classic search is that even if you don't type the "correct" words, semantic search usually "understands" what you are looking for. The information must of course be available within Omnia.

For developers and administrators
***********************************
Prerequisites: 

+ Sharepoint sync.
+ Activate the feature "Semantic search" (tenant level). 

You also must see to that there's a search category with the search provider "Semantic search" available for each business profile where you plan to use this functionality.

You can then decide for each search block to use semantic search or some other search provider by selecting search category.

For semantic search to work, pages and documents must be indexed. It's needed to be able to index page collections. Find these settings on page collection level for pages, and in document types for controlled documents. Semantic search does not work for other types of documents yet. 

**Very important!** The semantic search will soon be developed further in Omnia but for now it does **not support security trimming**. Therefore, the easiest way forward at this early stage, is to use semantic search only for common information that anyone in the organization have permission to read. 

Also, there's a permission group available where you can add the colleagues or groups that should be able to use semantic search. For more information, see: :doc:`Permissions for the tenant </admin-settings/tenant-settings/permissions/index>`

