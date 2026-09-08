Publishing App
==============

A Publishing App is a live site in a business profile - a news site, a policy library, a department site. It is always provisioned from an existing :doc:`Publishing App template <../publishing-app-template/index>`, which decides its permissions, features and metadata.

What you can ask for
********************

+ Create a Publishing App in this business profile from one of the available templates.

Example
*******

Ask for the app and let the connector offer the templates you can use:

::

   Create a Publishing App called "HR News" in
   https://contoso.omniacloud.net/sites/hr

.. TODO screenshot: Claude presenting the eligible templates

Then answer any metadata the template asks for. If the template uses a property set, the members marked required need values - unless the template already supplies a default for them:

::

   Use the News template, description "News and updates from HR",
   and set Owner to the HR communications team

.. TODO screenshot: the new Publishing App in the Omnia interface

Good to know
************

+ Creating an app needs a **business profile** scope and the permission to create apps there.
+ Only templates in **this business profile** that are for native Omnia sites are eligible. Templates attached to SharePoint are not yet supported by the connector.
+ The **address is generated from the title** when you do not give one. It has to be unique both as an Omnia address and as a SharePoint site alias across the tenant; if it is taken, you get a suggested alternative to retry with.
+ **You become the app's only administrator.** A template that requires more than one administrator cannot be used through the connector yet, because there is no way to assign additional people here - use the Omnia interface for those.
+ A required property with no value and no template default stops the creation, with the missing properties named.

Actions
*******

+ ``PublishingApp.Create`` - provision a Publishing App from a template.
