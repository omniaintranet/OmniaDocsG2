Publishing App template
=======================

A Publishing App template is the blueprint every Publishing App in a business profile is created from: who may request one, how it is permissioned, which features it activates, which metadata it carries, and which page collections it starts with. The connector can create a template from the conversation.

This is the most involved area of the connector, and deliberately the most talkative one - every choice that has a fixed set of valid answers is put back to you as a list rather than being decided for you.

.. TODO screenshot: Publishing App templates in the Omnia interface, for reference

What you can ask for
********************

+ Create a Publishing App template in this business profile.

A template covers:

+ **Title** (required, per language) and an optional **description**, with an optional minimum description length.
+ **User availability** - who may create an app from the template.
+ **Permission level** and the **minimum number of administrators** an app must have.
+ **Features** to activate on every app created from the template.
+ An **enterprise property set** for the app's metadata, and optional **default values** for its members.
+ **Page property mapping** - which property holds the page contact, and which holds the review date.
+ **Page collections** the app starts with, each with its own structure, page types and settings.

Example
*******

Start simply and answer the questions as they come:

::

   Create a Publishing App template called "News" in
   https://contoso.omniacloud.net/sites/hr

Every unanswered choice comes back as a list - user availability, permission level, minimum number of administrators, features, property set, contact and review date mapping - and you retry with what you picked. **Don't activate any feature**, **Don't use a property set** and **No mapping** are all valid answers.

.. TODO screenshot: Claude presenting the template choices as lists

Page collections are asked for in the same way. Each one needs a title and a structure - hierarchical or flat - and the page types that may be used inside it:

::

   Give the template one page collection called "Articles",
   flat structure, using the News Article page type

If the template should start with no page collections at all, that has to be said explicitly rather than left out.

.. TODO screenshot: the finished template in the Omnia interface

Good to know
************

+ Creating a template needs a **business profile** scope and the permission to manage templates there.
+ Only **features that can be activated on an app instance** can be chosen. Tenant-wide and business-profile features are not offered and are rejected if named.
+ **Default property values** support text, number, date, boolean, taxonomy, enterprise keywords, tags and rich text. Person properties and other types are rejected. A member property's required, hidden and multiple-value settings belong to the property set itself and cannot be overridden here.
+ Page collection titles must be **unique within the template**, the same rule the Omnia interface applies.
+ A page collection's **address is generated from its title** - there is no field for it, exactly as in the interface.
+ The page collections you define here become real page collections **when an app is provisioned from the template afterwards**. Existing apps and templates are not affected, and nothing appears in the interface until an app is created.
+ Page collections defined here have **no layout** until one is set afterwards in the Omnia interface, and **AI settings cannot be pre-configured** on them.
+ **Approvers** cannot yet be configured through the connector.

Actions
*******

+ ``PublishingAppTemplate.Create`` - create a Publishing App template.
