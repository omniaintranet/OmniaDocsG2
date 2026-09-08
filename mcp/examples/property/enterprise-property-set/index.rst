Enterprise property set
=======================

An enterprise property set is a named group of enterprise properties that belong together - the metadata a Publishing App template hands to every app instance created from it. The connector can list the sets in the tenant together with their member properties.

What you can ask for
********************

+ List the property sets in the tenant and see which properties each one contains.

Example
*******

::

   List the enterprise property sets and their properties

.. TODO screenshot: Claude listing the property sets and their members

This is most often a step on the way to something else - when you create a :doc:`Publishing App template <../../publishing-app-template/index>` you choose which property set the template uses, and the members of that set are what you can then give default values to.

Good to know
************

+ Reading the sets needs nothing but tenant scope.
+ Sets can only be **read** through the connector. Creating and changing them is done in the Omnia interface.
+ A member property's **required**, **hidden** and **allow multiple values** settings belong to the set itself and cannot be overridden per template.

Actions
*******

+ ``EnterprisePropertySet.List`` - the property sets in the tenant, each with its member properties.
