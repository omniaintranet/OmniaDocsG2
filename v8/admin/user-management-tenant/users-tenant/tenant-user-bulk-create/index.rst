Bulk create users - Tenant
===================================

Here's the settings you can use when bulk creating users. The first step is to select user type and the scenario:

+ **User type**: You can bulk create users for one user type in each session. Note the option "Undefined". If users imported from MS Graph does not match any of the rules, user type is set to "Undefined". You should probably not bulk create such users, but the option is there if you know what you're doing.
+ **Select bulk create users scenario**: Choose to send onboarding links to all users of that user type, or not. You can alos automatically onboard users that already have a password assigned to them.

The second step is to edit the template file. If you already have a template file you can edit the file for use in this session and upload it.

If you don't have a template file, download the default template and edit it with the application you normally use for csv files. 

There should be one row for each user to create (onboard) in the csv file. Also, you must not touch the top row, you should not edit anything there.

**Note!** If you use Excel to edit the csv file, you must select "Text to columns" before you start editing. 

