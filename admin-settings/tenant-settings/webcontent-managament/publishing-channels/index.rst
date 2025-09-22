Publishing channels
===========================

Here, you administer the publishing channels. They provide an alternative way of targeting information and to place pages in context.

If you enable publishing channels in a page collection, it will be possible for an author to set which channels the page should be published to. Normally approval by the administrator of the channel is needed for publication, but publishers can be defined for a channel and they don't need approval when publishing.

Publishing channels can be used in page rollups to show news articles and pages in different parts of the intranet. The end user can also subscribe to channels of interest. 

They are listed per publishing channels category. Here's an example with one category open:

.. image:: channels-list-v710.png

Click the pen to edit a channel, the dust bin to delete it. When you edit a channel, all settings used when creating a new channel can be edited, see below.

If any publishing to a channel that requires approval has been made, it's noted in the column "Waiting for Approval". The link there can then be clicked to handle the approval, see below.

Also note the search field at the top, where you can search for channels, if the list is long.

You can create and edit categories. See this page for more informaion: :doc:`Publishing Channels Categories </admin-settings/tenant-settings/webcontent-managament/publishing-channels-categories/index>`

Create a new channel
**********************
Here's how to create a new channel:

1. Click the plus.
2. Use the following settings:

.. image:: channels-settings-v710.png

+ **Title**: Add a title in any tenant langauge.
+ **Description**: Add a description of the purpose of the channel in any tenant langauge. 
+ **Category**: Add a category for the channel. If no categories are setup, the channel is automatically added to the default category. That category could be named General, or something else.
+ **URL**: Here you can add a Url to the channel's home page, if there is one. The home page can for example contain more information about the channel, a rollup of all pages published to the channel and so on. 
+ **ADD IMAGE**: To add an image to be shown for the channel, click here and use the Media picker to upload the image. When an image is selected you can delete it, or edit it by clicking the pen. For more information about the Media picker, see: :doc:`The Media Picker </general-assets/media-picker/index>`
+ **Owner**: One or more owners of the channel must be added. This is just information about who is responsible. The name/names will be shown when channels are listed.
+ **Administrator**: One or more administrators of the channel must be added. Administrators approve or reject publication to the channel. An administrator also has Publisher permissions to the channel.
+ **Publisher**: One or more publishers can be added. This is not mandatory. The colleagues you add here can always publish to the channel without approval.
+ **Force channel description to target group**: Targeting for the channel can be used to add a mandatory subscription to the channel for colleagues or groups. If you want to do that, select this option.
+ **Target channel to specific editors**: Available in Omnia 7.10 and later. Now you can target a channel to specific editors if needed.
+ **Add targeting filter**: Shown when any of the the options above is selected. Targeting settings are done the same way as in other places in Omnia, but the result is different. For the colleagues or groups targeted, a mandatory subscription to the channel is added. For more information about how to set up targeting, see this page : :doc:`Using Targeting </general-assets/targeting-in-omnia/index>`

3. Save when you're done.

Approve or reject publication
*******************************
If you're administrator of a channel, you can approve or reject publication of pages to that channel, but note that any colleague added as "publisher" for the channel, can publish directly, without approval.

If one or more requests for publication are created, the number of request are shown in this column:

.. image:: channels-request-v710.png

To approve or reject:

1. Click on the number of pages for a channel, to start the process.

The requests for that channel are then listed, for example:

.. image:: channels-requests-listed-v710.png

2. Click the link for a page you want to check. The page is opened in a new tab.
3. Go back to the list and select APPROVE or REJECT.

An Email is sent to the requester with information about the result.

**General note**: For a user to be able to receive Emails, the acccount must be Email enabled.

More on how to use and work with channels
******************************************
See these pages for more information:

There's a block available to rollup publishing channels for easy access for administrators. See this page for more information: :doc:`The Channel rollup block </blocks/channel-rollup/index>`

How to publish a page to a channel is described at the bottom of this page: :doc:`Publish page changes </pages/publish-page-changes/index>`

A list of pages belonging to one or more channels can be created using the Page rollup block: :doc:`The Page rollup block </blocks/page-rollup/index>`

Users can subscribe to channels, as described on this page: :doc:`My subscriptions </user-options/my-subscriptions/index>`

