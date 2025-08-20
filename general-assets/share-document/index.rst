Share documents
===========================================

A block can be set up, for example using an action button, to let users easily share a document with others by uploading it locally on a page. This can be very useful, especially in a community, but can be used in other types of apps as well. 

One document can be uploaded each time. A document uploaded this way will be read only.

This is needed:

+ A property, for example Document data.
+ A page type for this purpose, with an iFrame block pointing to the property.
+ A page set up to list the uploaded, local documents.

Note that this can be added to the central community template, and added to the community layouts, so functionality for sharing documents will be added automatically to all new communities.

Implementation example
*************************
Here's an example, where sharing documents is available in a community:

.. image:: share-document-button.png

When a user clicks SHARE DOCUMENT, this is shown:

.. image:: share-document-button-upload.png

The user can upload by using drag and drop, add a description (Summary) and tag the document. Also note that a name for the uploader is registered. The name can be changed if the user uploads a document for someone else.

The user must click PUBLISH for the upload to start.

For all users of the community to read a shared document, the button FIND DOCUMENTS will be used. When clicked, something like the following is shown:

.. image:: find-document-button-list.png

The document title can be clicked to read a document. The uploader's name can also be clicked to display that user's user profile card, if it's used within your organization, or the user's delve page if the profile card is not used.

How it is set up
------------------
This implementation example is set up the following way:

1. A page type called Shared document is set up, with an iFrame block in the middle.

.. image:: share-document-pagetype-1.png

Under Settings, the property Document data is added, and other properties that will be used in the page type.

.. image:: share-document-pagetype-2.png

The iFrame block is pointing to the Document data property.

.. image:: share-document-pagetype-3.png

2. Under Communities for the business profile, a layout and a template is set up.

The layout is called Shared docucments.

.. image:: share-document-layout-1.png

And it's set up this way:

.. image:: share-document-layout-2.png

SHARE DOCUMENT is set up using an action button with these settings:

.. image:: share-document-layout-3.png

FIND DOCUMENTS is set up using an action button with these settings:

.. image:: share-document-layout-4.png

The list is set up with a tab section:

.. image:: share-document-layout-5.png

And under that, a page rollup with the following query:

.. image:: share-document-layout-6.png

In the community template, the following is added to Setup:

.. image:: share-document-template.png


