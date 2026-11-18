Setting up a community
========================

Setting up a community is pretty straight forward. You need to be either tenant administrator or business profile administrator for the business profile where the community should be available.

You also need to have page editor permissions to a suitable page to set upp access to the community.

Prerequisite: The tenant feature “Communities” must be active for any community options to be available. Web content managament features must also be active for communities to work.

Creating a community
**********************
Do the following to create a community:

1. Go to Omnia admin.
2. Open "Communities" in the business profile settings.

The existing communities are listed (image from a test environment).

.. image:: communities-bp-712.png

3. If there are no templates available, you must create at least one, as describe here: :doc:`Templates for communities </admin-settings/business-group-settings/communities/communities-v7/templates/index>`. 
4. Create a community site according to the description on this page: :doc:`Directory of communities </admin-settings/business-group-settings/communities/communities-v7/directory/index>`
5. When the site has been created, you can use the link (Title) in Communities to go to the site. 
6. Setup access to the community some way, using the URL. (More information about that below.)

Setting up access to communities
**********************************
You set up access using the options available in Omnia. Here's an example using banners for access to the various communities available:

.. image:: communities-acccess-example.png

(MY SUBSCRIPTIONS is an action button in this example.)

This is just an example for inspiration. Access to communities can be set up many other ways in Omnia.

Settings for the community
*****************************
After the community has been created there are some settings you may want to do.

Settings for activity points
-------------------------------
You can select to award activity points for certain actions. When activity points is active, you can also choose to use badges, see below.

Activity points are counted within the page collection.

To enable activity points, do the following:

1. Go to the community and edit the start page.

.. image:: community-page-edit.png

2. Click "Edit".

.. image:: community-page-edit-click.png

3. Select "Settings", if it doesn't open automatically.

.. image:: community-page-edit-settings.png

4. Click "Enable activity tracking". and "Enable activity points". 

.. image:: community-page-edit-activity.png

5. Set the points that should be awarded to a user when creating a page (Knowledge page or Discussion page), updating a page etc.

.. image:: community-page-edit-activity-points.png

6. Publish the page.

.. image:: community-page-edit-publish-new.png

Using badges
--------------------
You can choose to award badges to users for reaching certain activity points levels. You must have activated activity points to be able to use badges.

Activity points for badges are counted within the publishing app.

To activate and create badges, do the following:

1. Go to the community and edit the start page.
2. Click "Edit".

.. image:: badges-edit-click.png

3. Open the page navigation, if it doesn't open automatically.

.. image:: badges-navigation.png

4. Click "Settings".  

.. image:: badges-settings.png

5. Click "Gamification".

.. image:: badges-gamification.png

6. Click "Enable Badges".

.. image:: badges-badges.png

7. Click the plus to create a badge.

.. image:: badges-badges-plus.png

8. Edit the settings for the badge.

.. image:: badges-badges-settings.png

+ **Icon type**: Select an icon type for the badge.
+ **Icon**: if you selected "Font Awesome", "Microsoft" or "Flags", use the list to select an icon.
+ **ADD ICON**: If you selected "Custom" above you can use any image as the icon. Click ADD ICON and use the Media Picker to select an image. When you have added an image it's shown here and you can edit it or remove it.
+ **Background color**: You can add a background color for the icon if you wish.
+ **Title**: Add a title (name) for the badge here.
+ **Description**: You can also type a description if you wish.
+ **Activity points required**: Set the number of activity points required to acquire this badge.

9. Click the tick to save the badge.

Here's an example of badges:

.. image:: badges-badges-example.png

The settings for the Ninja badge looks like this:

.. image:: badges-badges-example-ninja.png

Community page types
**********************
Two page types are installed when a community is created:

.. image:: communities-page-types.png

If you have page collection permissions you can edit these page types to your needs, the same way as you can edit any other page type, see: :doc:`Page types </pages/page-types/index>`


