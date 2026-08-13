6.8.0
========================================

- Guest users are now supported in Omnia Feed. Note: The domain needs to be supplied by the end user. (#136414).
- Its now possible to login using either UPN or Email.
- Corrected an issue related to targeting with certain user types (#136890)
- Corrected an issue with the notification counter (#136470, #126973)
- Deletions of signoff requests are now handled correctly. 
- Improved performance for G1 customers.


6.7.1
========================================
- Improved login stability.

6.7.0
========================================

- Intune SDK has been implemented. This should help solve login problems for any customer using Intune. 
- Its now possible to create queries for pages that has no value set in a specific property field. 
- You can now choose which business profiles are shown for selecting in the app.
- Sign off request functionality is now available as part of the 6.7 release. 
- And several other fixes and improvements (#134930).


6.6.0
========================================

- Major performance improvments.
 - Data load from the app.
 - Improved detection of Important Announcements and Pages.
- Better error handling (#134054).
- Variation setting logic is now aligned with the Page Rollup.
- When explicitly logging out, notification will no longer be sent (#120725).
- All comment and like notifications are now configurable
- Corrected an issue that would sometimes prevent RTF images from being displayed (#132697).
- All labels in the Mobile App can now be translated. Translated versions of the app will be rolled out shortly after release.
- Additional color settings for different elements in the mobile app. Per Business Profile. 
- Date Filters can now be made in page queries. 
- Current user filters can now be made in page queries.
- RTF Styles for tables have improved.
- When navigating to a web tab in the app, it is reset to avoid being stuck in certain login scenarios (#132296).
- Targeting is now possible on the tabs. 
- And several other improvements.



Versions
-----------------------------------------

.. toctree::
   :titlesonly:

   versions
