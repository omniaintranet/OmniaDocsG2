Single site collection
=====================================

This information is intended for experienced administrators, IT staff, and IT consultants.

Beginning in **Omnia 7.11**, it is possible to run Omnia in **Single site collection mode**. 

Key differences in Single site collection mode
*************************************************
When this feature is enabled:

+ New sites cannot be created through the Omnia UI. The CREATE button is hidden.
+ Teamwork sites are not supported.
+ Document Management and Process Management must be configured within a Publishing app.

To add a new site, administrators must:

1. Create the site outside of Omnia.
2. Run the required Site access setup scripts using PowerShell with Site Collection Administrator permissions (scripts are available in Omnia under Admin aettings).
3. Attach the site to Omnia, either as a Community site or a Publishing app using the standard ATTACH option.

Activating Single site collection mode
**********************************************
**Important:** This feature should only be activated on new tenants.

To activate:

1. Enable the tenant feature "Web Content Management core (limited access)".
2. In Omnia, go to **System > Microsoft 365 > Site access setup script** to configure the necessary settings and download the PowerShell scripts.


