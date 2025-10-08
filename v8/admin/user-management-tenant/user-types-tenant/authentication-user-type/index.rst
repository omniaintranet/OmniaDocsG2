Authentication settings
=====================================

Here you can set the following:

+ **External providers**: If there are more than one provider, make sure to select the correct one.
+ **Built-in providers**: Select the authentication you want to use for this user type and for more options, see below.
+ **Refresh tokens**: Used by mobile apps only. Set the number of days that can pass until a user is forced to log in again.
+ **INVALIDATE ALL USER TOKENS**: When permissions for Omnia has been changed, users needs to log out and log in for the changes to take effect. You can click this button to force a log out from Omnia for all users. Important information on this below.

When expanding one of the options for "Built-in providers", additional settings are available, for example:

.. image:: user-management-types-auth-more-8.png

The settings at the should be self-explanatory. If "Two-factor authentication" is selected, choose "One-time password" or "On-time link" and then set expiration time in minutes.

.. image:: user-management-types-auth-more-two-8.png

More on Invalidate all user tokens
------------------------------------
If the button INVALIDATE ALL USER TOKENS is clicked to force a log out from Omnia for all users, only Omnia is affected, not Sharepoint, Office apps, mail or anything else outside Omnia.

If an editor or author is working on a page in Omnia, the user will be logged out but content added to a page, even if it's not published, is automatically saved quite often, to minimize content lost.

