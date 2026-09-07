Announcement types
==================

An announcement type is a label you can put on an announcement - *Maintenance*, *Policy*, *Event* - so readers and editors can tell one kind of message from another. The types available are managed per business profile, and the connector can list them and maintain them.

What you can ask for
********************

+ List the announcement types in this part of the intranet.
+ Read one type in detail.
+ Add a type.
+ Rename a type.
+ Remove a type.

Example
*******

::

   Which announcement types exist in https://contoso.omniacloud.net/sites/hr?

::

   Add an announcement type called Maintenance, in English and Swedish

.. TODO screenshot: Claude listing the announcement types

::

   Rename the Maintenance announcement type to Planned maintenance

Good to know
************

+ A type has a **title only**, and the title can have a value per language.
+ Types are **per business profile**. The same name has to be created separately in each part of the intranet that needs it.
+ Renaming a type changes it everywhere it is used - existing announcements keep the type and show the new name.
+ Removing a type that announcements still use leaves those announcements without a type.
+ When you create an announcement without naming a type, the existing types are offered as a list, with **None** as a valid answer.

Actions
*******

+ ``AnnouncementType.List`` - the types in this business profile.
+ ``AnnouncementType.GetById`` - one type in detail.
+ ``AnnouncementType.Add`` - add a type.
+ ``AnnouncementType.Update`` - rename a type.
+ ``AnnouncementType.Remove`` - remove a type.
