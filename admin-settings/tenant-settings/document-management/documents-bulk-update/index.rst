Documents bulk update
=======================

This page describes the option for Omnia 7.11 and earlier. For 7.12 and later, see: :doc:`Documents bulk update in Omnia 7.12 </admin-settings/tenant-settings/document-management/documents-bulk-update-712/index>` 

Use this option to bulk update any of the defined document management properties. Note that not all properties can be updated this way. One example is Approver. 

Also note that the user executing the Bulk update must have access to the documents that should be updated. Documents that the user does not have access to are simply not shown in the list.

.. image:: documents-bulk-update-1-v7.png

1. Select "Search Property".
2. In "Property Value", add the value to be replaced.
3. Click FIND.

A list of published documents that has the selected property defined is displayed.

4. In "New Value", add the value that should replace the one you selected.
5. Select all documents that should replace the value.
6. Click REPLACE.

.. image:: documents-bulk-update-2-v7.png

Be aware that, if there are many documents selected, the update may take some time.

When the update is finished, the update is noted in the document history of each document.

Bulk update removed properties
*********************************
It's possible to replace properties that are not longer present in the system. A good example when this is useful is when a document owner has left the organization and already has been removed from the AD. This is how it's done:

1. Select the property to be replaced (for example Document Owner).
2. Enter the property to be replaced in the second Property Value field (for example a former colleague). Note that you can use FIND for a listing of for example the documents a former colleague are document owner of.
3. Enter a new value (for example a colleauge) in the "New Value" field.
4. Click REPLACE.

Heres's an example:

.. image:: bulk-update-owner-v7.png

Bulk update and templates
***************************
Note that Bulk update never updates the template. The republish via Bulk update always uses the current template.

