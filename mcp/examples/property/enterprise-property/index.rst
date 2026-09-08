Enterprise property
===================

An enterprise property is one metadata field defined once for the whole tenant: an internal name, a title, a data type and a category. Page types, property sets, search and rollups all refer back to these definitions, which is why creating one is a considered act rather than a quick one.

.. TODO screenshot: enterprise properties in Omnia admin, for reference

What you can ask for
********************

+ List every enterprise property in the tenant.
+ Look up specific properties.
+ List the available data types.
+ Create a property.
+ Change a property's title, category or search settings.

Example
*******

Look at what already exists before adding anything - reusing a property is almost always better than creating a near-duplicate:

::

   List all enterprise properties in the tenant and group them by category

::

   Which enterprise property data types are available?

Then create one. A property needs a title, an internal name, a data type and a category; if you leave the data type or the category out, the valid ones are returned as a list to pick from:

::

   Create a text enterprise property with internal name Department,
   title "Department" in English and "Avdelning" in Swedish,
   in the Common category, and make it searchable in SharePoint

.. TODO screenshot: Claude offering the available data types as a list

Good to know
************

+ The **internal name** and the **data type** are set at creation and cannot be changed afterwards. Pick both deliberately.
+ A **taxonomy** property needs a term set. You are asked for it if you do not supply one.
+ **SharePoint searchable** and **Microsoft Search searchable** can each be turned on, with their own managed property settings.
+ An update needs the property's id plus at least one field to change; only the fields you mention are touched.
+ **Extended properties** are not handled here - they have their own flow in the Omnia interface.
+ Properties are **tenant-wide**. A change reaches every page type, property set and rollup that uses the property.

Actions
*******

+ ``EnterpriseProperty.List`` - every property definition in the tenant.
+ ``EnterpriseProperty.GetByIds`` - specific property definitions.
+ ``EnterprisePropertyDataType.List`` - the available data types.
+ ``EnterpriseProperty.Create`` - create a property.
+ ``EnterpriseProperty.Update`` - change a property.
