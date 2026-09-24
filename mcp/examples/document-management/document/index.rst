Controlled documents
====================

A controlled document is a policy, procedure or instruction that lives in a controlled-document library and goes through drafts, editions, approval and publishing. Through the connector you can find a document, read it and its properties, download its file, create a new one, work on a draft, and publish, republish or unpublish it.

Controlled documents belong to a **site**, not to a business profile or a Publishing App. Almost every request therefore needs the address of the controlled-document site, such as ``https://contoso.sharepoint.com/sites/qms``. Pasting a link to a document on that site works too - the connector reduces it to the site address.

.. TODO screenshot: a controlled document in the Omnia interface, for reference

What you can ask for
********************

+ Find a document by name or title, across the sites you follow or on one site.
+ List the drafts, the published documents or the tasks of a controlled-document site.
+ Read a published document or its current draft, including every property.
+ Download a document's file so you can edit it.
+ Create a new controlled document from a document type and a template.
+ Start a new revision of a published document, upload an edited file, and change the draft's properties.
+ Preview a draft merged with its template.
+ Publish a draft - directly or through approval - and publish a new edition.
+ Publish a draft you only know by its title.
+ Republish a document, recover a document whose publishing failed, and unpublish a document.

Finding a document
******************

Most conversations start from a name, not an address. Ask for it as you would say it:

::

   Find the controlled document "Fire Safety Procedure"

Leaving the site out searches **every controlled-document site you follow**. You are told which sites were searched and which were skipped, and why - a site that times out or that you cannot open is skipped rather than failing the whole search. If you do not follow any controlled-document site, you are asked for the site address instead.

Naming the site narrows it down and is faster:

::

   Search for "fire safety" on https://contoso.sharepoint.com/sites/qms

The connector can also look a name up through the Quick Search of every business profile:

::

   Find documents named "Permissions 7.11" anywhere in the tenant

Each match comes back as a card with the title, the link, the document id, the edition, the revision and the status, so you can pick the right one before anything else happens.

.. TODO screenshot: document matches shown as selection cards

Listing a site
**************

::

   Show me all draft documents on https://contoso.sharepoint.com/sites/qms

::

   List the published documents on the QMS site

::

   Which document tasks are assigned to me on the QMS site?

Tasks are shown **assigned to me** unless you ask for the tasks **you assigned** or the **completed** tasks. Lists come back 25 at a time; ask for more to see the next page.

Reading a document
******************

::

   Show me the details of "Fire Safety Procedure", including all its properties

::

   Show me the current draft of "Fire Safety Procedure" so I can review it before publishing

Reading a document returns its core details - title, document id, edition, file - together with **every property** of its document type. If the properties cannot be loaded, the core details are still returned and you are told why the properties are missing.

Before any change to a published document, the connector shows you the exact edition, revision and status and waits for you to confirm it is the right one.

Downloading the file
********************

::

   Download the file of "Fire Safety Procedure" so I can edit it

You get the original file - usually a Word document - of the published edition, or of the draft if you ask for that. A view-only PDF copy can be downloaded instead. The connector does not change the contents of the file itself; you edit it and upload it again.

Creating a new document
***********************

::

   Create a new controlled document called "Fire Safety Procedure"
   on https://contoso.sharepoint.com/sites/qms

You are asked for what the connector cannot know:

1. The **document type**. Only selectable document types can be used, not groups, and you are offered the list to choose from.
2. The **template** the file is created from. A template is required - there is no blank-document option - and only templates that actually have a file can be used. You are offered the valid ones.
3. The **file name**. If you do not give one it is derived from the title, for example ``fire-safety-procedure.docx``, and shown to you so you can change it.

You can also give the document's language and property values. Everything is summarised back to you before the document is created.

The new document is created as a **draft**. It is not published until you ask for it.

.. TODO screenshot: Claude asking for the document type and template

Working on a draft
******************

Start a new revision
--------------------

::

   Create a new revision of the published "Fire Safety Procedure" so I can edit it

A document can have only one draft at a time. If there already is one, the request is refused and you are told to work on the existing draft - or, if it is locked by an approval workflow, to finish or cancel that workflow first.

Upload an edited file
---------------------

::

   Here is my edited version of "Fire Safety Procedure" - upload it as the new draft

The uploaded file creates a new revision draft, or replaces the file on the draft that already exists for that edition. You are told which of the two happened. An empty file is refused.

Change properties
-----------------

::

   Set the review date on the draft of "Fire Safety Procedure" to 1 March 2027.
   Do not change anything else.

You are always asked for the exact value and shown what will be written before anything changes. The property is matched against the tenant's enterprise properties; if the name does not match one, you are offered the available properties to choose from instead of the connector guessing the closest one.

Only the properties you mention change. After the change the connector **reads the value back**, and reports a failure if it did not actually stick - a "saved" message on its own is never taken as proof.

Changing a property **never publishes** the document. You are asked afterwards whether you want to publish it.

Preview the result
------------------

::

   Show me a preview of the "Fire Safety Procedure" draft before I publish it

The preview is the draft merged with its template, the way it will look when published.

.. TODO screenshot: a draft preview shown in the conversation

Publishing
**********

::

   Publish the draft of "Fire Safety Procedure". It needs approval from
   anna@contoso.com, due 15 October

::

   Publish the draft of "Fire Safety Procedure" directly, no approval needed

The connector never decides on its own whether a draft goes through approval. You say it:

+ **With approval** needs an **approver** and a real **due date**. The draft is submitted to the approval workflow, and it is published when the approver approves it - see :doc:`/mcp/examples/document-management/review-approval/index`.
+ **Directly** publishes the draft straight away, without approval.

If you do not say which, you are asked. The choice, the approver and the due date are summarised back to you before anything is submitted.

When you have edited a document in the same conversation, the connector remembers which draft you reviewed. If someone else has changed the draft in the meantime, publishing is refused, so you never publish something you have not seen. Read the draft again and retry.

Publishing a draft by its title
-------------------------------

::

   Publish the draft document "Fire Safety Procedure" on
   https://contoso.sharepoint.com/sites/qms

The connector first lists the drafts on the site, then matches the title - an exact match, or a title that starts with what you wrote. If several drafts match, you choose one. If none does, you get the list of drafts that exist, and nothing is created or published.

By default it tries to publish directly, and sends the draft for approval if the document requires it. That is why an **approver** and a **due date** are needed unless you ask for direct publishing only. The approver is checked before anything is published, so a mistyped name fails without leaving the draft half-way.

Republishing
------------

::

   Republish "Fire Safety Procedure" on the QMS site

Republishing looks the document up by title on the site. If it has a draft, the draft is **published directly, without approval**. If it has no draft, nothing happens and you are told to start a new revision first. If the title matches several documents, you choose one.

Fixing a failed publish
-----------------------

::

   "Fire Safety Procedure" is stuck in publishing failed - fix it

This resumes the publishing from the point where it stopped, instead of starting again from scratch. Afterwards the connector checks the document's status and tells you if it is still marked as failed.

Unpublishing
************

::

   Unpublish "Fire Safety Procedure 2024" on the QMS site

Unpublishing removes the published document. Afterwards the connector checks whether the document is really gone, and tells you if it can still be found - the removal happens in more than one place, so it can partly fail. Confirm carefully before you approve it.

Good to know
************

+ Controlled documents need the **site address** of the controlled-document library, not a business profile or Publishing App scope. A site address has a ``/sites/<name>`` or ``/teams/<name>`` part; an address for the tenant root is refused.
+ **Everything runs as you in SharePoint.** You need access to the site, and to create or change documents you need write access to it. If SharePoint does not accept your sign-in you get a clear error, and the connector never falls back to a system account.
+ The **controlled-document library** has to be activated on the site before a document can be created there - see :doc:`/mcp/examples/document-management/controlled-document-library/index`.
+ A **file name that already exists** in the library is refused when creating a document. Choose another one.
+ The document **title and the document id are different things**. The connector always uses the id it read from Omnia, never the title, and never mixes an id from one site with another site.
+ A tenant-wide title search covers at most the **first 25 sites** you follow and does not page. Name the site to search the others, or to page through a large site.
+ Searching one site matches the title against the site's published documents one page at a time. If a document is not found, ask for the next page.
+ Creating a document re-reads it afterwards and **warns** you if its document id or properties did not land, which can happen when a property value is rejected after the file is already created.
+ **Approval and publishing are separate.** "Approve" completes the approval tasks first; the connector never publishes in place of an approval, and never publishes as a side effect of another change.

Actions
*******

+ ``Document.FindByName`` - find documents by name through the Quick Search of every business profile.
+ ``Document.SearchByTitle`` - search published documents by title, on one site or across the sites you follow.
+ ``Document.ListDrafts`` - the draft documents of a site.
+ ``Document.ListPublished`` - the published documents of a site.
+ ``Document.ListTasks`` - the document tasks of a site: assigned to me, assigned by me, or completed.
+ ``Document.Get`` - read a published document and all its properties.
+ ``Document.GetDraft`` - read the current draft and all its properties.
+ ``Document.GetEdition`` - the edition, revision and status of a document, to confirm it is the right one.
+ ``Document.GetFields`` - the property values stored on a document's file.
+ ``Document.DownloadFile`` - download the file of a published edition or a draft.
+ ``Document.CreateNew`` - create a new controlled document as a draft.
+ ``Document.CreateDraft`` - start a new revision draft of a published document.
+ ``Document.UploadEditedFile`` - upload an edited file as the draft.
+ ``Document.UpdateDraft`` - change several property values on a draft.
+ ``Document.UpdateProperty`` - change one property on a draft.
+ ``Document.PreviewDraft`` - preview a draft merged with its template.
+ ``Document.Publish`` - publish a draft, with or without approval.
+ ``Document.PublishNewEdition`` - publish a revised draft as a new edition, with or without approval.
+ ``Document.PublishDirect`` - publish a draft directly, without approval.
+ ``Document.PublishDraftByTitle`` - publish a draft found by its title on a site.
+ ``Document.Republish`` - publish the pending draft of a document found by its title.
+ ``Document.FixPublishingFailed`` - resume a publish that failed part-way.
+ ``Document.Unpublish`` - remove a published document.
