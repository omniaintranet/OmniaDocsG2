Single site collection
=====================================

This information is intended for experienced administrators, IT staff and IT consultants.

In Omnia 7.11 and later it's possible to run Omnia in Single site collection mode.

The main differences are:

+ No new sites can not be created with the Omnia UI (CREATE button is hidden when the feature is activated).
+ Teamwork sites can not be used at all.
+ Document management and Process management must be used within a publishing app.

A new site must be created outside of Omnia, site access setup scripts (info available in Omnia admins settings) run in PowerShell site collection admin, and then the site can be attached to Omnia, as a community site or a publishing app, using the usual ATTACH option.

Activate Single site collection
**********************************
Single site collection should be activated on a new tenant only.

Here's how:

1. Activate the tenant feature "Web Content Management core (limited access)".
2. Add settings and find the scripts in "Site access setup script" in tenant settings: System > Microsoft 365 > Site access setup script.

