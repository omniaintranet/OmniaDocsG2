Publishing App
==============

A Publishing App is a live site in a business profile - a news site, a policy library, a department site. It is always provisioned from an existing :doc:`Publishing App template <../publishing-app-template/index>`, which decides its permissions, features and metadata. The connector can list the apps in a business profile, look at one app in detail, and create a new one.

What you can ask for
********************

+ List the Publishing Apps in this business profile.
+ List other kinds of apps in the business profile, such as workspaces or communities.
+ Look at one app - its status, address, administrators and the template it was created from.
+ Check whether an app that is being created is ready yet.
+ List the kinds of apps that exist in the tenant.
+ Create a Publishing App in this business profile from one of the available templates.

Listing apps
************

::

   List the Publishing Apps in https://contoso.omniacloud.net/sites/hr

The list is sorted by title and includes **every app, whatever its state** - apps that are still being created and apps whose creation failed are listed next to the ready ones, each with its status. Each app also comes with its address and the template it was created from.

.. TODO screenshot: Claude listing the Publishing Apps of a business profile

By default the list is of Publishing Apps. To list another kind of app in the same business profile, name it:

::

   List the workspaces in this business profile

The kinds of app the connector can list come from the tenant's **app definitions** - Publishing App, Workspace, Community and so on. You can ask for them directly:

::

   What kinds of apps exist in this tenant?

Looking at one app
******************

::

   Show me the details of https://contoso.omniacloud.net/_/team-news

You get the app's title and description, its address, its status, who its administrators are, which template it was created from, and when it was created and last changed.

Asking again is also how you follow an app that is being created. The connector does not wait for provisioning to finish - it tells you the status right now, so ask again until the app is ready:

::

   Is the HR News app ready yet?

If the creation failed, the status says so and the reason Omnia recorded is included.

.. TODO screenshot: Claude showing the status and details of one Publishing App

Creating an app
***************

Ask for the app and let the connector offer the templates you can use:

::

   Create a Publishing App called "HR News" in
   https://contoso.omniacloud.net/sites/hr

.. TODO screenshot: Claude presenting the eligible templates

Then answer any metadata the template asks for. If the template uses a property set, the members marked required need values - unless the template already supplies a default for them:

::

   Use the News template, description "News and updates from HR",
   and set Owner to the HR communications team

.. TODO screenshot: the new Publishing App in the Omnia interface

Good to know
************

+ Listing apps needs a **business profile** scope. Looking at one app needs a **Publishing App** scope - paste its URL, or pick it from the list first. Listing the kinds of apps needs only the tenant.
+ An app that is still being created, or whose creation failed early, may have **no address yet**. The rest of its entry is still correct.
+ The statuses **Ready** and **Ready with warning** mean the app can be used. **Error** means provisioning failed.
+ Administrators are shown as identities - the connector tells you whether each one is a user, a group or a role.
+ If the template an app was created from has since been deleted, the app's details are still shown, just without the template.
+ The list of app kinds includes kinds that Omnia hides from its own pickers, marked as hidden, so you can still recognise apps of that kind.
+ Creating an app needs a **business profile** scope and the permission to create apps there.
+ Only templates in **this business profile** that are for native Omnia sites are eligible. Templates attached to SharePoint are not yet supported by the connector.
+ The **address is generated from the title** when you do not give one. It has to be unique both as an Omnia address and as a SharePoint site alias across the tenant; if it is taken, you get a suggested alternative to retry with.
+ **You become the app's only administrator.** A template that requires more than one administrator cannot be used through the connector yet, because there is no way to assign additional people here - use the Omnia interface for those.
+ A required property with no value and no template default stops the creation, with the missing properties named.

Actions
*******

+ ``PublishingApp.List`` - the Publishing Apps, or apps of another kind, in the business profile, in every state.
+ ``PublishingApp.Get`` - one app with its status, administrators and template.
+ ``AppDefinition.List`` - the kinds of apps registered in the tenant.
+ ``PublishingApp.Create`` - provision a Publishing App from a template.
