Analytics widget
=============================================

This block is used to display Matomo analytics data. Several blocks can be used on a page, with different settings, to display different aspects of the analytics data.

If you will be using the same filter settings in several widget blocks, it can save some time to set the filter settings in an Analytics filters block and connect the widget blocks to the filters block.

Pre requisite: To use Matomo analytics, the tenant feature “Analytics core setup” must be activated, and for a business profile, the feature “Create new analytics website in Matomo” must be activated. It's also important to start collecting analytics data as sooon as possible, as no historic data can be collected. For more information, see: :doc:`Analytics (Matomo) settings </admin-settings/business-group-settings/settings/analytics/index>`

To be able to view the contents of the block, users need the permission "Matomo users" (settings for the business profile).

**Note!** If using a connection to an Analytics filter block doesn't work on a section tab, you may have to disable Lazy load. See more information about this at the bottom of the page.

The following settings are available for this block:

.. image:: analytics-widget-block-77.png

General
---------
Here you can add a title for teh block, if needed.

.. image:: analytics-block-widget-general-new.png

Query
---------
Here you select web site and category, and when you have selected a category, you can also select widget. Here's an example:

.. image:: analytics-widget-query-77.png

+ **Websites**: Select the website to show analytics data for. In most cases, a "website" is the analytics data for a business profile.
+ **Category**: Select the category to display in the block.
+ **Widget**: Depending on category selected, one or more widgets can be available. Select the widget you want to use.

Display
---------
The following settings are available here:

.. image:: analytics-block-widget-display-new.png

**Note!** A preview is shown in the block so you can easily try out different combinations of settings.

+ **View in widget**: For some widgets, different types of views can be available. If there are, this field is available.
+ **Optional querystring**: For some widgets, adding a query string is possible, but never mandatory. In Matomo, optional query strings are used to identify and track various elements of website visits, such as specific pages, campaigns, or user interactions. For more information, use ChatGPT (Matomo documentation is fully accessible using ChatGPT).
+ **Height (in px)**: You can either set a height for the block in pixels, or choose to automatically adjust the height. If you choose the latter, this option is not available.
+ **Show scrollbars**: Select this option if you want that.
+ **Automatically adjust height**: Select this option if the height of the block should be adjusted automatically.
+ **Include footer in widget**: For a footer in the widget block, select this option.
+ **Disable links in widget**: Per default, widget objects can be clicked for more detailed information. If you don't want that, select this option.

Filter
---------
These settings are available:

.. image:: analytics-block-widget-filter-new.png

+ **Use filter connection**: An anlytics report block kan be connected to one or more widget blocks to use the filters set up in the Analytics filter block. If you want to use the filters from an Analytics filter block here, select this option and add the connection key from that block.Then you don't need to set any filter settings in this block. If don't select this option, you can add filter settings for this block, as shown in the image. 
+ **Period**: Decide if you want to display period, and if you do, select the period in the list.
+ **Period date**: Decide if you want to display period date, and if you do, select period date in the list.
+ **Properties**: Add the properties you want use here. Click the plus for a property you select to add it.
+ **No dimension filters**: This is just information. When no properties has been set up as dimensions, this message is shown. 

Decide which filters to display, by selecting "Show" to activate a filter.

(The message "No dimension filters" are always shown when no properties/dimension filters has been added).

Here's an example of a dimension filter property setting:

.. image:: analytics-widget-settings-filter-dimension.png

Style
---------
Here you can set some padding if needed:

.. image:: analytics-block-widget-style.png

Layout and Write
******************
The Write tab is not used here. The Layout tab contains general settings for blocks. For more information see: :doc:`General block settings </blocks/general-block-settings/index>`

An implementation example
****************************
Here's an example of a number of Anlytics widget blocks to display analytics data in different ways:

.. image:: widgets-example.png

Using the Analytics widget block on a section tab
****************************************************
There is a known problem that may occur when using the Analytics filter block on a section tab. If you would like to connect the Analytics widget block to a Analytics filter block, you may have to disable lazy load, or the connection won't work. This will eventually be fixed, but, for now, if you encounter this problem, simply disable lazy load. And to make sure, disable lazy load on all sections on the same levels as well, even if they don't contain an analytics block.

This settings is found under "Advanced" in the settings for the section. For more information, see: :doc:`Settings for sections </pages/page-types/section-settings/index>`

