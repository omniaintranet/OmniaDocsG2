SharePoint page rollup
================================

In Omnia 7.12 and later, this block replaces Team news rollup.

**Work on this page has just started.**

The followig settings are availble:

.. image:: sharepoint-page-rollup.png

Use this block to show team news for the logged in user. 

General
**********
Under General, you can add a title for the block:

.. image:: sharepoint-page-rollup-general.png

Query
**********
You can either pick page or use the query builder.

Pick pages
--------------
If you choose to pick pages, the settings are the same as similar blocks:

.. image:: sharepoint-page-rollup-general-query-pick.png

+ **Pick pages**: To be able to pick some pages in Design mode, select this option.
+ **Pick pages in Write mode**: Select this option if authors should be able to pick pages in Write mode. **Note!** If you select this options, the ADD PAGE option is not available in the settings. 
+ **ADD PAGE**: When you have selected "Pick pages", you can pick some pages to always be displayed in the list. Click this option and use the SharePoint page picker. See this page for more information: (link to add)

Query builder
----------------
If you choose to use the query builder, you can choose to rollup all pages, with property filtering if needed, or rollup the pages in a specific SharePoint library:

.. image:: sharepoint-page-rollup-general-query.png

To rollup pages from a specific SharePoint library, add the URL to the site here, to list page libraries, and then select the library.

.. image:: sharepoint-page-rollup-library.png

To rollup all, or a part of all pages:

Use the three lists for base settings and the field to add a query parameter. 

.. image:: sharepoint-page-rollup-query-scope-settings.png

You use "Add" to add the settings to the Query field below. 

Note that you can type the script directly in the field, if you know how. You can use all options in the Keyword Query Language (KQL). See this Microsoft page for reference: https://docs.microsoft.com/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference

Additionally you can set:

.. image:: sharepoint-page-rollup-query-additional.png

+ **Day limit**: Use this settings for how old a news article should be to be displayed here. It's counted from the day it's published.
+ **Include legacy announcements**: If you're using the older Omnia solution for team announcements, select this option to show them here.
+ **Filter by followed sites**: If team news only from the sites the user follows should be shown, select this option.
+ **Filter by expiration time**: (A description will be added soon).

Display
---------
Here, the following can be set:

.. image:: sharepoint-page-rollup-general-display.png

General settings
------------------
+ **Row limit**: Decide the number of rows to show for each "page" of the list.
+ **View**: Select view for the list; "Card view", "Custom view", "Grouped by site" or "List".
+ **Order by**: Select what to sort the lists by.
+ **No result text**: If you would like a specific text to be shown when there are no news to display, add the text here, in any tenant language.
+ **Padding**: You can add some padding between the list and the block border if needed.

Card view
-----------
Has the following settings part from general settings:

+ **Description**: Add the property for the description of a card.
+ **Image**: Select the property that contains the image for the item(s) to display. Available for Card view.
+ **Date**: Add the property for the date shown on a card.
+ **Person**: Add the property for a person's name shown on a card.
+ **Term properties**: Can be used to show properties in Card view. Click "Add" and select a property. Continue the same way for additional properties.
+ **Cards per row**: As it says, set the number of cards to show per row. **Important note!** The card's placements are based on a grid with 12 positions. Therefore only numbers that is an integer part of 12 is available, for example 1,2,3,4 and 6.

Custom view
--------------
This is a custom list view. Select the column to show in the view. Note that you can se width for a colummn if needed, by clickning the cogwheel.

Grouped by site
-----------------
You can set general settings and:

+ **Force letter avatar**: If letter avatars always should be shown, select this option.
+ **Show thumbnail image**: If a thumbnail image should be shown for the news post, select this option.

List
---------
You can set general settings and:

+ **Show thumbnail image**: If a thumbnail image should be shown for the news post, select this option.

Filter
---------
The filter options are the same for most blocks, including this one. See this page: :doc:`Filter options for blocks </blocks/general-block-settings/filter-options-block/index>`

Layout and Write
**********************
The Write tab is not used here. The Layout tab contains general settings, see: :doc:`General block settings </blocks/general-block-settings/index>`

