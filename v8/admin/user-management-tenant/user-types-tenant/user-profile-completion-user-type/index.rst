User profile completion settings
=====================================

All edits can be done on the user profile card. On this tab you work with the settings for profile completion. 

The selected properties are listed here (in a new user type, this list is empty). Of course, the properties you add here must also be present in the card layout for the follow up on profile completion to be meaningful. 

Add a property
****************
You click ADD to add a property and the following are available:

.. image:: tab-profile-completion-property-v8.png

+ **Data source**: Select the data source to get the properties from; User (meaning Omnia user), User (Microsoft Graph) or User (Sharepoint). 
+ **Select properties**: Select the property here.
+ **Completeness impact**: You can set the completeness impact to Low, Medium or High. When the completeness impact is calculated, Low is 1, Medium is 2 and High 3. The aggregated points are then divided with the total points possible, to yield the percentage.

Edit or delete a property
***************************
To edit or delete a property, expand the property. You can edit the completion impact and delete the property if needed.

.. image:: tab-profile-completion-property-delete-v8.png

Schedule
------------
You can schedule the check for how complete the user profle is, according to the settings for the user type. Expand to see the settings:

.. image:: tab-profile-completion-schedule-change-v8.png

You can set the schedule to Never (meaning not set), Daily, Weekly or Monthly. For Daily, Weekly and Monthly, additional settings are avaible. Should be self explanatory.

The check is executed when the page containing the user profile progress block is updated.

