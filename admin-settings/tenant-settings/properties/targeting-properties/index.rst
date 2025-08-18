Targeting properties
===========================

Here you define the properties to use for targeting. A list can look like this:

.. image:: targeting-properties-v7.png

The properties must be added to Enterprise properties to be able to be selected here, as well as be of the type "Taxonomy".

**Note!** Term sets to be used as properties for targeting in Omnia, must be set to "Available for tagging" in SharePoint.

**Note!** In Omnia on-prem, it's only possible to target using SharePoint User Profile and Windows Active Directory group membership. 

Add a target property
***************************
To add a target property definition, click the plus and then use the following settings:

.. image:: targeting-properties-settings-v7.png

+ **Title**: Add the title to be shown for editors, for the Property, when targeting.
+ **Property**: Select tenant property from the list.
+ **Type**: Select type of targeting for this property; Group membership, User profile property, Entra ID property or UserpProperty. When "User profile property", "Entra ID property" or "User property" is selected, choose property from the list shown. For group membership, see below.

Map group membership
************************
When "Group membership" is selected, this link is shown:

.. image:: targeting-properties-settings-map-new-v7.png

When you click the link, the term set for the property you have selected is displayed. Here's an example:

.. image:: targeting-properties-settings-map-v7.png

What you do here is to map terms from he term set, to groups. You don't need to map all, if you don't need all.

1. Click the term you want to map.
2. Select a group in the list by searching (type beginning of a group and see what pops up).

.. image:: targeting-properties-settings-map-v7-group-list-new.png

Security groups and Microsoft 365 groups can be added here (In Omnia on-prem, Microsoft 365 groups can’t be used). Distribution lists can be selceted as well.

3. Continue this way until all terms you want to map is done. 
4. Save when you're finished.

Delete or edit target property
**********************************
To delete a target property, click the dust bin, to edit it, click the pen:

.. image:: targeting-properties-delete-edit-v7.png

All settings used when creating a targeting property can be edited, see above.
