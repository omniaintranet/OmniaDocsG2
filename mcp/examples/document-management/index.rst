Document management
===================

Omnia document management keeps controlled documents - policies, procedures, instructions - in a controlled-document library, with drafts, editions, review, approval and retention. The connector can help with both halves of it: **setting it up**, and **working with the documents** once it is in place.

This section has one page per part of document management, in the order you would normally meet them.

.. TODO screenshot: a controlled-document library in Omnia, for reference

Setting up
**********

Before the first controlled document can be created, a few things have to exist. Each has its own page:

+ A **document type** for the document to be filed under - see :doc:`document-type/index`.
+ A **document template** the new document's file is created from - see :doc:`document-template/index`.
+ A **Teamwork app** whose site hosts the library - see :doc:`teamwork-app/index`.
+ The **controlled-document library** itself, activated on that Teamwork app - see :doc:`controlled-document-library/index`.

The whole setup can be done in one conversation, from the Teamwork app template to the first document type:

::

   Create a teamwork app template called "Controlled Docs Team",
   then a teamwork app called "Quality Management" from it,
   and activate the controlled-document library on it

Working with documents
**********************

With the library in place, the remaining pages cover creating and finding documents, drafts and publishing, review and approval tasks, retention, and changing many documents at once.

Pages in this section
*********************

.. toctree::
   :titlesonly:

   document-type/index
   document-template/index
   controlled-document-library/index
   teamwork-app/index
   document/index
   review-approval/index
   retention/index
   bulk-update/index
