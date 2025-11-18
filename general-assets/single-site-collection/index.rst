Single site collection
=====================================

**This description is just started. Will be edited and expanded soon.**

Available in Omnia 7.11 and later.

When absolute security is needed, Omnia can be run in Single site collection mode, but works then quite differently. For example:

+ No new sites can be created with the Omnia UI (CREATE button is hidden).
+ Teamwork sites can not be used.
+ Follow site can not be used.
+ Document management and Process management must be used within a publishing app.

A new site must be created outside of Omnia, a script used in PowerShell site collection admin, and then the site can be attached to Omnia, as a community site or a publishing app. 

Activate Single site collection
**********************************
Single site collection should be activated on a new tenant only.

Here's how:

1. Activate the tenant feature "Web Content Management core (limited access)".
2. Use "Sites.Selected" in tenant settings: System > Microsoft 365 > Sites.Selected.


