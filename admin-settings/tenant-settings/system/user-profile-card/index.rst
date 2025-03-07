User profile card
===================

The user profile card will be shown (if the option is activated here) whenever you click on a user name in Omnia. The user profile card is designed to align with user profile cards in other services in Microsoft 365.

Here's an exmple:

.. image:: profile-card-example-613.png

**Note!** In Omnia on-prem, all options referring to Delve or My Site is removed, as it's Microsoft 365 features and therefore not available on-prem.

The user profile card also includes the possibility to browse who reports to whom in the organization. Here's an example:

.. image:: profile-card-example-613-2.png

Settings
***********
The following settings are available:

.. image:: profile-card-settings-v78.png

+ **Enable User profile card**: If the Profile Card should be used within the tenant, select this option. If you choose not to, the person's Delve profile is shown instead.
+ **Show link to details**: If it should be possible to go to the person's profile from the User Profile Card, select this option. In Omnia online the person's Delve page is linked to when this option is selected (see the Go to Delve link in images aboove). In Omnia o-nPrem, the link goes to the person's My Profile page.
+ **Show strengthen profile**: If the Strengthen Profile button should be shown on the card, select this option. The button is used to access the Strengthen Profile dialog.
+ **Show my subscriptions**: If the My Subscription button should be shown on the card, select this option. The button is used to access the My Subscriptions dialog.
+ **Exclude filters**: If some users registered in your system should NOT be displayed in the organization tree in the Organization Tree block, add filters for them using Entra ID properties and value. An example is if your organization is in education, probably just the staff should have access to the intranet, not the students.
+ **Show blocked login user**: Select this option to list logged in users that are excluded by the filter(s) you have added above. 

For more information about Strengthen Profile, see this page: :doc:`Strengthen Profile </user-options/strengthen-profile/index>`

For more information about My Subscriptions, see this page: :doc:`My Subscriptions </user-options/my-subscriptions/index>`

Adding exclude filters
*************************
To add exclude filters, do the following:

1. Click the plus to add a filter.

.. image:: exclude-filters-1-78.png

2. Select Entra ID property.

.. image:: exclude-filters-2-78.png

Note that if you can't find the property you are looking for in the last, it can still be available. Type the name of the property in the field to search for it.

3. Add a value for the property.

.. image:: exclude-filters-3-78.png

4. Click SAVE.
5. Continue the same way until all exclude filters has been added.


