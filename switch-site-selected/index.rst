Switch to site selected
==================================

This guidance is for existing Omnia implementations. New implementations already use Sites Selected mode by default.

The recommended standard is to grant Omnia app access only to selected site collections. 

If you're on an existing implementation of Omnia, you can switch to site selected this way:

1. Make sure "Web content management core" is updated to latest version. 

2. Reconsent "Web content management core" (if update is not needed).

3. Activate the feature "Sites selected permissions" as a site collection admin, on all sites that have specific Omnia functionality:

+ Publishing apps.
+ Communities.
+ Sites with controlled document libraries.
+ Sites with process management authoring.
+ The document management archive site.
+ The default context site.

4. Confirm key Omnia functionality works on all affected sites before disabling legacy permissions.
5. Deactivate the feature "Legacy app permissions".
6. In Omnia Admin, open the Azure AD permissions page and copy the consent link.
7. Open the link and complete admin consent.

