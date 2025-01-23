Search config
=======================================

Here you can work with search categories and set default search template.

.. image:: search-config-list-new.png

To edit a Search config, click the pen. To delete a search config, click the dust bin.

Search categories
*******************
To create a new search category, click the plus and use the settings available for the Search Provider. All settings listed below.

.. image:: search-config-categories-4-new2.png

+ **Title**: Add a title for the aearch category, in any available languge.
+ **Search providers**: Select search provider for the category. The following is available: Comments, Shared links, SharePoint search and Microsoft search. **Note!** In Omnia on-prem only SharePoint search and Shared links can be used as search providers.
+ **Search result source**: Select Source from the list.
+ **Search query**: Add the search query here. Tokens can be used for a dynamic search query, see this page: :doc:`Using tokens in Omnia </general-assets/using-tokens-in-omnia/index>`
+ **Enable query rules**: Query rules can be set up in SharePoint. If these query rules should be used for this category, select this option.
+ **Enable partial word search**: Per default the search will onfly find whole words, so a search for Chris will find just that, not for example Christina. But if you select this option, the search will find parts of words as well, so both Chris, Christina and Christian, for example.
+ **Sort by**: Choose property to sort by, or you can choose to sort by Relevance or Popularity (at the bottom of the list).
+ **Sort direction**: When you have chosen a property to sort by, you can select a sort direction here.
+ **Search templates**: Select one or more search templates from the list.
+ **Targeting filter**: A search category can be targeted to a specific group of people based on the targeting system in Omnia. This setting will be used both in quick and advanced search. More information is found here: :doc:`Using targeting </general-assets/targeting-in-omnia/index>`

The same settings are available when editing a search category.

Search templates
*********************
Search templates are created by developers and are simply listed here. A search template defines how to display a search result. If a search result happens to not match any search template, the default search template is used. You can set default search template by clicking any of the templates in the list.

In this example the selected default search template is actually named that, but any other template can be selected.

.. image:: search-templates-new2.png

