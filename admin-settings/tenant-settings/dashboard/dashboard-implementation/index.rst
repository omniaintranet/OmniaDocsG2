Dashboard implementation example
==============================================

**This page is being edited. Will be finished soon.**

Here's an example of a Dashoboard set up:

.. image:: admin-dashboard-usage-76.png

Under Usage, information about active readers and active contributors are shown. What should be considered an active reader or an active contributor is defined in the Metrics settings, see: :doc:`Metric Settings </admin-settings/tenant-settings/settings/metrics/index>`

Note that, a metrics can normally be clicked for more details. Here's en exampl of the pages 

Under Pages, the following is availble:

.. image:: admin-dashboard-page-status-76.png

A number of tabs are available. What you see in the above example, is the total status for the tenant, on the Status tab. You can choose to see status for just one of the publishing apps. 
Besides that, a number of lists has been set up; Most Visited (All), Most Visited (Last month), Underused Pages, Statistics and Broken links.

.. image:: admin-dashboard-page-status-lists-76.png

Most visited (All) and Most visitied (Last month), lists pages, with the most visited at the top, for example:

.. image:: admin-dashboard-page-status-lists-vitited-76.png

This example is from a test environment. Unique users will be higher in a real environment.

Note that the link for a page can be clicked to go to that page.

For Underused Pages, something like the following can be shown:

.. image:: admin-dashboard-underused-pages-76.png

What should be considered underused content is defined in the Metrics settings, see link above.

Note the list to the right, of pages that has not been vsitied for a very long time. For more information on the lists, see below.

For News, this has been set up:

.. image:: admin-dashboard-news.png

Besided Status for news pages, a number of lists is available; Reach, Most Visited (Last month), Most Commented (Last month), Most Liked (Last month) and Statsitics:

.. image:: admin-dashboard-news-lists.png

Regarding Reach: How well we reach our target audience based on what we expect. The metric can be configured to a specific scope of pages (for example News pages) and have a target number of users. For nmore information on the lists, see below.

For Teamwork, you can see the number of active teamworks and if any has been created this week or this month:

.. image:: admin-dashboard-teamwork-new.png

In the image above, status for all Teamwork Templates are shown. You can also choose to see the status for just one of the templates, meaning all teamworks created from a certain template.

Finally, in this example, status for searches made by users can be shown:

.. image:: admin-dashboard-search.png

How it's done
-----------------
The basic layout in this implementation example is a tab section with six tabs:

.. image:: dashboard-example-tab-section-new-frame.png

The settings for the tabs are similar. Here's the first tab as an example:

.. image:: dashboard-example-tab-settings-new.png

For Style, "Show Active Slider" is selected so it's clear which the active tab is:

.. image:: dashboard-example-tab-settings-style-new.png

Usage settings
------------------
On this tab a Metrics block is placed, with the following settings:

Scope is set to "User Activity":

.. image:: dashboard-example-Usage-scope.png

The following Metrics are set up:

.. image:: dashboard-example-Usage-metrics.png

Pages settings
----------------
For Pages, a section is added, and the following tabs are set up there:

.. image:: pages-tabs.png

The settings for the tabs are similar to those for Usage, see above.

On the Status tab, a Metrics block is placed with the following setting for Scope:

.. image:: dashboard-example-tab-page-scope.png

And the following settings for Metrics:

.. image:: dashboard-example-tab-page-metrics.png

Most Visited (All) is a Page Rollup block, with the following settings for query:

.. image:: dashboard-example-tab-page-visitied-all-query.png

The Display is List View with the these settings:

.. image:: dashboard-example-tab-page-visitied-all-lisview.png

and these:

.. image:: dashboard-example-tab-page-visitied-all-lisview-2.png

Here's an example of the list:

.. image:: dashboard-example-page-visited.png

Most Visited (Last month) has similar settings, but of course showing the last month only. Here's an example:

.. image:: dashboard-example-page-visited-month.png
 
Underused Pages is placed in a section with two tabs:

.. image:: dashboard-example-underused.png

The settings for the tabs are these:

.. image:: underused-pages-tabs.png

On the tab to the left, there's a Metrics block, with the following settings for Scope:

.. image:: underused-pages-tabs-underused-scope.png

And the following Metrics:

.. image:: underused-pages-tabs-underused-metrics.png

To the right, a Page Rollup block is used to list the pages that has not been visited for a very long time, listing all pages with List View Display and two columnms, with the follwing sorting:

.. image:: underused-pages-tabs-underused-sorting.png

News settings
--------------
News is organized in a section with five tabs:

.. image:: dashboard-news-tabs.png

Status for News is set up with a Metrics block, with the following Scope:

.. image:: dashboard-news-tabs-status-scope.png

And the following Metrics:

.. image:: dashboard-news-tabs-status-metrics.png

The Reach tab is set up with two Metrics blocks, one for Corporate News and the other for Local News:

.. image:: dashboard-news-reach.png

Scope and Metrics for Corporate News are these:

.. image:: dashboard-news-tabs-reach-corporate-scope.png

.. image:: dashboard-news-tabs-reach-corporate-metrics.png

Scope and Metrics for Local News are these:

.. image:: dashboard-news-tabs-reach-local-scope.png

.. image:: dashboard-news-tabs-reach-local-metrics.png

Most Visited news last month is set up with a Page Rollup block with this query:

.. image:: dashboard-news-most-visited-month-query.png

The Display is List View with the following columns:

.. image:: dashboard-news-most-visited-month-display-frame.png

Sorting is by Page Hits: All users, and the Time Period is set to One month from today.

Here's an example of that list:

.. image:: dashboard-news-most-visited-month-example.png

Most Commented (Last month) and Most Liked (Last month) are set up in a similar way:

.. image:: dashboard-news-most-mostcommented-example.png

.. image:: dashboard-news-most-mostliked-example.png

They have both this set of columns (although in a different order):

.. image:: dashboard-news-most-commented-month-display.png

The two lists are differently sorted, the first on Comments and the second on Likes.

Finally, Statistics is a tab that can be used to se statistics for different types of news and during different time periods:

.. image:: dashboard-news-statistics-example.png

Note the possibility to export the shown list to Excel.

The following Query is set:

.. image:: dashboard-news-most-cnews-statistics-quesry.png

The following settings are used for Display:

.. image:: dashboard-news-most-cnews-statistics-display.png

and these:

.. image:: dashboard-news-most-cnews-statistics-display-2.png

Filters are set up this way:

.. image:: dashboard-news-most-cnews-statistics-filter.png

(No settings for Time Period).

Teamwork settings
--------------------
For this tab, the Scope is set to "Teamwork", with six Metrics:

.. image:: dashboard-example-tab-teamwork-new2.png

A filter is also added so users can choose the type of teamwork, based on template:

.. image:: dashboard-example-tab-teamwork-filter-new.png

Search settings
------------------
The Searech tab is set up with a Metrics block, with the folowing Scope:

.. image:: dashboard-example-search-scope.png

And the following Metrics:

.. image:: dashboard-example-search-metrics-new.png
