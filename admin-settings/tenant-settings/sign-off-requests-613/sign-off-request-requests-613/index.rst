Requests
=============================================

All created requests are listed here, for example:

.. image:: sign-off-requests-requests-v77.png

The "Status" column indicates if the request is open or closed. the "Progress status" column to the right indicates the number of answers; white for none, yellow for some/ongoing and green for all that the request was sent to.

You can search for a request and you can filter the list on "Requested by" and "Progress status" (Not started, In progress or Completed).

For more details and the possibiblty to delete a request, click the link (title).

Create a new request
***********************
To create a new request, do the following:

1. Click the plus.

.. image:: sign-off-requests-click-plus-v77.png

2. The following is now shown:

.. image:: sign-off-requests-settings-1-v77.png

+ **Types**: Only available if more than one type has been set up, and is then mandatory. If just one type exists, it's used automaticalley and the settings for the type are available directly. The "Types" option is then not shown. 
+ **Template**: If more than one template has been added to the type, this option is shown and you must select a template for the the other settings to be shown. 

For more information, see:

+ :doc:`Types for sign-off requests </admin-settings/tenant-settings/sign-off-requests-613/sign-off-types-613/index>`
+ :doc:`Templates for sign-off requests </admin-settings/tenant-settings/sign-off-requests-613/sign-off-templates-613/index>`

When you have selected type, a number of settings are available, for example:

.. image:: sign-off-requests-settings-1b-v77.png

Some or all of these settings can be available for pages: 

+ **Name**: You can add a name for the request here. In some cases when you select a type, a code for the name is added automatically.
+ **Description**: You can add a description of the request here (recommended).
+ **Properties**: Available properties (if any) depends on the type used. The properties are useful for tagging the request. This can then be used as filters for what is to be displayed in a certain Sign-off requests rollup block. 
+ **To be signed off**: Here you add the pages that should be signed off, using the page picker. If the type was based on a template, the list of pages will most likely be pre populated with a number of pages. You can add or remove pages as needed. See below for more details.
+ **Sign-off type**: Choose how the sign-off request will be handled. If the type is based on a template, Sign-off type, and the following two fields can be pre populated with suggestions. If you select "Individual", all users added to "Request sent to" will receive a personal request. Everyone has to sign-off individually. If you select "Group", it works as one group request, meaning it's enough that any one of the recipients signs-off the request. All other recipients can see that the request was sent to them and can see if someone in the group has signed off, they can see if the task is done or not.
+ **Requested by**: Add one or more users, or groups, that will be shown as the "sender" of this request. Will be shown to the receivers. Your name will most lilkely be pre populated, but it can be removed. This field must always contain at least one person or group. To add several users or a group here can be useful, then all users, or the whole group, will be able to follow up on the request, for example through a Sign-off requests rollup on a suitable page. This field is mandatory.
+ **Request sent to**: If you selected "Indiviual", single users, security groups and Microsoft 365 groups can be added here (In Omnia on-prem, Microsoft 365 groups can’t be used). If you selected "Group", only groups can added to this field (of course). The field is mandatory. 
+ **Schedule send-out**: Select to set date, hour and minutes for when to send. You can also select the standard time to calculate on.

(For options for controlled documents, see below).

3. Add or remove pages/documents as needed.
4. Add a message for each page/document, if needed (for more information, see below).
5. Schedule the send-out if needed. 
6. Click SEND REQUEST to save the Sign-off request and send it. If you don't, nothing is saved.

To add or remove pages
----------------------------
Here's how to add or remove pages for a sign-off request. 

If you use a template, this list can be pre populated, for example:

.. image:: sign-off-requests-settings-2a-77.png

By clicking the pen, you can add a message for each page, if needed (not mandatory), in any tenant language. Here's an example:

.. image:: sign-off-requests-settings-2-77-message.png

To remove a page from the list, click the dust bin (this does not affect the template). To add additional pages, click the plus.

.. image:: sign-off-requests-settings-2-77-clickplus.png

The following is shown:

.. image:: sign-off-requests-settings-3-77.png

If you select "Current page" the actual page where the sign-off request is placed can be signed off, wherever that is, and no further settings are needed.

When you select "Specific page", continue like this:

1. Navigate and pick (Browse) or search for pages, the same way as in the page picker (it's a part of the page picker that is used here). See this page for more information: :doc:`The Page picker </general-assets/page-picker/index>`

2. Click ADD when you have selected one or more pages to add to the sign-off request.

.. image:: sign-off-requests-settings-3-77-pages-add.png

The selected pages are now added to the list of pages, see above.

3. Continue this way until you have added all pages that should be signed off.
4. Add specific messages for pages, where needed.

To add or remove documents
----------------------------
This option is available in Omnia 7.7 and later. You use it this way:

1. Select "Published document" at the top.

If you select "Current document", no further settings are needed, just click ADD.

If you select "Specific document", a list of all published documents in the tenant is shown, for example:

.. image:: sign-off-document-list-77-frame.png

2. Browse the list or search for part of or the whole document name.
3. Select one or more documents to be signed off.
4. Click ADD.

.. image:: sign-off-document-list-clickadd-77.png

(If you don't see the ADD button, scroll down to the bottom of the list).

5. Repeat the process til all documents for the sign-off request are added.
6. Set all other settings for the sign-off request as described for pages.

Checking up on a request
*************************
You can check up on a Sign-off request to see what has happened.

1. Click the link (Title) for the request.

Something like the following is shown:

.. image:: sign-off-requests-checking-1-613-new.png

Here you can see, for example, the status and the number of recipients that has completed the request. You can check the message (if any) for a page by clicking the pen.

For more information, you can click "Download details" to download an Excel file.

Additionally, you can send a reminder to all participants.

Close or delete a request
****************************
You can close a request that should no longer be active. You can delete a request no longer needed.

.. image:: sign-off-requests-checking-1a-613-new.png

When you close a request, you can choose to send an Email notification to the users that has not completed the request:

.. image:: sign-off-requests-checking-2-613.png

Just deselect if you don't need to send a message, and then click CLOSE REQUEST. If you choose to send a message, it's sent immediately.

It's just a notification Email that is sent from the system. You can't add any text to that message (no dialog for that purpose is available).

A closed request can be reopened, a deleted request can (of course) not.

Sign-off requests rollup block
*********************************
There's a block available to be used for listing the sign-off requests that is sent to the logged in user or a group that the user belongs to.

More information about the block is found here: :doc:`Sign-off requests rollup </blocks/sign-off-requests-rollup-613/index>`

