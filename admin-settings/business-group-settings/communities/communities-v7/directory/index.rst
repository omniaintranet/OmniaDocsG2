Directory of communities
=====================================

Within a business profile several communities can be active for different settings. To be able to create a community, at least one template for this purpose must be available. If none are, create a template first.

(Images from Omnia 7.9 in this description).

Here you will see a list of communities in the business profile, for example:

.. image:: communities-apps-v79.png

Use this icon to close the menu to the left and work in full window mode:

.. image:: communities-icon-v79.png

You can click the link to go to a community. You can search for a community and use the headings "Title", "Template" and "Created date" to sort the list, in Omnia 7.7 and earlier, "URL" and "Created date" in Omnia 7.8 and later.

The following actions, using the dot menu to the right, are available for a community in the "All" list:

.. image:: community-actions-v79-frame.png

**Note!** To be able to delete a community, you must be app administrator for the community and site collection admin for the site in SharePoint. Also note that deleting a community from this list deletes 
the connected Sharepoint site as well, which is different from publishing sites and teamwork sites.

For more information, see below.

Create a community
***********************
To create a community from here, do the following:

1. Click CREATE NEW.
2. Select template. 

Here's an example:

.. image:: community-template-v7.png

3. Add the information needed. All steps in the setup may not be needed for a certain template. Available settings depend on how the template is set up. Here's a common example:

.. image:: community-settings-v7.png

+ **Title**: Add a title for the community.
+ **Description**: Add a dscription if needed.
+ **Show in public listings**: If a link to the community should be available in public listings (meaning listings in Omnia) select this option. If this option is deselected, the community can only be reached by specific links, for example in a Workspace navigation.
+ **Default view access/Limit view acess**: If you select “Limit view access” you can change view permissions for the community to specific users.
+ **Alias**: The last part of the address to the site is created automatically but can be edited if necessary. If the name (address) already exists an alternative address is suggested.
+ **Languages**: The same language as the main business profile language is suggested. Another language can be selected if needed.  
+ **ADD IMAGE**: The editor setting up a community rollup can choose to show images for the communities, both for List and for Card display. Here you can select an image to be shown there, using the media picker. When an image has been selected it can be deleted or edited using the X and the pen that is shown then.

4. Click "Next" and use the following settings:

.. image:: community-settings2-v7.png

+ **App administrators**: The active administrator (you) is automatically added as app administrator. Add or delete administrators as needed. There must always be at least one.

5. The Properties step may be different in different templates, or maybe not be needed at all. Here's an example. Note that a star indicates if that the property is mandatory.

.. image:: community-settings-property-v7.png

When you click NEXT, a summary is shown, where you can click the pen the edit any of the steps.

6. Click CREATE to create the community or SEND FOR APPROVAL, depending on how the template has been set up.

.. image:: community-create-v7.png

Edit settings for a community
**********************************
Using the action EDIT you can edit the settings for a community. Available options depend on the template. Here's an example:

.. image:: edit-community-79.png

+ **SharePoint URL**: The app instance connected site's URL can be edited here, if needed. See additional information below.

An important note about SharePoint URL
-----------------------------------------
For the apps that needs a SharePoint site, the URL to that site is shown in the field "SharePoint URL/Alias". If, for some reason, the URL for the SharePoint site is edited in SharePoint admin, it must be edited in Omnia as well, or the Omnia app won't work. Beware that this is to be regarded as an advanced action and can cause problems. Be also aware that it can take some time, 10 minutes or more, before the new SharePoint URL is recognized by the system.

Edit alias
****************
If it should be needed to edit the alias (app route), Select "Alias" in the dot menu for the community and the following is shown:

.. image:: app-route-community-v79.png

Edit the alias and save.

Edit permissions
******************
If you need to add or remove owners (administrators) or contributors for a community, select "Permission" in the dot menu for the community.

.. image:: community-premissions-v79.png

Don't forget to save when you're done.

For more information on the people picker, see: :doc:`Using the people picker </general-assets/using-people-picker/index>`

Edit features
***************
If it's needed to upgrade a feature for the community, you need to go here. You also go here to activate or deactivate a feature. Available features can differ depending on how Omnia is set up. Here's an example:

.. image:: community-features-v79.png

For more information about a feature, expand it.

Pending approval
*****************
When a user creates a community where approval is needed, an administrator uses this list to approve or reject. Here's an example from a test environment:

.. image:: community-pending-approval-v79.png

Approval or rejection is done this way:

1. Click the link for the community.
2. Check the name, settings and so on.
3. If everything is OK, click "Approve", or if changes are needed, click "Reject".

.. image:: community-pending-approval-approve-v79.png

If you approve the creation of the community, a message is sent to the person requesting it, and the community is created.

If you reject, the following is shown:
 
.. image:: community-pending-approval-reject-v79.png

4. Type a message stating what needs to be done for approval, and click "Save" to send the message.

The person requesting the community receives the message and can then start a new community creation with your comments in mind. 

**Note!** Requesting a community must always be done from start each time. If rejected, nothing from the request is saved.


