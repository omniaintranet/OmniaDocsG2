Teamwork apps
=============

A Teamwork app is a workspace in a business profile - a SharePoint team site, a Microsoft 365 group, a Microsoft Team and so on - created from a Teamwork app template. For document management it is where the controlled-document library lives. The connector can create a Teamwork app template, create a Teamwork app from it, and list and activate the features of a Teamwork app.

.. TODO screenshot: a Teamwork app in the Omnia interface, for reference

What you can ask for
********************

+ Create a Teamwork app template.
+ Create a Teamwork app from a template.
+ List the features of a Teamwork app, with their current status.
+ Activate a feature on a Teamwork app.

Creating a template
*******************

A template needs a **title** and a **resource type** - what the apps created from it are backed by. If you leave out the resource type, the choices are offered as a list: SharePoint team site, Microsoft 365 group, Microsoft Team, Viva Engage (Yammer) group, Workplace from Meta group and SharePoint communication site.

::

   Create a teamwork app template called "Controlled Docs Team",
   backed by a SharePoint team site

You can also give it a description, make the apps created from it private, apply a SharePoint site design, and let the person creating an app choose its language and time zone.

.. TODO screenshot: Claude offering the resource types as a list

Creating a Teamwork app
***********************

A Teamwork app needs a **template** and a **title**. If you do not name a template, or name one that is not in this business profile, the templates that are there are offered as a list:

::

   Create a teamwork app named "Quality Management" from the Controlled Docs Team template

The site's **address is generated from the title** unless you give one. You are made the app's administrator.

.. TODO screenshot: Claude confirming the new Teamwork app

Features
********

::

   Which features are activated on the Quality Management team app?

::

   Activate a feature on the Quality Management team app

If you do not name a feature, the features that can be activated on the app are offered as a list. For the controlled-document library, use :doc:`../controlled-document-library/index` instead - it also waits for the app's site and reports how far the activation has come.

Good to know
************

+ Creating a template or a Teamwork app needs a **business profile** scope. The connector does not work around Omnia's permission model - without the right to do it in the Omnia interface you get Omnia's own refusal.
+ Listing and activating features finds the Teamwork app by its **exact title** (case-insensitive) in a named **business profile**, so give both.
+ A new template is created with **you as its default administrator**, and apps created from it are **not private** and do not let the creator choose language or time zone unless you say otherwise.
+ A template can be created for a **SharePoint communication site**, but a Teamwork app cannot be created from such a template through the connector - it is refused.
+ For a **SharePoint team site**, the address is checked before anything is created. If it is taken you are told, with a suggested alternative. If you are not allowed to create the site in SharePoint, you are told that too.
+ The Teamwork app's site is **provisioned in the background**. It can take a moment before the site exists and features such as the controlled-document library can be activated.
+ Changing and deleting templates and Teamwork apps is done in the Omnia interface - the connector only creates.
+ Activating a feature works the same way as elsewhere in the connector - see :doc:`../../feature/index`.

Actions
*******

+ ``TeamworkAppTemplate.Create`` - create a Teamwork app template.
+ ``TeamworkApp.Create`` - create a Teamwork app from a template.
+ ``TeamworkApp.ListFeatures`` - the features of a Teamwork app, with their current status.
+ ``TeamworkApp.ActivateFeature`` - activate a feature on a Teamwork app.
