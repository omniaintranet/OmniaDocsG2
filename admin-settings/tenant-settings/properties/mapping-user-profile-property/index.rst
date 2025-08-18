Mapping a user profile property
=====================================

In order to map an Omnia property to a user profile property, you need to first find the user profile property in Sharepoint. 

1. Go to the site.
2. Go to the admin portal (for example by typing https://admin.microsoft.com).
3. Select the Sharepoint admin center.

.. image:: sharepoint-admin-center-v7.png

4. Select "User Profiles". If it's not shown, select "More Features" first.

.. image:: sharepoint-admin-user-profiles-v7.png

4. Select "Manage User Profiles".

.. image:: sharepoint-admin-manage-profiles-v7.png

5. Type the name of the user you wish to inspect.

.. image:: sharepoint-admin-manage-profiles-user-v7.png

In order for a user profile property to be used in Omnia, it has to be mapped first, and in order for it to be mapped, you need to know the name of the property, which can be found in search.

.. image:: sharepoint-admin-manage-profiles-search-v7.png

1. Select "Manage Search Schema":

.. image:: sharepoint-admin-manage-manage-schema-v7.png

2. Type the name of the property you are looking for (example Department). 

.. image:: sharepoint-admin-manage-manage-schema-department-v7.png

In this example you can see that the name of the managed property is indeed Department, and the crawled properties are People:Department and ows_department.

Also notice that Department is of type Text, it is also queryable, retrievable and refinable but not searchable or sortable, which means that when you map it in Omnia, it needs to have the same attributes if you want it have the same functionality.

Mapping in Omnia (example Department): 

.. image:: tenant-properties-mapping-v7.png

Department is now a usable property that functions as both a value displayer and a refiner in blocks like People roll up and features like Search.

