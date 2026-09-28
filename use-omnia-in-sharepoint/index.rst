How to use Omnia in SharePoint
================================

In this section you will find documentation on how to use various parts of Omnia in SharePoint.

**The work on these pages has just started - there's a lot of new features and options in Omnia 7.12 that will be described here. More information will be added in the coming weeks.**

Webparts from Omnia in SharePoint
**********************************
This is an option that has been available for some time, and still is. There's a lot of useful blocks in Omnia. Some of them can be used as webparts on any SharePoint page. Find them in the tenant settings in Omnia admin here: System > Microsoft 365 > Webparts

How to use the Omnia webparts is described on this page: :doc:`Webparts </admin-settings/tenant-settings/system/microsoft-365/system-webparts/index>`

In Omnia 7.12 a new concept has been launched, with considerably added possibiblites to use Omnia functionality in a SharePoint set up, see below.

Using the same font
*********************
In Omnia 7.12 and later the font that has been configured in SharePoint can be applied to Omnia as well. (In Omnia up to 7.11, only the default SharePoint could be used in Omnia).

Activate this feature for each publishing app where it should be used:

.. image:: sharepoint-font-feature.png

Automated user activity tracking on SharePoint pages via Matomo
****************************************************************
Activity tracking via Matomo can be activated for any publishing app:

.. image:: sharepoint-matomo-feature.png

For more information about Matomo analytics, see page: :doc:`Analytics (Matomo) settings </admin-settings/business-group-settings/settings/analytics/index>`

Omnia 7.12 and later and SharePoint
*************************************
Omnia 7.12 introduces several improvements that bring Omnia and SharePoint Online closer together. These features allow users to access, navigate and work with Omnia content directly within SharePoint, creating a more consistent experience across both platforms.

The full page experience
-------------------------
The full page experience introduced in SharePoint is meant to be used with Omnia page rollup. The intended use is to show and present news articles in the Omnia rollup inside SharePoint and can show the full page on a SharePoint page. It is configurable to allow edit of the Omnia page inside SharePoint.

Enabling the full page experience
----------------------------------
To use the Omnia full page experience a feature needs to be enabled in the publishing app settings. When enabling, the feature will create a page called Omnia.aspx on the behind SharePoint site page library. This page provides the host for displaying Omnia pages inside SharePoint.

1. Enable the feature.

.. image:: full-page-feature.png

2. Go to Default rendering in Omnia admin and select the publishing app or site used for the full page experience.

Default rendering is found at business profile level under Settings.

.. image:: default-rendering-setting.png

The app instance shown is, as the text states, a fallback. Find sites where the feature has been activated by opening the list.

(To be continued)

