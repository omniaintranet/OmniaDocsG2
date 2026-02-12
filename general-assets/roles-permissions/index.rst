Roles and permissions in Omnia
==================================

This page contains a short overview of roles and permissions in Omnia.

Roles and permissions in Omnia admin
****************************************

Tenant Administrator
----------------------
A tenant administrator can: 

+ Edit all tenant settings in Omnia admin.
+ Add colleagues to various permissions within the tenant.
+ Create business profiles and add business profile administrators.

These permissions can be set for the tenant:

.. image:: permissions-tenant-new.png

**Directory Reader**: Can view all user profiles in the user directory (read-only access). This includes permissions to use the identity picker for selecting users and to access aggregated user information in the people rollup using the Users scope.

**Shared links administrator (tenant)**: Can use all Shared links options for the tenant.

.. image:: shared-links-tenant-new.png

**Announcements administrator (tenant)**: Can use all announcements options for the tenant.

.. image:: announcements-tenant.png

**Block gallery editor**: If the block gallery is used, additional editors can be added here. Tenant administrators can always edit the block gallery.

**Semantic search reader**: If Semantic search is activated in the tenant, the colleagues and groups that should be able to use semantic search must be added here. For more information about semantic search, see the heading *The semantic search reader setting* on this page: :doc:`Permissions for the tenant </admin-settings/tenant-settings/permissions/index>`

Business profile administrator
--------------------------------
A tenant administrator creates the business profiles needed, and adds at least one administrator for each business profile.

A business profile administrator can:

+ Edit all settings for the business profile, in Omnia admin.
+ Edit permissions for the business profile, including adding and removing business profile administrators.
+ Create publishing apps in the business profile and add publishing app administrators.

These permissions can be set in the business profile:

.. image:: permissions-bp.png

**Business profile viewers**: To be able to access a business profile and use the various user options, user’s must be added to the Business profile viewers list. 

**Workspace designer**: Can work with all workspace settings within the business profile.

.. image:: workspace-settings.png

**Workspace contributor**: Users/groups that should be able to comment on business profile announcements and be able to send organization wide posts, must be added as workspace contributors.

**Workspace reader**: Can use the workspace navigation within the business profile.

**Analytics readers**: All users that should have permission to see analytics data for the business profile must be added as “Analytics readers". That’s true for tenant administrators and business profile administrators as well. No administrator has automatic access to analytics. An analytics reader will also be added as a user within Matomo.

**Shared links administrator (business profile)**: Can use the options for Shared links within the business profile. 

**Announcements administrator (business profile)**: Can use the Announcements options within the business profile.

.. image:: announcements-bp.png

**Search administrator**: Can edit all settings for search within the business profile. 

.. image:: search-settings.png

Roles and permissions in a Publishing app
******************************************

Publishing app administrator
------------------------------
A business profile administrator creates the publishing app and adds at least one publishing app administrator. 

A publishing app administrator can:

+ Edit all settings for the app.
+ Create page collections within the publishing app and add page collection administrators.
+ Edit permissions for a page collection within the app.
+ Create and edit local page types, meaning page types that exists in a page collection in the app only (not tenant page types).
+ Delete a comment in the app (in the Page likes and comments block).
+ Create a form using an action button.
+ Act as a page collection administrator when needed.

The publishing app settings are available here:

.. image:: app-settings.png

**Publishing app contributor**: Contributor permissions is needed for colleagues that should be able to add comments to publishing pages. This permission can be set when editing app permissions:

.. image:: contributors-app-new.png

Roles and permissions in a Page Collection
*********************************************

Page collection administrator
-----------------------------------
Page collection administrators can be added to a page collection by the app administrator. A page collection administrator can:

+ Edit all page collection settings.
+ Edit permissions for the page collection: Administrator, Editor, Author and Reader permissions.
+ Edit the root page of the page collection (a page editor or author can not do that).

The page collection settings are available when the top node in the page collection is selected:

.. image:: top-node-settings-new.png

The permissions settings are available here:

.. image:: top-node-settings-permissions.png

And these permissions can be set here:

.. image:: page-collection-permissions-711.png

Note that all permissions for editing and deleting pages and cerating pages and other nodes, are inherited in the page collection, but permissions for specific pages and other nodes can be changed if needed.

Page collection permissions are described on this page: :doc:`General block settings </pages/page-collections/page-collection-permissions/index>`


