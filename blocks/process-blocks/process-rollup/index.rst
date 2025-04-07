Process rollup block
========================

Use the Process rollup block for a list of available processes. To display processes when a user clicks a process you don't have to set up specific pages if you don't want to. You can use the system page for processes that is always available.

Note that this block is found in the "Content rollup" catagory, not the "Process information" category.

Here's an example of a process rollup:

.. image:: process-rollup-block-example.png

The settings
*************
Use these settings for the block:

.. image:: process-rollup-block-settings-v78.png

Display
---------
The following settings are available for Display:

.. image:: process-rollup-block-settings-display-v78.png

Note that you have select List view for the options to show up, even if that's the only available view.

(All options are not shown in the image but described below.)

+ **Add column**: Add the columns for the information to be shown on the list. At least one column must be added or nothing will be shown.
+ **Adjust columns**: (Displayed when you are adding columns.) Use this option for the order in which the selected columns are shown, left to right.
+ **Fixed header**: Select this option for the header to always be shwon when scrolling. 
+ **Title**: If variatons exists for the page, you can only set the title in the default language. Titles in other languages are set in the variations. If no variations exists, it looks like in the image above, and you can add a title in any or all available languages. 
+ **View page URL**: If you have created a page that will be used to display any process when a user clicks on it, add the Url to the page here. Note that you don't have to create a page for this purpose. If you don't, a system page will be used.
+ **Open in a new window**: Select this option if the clicked process should be opened in a new window.
+ **Paging**: Select how paging should work; “No paging”, “Classic” or “Scroll”. 
+ **Item limit**: To limit the number of processes being displayed per "page", add a fixed number here. Works together with Paging.
+ **Sort by**: Select the property to sort the list by.
+ **Descending/Ascending**: Select Descending or Ascending sorting here.
+ **No result text**: To show a specific text when there is nothing to display in the rollup, add the text here.
+ **Padding**: Add some padding if nedded.

Query
---------
Select to display published processes or archived processes.

.. image:: process-rollup-block-settings-query-v78.png

If all published or archived processes should be available in the list, that's it, you don't need to actually add a query.

If just some of the processes should be displayed, add one or more queries this way:

1. Select property for the query.
2. Use the additonal settings available.

Here's an example:

.. image:: process-rollup-block-settings-query-example-78.png

Custom date filtering
^^^^^^^^^^^^^^^^^^^^^^^
If the scope is filtered on some kind of time property, custom date filtering can be set.

Here's an example:

.. image:: process-rollup-block-custom-date-78.png

See this page for more information about custom date filtering: :doc:`Custom date filtering </general-assets/custom-date-filtering/index>` 

Filter
------
Filter options are the same in most blocks, see: :doc:`Filter options for blocks </blocks/general-block-settings/filter-options-block/index>`

Layout and Write
*********************
The WRITE Tab is not used here. The LAYOUT tab contains general settings, see: :doc:`General block settings </blocks/general-block-settings/index>`

