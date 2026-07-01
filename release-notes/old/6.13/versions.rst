6.13.31
========================================
(Omnia 6.13.31 / Workplace 6.13.17 / WCM 6.13.19 / MS 6.13.14)

- Performance improvements to 7.0 preparation user sync.

6.13.27
========================================
(Omnia 6.13.27 / Workplace 6.13.17 / WCM 6.13.19 / MS 6.13.14)

- Stability improvements to 7.0 preparation user sync.

6.13.21
========================================
(Omnia 6.13.21 / Workplace 6.13.17 / WCM 6.13.19 / MS 6.13.13)

- Improved stability in move controlled document (#148602).
- Fixed an issue that prevented the deletion of appendix.
- Language is now set correctly when incorrect syntax is returned from MS Graph (#146619).

6.13.20
========================================
(Omnia 6.13.20 / Workplace 6.13.17 / WCM 6.13.19 / MS 6.13.12)

- Printing now displays all content of a page (#148147).
- Additional auto translation improvements (#148172).

6.13.19
========================================
(Omnia 6.13.19 / Workplace 6.13.16 / WCM 6.13.18 / MS 6.13.11)

- Media picker can now pick .wmv and .webm files (#147845).
- Copy text from clipboard now works as expected for MacOS (#146794).
- Fixed an issue with navigation path in the page rollup (#147488).
- Fixed an issue with the current navigation. (#148491, #148513, #148503)
- Users time zone is now fetched from the client instead of the mailbox settings, this improves performance and reduces permissions needed for the Omnia AAD app (#146999) 
- Fixed an issue with calculated fields on old data (#147541).
- Fixed an incorrect replacement for custom domain tenants causing permissions to not be saved (#145993).
- Improvements to auto translations (#148051).



6.13.13
========================================
(Omnia 6.13.12 / Workplace 6.13.15 / WCM 6.13.15 / MS 6.13.10)

- Custom sort order for Quick links now works as expected when used without a category (#144409).
- Improved logic for pasting content from Excel and PowerPoint (#147467).
- Corrected the email template for Notifications for Controlled documents (#147345).
- Updated to publish flow of controlled documents to ensure better compatibility with migrated documents (#147242, #147451).
- Updated the max number of refiners in the Document rollup to 500 (#147677).
- Fixed an issue that would cause Birthday to no render correctly for some users (#147208).


6.13.12
========================================
(Omnia 6.13.12 / Workplace 6.13.15 / WCM 6.13.15 / MS 6.13.10)

- Outlook events created through Event Management now contain the correct time zone (#147063, #142261).
- Links in related links now open as configured (#147389).
- Fixed an issue that prevented page type filters from rendering correctly in the page rollup (#147243).
- Admin can now correctly delete other people’s sign-off requests (#147047).
- Stability improvements to the controlled documents publish flow (#147157).
- Improved login flow for SPFx when using custom domain for Omnia.


6.13.11
========================================
(Omnia 6.13.11 / Workplace 6.13.14 / WCM 6.13.14 / MS 6.13.8)

- Auto detect language now works as expected. 
- Default value properties on pages now works correctly in a scaled-out environment (#146935).
- Stability improvements to setting edit permissions on individual pages.
- Teamwork rollup links now use the Default context URL instead of the root URL to resolve links (#146737).
- Document Management statistics should now show correct numbers (#146555).
- Stability improvements to the creation of Document Management tasks (#146798).
- OnPrem: Omnia now supports additional server date formats (#146848).
- Stability improvements to Document Management email generation (#145549).


6.13.10
========================================
(Omnia 6.13.10 / Workplace 6.13.13 / WCM 6.13.13 / MS 6.13.7)

- Sign off request sign off has an improved experience in mobile (#146679).
- Stability improvements to the Controlled Documents Library feature.
- Updated permissions to prepare for the 7.0 upgrade.
- Updated Norwegian translations (#146459).
- Several smaller fixes to the Sign-Off Request feature (#146679, #46317)
- Preconfigured images from the page type now works as expected (#146634).
- Stability improvements to move page functionality (#146636).


6.13.9
========================================
(Omnia 6.13.9 / Workplace 6.13.11 / WCM 6.13.11 / MS 6.13.5)

- Fixed an additional issue in naming policies together with approval (#143531).
- Fixed a rendering issue in Sign Off Request. User who completed request now displays correctly.
- Fixed a rare race condition that would cause scheduled pages not to publish on time.
- Date properties now work as expected on documents in all time zones (#146383).



6.13.7
========================================
(Omnia 6.13.7 / Workplace 6.13.9 / WCM 6.13.10 / MS 6.13.4)

- Improved Sync to SharePoint to ignore ASCII control characters (#145817)
- Blocks using User Profile Property targeting will cause page to not load for guest users.


6.13.6
========================================
(Omnia 6.13.6 / Workplace 6.13.8 / WCM 6.13.9 / MS 6.13.4)

- OnPrem: Settings for spellcheck are now hidden due its cloud only nature.
- OnPrem: Last activity for teamwork now works as expected.
- Stability improvements to pages that are both scheduled and under approval. 
- Fixed an issue where certain properties would become queryable properties on feature upgrades.


6.13.5
========================================
(Omnia 6.13.5 / Workplace 6.13.7 / WCM 6.13.8 / MS 6.13.3)

- Improved logic for footer in the print process feature (#145623)
- Ensured rendering of the dynamic roller on mobile (#145261).
- Corrected bug that would cause nodes in the WCM editor to expand on contract when not supposed to (#145858).
- Stability improvements to publish processes (#145658).
- Increased max page size on the navigation query in the page rollup from 30 to 200 (#145096).
- Resolved issues related to large groups in Sign-off requests. (#145822, #145897).
- Performance improvements to creating sign-off requests. (#145824).
- Ensured soft deleted processes no longer show up as related processes in Document Management (#145856).
- Base URL for draftable can now be set in Omnia Admin.
- Fixed a paging bug in event management (#145585).
- Fixed a cache problem that would occur when publishing page types and the total amount of page types exceeds 9 (#145801, #145836, #145893, #145898, #145960, #145984).
- Added back shortcut actions to the tasks form in Document Management.


6.13.1
========================================
(Omnia 6.13.1 / Workplace 6.13.1 / WCM 6.13.2 / MS 6.13.1)

- Reindex to SharePoint now correctly keeps original modified date (#145591).
- Fixed a width rendering issue in the current navigation (#145610).
- Fixed an issue with send email in send for comments flow when sites have been deleted.
- Fixed an issue with filters for channel in the page rollup.


6.13.0
========================================
 (Omnia 6.13.0 / Workplace 6.13.0 / WCM 6.13.0 / MS 6.13.0)


Setup Wizard
***********

- Now supports the setup of Knowledge sharing.
- Now supports the setup of a Learning Center.
- Now support additional News Centers. 
- Setup wizard can now be accessed from Omnia Admin in Business Profile and Tenant scopes, respectively. Old query strings are removed.
- Added default SharePoint search mapping for built in user fields.



Web Content Management
***********

- Fixed an issue that prevented the Channels admin UI to load correctly (#143892).
- Added support for scenarios when channels and variations are combined in the page rollup (#141379).
- Improved UX for commenting on mobile, the keyboard now opens automatically.
- Posts block now manages permissions in a better way (#143491).
- Digital Signage now supports video and Static Content.
- Modified by now works as expected when used as a property in the JSON based endpoint of Digital Signage.
- Performance improvements for the Page Rollup.
- Improved stability for move page and move page collection. 
- Corrected the page collection and publishing app sorting in the page picker (#143406).
- Now possible to more easily rollup pages checked out by me that have already been published.
- Fixed several z-index issues with dialogs and the workplace megamenu.
- Ensured Tab rendering (#145162).

Teamwork
*********
- Corrected an issue where saved sensitivity label setting "Let the user decide" would not repopulate correctly in the form.
- Modified by now works as expected when used as a property in the JSON based endpoint of digital signage.

Workplace
********
- The User Profile Completion Wizard taxonomy picker no longer closes upon selection (#142754).
- Fixed an issue where the posts block would not always show its context menu.

Sign Off Requests
***********

- Sign Off Requests now supports any enterprise property as metadata.
- A new section for queryable properties for Sign Off requests have been added. 
- A new Sign Off Request rollup has been added which includes configurable columns.
- A new type of Sign Off Request is now available, Group Request. This allows for multiple people to Share the same sign off. 
- A new detail view of sign of requests. 
 

Document Management
***********
- Controlled documents now have an improved recycle bin.
- Direct links to New Stream videos can now be used in the Media picker.
- Added a clearer end user message when changing document template in Controlled Documents (#143514).


System
***********
- MS Teams Manifest updated to the latest version (Used when generating MS Teams apps through the Omnia admin interface.)
- Performance improvements on publishing pages.
- Its now possible to Remove features completely via an API call (For Extensions development).
- Stability improvements in the Page Archive flow.
- In preparation for future rollouts, Omnia can now run in a Read Only mode.
