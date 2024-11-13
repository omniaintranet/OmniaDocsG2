Sign-off requests rollup
=============================================

The block can be used for different purposes regarding sign-off requests for pages. In Omnia 7.7 and later, controlled documents can also be requested for sign-off. 

Settings for Sign-off requests are available in tenant settings: :doc:`Settings for Sign-off requests </admin-settings/tenant-settings/sign-off-requests-613/index>`

One way of using this block is a listing of sign-off requests that is sent to the logged in user or a group that the user belongs to. Here's an example:

.. image:: sign-off-block-example-77.png

The colored dots indicates the progress for the whole request, meaning the progress for all recipients: green for all has signed off, yellow for some and white for none.

A request contains one or more pages/documents to sign-off. In this example, the user has read and signed off seven of the posts, but has yet to read and sign-off two more.

.. image:: sign-off-block-example-signed-off.png

The user can read the information by clicking the link and can then sign off using a button. Here's two examples of how that button can look:

.. image:: sign-off-request-rollup-example-signedoff-77.png

Or:

.. image:: sign-off-request-rollup-example-signedoff-613-2.png

Of course, the user can also sign-off by simply ticking the box in the list.

It's also possible to "undo" a request, really meaning reading the information again. "Undo" is simply done by unchecking the box.

The other two scopes - "Requested by me" and "All requests" can be useful for colleagues creating requests. The "Requested by me" scope can be very useful to keep track of sign-off requests that a colleague has sent.

Signing off documents
-------------------------
In Omnia 7.7and later, controlled documents can also be part of a sig-off request. A single sign-off request can contain both pages and documents.

In this example, the first two posts are documents, the last one is a page:

.. image:: sign-off-both.png

(More info will be added soon).

Settings
**********
The following settings can be available:

.. image:: sign-off-requests-block-settings-613-border.png

The WRITE TAB is not used here. The LAYOUT tab contains general settings, see: :doc:`General block settings </blocks/general-block-settings/index>`

General
----------
On the General tab you can add a title for the block, of needed:

.. image:: sign-off-requests-block-settings-general-613.png

Query
----------
On this tab you decide what the block should display and for whom.

.. image:: sign-off-requests-block-settings-query-613.png

+ **Scope**: You can choose to display "All requests", "Requested by me", meaning all sign-off request the logged in user has sent, or "Targeted to me", meaning sign-off requests targeted to the logged in user, or a group the logged in user belongs to.
+ **(First list)**: Use the first list to set the type of query within the scope. 
+ **(Second list)**: Use the second list for further settings. An example: if you select "Progress status" in the first list, in the second list you can choose any or all of "Not started", "In progress" or "Completed".
+ **Add filter**: Add a filter for the query, if you don't want all the requests within the scope to be displayed. You can select "Requested by", "Progress status", "My progress status" or "Status". Additional filters can be available depending on the type used when the request was created. "My progress status" displays the status for the logged in user. For information about what the other default filters can display, see: :doc:`Requests </admin-settings/tenant-settings/sign-off-requests-613/sign-off-request-requests-613/index>`
+ **Page size**: To limit the number of items being displayed per “page”, add a fixed number here or use the slider.

Custom date filtering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In Omnia 7.7 and later you may be able to use custom filtering for the query for this block.

If the scope is filtered on some kind of time property, custom date filtering can be set.

Here's an example:

.. image:: sign-off-requests-block-custom-date.png

See this page for more information about custom date filtering: :doc:`Custom date filtering </general-assets/custom-date-filtering/index>` 

Display
---------
This tab contains settings for the view:

.. image:: sign-off-requests-block-settings-display-613.png

+ **View**: Can be "Summary view" or "List view". Summary view can only be used for the scope "Targeted to me". The image at the top of this page is an example of a summary view.
+ **Add column**: For List view you must add at least one column. Click this option to do that. For more information, see below.
+ **Display details in**: In a List view, a post can be clicked for further details. Here you set how the details should be displayed; in a dialog to the left or a dialog to the right. 
+ **Paging**: Avalailable for Summary view. Can be "No paging", "Classic" or "Scroll".
+ **Sort by**: Select what the view will be sorted by.
+ **Ascending/Descending**: Sort order is selected here, you know the drill.
+ **No result text**: If a text should be shown when the result of the query is empty, add the text here.
+ **Padding**: You can add some padding if needed, the usual way for a block.

When you add a column, first select the column in the list:

.. image:: sign-off-requests-block-settings-display-column-613.png

It's then possible to set a fixed width for the column, if needed, an decide to show the label or set a custom label.

If you need to edit the settings for a column, you can click the cogwheel to display them:

.. image:: sign-off-requests-block-settings-display-column-cogwheel-613.png

STYLE
--------
The following settings are available for filter style:

.. image:: sign-off-rollup-filter-style.png

