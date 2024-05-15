Analytics (Matomo) settings
=============================================

Pre requisite: To use Matomo analytics, the tenant feature "Analytics core setup" must be activated, and for a business profile, the feature "Create new analytics website in Matomo" must be activated. 

No set up at tenant level is required.

Analytics data is always collected separetaly for each business profile.

**Note!** All users that should have permission to see the analytics data must be added as Analytics readers: Business profil > Permissions > Users and groups > Analytics.

These settings are available for Matomo analytics, in a business profile:

.. image:: analytics-matomo-settings.png

+ **Matomo**: You can use the link shown here to go to the Matomo analytics page for this business profile.
+ **Enable data collection**: For Matomo analytics to work, this option must be selected. **Very important**: No historic data can be collected so it's important to enable this as early as possible, even before you have set up anyhting else regarding the analytics.
+ **Dimensions**: Here you decide what analytics data to store for users. See more information below.

Add and remove dimensions
**************************
To add a dimension, do the following:

1. Select the property.
2. In the dimension list, select "Create dimension". If the dimension is already created, you can map another property to it.
3. Click the plus.

To remove a dimension, just click the dust bin. **Important!** Read the note at the bottom carefully!

Here's an example of an analytics page. The dimensions set up in the image above are available here:

.. image:: analytics-matomo-settings-example.png

For more information about how to use Matomo analytics, see this page: https://matomo.org/help/

Blocks for analytics
***********************
Another alternative for displaying analytics is to use the two blocks for this purpose, see:

+ :doc:`Analytics filters block </blocks/analytics-filters/index>`
+ :doc:`Analytics widget block </blocks/analytics-widget/index>`

About Matomo marketplace
***************************
There are a lot of additional plugins, themes and more, that can be purchased/downloaded from Matomo marketplace (see link to Matomo above). If you decide to use any additions, just be aware that Omnia can not guarantee that these additions works as expected, and can not offer any support on the additions.


