Reports
==========

A number of reports are available for pages in the active publishing app. Note that some settings must be made for the reports to work, see below.

**Also note** that Title has to be set up as querable for pages, for anything to be shown in the reports.

Select "Reports" here:

.. image:: pages-reports-menu-new2.png

The following reports are available:

.. image:: pages-reports-all-new3.png

All reports can be exported to Excel by clicking here:

.. image:: reports-excel-new3.png

You can sort the lists on most column headings by clicking the heading, for example:

.. image:: reports-sort-new3.png

You can use the links in the "Page" column to go to a page, and the links in people columns (for example "Contact") to click the name to see more information about that colleague, for example contact information. The user profile card will then open, if it's used within your organization. If it's not, the colleague's Delve page will be displayed.

Also note that the icon on the lower right of a person image indicates Microsoft Teams presence. The icon in the image above indicates that Annabelle Dixon is offline.

Usage
*********
This list contains all pages in the Publishing App. You can filter the list by using the fields and lists at the top.

.. image:: reports-usage.png

**Important note!** The usage report can't show more than five million entries. When that limit is reached, a message is shown and the recommendation is to use Matomo analytics instead. 

For more information about Matomo analytics, see: :doc:`Analytics (Matomo) settings </admin-settings/business-group-settings/settings/analytics/index>`

Checked out
************
In this list you can see all pages that are currently checked out, meaning someone is working on them. New pages are shown here as well, even if they are not published yet, as long as a draft has been saved.

.. image:: pages-reports-checked-out-new3.png

Use the lists at the top to filter the Checked out-list.

Review
********
If a property for review date for pages is being used, this list displays all pages that has a review date set.

.. image:: pages-reports-review-new3.png

You can filter the list on Contact (Page contact). If the review date has passed, it's indicated by a black triangle, so in the example above, the page editors has a lot of work to do!
 
Pending approval
**********************
If approval for pages has been set up, this list will show all pages with pending approval.

.. image:: pending-approval-example-new2.png

(This image is from a test environment, these requests should normally not be that old.)

How to approve or reject here is described on this page, where you can find more information about approval: :doc:`Approve pages </pages/page-approval/index>`

Scheduled
***********
This report displays an overview of all pages that are scheduled for publishing, in the publishing app. Here's an example:

.. image:: pages-repoprt-scheduled.png

You can filter the list on dates, for a shorter list. Set Start Date and and End Date. You can also filter on page type and who the publication was scheduled by. 

Default is List view, as shown in the image above. You can also choose to see a calendar view, monthly or weekly. Here's an example with WEEK VIEW selected:

.. image:: pages-repoprt-scheduled-week.png

Analysis
***********
OpenAI can be used for content analysis. If set up, this tab is available.

**Note!** An analysis can only be executed on pages within the active page collection.

The first you will see is a list of already created analysis, if any. Here's a simple example:

.. image:: analysis-tab-v7.png

To remove an analysis that is no longer needed, click the dust bin, but remember that the report from the analysis can easily be updated, see below.

To read a report for the analysis, click the i-icon:

.. image:: analysis-i-icon-v7.png

Here's an example of a report:

.. image:: analysis-report-v7.png

You can execute the analysis on the latest version of a page by clicking here, in effect updating the analysis:

.. image:: analysis-report-again-v7.png

Create a new analysis
-----------------------
When you create a new analysis, the following settings are available:

.. image:: analysis-new-settings-new.png

+ **Content analysis**: A number of analysis settings to execute can be available in this list. They are set up in Omni admin, see: :doc:`Content analysis (OpenAI) </admin-settings/tenant-settings/settings/open-ai/content-analysis/index>`
+ **Text properties**: Select one or more text properties to run the analysis on.
+ **Pages to include in the report**: You must also choose one or more pages to run the analysis on. You can either pick pages, using the page picker, or use the query builder. Either way, only pages belonging to the active page collection can be selected.

If you select "Pick pages", click ADD Page to start the page picker. For more information, see: :doc:`Page picker </general-assets/page-picker/index>`

If you select "Use Query Builder", the following is shown:

.. image:: analysis-new-query-new.png

Add the query this way:

1. Choose "Dynamic" or the name of the page collection.
2. If you chose "Dynamic", select a token by clicking the i-icon.

.. image:: analysis-new-query-token.png

Note the description of the tokens in the column to the right.

3. Click ADD.
4. Repeat until all parts of the query is in place.

If you happened to add a query part you don't want, just click the dust bin to remove it.

5. Expand a query part for filter settings.

.. image:: analysis-new-query-filter-new.png

Doing so you can choose to run the query on specific pages only. Here's an example where the analysis should be executed on pages of the community types only:

.. image:: analysis-new-query-filtered-new.png

You can add several filters the same way, if needed.

6. Select status for the pages to be analyzed: Published, Never published or Any status (meaning both).

.. image:: analysis-new-query-status-new-border.png

7. Click ADD PAGE to add the pages for the query. If there are pages that corresponds with the settings, they are listed here:

.. image:: analysis-new-query-add-pages.png

Note that if no pages corresponds with the settings, no pages are listed (no message about that is shown). You have to add at least one page to be able to save the analysis.

If any of these pages should be removed from the analysis, just click the dust bin for the page.

8. When all is done, click SAVE to save the analysis. 

.. image:: analysis-new-query-save-new.png

Settings for reports
*********************
Two settings are needed for the reports to work.

A property for page contact has to have been set up in Omnia admin, and a property for review date, if review date will be used for pages.

Go to the publishing app aettings and the Advanced tab.

.. image:: reports-settings-new4.png

The correct properties must be selected here for the reports to work:

.. image:: reports-settings-lists-new4.png

