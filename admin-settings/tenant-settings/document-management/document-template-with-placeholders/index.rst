Creating a document template with place holders
================================================

A document property place holder starts with [[ and ends with ]] and can be placed anywhere inside a DOCX document. Most place holders can also be placed anywhere inside an XLSX document, including header and footer, and in PowerPoint (PPTX) documents as well, in both header and content. Place holders support any document property. 

For more information on placeholders available for each application, see below.

.. note:: In a template you probably want the published copy of the template to include the placeholders. To ensure that the placeholders are not replaced by document properties on the template, you need to escape the placeholders using the character “\\”. An escaped placeholder would look like this:

\\[\\[_PubDate\\]\\]

Another, and most likely better, way is to use a dedicated document type for all templates and there set that the placeholders should not be replaced for documents of that type. In that case, place holders can be added as described below - escape characters are not needed. See the heading "Publish" on this page for more information: :doc:`Document types </admin-settings/tenant-settings/document-management/document-types/index>`

Make sure to use the internal name (or the short name) of the property, example:

[[ODMPublished]]

You can use the following short names for built-in properties in ODM:

- _DocId: Document Id including prefix.
- _DocIdN: Document Id number only.
- _Edition: Edition.
- _PubDate: Published Date.
- _Comment: Edition Comment.
- _DocType: Document Type.
- _ApprDate: Approved.
- _ApprBy: Approved By.
- _Lang: Content Language:
- _RevDate: Review Date.

There's also a special place holder if you need to show document history somewhere in a Microsoft Word document:

[[_DocHistory]]

On publication, this place holder will be replaced with a table listing all editions, for example:

.. image:: place-holder.png

.. note:: The [_DocHistory]] can only be used in Microsoft Word, not in Excel or PowerPoint.

If you want dates to be displayed with the appropriate format you can use the following syntax for date and date including time:

[[_PubDate|Date]]

[[_PubDate]]

**Tip: date format**: Using the [[_PubDate|Date]] place holder, you can add the time format you want, instead of Date, example: [[_PubDate|MM/DD/YYYY]]

**General tip:** If you want to prevent authors from deleting place holders within the document (for example in a header), you can put them inside locked content controls added using the “Developer” tab in Word. Note that this tab is not shown as default, it has to be added using the settings.

.. note:: When a controlled document is merged with a document template, the number of different header/footer sections in the template must match the number of different header/footer sections in the controlled documents. (For example, if you try to upload a controlled document and merge it with a document template that has a first page header and a second header, the template also has to include a first page header and a second header.)

.. note:: When a document is merged with a template, neither the document nor the template is allowed to have any shapes in the header/footer. If you want a line, use borders instead of a line shape. (Note! Text boxes are also considered shapes. Don't use it. Add a table to structure the text instead.)
