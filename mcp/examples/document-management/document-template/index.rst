Document templates
==================

A document template is the file a new document starts from. Every controlled document is created from one - there is no blank-document path - so at least one template has to exist before the first document can be created. A template's content is either **uploaded** - a file given to Omnia per language - or **linked** to an existing document in the controlled-document library. The connector can list and create templates, create template categories, and download an uploaded template's file to check it arrived intact.

.. TODO screenshot: document templates in Omnia admin, for reference

What you can ask for
********************

+ List the document templates, with their content per language.
+ Create a template for controlled documents or for normal documents.
+ Create a template category.
+ Download the file of an uploaded template.

Listing templates
*****************

::

   List the document templates

The list has one entry per template **per language**. Each entry tells you whether its content is **uploaded** or **linked**, and gives the file name of an uploaded file or the document a linked one points at.

Creating a template
*******************

A template needs a **title** and a **type** - for controlled documents or for normal documents. If you leave out the type, both are offered as a list:

::

   Create a controlled-document template named "Standard Policy Template"

To give the template a file, attach it in the conversation and say which language it is for:

::

   Create a controlled-document template named "Standard Policy Template"
   from the attached Word file, for English

Or link it to a document that is already in the controlled-document library:

::

   Create a template named "Meeting Minutes" for normal documents,
   linked to the Meeting Minutes document

.. TODO screenshot: Claude confirming the new document template

To check that an uploaded file was stored correctly:

::

   Download the file of the Standard Policy Template to check it

Creating a category
*******************

::

   Create a document template category called "Policies"

A category needs a title in at least one language.

Good to know
************

+ Document templates are managed at **tenant** level. The connector does not work around Omnia's permission model - without the right to manage templates you get Omnia's own refusal.
+ A template's **title is given per language**, and each language with a title gets its own content. Uploaded files are given per language too.
+ A template is either **uploaded or linked** - asking for both at once is refused. A linked template uses the same document for every language. A language that has a title but no uploaded file is created as linked content.
+ A template can also be created **without any content** - a shell with a title and a type, but no file and no linked document.
+ An uploaded file needs a **file name** and **content**, and is refused if either is missing or the content cannot be read.
+ An uploaded template entry **without a file name has no file**, and cannot be used to create a document. Pick one that shows a file name.
+ Templates cannot be **placed in a category** through the connector - create the category here and assign templates to it in the Omnia interface.
+ To make a template available for a document type, set it on the document type's Templates tab - see :doc:`../document-type/index`.
+ Templates and categories cannot be changed or deleted through the connector.

Actions
*******

+ ``DocumentTemplate.List`` - the document templates and their content per language.
+ ``DocumentTemplate.Create`` - create an uploaded or linked template.
+ ``DocumentTemplate.CreateCategory`` - create a template category.
+ ``DocumentTemplate.DownloadUploadedContent`` - download an uploaded template's file.
