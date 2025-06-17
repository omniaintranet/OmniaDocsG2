Directory for publishing apps
================================================

Within a business profile several publishing apps can be active for different settings. To be able to create a publishing app, at least one template for that purpose must be available. If none are, create a template first.

(Images from Omnia 7.9 in this description).

Here you will see a list of publishing apps in the business profile, for example:

.. image:: publishing-apps-apps-v79.png

Use this icon to close the menu to the left and work in full window mode:

.. image:: publishing-apps-icon-v79.png

You can click the link to go to an app. You can search for an app and use the headings "Title", "Template" and "CreateddDate" to sort the list in Omnia 7.7 and earlier, "URL" and "Created date" in Omnia 7.8 and later.

The following actions, using the dot menu to the right, are available for an app:

.. image:: publishing-acstions-v79.png

For more information, see below.

**Note!** To be able to delete a publishing app, you must be app administrator for that publishing app. 

Attach site
**************
This option can be used in a rare setup case. If your organization creates SharePoint communication sites some other way, they can be attached to Omnia using this option.

**Note!** The communication sites attached this way should be empty, meaning just created but no content (pages or other content) added. The actual usage of the communication sites should be through Omnia.

The following permissions are required to be able to attach: Collection administrator permissions.

Do the following to attach a site:

1. Copy the URL for the communication site you want to attach.
2. Select ATTACH SITE.

The following is shown:

.. image:: publishing-attach-v7.png

3. Paste the URL and click RESOLVE.

You can "detach" (delete) a site if needed. Then the following permissions are needed: Site owner or Site collection administrator permissions.

**Note!** What actually happens when you click the dust bin to delete a site, is that the site is detached. That is true for all communcation sites, regardless of if they have been created in or attached to Omnia.

**Note!** When a site is detached, an Email is sent to the site owner(s). Note that, for a user to be able to receive Emails, the acccount must be Email enabled.

Create a new publishing app
*****************************
Do the following:

1. Click CREATE NEW.
2. Select a template (examples).

.. image:: publishing-app-template-v7.png

3. Use the following settings:

.. image:: publishing-app-template-settings-v7.png

Available settings depends on how the template is set up. Here are some common examples:

+ **Title**: Add a title for the publishing app.
+ **Description**: Add a description if needed.
+ **ADD IMAGE**: The editor setting up a rollup can choose to show images for the apps, both for List and for Card display. Here you can select an image to be shown there, using the media picker. When an image has been selected it can be deleted or edited using the X and the pen that is shown then.
+ **Show in public listings**: If a link to the app should be available in public listings (meaning listings in Omnia) select this option. If this option is deselected, the app can only be reached by specific links, for example in a workspace navigation.
+ **Default view access/Limit view access**: If you select “Limit view access” you can change view permissions for the app to specific users.
+ **Alias**: The last part of the address to the site is created automatically but can be edited if necessary. If the name (address) already exists an alternative address is suggested.

4. Click "Next" and use the following settings:

.. image:: publishing-apps-settings-v7.png

+ **App administrators**: The active administrator (you) is automatically added as app administrator. Add or delete administrators as needed. There must always be at least one.

3. In the last step, Summary, you can check the settings you have made, and edit them if necessary.

4. When you're done: click CREATE or SEND FOR APPROVAL, depending on how the temnplate is set up.

.. image:: publishing-apps-settings-create-v7.png

Edit settings for a publishing app
************************************
Using the action EDIT you can edit the settings for a publishing app. What can be edited can depend on the template used. Here's an example:

.. image:: edit-publishing-79.png

+ **Sharepoint URL**: The app instance connected site's URL can be edited here, if needed. See additional information below.

A number of additional settings for a publishing app are available in the Settings menu when working with pages, see: :doc:`Publishing app settings </pages/page-settings/index>`

An important note about SharePoint URL
-----------------------------------------
For the apps that needs a SharePoint site, the URL to that site is shown in the field "SharePoint URL/alias". If, for some reason, the URL for the SharePoint site is edited in SharePoint admin, it must be edited in Omnia as well, or the Omnia app won't work. Beware that this is to be regarded as an advanced action and can cause problems. Be also aware that it can take some time, 10 minutes or more, before the new SharePoint URL is recognized by the system.

Edit alias
*****************
If it should be needed to edit the alias, you can do it as part of the actions:

.. image:: publishing-apps-app-route-v79.png

Edit permissions
*****************
If you need to add or remove administrator(s) for a publishing app, you can do it as part of the actions:

.. image:: publishing-apps-app-premissions-v79.png

Contributor permissions is needed for colleagues that should be able to add comments to publishing pages.

Edit features
**************
If it's needed to upgrade a feature for the publishing app, you need to go to this part of the actions. You also go here to activate or deactivate a feature.

.. image:: publishing-apps-app-features-v79.png

For more information about a feature, expand it.

Pending approval
*****************
If approval for creation of an app is activated for the template, an administrator uses this list to work with approval or rejection. Here's an example from a test site:

.. image:: publishing-pending-approval-v79.png

To approve or reject, click the link and browse the settings. Under "Summary" you decide:

.. image:: publishing-pending-approval-approve-v79.png

If you click "Approve", the publishing app is created and the colleague requesting the approval is notified. If you click "Reject" you add a comment of what needs to be done before it can be approved:

.. image:: publishing-pending-approval-comment-v79.png

**Note!** Requesting an app must always be done from start each time. If rejected, nothing from the request is saved.

