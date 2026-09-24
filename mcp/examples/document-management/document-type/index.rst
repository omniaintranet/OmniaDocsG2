Document types
==============

A document type is what a controlled document is filed under - "Policy", "Procedure", "Work instruction". It decides which metadata a document carries, which templates it can be created from, and how it behaves once it is published. Document types are arranged in a tree: **groups** hold other document types, and the document types a document can actually be filed under sit inside them. The connector can list, create and configure document types, one settings tab at a time or all at once.

.. TODO screenshot: document types in Omnia admin, for reference

What you can ask for
********************

+ List the document types, either one level of the tree or the whole tree.
+ Create a document type under an existing one.
+ Read back all the settings of a document type.
+ Check whether a new document type has finished syncing to SharePoint.
+ Change the settings of one tab - **General**, **Behavior**, **Change tracking**, **Properties** or **Templates**.
+ Change several settings of a document type in one go.

Listing document types
**********************

::

   List the document types in this tenant

Without anything more, you get the top level of the tree. Each entry tells you whether it is a **group** or a document type that can be **selected** for a document, and how many document types sit below it. To see everything at once:

::

   Show me the whole document type tree, including everything inside the groups

Creating a document type
************************

A document type needs a **title**, a **parent** and an **enterprise property set**. If you leave out the parent or the property set, the valid choices are offered as a list:

::

   Create a document type called "Policy Document" under Governance,
   using the Policy Metadata property set

.. TODO screenshot: Claude offering the parent document types and property sets as lists

What you get back is the new document type and its parent. It is created as a document type that documents can be filed under, not as a group, with every property of the chosen property set mapped to it.

The document type still has to be synced to SharePoint before a document can be created with it. To check:

::

   Has the Policy Document document type finished syncing?

Ask again until it is no longer reported as syncing.

Reading the settings
********************

::

   Show me the current settings for the Policy Document document type

The settings come back grouped the same way as the tabs you change them with - General, Behavior, Change tracking, Properties and Templates - plus the remaining settings, such as sign-off, archive, review reminder, retention and publishing approval, under **Advanced**. Asking for the settings before changing them is the easiest way to see what is there.

Changing one tab
****************

Each tab has its own action, and each one only changes what you mention - everything else is left as it is.

**General** - the title, the description and the parent:

::

   Change the Policy Document description to "Company-wide policies"
   and move it under Governance

**Behavior** - appendices, signed copies, records, whether drafts can be created, documents moved or unpublished, revisions, bypassing approval for revisions, replacing tokens on publishing, and how documents are created:

::

   On the Policy Document document type, allow revisions and enable signed copies

**Change tracking** - tracking changes when sending for comments, read receipts, and the change button and create-document icon shown to authors and in rollups:

::

   Enable read receipts and the rollup change button for the Policy Document document type

**Properties** - which enterprise property set the document type uses:

::

   Map the Policy Metadata enterprise property set to the Policy Document document type

**Templates** - which document templates can be used for documents of this type, and which one is pre-selected:

::

   Set the Policy Document document type's templates to Standard Policy Template
   and make it the default

.. TODO screenshot: Claude confirming a changed settings tab

Changing several settings at once
*********************************

When a change spans several tabs - or touches a setting that has no tab of its own, such as sign-off requests, conversions, semantic search, feedback recipients or per-property settings - ask for it in one request:

::

   On the Policy Document document type, turn on sign-off requests,
   allow appendices and make Standard Policy Template the default template

The connector reads the current document type first, applies only what you asked for, and checks the result against the same rules Omnia applies before saving it.

Good to know
************

+ Document types are managed at **tenant** level. The connector does not work around Omnia's permission model - without the right to manage document types you get Omnia's own refusal.
+ **Root document types are not supported.** A new document type always needs a parent, and a parent can never be removed or set to the document type itself.
+ A new document type starts with Omnia's **default settings**. Among them, **creating drafts, moving documents and unpublishing are turned off** - turn them on with the Behavior tab if you need them.
+ A new document type must be **synced to SharePoint** before a document can be created with it. Check the sync status before creating the first document.
+ A title, when you change it, must have a value in at least one language.
+ **Mapping a property set replaces the property mapping.** Every property of the set is mapped afresh, so any per-property settings made earlier - such as alternative internal names or fixed default values - are reset.
+ On the Templates tab, only **templates that exist** can be chosen - an unknown template is refused and the available ones are offered instead. The **default template must be one of the chosen templates**. Clearing the list of templates also clears the default.
+ A **group cannot become a document type**, or the other way round. Settings that belong to a document type are refused on it.
+ When several settings are changed at once, the combined result is checked before it is saved: the property set must exist, per-property settings must match properties in that set and their type, **Data and Media properties** cannot be configured, alternative internal names must be unique, and feedback recipients must be **person** properties of the set or the document's approver group.
+ Document types cannot be deleted through the connector.

Actions
*******

+ ``DocumentType.List`` - the document types at one level of the tree, or the whole tree.
+ ``DocumentType.Create`` - create a document type under an existing one.
+ ``DocumentType.GetSettings`` - all the settings of a document type, grouped by tab.
+ ``DocumentType.GetSyncStatus`` - whether a document type has finished syncing to SharePoint.
+ ``DocumentType.SetGeneral`` - change the title, description or parent.
+ ``DocumentType.SetBehavior`` - change the Behavior tab.
+ ``DocumentType.SetChangeTracking`` - change the Change tracking tab.
+ ``DocumentType.SetProperties`` - map an enterprise property set.
+ ``DocumentType.SetTemplates`` - choose the templates and the default template.
+ ``DocumentType.Update`` - change several settings at once, with validation.
