Azure AD permissions
====================

Omnia asks for permissions in Azure AD - to read users and groups, to reach SharePoint, to send mail on a user's behalf. Some of those permissions need a tenant administrator to grant consent before the features that depend on them can work. The connector can read that whole picture, which makes it a quick way to answer "why is this feature stuck?".

.. TODO screenshot: Azure AD permissions in Omnia admin, for reference

What you can ask for
********************

+ Whether anything currently needs admin consent, and the URL an administrator opens to grant it.
+ A per-service summary, with how many permissions are unapproved.
+ The permissions of one service, and which extensions and features require each one.

Example
*******

::

   Does anything in Omnia need Azure AD admin consent?

.. TODO screenshot: Claude reporting the consent status and per-service counts

::

   Show the unapproved permissions for Microsoft Graph and what needs them

.. TODO screenshot: Claude listing one service's permissions

Reading the result
******************

+ Each service is reported with how many permissions are **in use and unapproved**, and how many are **unapproved in total**. The difference matters: only the in-use ones actually block anything, which is what "needs consent" is based on. The total also counts permissions nothing currently uses.
+ Each permission says whether it is an **application** or a **delegated** permission, whether the tenant has **approved** it, and whether **Omnia currently asks for it**. Those last two are independent - a permission can be one without the other.
+ You can narrow a service's permissions to just the approved or just the unapproved ones.

Good to know
************

+ The **admin consent URL grants nothing by itself**. An Azure AD administrator has to open it. Reading it here is safe.
+ When the URL comes back empty, that is Omnia's way of saying nothing needs consenting.
+ If Omnia itself lacks the directory permission needed to read the permission state, you are told that explicitly rather than being shown a misleading "nothing needs consent".
+ If a name lookup fails, that is reported too - so an extension or feature that comes back without a name may be unnamed for that reason rather than because it does not exist.
+ This is a **read-only** area. Granting consent happens in Azure AD, and activating features happens under :doc:`../feature/index`.

Actions
*******

+ ``AzureAdPermission.List`` - the consent status, the admin consent URL, and a per-service summary.
+ ``AzureAdPermission.Get`` - one service's permissions, and what requires them.
