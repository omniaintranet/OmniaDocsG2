Features
========

Features are the parts of Omnia that are switched on where they are needed. A feature is activated at one of three levels - the **tenant**, a **business profile**, or a single **app instance** such as a Publishing App - and the connector can list what is activated at each level and activate or deactivate it.

.. TODO screenshot: features in Omnia admin, for reference

What you can ask for
********************

+ List the features available at a level, with their current status.
+ Activate a feature.
+ Deactivate a feature.

Example
*******

::

   Which features are activated on this tenant?

::

   Which features are activated on https://contoso.omniacloud.net/sites/hr?

.. TODO screenshot: Claude listing features and their status

If you do not name a feature, the ones available at that level are offered as a list **with their current status**, so you can see that something is already active before you act on it:

::

   Activate the AI Engine feature on this tenant

.. TODO screenshot: Claude activating a feature and reporting the resulting status

Reading the result
******************

Activation and deactivation are asynchronous in Omnia. The connector waits up to 30 seconds and reports the last status it saw, which is one of:

+ **Not activated** - the feature could be activated here, but never has been.
+ **Activated** - it is on.
+ **Activating, Upgrading, Deactivating** and the waiting states - the platform is still working.
+ **Error** - the platform reported a problem, and the message comes back with it.
+ **Waiting for admin consent** - the work is blocked on a person, not on the platform. See below.

If the wait times out, that is **not a failure**: the platform is still working on it. Ask for the feature list again rather than activating a second time, which would start a second run.

Good to know
************

+ Each level needs its matching scope: the tenant, the business profile, or the app instance. For an app instance, the picker offers **Publishing Apps** - other kinds of app instance can be reached, but only with an id you already have.
+ Activating a feature needs the permission to manage features at that level.
+ Some features need **Azure AD admin consent** before they can finish activating, and they will wait indefinitely until an Azure AD administrator grants it. When that happens you are told so, and pointed at :doc:`../azure-ad-permission/index`, which has the consent status and the URL an administrator opens.
+ A feature can accept **properties** when it is activated. They are passed to Omnia untouched, and anything Omnia rejects is reported back on the result.
+ A feature listed as *Not activated* has no record yet - it only means it *could* be activated at that level.

Actions
*******

+ ``TenantFeature.List`` / ``TenantFeature.Activate`` / ``TenantFeature.Deactivate``
+ ``BusinessProfileFeature.List`` / ``BusinessProfileFeature.Activate`` / ``BusinessProfileFeature.Deactivate``
+ ``AppInstanceFeature.List`` / ``AppInstanceFeature.Activate`` / ``AppInstanceFeature.Deactivate``
