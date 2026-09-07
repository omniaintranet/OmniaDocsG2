Announcement statuses
=====================

An announcement status says where a message stands - *Active*, *Resolved*, *Postponed*. It is most useful for announcements that follow a course of events, such as an incident that is first reported and later resolved. Statuses are managed per business profile, and the connector can list them and maintain them.

What you can ask for
********************

+ List the announcement statuses in this part of the intranet.
+ Read one status in detail.
+ Add a status.
+ Rename a status.
+ Remove a status.

Example
*******

::

   Which announcement statuses exist in https://contoso.omniacloud.net/sites/it?

::

   Add the announcement statuses Investigating, Identified and Resolved

.. TODO screenshot: Claude listing the announcement statuses

Then use them as an incident develops:

::

   Set the status of the mail outage announcement to Resolved
   and add "Mail is working again as of 14:30" to the description

Good to know
************

+ A status has a **title only**, and the title can have a value per language.
+ Statuses are **per business profile**.
+ Renaming a status changes it everywhere it is used.
+ Removing a status that announcements still use leaves those announcements without a status.
+ When you create an announcement without naming a status, the existing statuses are offered as a list, with **None** as a valid answer.

Actions
*******

+ ``AnnouncementStatus.List`` - the statuses in this business profile.
+ ``AnnouncementStatus.GetById`` - one status in detail.
+ ``AnnouncementStatus.Add`` - add a status.
+ ``AnnouncementStatus.Update`` - rename a status.
+ ``AnnouncementStatus.Remove`` - remove a status.
