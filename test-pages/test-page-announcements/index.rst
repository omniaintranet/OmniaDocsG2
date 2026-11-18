Test page AI generated Announcement settings
================================================

This page explains how to manage tenant-wide announcements in Omnia Workplace. It covers the announcement list and its **Status and Types** settings. It does not cover the separate display settings for an Announcements block placed on a page.

Access
*********

In the Admin experience, open **Tenant > Announcements**. The navigation item is available to users with the **Announcements Tenant Admin** role (`AnnouncementsTenantAdmin`).

Tenant announcements are managed separately from business-profile announcements. Tenant announcements can be included alongside the current business profile's announcements in the user-facing announcements experience.

Manage announcements
***********************

The list shows each announcement's **Title**, **Priority**, **Order**, **Created By**, and **Modified By**. Use **Create** to add an announcement, select an existing row's edit action to change one, or use its delete action to remove it.

Create or edit an announcement
---------------------------------

The form provides these fields:

| Field | Description |
|---|---|
| **Title** | Localized announcement title. Required. |
| **Description** | Localized rich-text content. Required. |
| **Priority** | **High** or **Normal**. Required. |
| **Order** | Position among announcements of the same priority. High- and normal-priority announcements have separate order choices. |
| **Start Date / End Date** | Set the announcement's display period. |
| **Type / Status** | Optional classifications selected from the tenant's configured types and statuses. |
| **Allow comments** | Lets users comment on the announcement. |
| **Allow users to close announcement** | Available for high-priority announcements; lets users dismiss/close them. |
| **Targeting filter** | Limits the audience according to the selected targeting criteria. |

Select **Save** to apply changes or **Cancel** to leave the form without saving. When editing a high-priority announcement, Omnia asks whether it should be displayed again. Choosing **Yes** marks it to be redisplayed; choosing **No** saves the edit without that flag.

Configure statuses and types
********************************

From the announcement list, select the **Status and Types** settings action.

Types
---------

A type has a localized **Title** and an **Icon**. Add a type with the add action, edit its title or icon, and save with the checkmark. The icon picker supports the icon options provided by Omnia.

Statuses
-----------

A status has a localized **Title**, **Background Color**, and **Text Color**. Add a status with the add action, edit its values, and save with the checkmark.

For both types and statuses, use the cancel action to discard an unsaved add or edit. The delete action asks for confirmation before removing the item. These configured values are offered in the announcement form's **Type** and **Status** fields.

Tenant-scope titles use the tenant's configured languages. Enter translations for the languages that should display to users.

Notes
**********

- The tenant announcement list manages tenant-scope announcements; business-profile announcements are managed separately under the corresponding business profile.
- Users can see tenant announcements together with their business-profile announcements where the announcements experience includes tenant-scope items. Targeting and the announcement's active period still affect which announcements are shown.
- The announcement list's **Order** column is an ordering value, not a date or priority setting.




