6.12.21
========================================
(Omnia 6.12.21 / Workplace 6.12.11 / WCM 6.12.13 / MS 6.12.10)

- Stability improvements to the MS Teams provisioning flow.

6.12.19
========================================
(Omnia 6.12.19 / Workplace 6.12.11 / WCM 6.12.13 / MS 6.12.10)

- Corrected an issue in table style rendering between edit and view mode (#140402).
- Updated compatibility with certain RSS feeds for the RSS block (#144853).
- Added the option to force a full sync to the Azure AD sync.
- Corrected query logic in page rollup when using the same page collection multiple times (#145258).
- Permissions will now apply correctly when breaking inheritance (#145519).
- Ensured User Profile completeness will reach 100% when configured and filled in to do so (#144806).
- Click out now works as expected for the document properties dialog.
- Document Types can now use a term set with reused terms
- Several improvements to the SharePoint User Profile sync, including the option to resync all failed users.


6.12.17
========================================
 (Omnia 6.12.17 / Workplace 6.12.10 / WCM 6.12.12 / MS 6.12.9)
 
 - Improved compatibility for naming policies when using both omnia and M365 policies at the same time (#143531).
 - Added clear warning message of the consequence of terminating an enterprise property (#145119).
 - Fixed a section rendering issue casing edit and view mode to display differently (#145087).
 - It is now possible to assign permissions to teamwork where the teamwork SharePoint site has been deleted (#144942).
 - Fixed a RTF rendering issue in relation to block quotes (#141760).
 - Fixed a rendering issue in the people rollup card view (#145152).
 - Fixed an issue with pick page in page rollup.

6.12.14
========================================
 (Omnia 6.12.14 / Workplace 6.12.9 / WCM 6.12.11 / MS 6.12.8)
 
 - Second review reminder emails in Controlled Documents are now sent as expected.
 - Teamwork provisioning templates now only allow the selection of supported languages.
 - Stability improvements to RTF images in relation to drag and drop.
 - Publishing Apps and Communities with status “Ready With Warning” will now show up in the Publishing app and community rollup respectively. 
 - Stability improvements to moving documents between authoring sites in Controlled Documents (#145064).
 - z-index fix to the modern mega menu (#144844).
 - Fixed an issue that could cause appendices to show duplicated (#144868).
 - Improved stability to teamwork creation (#143355).


6.12.12
========================================
 (Omnia 6.12.12 / Workplace 6.12.8 / WCM 6.12.10 / MS 6.12.7)
 
 - Added additional settings to the New MS Stream media provider.
 - Corrected an issue in setting Site Collection Administrator as AD group via Omnia (#144639). Also fixes (#144357).
 - Search improvements to people search, full email search should now work as expected (#136764, #140571).
 - Added additional logging to search flows for improved troubleshooting (#144296).
 - Corrected a breaking API change in the Page Query API (#143495).
 - Updates to naming policy behaviours to better align with M365 OOTB policies (if set) (#143531).
 - Added information that search spelling suggestions only work in English (#144301).
 - OneDrive no longer show up as an option when running Omnia OnPrem.
 - Fixed an issue with RSS rendering of certain feeds (#144233).
 - Corrected a rendering issue with black boxes around tabs. Box and margin now only show when running with accessibility on. (#144593, #143957).
 - Improved logic for copying ODM documents (#144023).
 - Stability improvements to ODM document publish flow (#144858).
 - Copying images from different RTF source now have much better compatibility. (#143366).


6.12.9
========================================
 (Omnia 6.12.9 / Workplace 6.12.7 / WCM 6.12.9 / MS 6.12.5)
 
 - Updated support for MS Teams provisioning to support more channel languages (#143862).
 - Corrected a client-side store issue related to rename node (#143966).
 - Corrected a design issue on the page rollup card view (#143795).
 - Improved stability when login tokens expire in SPFx (#140929).
 - Corrected a current node race condition for the page rollup (#143797).
 - Event management outlook events are now prevented from being forwarded (#133219).
 - An archived node no longer shows up in move page (#143811).
 - Accordion section setting to always show expanded now works as expected (#144259).
 - Several improvements to the RTF editor in regard to copying images between omnia pages and from MS Teams.
 - Several improvements to the page rollup targeting system (#144090, #143919).
 - Hide if no content logic updated to always show content when supposed to (#144297, #144843, #144226).
 - Page rollup query builder settings no longer affect when page rollup in pick pages mode (#144600, #144602).


6.12.7
========================================
 (Omnia 6.12.7 / Workplace 6.12.6 / WCM 6.12.6 / MS 6.12.3)
 
- Improved loading stability of SPFx integration (#140929).
 - Corrected a display template race condition that would sometimes case parts of search to not render correctly (#142194).
 - Improved support for MS Teams dark mode.
 - Fixed an issue with User Profile Card exclusion filters.
 - Stability improvements to MS Teams Tabs and Channel provisioning.
 - Automatic translations correctly update the page rollups (#143502, #143548). 
 - Fixed an issue where the related processes icon would sometimes not render correctly (#143314
).
 - Controlled Documents attachments now correctly open in a new tab (#143181). 
 - Also fixes #142359.

 
 6.12.4
========================================
 (Omnia 6.12.4 / Workplace 6.12.3 / WCM 6.12.3 / MS 6.12.2)
 
- Improved performance for the page rollup.
- Corrected an issue with upgrading the Controlled Document library feature
- Exclude variations now works as expected in the Digital Signage API (#142800)
- Corrected an issue with copying and pasting multiple images in RTF.
- Updated icon for comments/page with no reaction.
- Corrected an issue with Controlled Documents where a blank space would sometimes be incorrectly added (#142753).
- Corrected stepper rendering on narrow screens (#142446).
- Tags handling now better supports multiple tags with different casing (#142544)
- Help text now show up on all text block modes (#143151).
- Corrected an issue where a section would move during the publish process (#142611).
 
 

6.12.0
========================================
(Omnia 6.12.0 / Workplace 6.12.0 / WCM 6.12.0 / MS 6.12.0)

Omnia
*****
-	All blocks now hide and show "no data" messages consistently (#127257, #128888, #129537, #131965, #133529, #138982)
-	Social reactions are now available including a revisit of all comment components for improved consistency (#138539).
-	Audit log improved to contain the start and end of a page archive action.
-	The setup wizard now supports "Basic Intranet" as well as Teamwork Content.
-	A sneak peak of what is to come as been added to the setup wizard.
-	Fixed a bug that would cause the link picker to highlight multiple categories. (#137969)
- 	Corrected a styling issue in the media picker that would sometimes cause white text on white background (#141818).
- 	The Setup Wizard has gotten several improvements as well as the option to provision a basic intranet, a solution with only one publishing app. 
-	The default settings for the RTF editor are now correctly populated (#137218).
-	The metrics block has received an updated design.
-	Machine translations are now extendible making it possible to plug a third-party provider into Omnia for translations.
-	Central image locations are now central media locations and will also support video stored in SharePoint.
-	Omnia admin has gotten a small restructure, Microsoft 365 and Services integration points have been clustered into their own categories.
-	Emoticons can now be enabled in the RTF editor.
-	The blockquote style has been corrected in the RTF editor. 
-	Added MS Teams presence to Posts, Organization tree and Teams Channel feed.
-	Document upload in picker and settings have been streamlined, see main release notes.
- 	Several performance improvements and security patches of related libraries.


Web Content Management
******

-	Social reactions can now be used instead of just likes. 
-	Gifs via Giphy can now be inserted into comments and content (#126061).
-	Navigation nodes to specific layouts can now be exposed in the WCM editor. This together with the new Page Rollup capabilities solves all editorial listing issues (#127215, #116794, #117789, #127484)
-	The page rollup can now show any query as a count metric.
-	The page rollup card view can now show the latest comment.
-	Documents in a document property can now be previewed on the page rollup.
-	The Editor now has adjustable panels to the left and right, resolving many spacing issues in that UI. (#124216)
-	Central Media Locations now supports picking videos stored in SharePoint (#134797).
-	Its now possible to create metrics using the count of a page rollup. (#123253).
-	RTF: Copy from word with multiple images greatly improved. (#137289)
-	RTF: Improved the rendering of option buttons when right aligning an image (#138182, #139470).
-	Image too large warning box have improved design and wording.
-	A page collection can now be changed between flat or hierarchy in the UI. 
-	Fixed an issue with the sign-off request block making it impossible to leave the title empty (#141758).
-	Improved UX for the publishing app setting UI. 
- 	Naming updates for a number of columns in the Page Rollup to better match what they are (example: "Reaction Count").
- 	Page Types can now be deleted even if there are old versions of pages using that page type.
-	Page collection nodes in the WCM editor are now ordered as: Default page collection on top, rest in alphabetical order (#135404).
- 	When opening a second WCM editor (e.g., the tenant page types in Omnia admin), the first editor will automatically close. 
-	Like/React and Share is now available in the page rollup dialog view.
-	Improved stability of the copy block feature.
- 	Better breadcrumb rendering for RTL languages.
-	Corrected an issue where the term options on a page would be in the wrong language (#139500).
-	The left navigation will no longer us break word in its styling (#138638).
-	Corrected logic for archiving, the comment will only be mandatory when multiple pages will be deleted (#124125).
-	The FAQ block now correctly gets its language from the Business Profile (#137196).
-	Corrected alignment of the people rollup card properties.
-	Copy banner now works as expected (#138302).
-	Corrected an issue where mentioning a user would cause the browser to hang (#141782)
-	Event management copy event will now work even when no system account for event management is setup (#127051).
-	Several stability improvements to Event Management, outlook invitations will now behave as expected (#133773).)
-	Improved export to excel in the page rollup.
-	Approvals can now be configured to only apply to Authors and not editors (#120455).
- 	Queries and filtering for the Process datatype now works as expected in the Page Rollup. 
- 	Corrected an issue where the browser title would be lost of filters are kept by query string.
-	An administrator can now correctly remove other people’s comments. 
-	Improved handling of time zones in page data.
- 	Corrected an issue with page property padding (#138463).
- 	Digital signage now supports display names for term properties and display names for people properties. 
-	Page rollup can now show targets in its statistics centred views.
-	Page rollup Channel filter now correctly has a scrollbar.
-	Improved stability for the Publishing App Admin sync to Site collection admin (#139157, #140381).
-	Community pages can now be correctly shown in the page rollup via "App" query scope.
-	A page collection can now be connected to a taxonomy, making each page create a taxonomy term.
-	A new action has been made available to the action button to add any page to your calendar via an .ics file.
-	Term "Pending Publishing" has been renamed "Unpublished Changes" in the page rollup for clarity.
-	Team news rollup now show thumbnail correctly.
-	QR code block can now render a QR code of the URL of the current page.
-	Digital signage have a new and improved design.
-	QR codes also supported in Digital Signage HTML views.
- 	Calendar rollup now correctly respects the UI item limit setting (#140246).
-	HTML tables should now keep their style and position when processed by machine translation.
- Tags have been improved, they can now be added directly in the RTF editor. 
- Page rollup card view now has explicit settings for where on the card to show different metadata.
- Creating App/Teamwork in dialog mode now renders correctly (#141474).
- Sort in page rollup now works as expected when querying by navigation path.




Search and People Rollup
*****
-	Corrected an issue where the search dialog would not close correctly on navigate (#139364, #140210). 
-	Spelling suggestions are now available for searching (#116122, #116114, #126845).
-	Search queries can now use a number of tokens to combine user properties, user language, page properties and app instance properties into intelligent search queries (#115142, #115263, #120230)
- Document Rollup and People Rollup can now use a number of tokens to combine user properties, user language, page properties and app instance properties into intelligent search queries.
-	Search statistics are now available in omnia admin, see main release notes.
-	Fixed a race condition that would sometimes cause the previous search result to be rendered (#137980).
-	Shared Links item template now includes description and has aligned its look and feel with other views.
-	Date refiners can now have a default value.
- 	Corrected an issue with paging in the search (#139335).
-	A permission role for Search has been added (Search Administrator).
-	Quick search now shows the total numbers of results in advanced search for each category.
-	Birthday queries can now be made in the people rollup. 


Teamwork and Workplace
***********

-	Security groups can now be correctly synced to SharePoint on Team Sites and Communication sites (#140845).
-	Updates to Active/Inactive Teamwork metrics.
-	The Omnia header no longer shows incorrectly in some MS teams Tab types (#139911, #139956).
- 	The all tab in "Manage Links" now behaves the same as the "All Links" option in search on my links (#131815, #139096)
- 	Teamwork navigation will now always open a SharePoint site in a new tab (to prevent issues from within the MS Teams client (#133140).
-	A Process can now be shown in the context of a project Team, see main release notes for more information.
-	Omnia App Instance properties can now be access from within MS Teams via a new button.
-	The User profile completeness block now works correctly in Dark Themes (#140327).
-	Added correct validation of length of title and alias when creating teamwork (#140627).
-	Security on App level has been removed from Omnia Admin; it is no longer needed.
-	Corrected an issue with Announcement emails, they now replace tokens correctly.
-	App Instance properties can now be shown/hidden per property in new and edit forms respectively (#123637, #118788).
-	Images can now be attached on a post in the posts block.
- 	Team News Rollup now supports more news image thumbnails. 
-	The teamwork rollup can now open the associated omnia layout instead of the teamwork resource itself.
- Updated email template on comments for important announcements. Title token now works as expected.
- Teamwork title and Alias now correctly validates max length that is enforced by Microsoft (#131843, #142447).
- Updated the way we set members in the teamwork creation wizard for better compatibility with MS Teams (#141688).



Management System
*****

-	Document management now integrates with Draftable, see main release notes.
- 	A signed copy can now be uploaded to published documents, see main release notes. 
-	Date format of tokens in documents can now be set by putting the formatting in the token. Example: [[InternalName|YYYY-MM-DD]].
-	Corrected an issue in the Swedish feedback email (#14026).
-	Documents can now be flagged as “Is Record” allowing the admin to disable certain actions such as create draft (#123956).
-	Metadata can now be inserted into the content of excel files.
-	Marco enabled files now have correct higher resolution icons (#139585).
- 	Process Management print functionality now better supports inline images. 
-	When publishing a page, the properties dialog will now clearly indicate which properties are missing (#117951, #138156).
- 	Corrected the query logic for Draft Controlled Documents (#138189).
-	Default document template can now be removed from a document type.
- 	Corrected an issue that would sometimes show "undefined" in the create document dialog. 
- 	Fixed an issue that would case the wrong document to open in the managed properties dialog on a controlled document (#139906).
-	Workflow history has been improved to more clearly show which action were taken for a specific document.
-	Metadata placeholders are now supported in PowerPoint.
-	Improved timer job workflows to use the correct modified by user when possible (#122298).
-	All Controlled documents view now correctly follow the Tenant Regional setting by default.
-	Property help texts are now available in when creating or editing controlled documents.
-	Built in ODM properties now handle time zones in a better way (#128197, #128348, #128544, #128345).
-	A document type can now be declared a document type for "records" this will allow the admin to disable some actions on that document.



WCAG
********
-	Configurable arial role has been added to all buttons in the Workspace action menu.
-	User profile completion block is now WCAG compliant. 
-	Improved keyboards controls for comments, tabs block, Action menu and card view in page rollup.
-	Dynamic roller view next/prev arrows now has correct aria labels.
-	The RSS viewer will now show alt-text if supported by the RSS feed (#119782).
-	The tabs section now supports keyboard controls.
- Improved keyboard controls for the advanced search.
- Added alt text to the placeholder image in the page rollup.

Also fixes preview issues: #142201, #142533, #142203, #142204

