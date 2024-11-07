7.6.44
========================================
(Omnia 7.6.43 / Workplace 7.6.31 / WCM 7.6.33 / MS 7.6.24 / Analytics 7.6.2)

- The 404 page is now displayed if clicking on a link using the page redirect service (#161933).
- Certain actions are now blocked in the WCM editor while the page is loading to prevent accidental deletes.
- When having a variation on a page collection root page, page creation settings are now always read from the default page (#161145).
- Better end user error messages when a controlled document fails to publish (#161347).


7.6.43
========================================
(Omnia 7.6.43 / Workplace 7.6.31 / WCM 7.6.33 / MS 7.6.24 / Analytics 7.6.2)

- Major performance improvement for the people picker for bigger tenants (#161407).
- Fixed a theme bug causing the filter block setting button to become invisible (#161407).
- Fixed an issue in the page rollup accelerator that would occur if a page were added to a channel as a draft.
- User profile images are now synced automatically to Omnia (#160285).
- Added the correct completed date to the Sign-off request excel export (#161454).
- OnPrem: Improved compatibility for ODM in team sites (#159794).

7.6.41
========================================
(Omnia 7.6.41 / Workplace 7.6.30 / WCM 7.6.32 / MS 7.6.23 / Analytics 7.6.2)

- Fixed an issue in move page collection that could cause broken images (#159029).
- Variation targeting now correctly handles scenarios when a variation only exists as draft (#161182)
- Communication sites can now be created both as Teamwork and as Publishing sites (#161363).


7.6.40
========================================
(Omnia 7.6.40 / Workplace 7.6.29 / WCM 7.6.31 / MS 7.6.23 / Analytics 7.6.2)

- Fixed an issue causing the send page by email to be incorrect (#160480).
- The SP User Profile birthday property can now be correctly set in the new profile card (#157032).
- Fixed an authentication issue due to changes in EntraID (#161045).
- Controlled documents can now be unpublished even when the document type has been deleted (#161248).
- Fixed a naming mismatch in controlled documents permission settings causing certain permissions to not be assaignable (#160450).
- Improved performance in the Media Rollup. 
- Fixed an issue that would give an incorrect error message if assigning permissions in a page collection with more than 5000 pages (#160426).
- WCAG fixes for the block header.
- Corrected padding settings for the process navigation block (#160645).
- Documents in a document rollup that are shown via pick document, no longer shows in read mode if deleted.
- Microsoft Search integration with externalItem now supports sort by.
- Added support for syncing multi value phone number from EntraID properties (#159881).
- When usink bulk create for omnia users, the correct onboarding url is now set (#160535).



7.6.38
========================================
(Omnia 7.6.38 / Workplace 7.6.28 / WCM 7.6.29 / MS 7.6.21 / Analytics 7.6.2)

- Added the possibility to ignore variations on the navigation path query of the page rollup (#160527).
- Fixed an issue where the save button would not display correctly when navigating from a draft to a custom link in the WCM editor (#160467).
- Fixed an issue in user management that would occur when BP language settings where inherited from tenant (#160464).
- When consenting a new tenant, the user that consents now correctly becomes an Omnia tenant admin (#160694). 
- Performance and stability improvements. 
- Documents under approval now have a disabled link to avoid accidental edits (#160327).
- Fixed an icon rendering issue that would occur when using section background images on the page (#160553).



7.6.36
========================================
(Omnia 7.6.36 / Workplace 7.6.27 / WCM 7.6.28 / MS 7.6.20 / Analytics 7.6.2)

- Stability improvements to the page rollup accelerator (#160385).
- Removed dependency on external service for Geolocation on logins, this will speed up login of Omnia Users. 
- Stability improvements to MS Teams tab provisioning (#151771).
- Performance improvements to the search statistics UI for lager tenants (#160066).
- Fixed an issue that would cause review tasks not to create correctly. 
- Display name has been added to the form result export.
- Fixed a routing issue in OPM that would cause content to not load properly (#160025).
- New tenants will no longer have issues with the media rollup before the default media queries are resaved. 
- Performance improvements to the AD sync. 
- Fixed an issue with date formatting in the RSS feed. 
- Fixed an issue in the term picker so it now always handles default value overrides correctly on pages (#159805).
- Fixed an issue in syncing certain date time properties from the Entra ID to Omnia user properties (#160235).
- Unanswered polls can no longer be submitted.
- Fixed an issue that would sometimes not cause all group updates to carry over when running a full sync. 
- Removed permission Files.Read.All delegated from all features since it’s no longer needed.



7.6.33
========================================
(Omnia 7.6.33 / Workplace 7.6.24 / WCM 7.6.25 / MS 7.6.19 / Analytics 7.6.2)

- Fixed an upgrade issue that could occur with substantial amounts of pages scheduled for automatic termination. 
- Clarified the EntraID sync that we filter for external users and not guests/members (#158499).
- Stability improvements to teamwork provisioning and planner tab provisioning (#151771).
- Fixed an issue with paging in the list of Publishing apps in Omnia admin (#159807).
- Fixed an issue causing Document Rollup excel export to take an abnormally long time to generate (#159484, #159146, #159522, #160097)
- Increased the image scale file size limit to 50 Mb.
- The send page as email feature now renders the correct content when using supported blocks (#159742).
- Fixed an issue with user login when the system contains duplicated emails.
- Performance and stability improvements. 
- Fixed an issue with Modified date on Sign-off requests, it now updates correctly.
- Fixed an issue in the calendar view of the page rollup, it now directly shows the correct day (#159743).
- Fixed a design glitch in the page rollup card view (#159747).

7.6.29
========================================
(Omnia 7.6.26 / Workplace 7.6.20 / WCM 7.6.20 / MS 7.6.16 / Analytics 7.6.2)

- Performance and stability improvements. 
- Increased compatibility for phone number conversions from EntraID to Omnia User properties


7.6.26
========================================
(Omnia 7.6.26 / Workplace 7.6.20 / WCM 7.6.20 / MS 7.6.16 / Analytics 7.6.2)

- Page types can now have custom link icons in the template. Note: You need to re add the icons to the page type for the fix to apply.
- Fixed an issue that would prevent creating terms in open term sets through Omnia on certain permission configurations (#158521).
- If an extension modifies or creates an entity, the word "System" is now shown instead of the extension Guid.
- The document rollup can now correctly open all documents in word online if configured to do so (#159385).
- The settings in the link picker for documents now behaves as expected (#153277).
- Fixed an issue in Sign-off requests causing bcc emails to be wrongly created with certain email providers (#158588).
- Improved login token handling, leading to improved performance and stability.

7.6.23
========================================
(Omnia 7.6.23 / Workplace 7.6.18 / WCM 7.6.18 / MS 7.6.13 / Analytics 7.6.2)

- Fixed an issue that caused the announcement edit UI to freeze the browser (#159334).
- Added missing feature descriptions (#156197).
- Entra ID sync performance improvements (#158766). 
- Fixed an issue with query templating in the document rollup that affected some users (#158865, #159550).
- Fixed an issue that would prevent publishing of a page after chaining page type in the create new page dialog (#159200).


7.6.22
========================================
(Omnia 7.6.22 / Workplace 7.6.17 / WCM 7.6.17 / MS 7.6.12 / Analytics 7.6.2)

- Performance improvements to page rollup loads.
- Fixed an issue causing page properties to not render when main channel was displayed (#159129, #159158).
- Fixed an issue block input of person fields in the User Profile completion form (#158971).
- Improved integration with the Bing image provider (#158622).
- Stability improvements to Omnia Search index updates for big tenants. 
- Fixed an issue preventing linked images to be centred in the RTF editor (#159016).
- Prevented incorrect node structure to be created when move page from navigation structure page collection to flat page collection (#159056).
- Fixed a case where the media rollup would not show any result when having one corrupt image in the search result (#158945).


7.6.18
========================================
(Omnia 7.6.18 / Workplace 7.6.14 / WCM 7.6.14 / MS 7.6.11 / Analytics 7.6.2)

- Improved stability to the SharePoint page sync job.
- Fixed an issue when using multilingual titles for process steps (#158116).
- Rich text App Instances properties no render correctly in the properties block (#158448).


7.6.16
========================================
(Omnia 7.6.16 / Workplace 7.6.13 / WCM 7.6.12 / MS 7.6.10 / Analytics 7.6.2)

- Several performance improvements related to authentication tokens.
- Business profile viewers can now get app instance metadata (#158542).
- The process rollup title now has the correct colour (#158469).
- Fixed an issue preventing direct input in date pickers (#158666).
- When creating pages using default values from the current page, the values now properly render in the new page dialog (#158584).
- The document rollup now supports a multilingual title.
- Fixed an issue in the page rollup to ensure the current page is excluded if configured to do so (#158631, #158640).
- Fixed an issue causing old forms to require too high permissions to be shown (#158840, #158812).
- The send page as email feature now has better handling for images (#158793).

7.6.9
========================================
(Omnia 7.6.9 / Workplace 7.6.7 / WCM 7.6.7 / MS 7.6.6 / Analytics 7.6.2)

- Fixed an issue causing document related links to show as custom links (#158701).
- Fixes for WCAG to the current navigation (#153826).
- The forms rollup now gives correct results when querying forms from multiple apps (#158649).


7.6.7
========================================
(Omnia 7.6.7 / Workplace 7.6.6 / WCM 7.6.6 / MS 7.6.5 / Analytics 7.6.2)

- The analytics reports block is now available.
- It is now possible to make comments mandatory when unpublishing a controlled document.
- When resetting an Omnia account, the user will now be redirected correctly.
- Fixed an issue when saving a form that have active answers. 
- The "no result message" now works as expected in the Media rollup.
- Process tasks can now display longer titles.
- "Set as Default control" now works as expected in Controlled documents.
- Sign-off requests will now send emails to Omnia users.
- Improvements to the editing experience on Mobile.
- Capital letters now display as expected in rollup filters (#158342).
- Media rollup refiners now work as expected. 
- Performance optimizations. 
- Fixed an issue related to adding options in forms (#158104).
- When adding a website tab in Teams, omnia will no longer load (so that the SharePoint page can work) (#152811).
- THe page property block now hides itself if no properties in the block has values (#156655).
- 


7.6.6
========================================
(Omnia 7.6.6 / Workplace 7.6.4 / WCM 7.6.5 / MS 7.6.4/ Analytics 7.6.2)

- Fixed an issue causing duplicate anchor names in steppers (#158303).
- For single step page approval, the correct approval email is now sent (#157741).

7.6.5
========================================
(Omnia 7.6.5 / Workplace 7.6.3 / WCM 7.6.4 / MS 7.6.3/ Analytics 7.6.2)

- Updated matomo to the latest version (#158402).
- Fixed an issue in the RTF editor when positioning an image next to a bullet list.
- Process management sub process titles and shape titles are now better separated to support really long titles (#158175).
- Stability improvements to the page rollup accelerator (#158092).

7.6.4
========================================
(Omnia 7.6.4 / Workplace 7.6.3 / WCM 7.6.3 / MS 7.6.2/Analytics 7.6.0)

- Navigation nodes can now be moved as a sibling to a place in the navigation structure (#158150).
- Improved handling for when an MFA sign in to Omnia fails (#158170).
- (OnPrem) Fixed the permission syncing for the teamwork rollup (#158174).
- Improved stability to process authoring when publishing a process (#158123).
- Fixed an issue in the forms block preventing an editor to select forms they should have access to (#158340).
- Fixed an issue related to app instance URL updates (#156784).


7.6.3
========================================
(Omnia 7.6.3 / Workplace 7.6.2 / WCM 7.6.2 / MS 7.6.1 / Analytics 7.6.0)

- Fixed an issue in adding or removing poll options (#158104).
- Fixed an issue that would cause search results to not open correctly (#157900).
- Improved the handling of adding anchor links.
- Stability improvements to teamwork creation (#151771).
- Matomo update request emails are no longer being sent (Matomo updates will be included in Omnia releases and should not be updated using Matomo itself)
- Removed a required feature upgrade for Controlled Documents.
- Stability improvements to automatic translations (#157854).
- Added correct date converter to show birthday in the new profile card.



7.6.2
========================================
(Omnia 7.6.2 / Workplace 7.6.1 / WCM 7.6.1 / MS 7.6.0 / Analytics 7.6.0)

New features
************

- Forms are now supported on a per app basis
- Forms now have support for images
- Forms can now be handled in a rollup manner like other entities.
- Sign-off requests can now be scheduled. 
- Sign-off requests can now be setup as recurring requests.
- Several user management improvements including local account ownership.
- Subscript and superscript are now available as RTF actions. 
- Its now possible to use bulk update on Tasks.
- Analytics reports block.

Fixes
************

- Improvements to the profile card to correctly hide empty properties (#153287).
- Stability improvements when restoring from the archive (#153394, #152480).
- Improved performance when checking out pages that are very complex (#154227).
- Fixed an issue preventing the preview to render correctly on root page collection layouts (#156179).
- Fixed an issue preventing certain naming policies from being applied correctly.
- Stability fixes to the Entra ID sync (#155695).
- Links now works as expected in important announcements (#156496).
- Fixed an intermittent issue that would prevent a page from being added to a channel (#154464).
- Page rollups using navigation path and variation now fallbacks correctly (#145934, #147197, #153918).
- Page rollups now show default language correctly when a draft in a new variation language is created (#153662).
- Stability and language improvements to the user onboarding flows (#157598).
- Quick links now better displays long categories in its legend (#156563).
- Improved UX when creating pages with duplicate URLs without normally showing the URL input field (#157320).


7.5.34
========================================
(Omnia 7.5.34 / Workplace 7.5.26 / WCM 7.5.22 / MS 7.5.16 / Analytics 7.5.6)

- Fixed an issue where teams presence would not render correctly on first page load (#157864).
- Improved search as you type logic when using the page rollup accelerator (#158009).
- The page rollup accelerator now correctly adds pages approved into a channel into the index (#157937).
- Fixed a migration issue for the new date format setting in page rollup views.

7.5.33
========================================
(Omnia 7.5.33 / Workplace 7.5.24 / WCM 7.5.20 / MS 7.5.16 / Analytics 7.5.6)

- Re-enabled HTML formatting when using the Page Rollup accelerator (#157574, #157748)
- Node-reordeting for big strcutures is now more stable (#149006).
- Fixed an issue where the event management participant list would not show correctly for readers when external users were added (#157447, #155730).
- Document picker filters using boolean properties now works as expected. 
- Fixed an issue that would cause the Page Rollup to lock its setting when getting an empty result back (#153667, #153590, #156096).
- Scheduling pages with manual variations now works as expected (#157621).
- Fixed an issue that preventing the move of the FAQ's blocks sections (#157693).

7.5.31
========================================
(Omnia 7.5.31 / Workplace 7.5.23 / WCM 7.5.19 / MS 7.5.15 / Analytics 7.5.6)

- Fixed an issue that would not send correct emails to AD security groups in sign-off requests (#156745).
- Fixed an intermittent issue in editing of custom figures in OPM (#154260).
- Performance improvement to our token handling.
- Correct people properties now show for pages that were scheduled and have automatic page translation (#157233).
- Fixes to tasks list rendering in process management layouts (#157265).


7.5.29
========================================
(Omnia 7.5.29 / Workplace 7.5.22 / WCM 7.5.18 / MS 7.5.14 / Analytics 7.5.6)

- Updates to better detect deleted M365 groups and SharePoint sites in Teamwork administration (#156768).
- The info icon now works as expected in the Controlled Documents archive (#157234).
- Site Designs now works as expected for communication sites (#157221).
- The start chat button in the profile card now works as expected for all users that is supported, its hidden for Omnia users (#154376).
- E-mails related to multi page approval will now be sent in the recipients language (if set) (#156638).
- The page property block now hides correctly if no values set (#151382).
- Fixes to migration of settings for date property settings in page rollup views (#156717).
- Page rollup accelerator stability improvements.


7.5.28
========================================
(Omnia 7.5.28 / Workplace 7.5.21 / WCM 7.5.17 / MS 7.5.13 / Analytics 7.5.6)

- Fixed an issue where channels would not save correctly when saving as draft (#155869).
- Taxonomy properties now render correctly in the people rollup roller view (#157059).
- Better term picker logic for large term sets with very short terms (#154937).
- Fixed a permission error that would prevent shared links admins from editing tenant shared links (#156524).
- Fixed an error that would sometimes show an error message when restoring documents (#156844).
- Better handling of the "keep text" button when pasting i RTF (#145351).
- Fixed an issue in the SharePoint user profile sync that would prevent the automatic job from running correctly (#156922).
- Fixes to automatic page creation across tenants (#157123).
- Corrected rendering of checked out to in the page rollup (#156609).
- The anchor links block no longer causes issues with page rendering in the WCM editor (#157030).
- Controlled Documents now correctly handles dynamic groups for setting read permissions (#157147, #156450).
- Corrected an issue where banner links could link to the wrong page under certain conditions (#156021).
- Page Rollup Accelerator stability fixes.



7.5.25
========================================
(Omnia 7.5.25 / Workplace 7.5.18 / WCM 7.5.15 / MS 7.5.11 / Analytics 7.5.6)

- Improved performance for the queue log display (#156684).
- Fixed an issue that caused page views for workspace pages to not register correctly in Matomo.
- Fixed a styling issue on mobile that caused certain links to not display correctly (#155844).
- Improved loading behaviour and performance for search statistics (#156339).
- Analytics reader permissions now show correctly if you do not have a workspace provisioned (#156719).
- Stability improvements to scheduled publishing (#156709).
- Stability improvements to Teamwork provisioning as per Microsoft recommendations.
- Improved logging for failed translations (#156293).
- All day events now display correctly in negative offset time zones (#154854).

7.5.24
========================================
(Omnia 7.5.24 / Workplace 7.5.17 / WCM 7.5.14 / MS 7.5.11 / Analytics 7.5.6)

- Fixed a logical glitch when using multiple translations together with automatic page creation (#156046).
- Stability improvements to the review workflow timer job and logic (#155304).
- The SharePoint user profile sync correctly shows without SharePoint add-in permissions being configured (#156252, #156587)
- Better handling for removed users in the process authoring site (#155980).
- Improved stability for the page deletion job to better handle substantial amounts of data (#155868).
- Improvements to the Page rollup accelerator feature.
- Added a sign-off request tenant feature to improve performance in solutions where sign-off requests are not used.


7.5.23
========================================
(Omnia 7.5.23 / Workplace 7.5.16 / WCM 7.5.13 / MS 7.5.10 / Analytics 7.5.6)

- Improvements to the Page rollup accelerator feature (#156459).
- Corrected an issue that prevented the process rollup to be sorted on published date (#156036).
- Classic date format is now available for all page rollup views.
- Corrected a migration error which caused some sites to not be able to create new controlled documents (#156125).
- Improved logic for links when several navigation paths are duplicated (#156021).
- Fixes to permissions logic to display public information on a teamwork (#153537).
- The Matomo data gather script is correctly removed once the feature is disabled (#156037).


7.5.22
========================================
(Omnia 7.5.22 / Workplace 7.5.15 / WCM 7.5.12 / MS 7.5.9 / Analytics 7.5.6)

- Adjustments to the create MS Teams API (#151771).
- Performance improvements to the Teamwork rollup (#155703).
- Fixed an issue that caused iframes to get the wrong height (#155838).
- Entra ID sync stability fixes (#155695).
- Fixed a save issue for the YouTube media provider (#155695).
- Improved rendering for the Digital signage web view (#154062).
- Fixed WCAG issues in the page rollup calendar view (#149302).
- User profile card layouts now work as expected when creating a new tenant (#155958).

7.5.18
========================================
(Omnia 7.5.18 / Workplace 7.5.12 / WCM 7.5.8 / MS 7.5.5)

- Fixed an issue that would prevent stream videos from playing correctly on some devices (#152767, #152769).
- Fixed an issue that would prevent Analytics readers from being added correctly to Matomo (#155538).
- Videos with special characters can now be picked in the MS Stream video provider (#154963).
- Images can now be embedded into Digital Signage without the extension requiring API full control. 
- Incorrect captions from Media flow are now hidden (#155420).


7.5.15
========================================
(Omnia 7.5.15 / Workplace 7.5.11 / WCM 7.5.6 / MS 7.5.5)

- Fixed an issue that would prevent old, signed copies from being retried in Controlled Documents (#153282, #153103).
- Added a setting to the new filter engine to not select child’s terms by default (#154869).
- The community feature no longer incorrectly adds PageContent as a queryable property (#155196).

7.5.10
========================================
(Omnia 7.5.10 / Workplace 7.5.10 / WCM 7.5.5 / MS 7.5.4)

- Fixed load time issue for very large term sets in the new filter engine.
- Fixed an issue with shared comments and likes between variations (#152292).
- Limit read access in Controlled Documents now populates correctly when creating a new draft (#155030).
- Fixed an issue that would cause the Sign-off request rollup to show too many items (#154136).
- Stability fixes to the Azure AD Sync.
- When using Omnia File storage, links can now be correctly renamed (#154403).



7.5.8
========================================
(Omnia 7.5.8 / Workplace 7.5.9 / WCM 7.5.4 / MS 7.5.3)

- Fixed an issue with the setup wizard that would cause existing notification panels to break (#154803).
- The Calendar rollup now handles all day events correctly in time zones with a negative offset (#154854).
- Fixed an issue that would prevent certain connected process management documents from being deleted (#154833).
- Ensured permissions on business profile level are not needed to use the media flow connector (#154463).
- Improved on how Process Management saves its changes (#154261, #154260).
- When attaching a site, the show in public listings preview value is now correct (#154828).
- Improved support for combining automatic translation and automatic page creation (#152788).
- Performance improvements to the Posts block (#152718).
- Several WCAG improvements.


7.5.6
========================================
(Omnia 7.5.6 / Workplace 7.5.8 / WCM 7.5.3 / MS 7.5.2)

- Fixed an issue that would prevent processes from saving to SharePoint (#154240).
- Stability improvements to the Entra ID sync. (#154611).
- Fixed a migration issue for old media block data (#154732).
- Fixed an issue preventing old, controlled documents from being unpublished (#154438).
- Several WCAG improvements. 
- Fixed an issue that prevented the Teams Channel rollup from rendering (#154414).
- The rich text block now handles table borders in a better way (#154530).
- Search in big term sets in the new filters now works as expected.
- Fixed an issue that prevented appendices from being opened from document history.

7.5.4
========================================
(Omnia 7.5.4 / Workplace 7.5.7 / WCM 7.5.2 / MS 7.5.1)


Fixes
*********

- Improvements to the page rollup accelerator.
- The status dropdown when following a process in a teamwork now has the correct translations (#153629).
- Fixed an issue in the Matomo setup feature when activated multiple times (#153939).
- Several enhancements to the setup wizard (#154165).
- The page rollup calendar view now works as expected in time zones with a negative offset.
- Fixed an issue with teamwork templates with public content (#153537, #152205).


New features
************

- The EntraID sync can now evaluate user types based on empty values.
- When saving the default context URL, Omnia now ensures sites selected is applied.

7.5.2
========================================
(Omnia 7.5.2 / Workplace 7.5.4 / WCM 7.5.1 / MS 7.5.1)

Main release notes reference
******
- Business profile users and groups
- Self-service account creation and on-boarding
- Improved identity picker
- Improved user profile cards
- New scope in the People rollup block
- Improved user management governance
- Analytics powered by Matomo
- Anchor navigation
- Publishing campaigns
- Improved metrics
- Improved page feedback (#150001).

Release notes
******

- Possibility to have app only access to the term store.
- Possibility to view logs on the new Mellisearch based search index.
- Page rollup accelerator, a new technology has been released to improve the performance of page rollups, this can be enabled in Omnia admin.
- Configurable refresh token times per user type for enhanced security.
- The SharePoint add-in for the SharePoint user profile sync is deprecated, update and consent the "SharePoint user profiles sync" feature to use only Microsoft Graph.
- Media and text blocks can now be used on anonymous pages.
- Preferred language is now editable in the Entra to Omnia property sync.
- Updates to the user information block in mobile mode.
- Custom date queries are now possible in the page rollup, Sign-off requests rollup, Teamwork rollup, Community Rollup, Publishing App rollup and process rollup.
- Several fixes and updates to the properties block (#149403).
- The page rollup calendar view can now navigate to a specific day when clicking on the day in month view.
- EntraID to Omnia property sync can now resolve term ids based on label.
- User properties can now be configured to be private, making them readable only for the current user.
- Bulk creation of Omnia users is now possible via csv import in Omnia admin (#148752).
- Fixed issues with background colors in Process layouts.
- WCAG fixes to block headings and page rollup calendar view (#149303).
- Empty string can now be used as a Document ID prefix (#153957).
- Compatibility improvements to the RSS reader block (#153944).
- Fixed a rendering issue in the tooltips of the new filtering engine (#153962, #153923).
- Boolean values can now be synced with the SharePoint user profile sync feature (#154068).
- Stability improvements to teamwork creation (#153715).
- Improved filter rendering when using a text property and dropdown (#153189, #153688).
- A login log is now available to view login attempts from Omnia users.
- Selected user can now be used in all rollups. This is useful to create rich profile cards with queryable content. For KQL based rollups, its possible to use [SelectedUser.Id], [SelectedUser.Name], [SelectedUser.Email]. 
- Fixed an issue that would duplicate images in the media picker under certain conditions (#153322, #152839).
- A new way to update your profile photo has been added, this works for all account types including Omnia users (#152278).
- It is now possible to assign a tenant administrator before the Omnia user sync has been run.
- Localization now works as expected for Omnias onboarding emails (#151910).
- Omnia users now have its first/latest login timestamp recorded and presented in the user management UI.
- Improved security.
- Omnia users can now be forced to change their password on first login. 
- An SMTP server can now be configured for Omnia emails.
- It is now possible to use forgot password even when a user is not onboarded yet (#152738).
- Updated localization for natural language date formatting in rollups (#151635).
- Improvements to the feature consent workflow.


7.1.46
========================================
(Omnia 7.1.46 / Workplace 7.1.25 / WCM 7.1.32 / MS 7.1.27)

- Fixed an issue where terms would not render correctly if term subscription is turned on.
- Fixed a migration issue for old images in the page rollup.
- The new filters now have better compatibility with old settings data.
- Fixed an issue with process rendering that occurred due to a framework update (#153802).
- More tokens have been added to the Document Rollup to enable more complex queries (#151825).
- Fixed an issue in process management that could corrupt the drawing when resizing the canvas (#153905, #153562).
- Omnias AI capabilities are upgraded to support Dall-e 3 and Open AI GPT4.
- Due to a breaking change in the new MS Teams client, controlled documents are now opened in a new browser window instead of inside of the MS Teams client (#151548, #151496). A bugfix from Microsoft is required to resolve this.
- Fixed an issue in the URL router that could cause inconsistent behaviours when the URL segment and its variation segment are the same (#153656).


7.1.43
========================================
(Omnia 7.1.43 / Workplace 7.1.22 / WCM 7.1.30 / MS 7.1.25)

- The published view in and ODM authoring site can now be searched even if the library has more than 5000 items (Feature activation required) (#152912).
- Fixed a migration issue when current user was set as a default value in a filter (#153272).
- Fixed a loading issue for available page types in Digital Signage (#153276).
- Fixed an issue in the MS Teams app generator due to an updated manifest from Microsoft.


7.1.41
========================================
(Omnia 7.1.41 / Workplace 7.1.21 / WCM 7.1.29 / MS 7.1.24)

- Fixed an issue that would cause duplicate tasks in ODM when the default context site has the wrong permissions (#153109).
- Fixed an issue that would prevent the user from setting their language on some mobile devices (#151604).
- Related links word online query strings now work as expected (#152925).
- User image now renders correctly on replies to posts when in SPFx (#153139).
- Fixed an issue that would sometimes prevent a page from being moved (#153101).


7.1.38
========================================
(Omnia 7.1.38 / Workplace 7.1.20 / WCM 7.1.27 / MS 7.1.23)

- Fixed an issue that would case different casing in emails to not correctly register attendance in event management (#152733).
- Fixed an issue related to the combination of scheduling and multi-level approval (#152785).
- The filter panel can now show more than 100 refiners (#152918).
- Fixed an issue that selected the wrong default rendition (#152777).



7.1.37
========================================
(Omnia 7.1.37 / Workplace 7.1.20 / WCM 7.1.26 / MS 7.1.22)

- It is now possible to publish documents in a controlled documents library when the tasks list has more than 5000 items.
- Performance improvements in infrastructure cache layer.
- A direct SMTP connection can now be used for sending emails from Omnia.
- The filter list view will now get as wide as its biggest filter (#152564).
- Multiple videos in the posts block now works as expected.
- Fixed an issue with scheduled pages when upgrading from 6.13 to 7.1 (#152809).
- Fixed an issue when saving publishing app settings when BP language did not include the tenant default language.


7.1.36
========================================
(Omnia 7.1.36 / Workplace 7.1.19 / WCM 7.1.25 / MS 7.1.21)

- Removed the limitation that groups need to have email to be selected in sign of request functionalities (#152607).
- Fixed an issue that prevented the iframe block input box from being rendered (#152282).
- Refiners now works as expected when using AND chaining (#152727).
- The media gallery now works as expected on app posts (#152759).
- Stability fixes to the Azure AD sync to Omnia (#152337).
- SharePoint user profile sync will now retry all users that log in for the first time (#138514, #152354, #152751).
- Refiner limit is now restored to 500 items (#152918).
- Improved stability in the published process rendering (#152665).

7.1.35
========================================
(Omnia 7.1.35 / Workplace 7.1.18 / WCM 7.1.24 / MS 7.1.20)

- Fixed an issue with automatic deletion from the archive (#152439, #152313).
- Improved machine translations for several languages (#152077, #152437).
- Fixed an issue with nested groups in sign-off requests. 
- Fixed an issue that would prevent automatic saving of process drafts from working correctly (#152156).
- Page approval emails can now be configured per step.
- Fixed an issue that could sometimes make the page rollup calendar view show an incomplete set of items (#151129).
- Fixed an issue in the migration that could cause the export of usage reports to not work as expected. (#152539).
- Improved performance for certain start page load scenarios.
- Fixed an issue that would prevent page rollups from loading if they had incorrect filter configurations (#152486).
- Taxonomy filtering now works as expected when the taxonomy hidden list data is corrupted in SharePoint (#152530).
- Fixed a styling glitch in the page rollup view listing with image (#152491).

7.1.31
========================================
(Omnia 7.1.31 / Workplace 7.1.17 / WCM 7.1.22 / MS 7.1.18)

- Multi step approval for pages now has configurable action buttons per step.
- Fixed an issue for Omnia connected communication sites that would incorrectly redirect to the start page of the site (#152302).
- Process printing now works as expected with all tokens in print page (#151993).
- The time picker now correctly uses 12-hour format if configured to do so (#152172).
- Fixed an issue with publishing documents that could occur after an update to Omnia 7 (#152064).
- Max upload size of files increased (#152000).
- Characters with umlauts now correctly display when selected in end user filters (#152071).
- Machine translation now works as expected for exceptionally large pages (#151757).
- The sign-off request excel export now works as expected when it has deleted users.
- The legacy profile card no longer loads forever when opened on a guest user (#152263).
- Stability improvements for enabling cross variation comments and reactions (#152292).
- Data model preparation for account type change and re-boarding.


7.1.23
========================================
(Omnia 7.1.23 / Workplace 7.1.15 / WCM 7.1.19 / MS 7.1.15)

- Several migration fixes to the 6.13 -> 7.1 upgrade (#151558).
- Corrected a theming issue that would sometimes cause wrong tab title colors (#151618).
- Classic date format now has the correct localization (#151635).


7.1.13
========================================
(Omnia 7.1.13 / Workplace 7.1.6 / WCM 7.11 / MS 7.1.8)

- Stability improvements to the scheduled pages job (#151280).
- Several migration fixes to the 6.13 -> 7.1 upgrade (#151417).
- Fixes an issue where a test sync in the SharePoint user profile sync would incorrectly trigger a full sync (#151495).
- The page properties block now hides correctly if no properties at all are set (#151382).
- Fixed an issue that would in some configurations cause the sign out to not work correctly (#151392).
- Corrected an issue where the current navigation block would be hidden in some scenarios (#151219).
- Pagination now works as expected in the teamwork rollup (#151375).
- Keyboard navigation now works as expected for process layouts (#151301, #151463).

7.1.10
========================================
(Omnia 7.1.10 / Workplace 7.1.4 / WCM 7.1.6 / MS 7.1.4)

- Custom Azure cognitive services now support multiple regions.
- SharePoint User Profile Sync now works as expected when running in legacy system account mode (#151261).
- Process authoring sites now loads correctly when containing deleted users. (#151271).
- SVGs are now fully supported in all media pickers.
- Corrected an issue where image caption could not be deleted (#151144).
- UI fixes to the dynamic roller page rollup view. (#151187, #151508).

7.1.9
========================================
(Omnia 7.1.9 / Workplace 7.1.3 / WCM 7.1.5 / MS 7.1.3)

- Fixed an issue that caused page rollup paging to not update images correctly (#151215).
- The M365 app launcher have an updated name to go to the M365 home (#151134).
- Fixed an issue that would prevent the configuration of styles in the RTF editor.
- Fixed an issue that prevented App Instances to be provisioned via an extension identity.
- Several stability improvements to the 6.13 to 7.1 upgrade.
- Improved stability of the multi-step page approval flow.
- Corrected the breadcrumb navigation behaviour when viewing a process from the process rollup (#150794).
- Navigation between link nodes in the WCM editor now works as expected.
- Corrected a display issue of event management settings when the user has been removed (#150876).
- Performance improvement to the page rollup.
- Fixed an issue in controlled documents that would sometimes prevent the approval when using a group (#151070).
- Corrected paging of related documents in process management (#150999).
- Corrected behaviour of the process management change comment (#150981).


7.1.0
========================================
(Omnia 7.1.0 / Workplace 7.1.1 / WCM 7.1.0 / MS 7.1.0) 


Improvements
******
- Media flow is now available as a possible media picker, NOTE: License with Media flow is required to use this feature.
- The media block now supports multiple images.
- Added additional default properties to the setup feature "Enterprise properties - Documents".
- Added additional default properties to the setup feature "Enterprise properties - People".
- Document Management and Process Management now have different comments for "Change comment" and "Message to approver".
- It is now possible to force a page to have a Publishing Channel when it gets created. 
- It is now possible to attach a publishing app to an existing communication site.
- Custom 404/401 pages can now be designed in Omnia Admin (#119744, #133793).
- Broken links statistics are now available in the metrics block. 
- The page rollup list view can now show people with only name or only user image.
- Limit read access are now persistent between versions in Process Management (#122305)
- App instance connected sites URLs can now be edited in Omnia Admin.
- The page rollup calendar view now has an improved date range selector. 
- Only valid languages can now be selected for a Teamwork template (#145938).
- It is now possible to copy link to document from the document rollup information panel (#147490, #147010). 
- Identity picker can now differentiate between email enabled and Permission enabled groups.
- The process property type now supports multiple values.
- Additional data is now included in the Sign-off request export.
- It is now possible to exclude mandatory links from the quick links block.
- For controlled documents with no document type set, multiple documents can now be set at once (#143517).
- Lazy load can now be disabled for tabs, to allow for trim duplicates to work as expected (#147084).
- Added clearer error handling to the enterprise glossary to inform the user term store permissions are missing (#143078).
- Improved rendering of the recipient list of sign-off requests (#146972).
- Teamwork provisioning emails are no longer sent on edits of an app instance (#148412).
- Work email is now used to send emails in event management instead of login name, this to improve compatibility with external and omnia users (#141587).
- Send page as email now works from preview (#149812).
- SharePoint user profile sync property mappings are now case insensitive.
- The SharePoint user profile sync feature is now tied to a new feature that will provision correct AAD permissions (#149390).
- It is now possible to limit who can be set in a person property of controlled documents (#138296).
- Digital signage now support reusable Json mapping templates.
- If using Draftable, the show changes button is now configurable per document type.
- Selection list in rollups for business profile are now sorted alphabetically. 
- Additional reviewers can now be added to the send for comments flow in ODM.
- Multi level approval is now possible for pages. (See main release notes)
- Open AI Integrations (See main release notes).
- When saving filter state, if using classic paging, the page number is now remembered (#146197).
- Its now possible to write to your user profile using an action button, this can be used to track for example completed courses.
- All page rollups (except the calendar view) can now sort on Navigation.
- Security trimmed teamwork rollups (See main release notes).
- Media in pages now supports image caption.
- The process rollup now supports metadata queries based on currently rendered process.
- A process can now use properties of type media.
- It is now possible to configure the Omnia MS Teams app using a custom domain.
- Additional colour codes (Page Type and Page Workflow Status) are now possible for the page rollup calendar view.
- Document rollup copy link feature now uses a web link.
- A new add shapes UI with descriptions have been added to Process Management.
- Fixed label "All Languages" it no longer has an incorrect comma.
- It is now possible to move page collections across business profiles.
- Enhancements to the audit log.
- Review interval in ODM can now be configured to use either approval or publish date (#144801).


Fixes
******

- Sort by using the column header now uses the correct configured managed property (#133600).
- Fixed an issue with available seats in Event Management (#148057).
- Advanced search now handles dates in the same way as the document rollup (#148143).
- Refiner collapse setting now works as expected for date refiners (#147647).
- Suggested templates in the new document wizard now show correct when switching between normal and controlled document (#140277).
- WCAG: The left navigation now has the correct aria labels for use together with screen readers.
- WCAG: All views of the page rollup now use actual anchor elements, allowing for browser functions to work as expected (#142189).
- WCAG: Related processes now uses actual anchor elements, allowing for browser functions to work as expected (#146686).
- WCAG: Video description is now available to be set.
- WCAG: Correct aria labels set for input fields for Comments, My links search and app posts.
- WCAG: The document rollup now has correct tooltips if the value is cut (#140431).
- WCAG: Block headers now render correct non interactive HTML (#149303).
- WCAG: Search input field in the search block now has correct aria-label (#149303).
- WCAG: The calendar page rollup view now has interactive days and its date picker is now compliant (#149437).
- The org chart now displays all users if there are more than 100 on one level (#147538).
- Mailto links can now be added as a related link (#143722).
- Text styles now properly apply to bullet lists (#148259).
- Fixed a layout issue in the people rollup for small screens (#144373).
- AAD Permission read all applications as application permission removed.
- Stability improvements to tab navigations (#144707).
- Horizontal rendering for multiple people has been improved (#145312).
- Stability improvements to the setup wizard (#147091).
- Stream videos can now set Autoplay correctly (#148122).
- The WCM page archive now displays correct date format (#144979).
- Vertical text alignment of tabs updated (#143472).
- When combining scheduling and approval for pages, cancelling the approval now works as expected (#145639).
- Links in email now uses the custom email if available (#145697).
- The keep text button now shows when text are dragged into the RTF editor (#145351).
- Borders for banners now apply directly (#144626).
- Poll dialog is now hidden if no final text has been set (#145426).
- Fixed an issue that would prevent a form from opening when withing a stepper section (#44158).
- Improved active tab rendering for small screens (#146318).
- The dynamic roller page rollup view now allows for more text to be shown (#144992, #147721).
- Page rollup settings no longer try to adjust View and query settings dependent of each other (#136304, #145096).
- When pasting content into the RTF editor, the cursor is now placed correctly after the paste (#147276).
- The properties block can now be configured to have the correct date format settings (#149615).
- All blocks now hide correctly if they have no data to render (#145860).
- Fixed a rendering issue in Process Management (#149872).
- Fixed an issue with auto translation when using many images in the RTF content (#149437).
- Fixed an issue with the padding setting of the task rollup.
- A teamwork under approval can now have its fields edited as long as a naming policy based on users are not used (#147689, #146927).
- Manual translation tools now work as expected for drafts.
- OmniaVariationSegment is now updated as expected on resync to SharePoint.
- Updates to the SharePoint User Profile sync instructions. 
- Using the back button from advanced search now works as expected. 
- Digital signage preview URL now uses the custom domain if configured.
- Fixed an issue that would incorrectly hide blocks in edit mode when certain display breakpoints were set.
- Publishing app default settings now use the correct enterprise property picker.
- When trying to remove an enterprise property that is part of a property set, correct error feedback is now given.



- Also fixes preview bugs (#149420, #148905, #148253, #150468, #149862).

7.0.20
========================================
(Omnia 7.0.20 / Workplace 7.0.16 / WCM 7.0.20 / MS 7.0.16)

- Fixed an issue that prevented xslx files to be uploaded when documents are stored in Omnia (#150117).
- Fixed an issue that would sometimes cause the scroll arrows of OPM to not render correctly (#150075).
- The create page button now correctly opens edit mode (#150201).
- Fixed a targeting issue that would occur when a term set is deleted (#149570).
- Localization of social dates are now correct for Swedish locale.
- Fixed an issue with the page rollup calendar view when an event stretches over two months (#149970).
- Several migration improvements (#149933, #149826).
- Fixed an issue where pick pages would not work if the page rollup was added in the page type (#150142).
- Corrected an issue with mail enabled groups for odm notifications (#149316).
- Fixes to the page rollup padding settings (#149771).
- Stability updates to token replace for controlled documents (#142753).


7.0.16
========================================
(Omnia 7.0.16 / Workplace 7.0.12 / WCM 7.0.13 / MS 7.0.11)

- Fixes to new filter migration (#148620).


7.0.15
========================================
(Omnia 7.0.15 / Workplace 7.0.12 / WCM 7.0.12 / MS 7.0.10)

- Fixed issue in people rollup relating to Yes/No fields in the new filters.
- Archived pages now show as expected.
- Fixed an intermitted issue where granted permissions would not take effect.
- 6.13 -> 7.0 Data migration fixes.


7.0.12
========================================
(Omnia 7.0.12 / Workplace 7.0.9 / WCM 7.0.10 / MS 7.0.9) 

- Fixed an issue that would cause documents to fail in the controlled documents publish flow (#149283).
- Fixed an issue related to date formatting in event management (#149203).
- The new profile card should now work as expected for newly created Azure Ad users (#149111). 


7.0.5
========================================
(Omnia 7.0.5 / Workplace 7.0.4 / WCM 7.0.4 / MS 7.0.4) 

System wide
******
- New Filter UX and settings for all rollups. Resolves (#146912, #136058, #138038, #144147, #142858, #144762, #143976).
- The date picker now shows in the correct language.
- Terms picked now searched the full content of the term (#137357).
- All filters can be configured to have a fixed position.
- In a term set filter, it’s now possible to select if deprecated terms should be displayed or not (#115011).
- Long term names can now be viewed via tool tip, including the path to the term (#143157, #143460).
- Omnia users are now available and Kaizala logins are now no longer supported (#123798).
- Fixes to theming issues in Omnia Admin (#144292)
- Azure AD Group targeting is now case insensitive (#145285).
- Anchors to tabs can now both scroll the page and select the correct tab/accordion (#140710, #141196, #137953).
- New feature system, Omnia App permission is now handled on a per feature basis.
- All features’ names and descriptions have been updated.
- All features now have a permission description if they require Azure AD app permissions.
- Several new Omnia Features have been introduced to be able to limit the permissions of the Omnia Azure AD app.
- Only valid app instance features can now be selected on an app instance template (#117577, #120285).
- The org chart block now respects the msExchHideFromAddressLists property (#133417, #136830, #147094).
- For all rollups, partial word search is now always turned on. The setting has been removed.
- When using the image picker, correct message is now shown while searching.
- Several label updates and corrections.
- The filter state of all rollups can now be stored to the URL.
- Tenant and Business Profile titles are now multi-lingual.


Workplace
*****
- Sign-off Request rollup now shows the correct requests in regard to admin and normal users (#146317). 
- User profile completion feedback emails now work for users with different email and login name (#140368).
- A value can now be written to the user profile from an action button. This can be used in LMS.
- Sign-off request export now includes the time of sign off in the excel report. 
- Multiple status filters can now be used in the sign-off request rollup.
- Click out now works as expected for the User Profile completeness form.
- The old profile card can be activated using a tenant feature.


Communities
*****

- Auto translated pages no longer creates empty rows in the Activity feed (#137822).
- Fixed an issue that would create non clickable notifications on comment (#147554, #136648).  

Web Content Management
******

- Resource readers are no longer synced to a SharePoint permission (#141928).
- The create page action button now works as expected when placed on a Workspace page (#141516, #142027).
- Links created in the RTF content no longer contains and extra blank space (#129934, #143227, #143642, #130377, #147698).
- People rollup card view alignments have been corrected (#137509).
- Corrected quick poll submit button spacing (#145113).
- Page properties block text colour now works as expected (#142137, #140879).
- Fixed an intermittent issue with page type default values (#142421).
- Page Type names are now multilingual (#127732).
- Adding a link to RTF now supports links other than https links (#128013).
- Link to delve is no longer exposed in emails from the system (#144270).
- Distribution groups are now hidden from the identity picker where you can set permissions (#133992).
- Custom link nodes in the navigation structure are now multi-lingual (#132960).
- Thumbnails from a new stream video now have the correct ratio (#133809).
- The mega menu loading has been stabilized (#147842).
- Pages that are both under approval and scheduling now works as expected (#147464, #140255).
- Stability fixes to automatic page creation using auto publish (#147616). 
- Fixed an issue that prevented some users from seeing total page likes (#146569).
- Page Types can now be soft-deleted in the UI.
- Connected tenants can now be setup, to allow automatic page creation between tenants.
- Page rollup list view can now be configured with a fixed position.
- In the case of trying to create a duplicated URL to a page, better feedback is now provided, and the result is prettier. 
- Comments and likes can now be shared between variations of a page. (#142216).
- It is now possible to stop using variations if it was turned on by mistake.
- Publishing app settings have a new UI with only one save button.
- Page collections can now be moved across business profiles. 
- Page rollup filters will only show tenant page types and current publishing app page types.

Teamwork
****

- New Admin UI for teamwork (#142065, #148411).
- Several changes have been made to the handling of permissions in omnia, solves several sync to SharePoint issues (#141378, #144775, #125161). 
- Security trimming is now available for teamwork rollup (#128494, #138068).
- Better handling and user information when deleting a teamwork template (#142404).
- A site template can now define default values for different properties (#107193, #117587).
- Visibility of properties can now be configured. Properties can be shown in new and edit form respectively (#123637). 
- When deleting a teamwork, the list now updates immediately (#142098).
- "Open in client app" in the controlled documents library will now work for PDF documents (the document is opened in MS Teams) (#142086).
- Teamwork synchronization now uses the new Sites selected model. To manually sync last activity has been removed.
- Only supported languages can now be selected for a teamwork template.
- Communication site templates have moved and can now be found under publishing.
- When switching teamwork template, only valid choices are now shown. 



Process Management
*****

- Several improvements to the drawing capabilities of the editor (#122306).
- Edit button of shapes is now placed above the shape instead of on the shape (#120201).
- Possibly to edit z-index. Send to back, send backward, send to front, send forward (#128355, #122279).
- Shapes can now be moved using the keyboard (#120199, #129303).
- Multiple shapes can now be moved at once (#118677, #129301).
- A copied shape now retains its orientation (#135509).
- Rotating shapes will snap to a rotation grid if shift is pressed.
- Shape width and height can now be set using exact pixel sizes if desired (#120228). 
- Default canvas size can now be set for a process (#129245).
- Its now possible to link to a draft process (#123246).
- Better handling when a process authoring site is deleted (#141038).
- Multiple document rollups can now be added to a process, resolving the need for categorizing documents (#124937).
- Image cropping is now available for Background images and shapes (#127246, #128403).
- When using Process templates, search results will now render according to the template (#144094).
- The process rollup can now sort on process title (#135580).
- The browser back button now works as expecting when navigating away from a process (#136680, #136838, #125505).
- Fixed an issue where media-based shapes would not show up automatically (#140047).
- Individual process steps can now be found using search (#143938).
- Empty process drawings (using only a background image) can now be rendered (#132564).
- Fixed an issue that caused drawing background image to not update correctly (#133588).
- The process rollup is now supported in SPFx.
- Process approval tasks titles now have the correct translation (#128402).
- Archived processes can now be restored.
- The process picker will now show processes without searching.

Document Management
*****

- Click out now works as expected for document properties dialog (#138950).
- Recipient is now required in the send for comments form (#144813).
- Reviewers are now required in the send for review form.
- Compatible video files will now open in the browser (#146362).
- Bulk update now gives consistent results for users with different email and login name (#144982).
- Document types can now be configured to be compliant with Microsoft AIP. This by disabling features that replace properties and put the document into review mode.
- More tokens are now available to be used in the Document Management related emails. These include all enterprise properties and change comment.
- Document history now contains Published by (#138412).
- Bulk update can now search for user properties where the user has been deleted (#138222).
- Draft documents can now be restored from the SharePoint recycle bin (#136051).
- Document management file history now shows correct file names.
- Descriptions of the Document Type are now shown in the create document wizard (#136056).

Notes for developers
*****

- Omnia now uses Vue 2.7.
- Backend is upgraded to .NET Core 7.

Also solves preview issues: (#148163, #148232, #148911)
