List rollup
===================================

Available in Omnia 7.10 and later. Use this block to rollup data from SharePoint lists, especially custom lists. You can also aggregate data from several SharePoint lists for the rollup, using the query builder.

Settings
***********
These settings are available for the block:

.. image:: list-rollup-settings-all.png

More will be added to this description soon.

General
---------
As for most blocks, you can add a block title here if needed:

.. image:: list-rollup-general.png

Query
------
Decide to use the query builder or to just pick a single list. Here's the option for "Use query builder". You use it in a similar way to other Omnia rollups.

.. image:: list-rollup-query-query-new.png

If you decide to choose only one list, add the URL to the list here:

.. image:: list-rollup-query-list-new.png

Display
--------
For now, only List view is available. Note that you must still select "List view", even as there is just one option. Here's the available settings for List view:

.. image:: list-rollup-display-new.png

The following settings are available for the views:

+ **Add column**: This is not like columns in a table. You should think: What information do I want to display in the list? You must always add at least one column or nothing will be shown!
+ **Adjust columns**: Shown when adding columns. Use this option to set the order for the selected columns.
+ **Sort by**: Select the property to sort the list by.
+ **Paging**: Select how paging should work; “No paging”, “Classic” or “Scroll”. 
+ **Item limit**: To limit the number of items being displayed per "page", add a fixed number here. Works together with Paging. Also see the comment below.
+ **No result text**: If a specific text should be displayed when there's no items to show in the list, add the text here.
+ **Padding**: Use this option to add some padding between the list and the border of the block, if needed.

**Important note on "No paging"**: If you choose "No paging" and set "Item limit" to a specific number, that is the number of items that will be available in the list, regardless of how many that actually meets the search criteria.

Filter
-------
Filtering options are similar to other Omnia rollups.

.. image:: list-rollup-filter-new.png

For more information about filtering for blocks, see: :doc:`Filter options for blocks </blocks/general-block-settings/filter-options-block/index>`

Export
--------
Export to Excel can be available for users, if you select this option.

.. image:: list-rollup-export-new.png

When Export to Excel is active, you can set how the rows should be sorted, using "Sort by". 

You can also add columns as addition(s) to the standard columns. New columns are placed to the right. If you have added several extra columns, you can select ""Adjust columns" to set the order (left to right) among the new columns.

.. image:: list-rollup-export2.png





