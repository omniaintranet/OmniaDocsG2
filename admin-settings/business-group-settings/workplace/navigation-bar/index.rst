Navigation bar
=================

Here you can edit navigation bar settings for the business profile's workspace. You can add different settings for the default navigation bar and for the navigation bar used in MS Teams. 

You can use several mega menu objects and several action menu objects, if needed.

When working with the layout, you can use all the sections and blocks that normally are available for pages, so the possibilities are almost endless. You can even add different layouts for different screen sizes, if needed, to fit for example both computer and mobile phone.

Home settings
***************
Here you can edit the settings for the link to the workspace home page. 

.. image:: workplace-navigation-home-settings-new2.png

+ **Home title**: If you would like to show a Home title, add it here, in any tenant language. Then select "Show title" below.
+ **Icon type**: To show an icon, select icon type here. If you select "Custom" here, you can upload any image, using the media picker, to use as an icon. (If an icon type is seleted, but no icon is selected, no icon is shown).
+ **Icon**: To show an icon, select icon in the list. Then select "Show icon" below.
+ **Logo text**: If you would like to show a logo text by the home title, add it here, in any tenant language. 
+ **Show logo**: If a logo should be displayed, select this option. Note that you use ADD LOGO to upload the logo, see below.
+ **Show icon**: If an icon should be displayed, either an icon selected in the icon list, or one you have uploaded, select this option.
+ **Show title**: If the Home title should be displayed, select this option.

Note the separate settings for the home page in Microsoft Teams.

To add a Logo, do the following:

1. Click ADD LOGO.

.. image:: workplace-navigation-home-settings-click-add-new2.png

2. Use the media picker to find and select the image.

.. image:: workplace-navigation-home-settings-media-picker-new.png

See this page for more information: :doc:`The media picker </general-assets/media-picker/index>`

Don't forget to save when you're done.

Mega menu settings
************************
To open the Mega menu settings, click the cog wheel:

.. image:: workplace-navigation-mega-menu-settings-cogwheel-new.png

Separate settings are available for the default mega menu, and for the mega menu used in MS Teams.

.. image:: workplace-navigation-settings-mega-menu-new.png

+ **Show icon**: Select to show/hide navigation icons.
+ **Show text**: Select to show/hide mavigation texts.
+ **Max Wwdth**: You can set a maximum width in pixels for the navigation bar, if needed.
+ **Max height**: You can set a maximum height in pixels for the navigation bar, if needed.
+ **Layout theming**: If you would like to use custom settings for the layout, open this section and select "Custom theme". 
+ **Block theming**: If you would like to use custom settings for the layout, open this section and select "Custom theme". 

Layout theming are the same settings as are described here: :doc:`Layout theming </general-assets/layout-explorer/page-layout/layout-theming/index>`

Block theming are the same settings as are decsribed here: :doc:`Block theming </general-assets/layout-explorer/page-layout/block-theming/index>`

See below for information on how to add mega menu objects.

Action menu settings
**********************
To open the settings for the action menu, click the cog wheel:

.. image:: workplace-navigation-action-menu-settings-cogwheel-new.png

The following settings are available here, for the default action menu and for the action menu used in MS Teams (the action menu in MS Teams is not applicable in Omnia on-prem):

.. image:: workplace-navigation-settings-action-menu-new.png

+ **Show icon**: For the top action menu, showing an icon is default. If you add other action menus, you can choose to show icons or not.
+ **Show text**: For the top action menu, showing text is default. If you add other action menus, you can choose to show texts or not.
+ **Item limit**: Set the number of items that should be listed before a "Show more" link is shown.

See below for information on how to add action menu objects.

Adding a mega menu object
***************************
To add a mega menu object, click the plus:

.. image:: mega-menu-add-new-plus.png

and choose to add a layout or create a link.

.. image:: mega-menu-add-new2.png

Create layout
--------------
When you choose to create a mega menu layout, the following is shown:

.. image:: mega-menu-add-layout-new.png

1. Add a title in any of the Tenant languages, and an icon if you like. 

What you add here is only shown in the list of mega menus, not shown for users.

2. Click "Create".
3. Create the mega menu layout by using sections and blocks available in Omnia.

For more information, see *Working with the layout* and *Saving a draft and publishing* below.

Create a link
---------------
You can create a mega menu link to anything you can link to, for example a page in Omnia or external functionality.

Set the following for the link:

.. image:: mega-menu-add-link-new.png

+ **URL**: Add the URL for the link here.
+ **Title**: Add a title in any tenant language here.
+ **Open link in new tab**: If the link should be opened in a new tab, select this option.
+ **Icon type/Icon**: Add an icon for the link if you wish.

Mega menu object settings
---------------------------
Some settings are available for each mega menu object, here:

.. image:: mega-menu-select-settings.png

To edit them, click Edit:

.. image:: mega-menu-select-settings-edit.png

The follwing settings are then available:

.. image:: mega-menu-settings-edit.png

+ **Title**: You can edit the title for any of the languages.
+ **Icon type/Icon**: You can edit the settings for icon here.
+ **Inherit size from mega menu settings**: Per default, this object has the same size settings as the whole mega menu. If you want to set specific size settings for this object, deselect the option.
+ **Targeting**: Here you can set targeting for the mega menu object. See below for more information.
+ **A list of start URLs that will make the node selected**: This is a way of showing how different parts of the solution is connected. Any URL can make this node selected.

Here's an example:

.. image:: node-selected-list.png

And here's how OUR ORGANIZATION is selected when any of these options is active:

.. image:: node-selected-selected.png

Target a mega menu object
-------------------------------
When the mega menu object is created you can add a targeting filter, meaning you can decide who this mega menu object will be available for.

1. Select the mega menu object.
2. Open the settings (see above).
3. Click "Edit" if needed.
3. Add targeting filters.

.. image:: mega-menu-targeting-new.png

You do that the same way as for many other options in Omnia. See this page for more information: :doc:`Using targeting </general-assets/targeting-in-omnia/index>`

Adding an action menu object
******************************
The action menu can include almost any action available in Omnia. To add an action menu object, do the following:

1. Click the plus.

.. image:: action-menu-add-new.png

The following is shown:

.. image:: action-menu-add-settings-new.png

2. Add the settings.

+ **Action type**: Select action type from the list. Note that these actions are the same as can be added using an Action button block.
+ **Title**: Add a title for the action here. If it's a button this will also be used as the tool tip. **Important note!** If you use several languages as system language in your solution, you have to add the title in all languages, otherwise the tool tip will be in the main language only.
+ **Icon type/Icon**: Add an icon if you wish.

Different fields are shown depending on action type selected. See this page for detailed information about those fields: :doc:`Action button block </blocks/button-link/index>`

Action menu object settings
-----------------------------
In the settings for an action menu object, you can edit the settings you used when adding the object:

.. image:: action-menu-settings.png

Target an action menu object
-------------------------------
When the action menu object is created you can add a targeting filter, meaning you can decide who this action menu object will be available for.

.. image:: action-menu-add-settings-targeting-new2.png

You do that the same way as for many other options in Omnia. See this page for more information: :doc:`Using targeting </general-assets/targeting-in-omnia/index>`

Edit the order
****************
If you have created several objects of one type, you can decide in what order these objects should be shown for users.

Use this icon and drag and drop the desired order:

.. image:: action-menu-add-settings-order-new.png

Working with the layout
*************************
You start your work with the layout by adding sections and blocks, the way this page describes: :doc:`Working with layouts </general-assets/working-with-layouts/index>`

**A tip:** One way of creating a mega menu-like navigation is to use a page rollup, with scope "Navigation path" and "Navigation view".

Different layouts for different screen sizes
----------------------------------------------
In addition to the options described above, you can add different layouts for different screen sizes, if needed.

The default screen size is for computer screens. You can use the other screen sizes to check what the layout will look like in smaller sizes, and decide if specific layouts for other sizes are needed.

If you would like to add different layouts for one or more of the other scren sizes available, do the following:

1. Select Screen size.

.. image:: layout-screen-size-new.png

2. Open the list and select "Create new layout".

.. image:: layout-screen-size-new-layout-new.png

You work with the layout for the different screen sizes as described above.

