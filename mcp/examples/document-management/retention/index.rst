Retention
=========

Retention keeps controlled documents for a set time and schedules them for deletion afterwards. Through the connector you can see which documents a retention covers and when they are scheduled to be deleted, and terminate the retention for the documents you choose.

.. TODO screenshot: retention documents in Omnia, for reference

What you can ask for
********************

+ List the documents under a retention, with their status and scheduled deletion date.
+ Terminate the retention for the documents you choose.

Listing documents under retention
*********************************

::

   Which documents are under retention 3f2c9a10-7d41-4b8e-9e0a-2c55d1f4a7b2,
   and when are they scheduled for deletion?

Each document is listed with its title, status, scheduled deletion date and site, along with how many documents the retention covers.

Terminating retention
*********************

::

   Terminate the retention for the first two of those documents,
   reason "Superseded by the 2026 procedure"

Name the documents the termination applies to; a reason is optional. Terminating is a write, so you are asked to approve it first.

Afterwards the connector lists the retention documents again and tells you if any are still there. Terminating removes the retention in several places independently, so one of them can fail while the others succeed - the warning tells you to check before you retry.

.. TODO screenshot: Claude reporting the result of a retention termination

Good to know
************

+ Both actions need the **retention document id**. The connector cannot look it up by name, so get it from Omnia or from your administrator.
+ Terminating retention takes away the hold that keeps the documents, so **confirm the selection carefully** before you approve it.
+ A termination is reported with the number of documents it targeted. If the re-check shows documents left over, retry only for those.

Actions
*******

+ ``Retention.List`` - the documents under a retention and their scheduled deletion dates.
+ ``Retention.Terminate`` - terminate the retention for selected documents.
