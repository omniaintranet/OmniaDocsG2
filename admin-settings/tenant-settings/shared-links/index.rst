Shared links
=======================

Using Shared links a tenant administrator, (or any other user added in the permissions list, see below) can create links that users can access through "My links". It makes it possible to create a central list of links, in Omnia admin, to resources that are commonly used within the organization. 

Some links can be mandatory and it's also possible to target links to certain groups. 

These links can also be accessed through a Quick links block on any page, see: :doc:`The Quick links block </blocks/quick-links/index>`

There can be shared links specifically for a business profile. Such links are created and edited through the Shared links option under the business profile. Options for tenant shared links and business profile shared links are identical. Shared links for a business profile can coexist with shared links for the tenant.

**Note!** Do not delete or alter the links to Microsoft 365 applications, if present. They are needed for the app launcher menu in Omnia.

For information about how end users can use use My links, see: :doc:`My links</user-options/my-links/index>`

Settings
**********
In the list of shared links, click the pen to edit a link or the dust bin to delete a link.

.. image:: shared-links-edit-v78.png

When editing a link, all options available when creating a new link can be edited, see below.

Create a Shared Link
---------------------
Do the following:

1. Click the plus.

.. image:: shared-links-click-plus-v78.png

2. Set the following:

.. image:: shared-links-settings-v78.png

+ **Title**: The title is shown as the clickable text for the link. Note that you must always add a title in the default langauge, other languages are optional.
+ **URL**: The URL to go to when the user clicks the link.
+ **Category**: Links that are the same category will automatically be sorted together when the user chooses to display the categories. 
+ **Information**: This field can be used for additional information about the link. If you enter something here, an information icon is shown next to the link. Users can click the icon to read the information. Not mandatory. 
+ **Open in new window**: Select to open the URL in a new browser window. Normally a good idea for external links.
+ **Mandatory**: If selected, the link is always shown for all users (or the limited set of users, if targeted), and can not be deselected.
+ **Icon type**: An icon is always shown for a link. If you would like another icon for this link, select the set of Icons here: "Font Awesome", "Microsoft" or "Custom". When selecting "Custom" you can choose any image as the icon, using the media picker. For more information, see: :doc:`Using the media picker </general-assets/media-picker/index>`
+ **Icon**: When you have select icon type, use this list to select the icon. If you selected "Custom", an ADD ICON button is shown instead. Note the icon preview under the color settings.
+ **Icon color**: You can set a custom color for the icon, if you wish. You can't select color for a custom icon.
+ **Icon background color**: Set the background color for the icon here. If note set, default icon background color is used.
+ **Targeting filter**: Use these settings for targeting, for the link. 

Targeting a link works the same way as in many other parts of Omnia. See this page for more information: :doc:`Using Targeting </general-assets/targeting-in-omnia/index>`

Permissions for Shared links
*****************************
The Shared links option has a seperate permissions setting, so any user can be set as a shared links administrator. This includes external users that has been invited in Entra ID, meaning they can log in with their own Microsoft 365 account. 

For more information about permissions, see: :doc:`Permissions for the tenant </admin-settings/tenant-settings/permissions/index>`

Note that tenant administrators always can work with shared links.

