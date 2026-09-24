Bulk update and republish
=========================

Sometimes the same property has to change on many published documents at once - most often the **review date** after an annual review. Bulk update does that without opening a draft on each document: it finds the documents, sets the new value and republishes them, and lets you follow the progress.

.. TODO screenshot: bulk update of controlled documents in Omnia, for reference

What you can ask for
********************

+ Find the published documents on a site that match a property or a search query.
+ Set one property to a new value on those documents and republish them.
+ Do the same for documents you give as links.
+ Check the progress of the republish.

Finding the documents
*********************

::

   Find all published controlled documents on https://contoso.sharepoint.com/sites/qms
   whose review date is before 1 January 2026

You can filter on a property, on several criteria, or with a search query of your own. Up to 100 documents come back per page.

Updating and republishing
*************************

::

   Set the review date to 31 December 2026 on all of those documents and
   republish them, with the history note "Annual review"

One property is set to the new value on every document, and each document is republished. The history note is written to each document's history, so the change can be traced later. Nothing changes until you approve the write.

If you already have the links, you do not need to search first:

::

   Republish https://contoso.sharepoint.com/sites/qms/Published/fire-safety-procedure.pdf
   and set its review date to 31 December 2026, history note "Annual review"

Links can be file links or viewer links, and can point at documents on different sites. A link that does not lead to a published controlled document is listed back to you as **unresolved** - it does not stop the other documents from being updated.

.. TODO screenshot: Claude reporting submitted and unresolved documents

Following the progress
**********************

Republishing is **queued** per document and runs in the background:

::

   What is the status of the review-date republish?

Ask again until no document is still republishing. A document whose republish failed can simply be submitted again.

Good to know
************

+ Bulk update needs the **site address** of the controlled-document library, not a business profile or Publishing App scope.
+ **Everything runs as you.** Finding needs access to the site, and updating needs edit access to each document; Omnia checks it for every document.
+ Finding uses the **search index**, not the library itself, so a document that has just been published only shows up once it has been crawled. An empty result can simply mean the index has not caught up yet.
+ To filter on **several values**, ask for them as separate criteria or as a search query. A single filter property cannot take a comma-separated list, and the connector refuses it.
+ A date can be given as a plain date - the connector converts it to the format Omnia stores.
+ The new value **replaces** the old one unless you ask for something else.

Actions
*******

+ ``DocumentBulkUpdate.Find`` - find published documents on a site by property or search query.
+ ``DocumentBulkUpdate.UpdateAndRepublish`` - set a property on the documents and queue them for republishing.
+ ``DocumentBulkUpdate.GetStatus`` - the republish status of each document.
