Enterprise property category
============================

An enterprise property category is a heading that enterprise properties are grouped under in Omnia admin - Common, News, HR and so on. Every enterprise property belongs to one category. The connector can list the categories in the tenant and create a new one.

What you can ask for
********************

+ List the enterprise property categories in the tenant.
+ Create a new category.

Example
*******

Look at the categories that already exist first:

::

   List the enterprise property categories

Each category comes with its id, its title in every language it has, and its position in the list.

If none of them fits, create one. The title can be given in one language or in several:

::

   Create an enterprise property category called "Quality" in English
   and "Kvalitet" in Swedish

.. TODO screenshot: Claude listing the enterprise property categories

The new category can then be used straight away when you :doc:`create an enterprise property <../enterprise-property/index>`.

Good to know
************

+ Categories are **tenant-wide** and need the permission to manage enterprise properties.
+ A title needs **at least one language** with a value.
+ **Omnia allows two categories with the same title.** The connector does not stop you, so check the list first to avoid near-duplicates.
+ Categories cannot be renamed, reordered or deleted through the connector - use Omnia admin for that.

Actions
*******

+ ``EnterprisePropertyCategory.List`` - every category in the tenant.
+ ``EnterprisePropertyCategory.Create`` - create a category.
