6.11.46
========================================
(6.11.46 / Workplace 6.11.24 / WCM 6.11.43 / MS 6.11.25)

- Corrected an issue with the term picker using a large term set with one root term (#143089).
- Targeted teamwork now works as expected (#143123).
- Permissions now correctly sync to SharePoint when having more than 5000 items in one page collection.


6.11.45
========================================
(Omnia 6.11.45 / Workplace 6.11.24 / WCM 6.11.39 / MS 6.11.25)

- Fixes to term picker to better support large termsets (#143089).

6.11.44
========================================
(Omnia 6.11.44 / Workplace 6.11.24 / WCM 6.11.42 / MS 6.11.25)

- Added dirty checking on channel editor interface. Also fixes (#142003).
- Improved loading speed of images in Process management (#140124).
- Improved performance for page rollup. Also fixes (#142109).
- Clearing page rollup filter will now correctly trigger a new empty search.
- Corrected an issue where multiple review reminders would be sent in some scenarios (#141583, #142030).
- Improved stability in teamwork creation (#141306).
- OnPrem: Internal user group can now be added in Process Management.
- Corrected an issue where the wrong users would be shown in the activity feed (#141306).
- Corrected link to task from Document management that would sometimes be incorrect due to special characters (#142247).
- Updated archive flow to prevent corrupt data to be synced as searchable pages in some scenarios (#141135, #141245).
- Fixed a rendering issue in the notification panel with the document rollup (#141387).
- Corrected an issue with multilingual categories in Shared Links (#142396).
- Fixed a time zone related issue with the Birthday field of the profile card (#142516).
- Corrected a potential race condition that could occur when creating pages with broken inheritance (#142304).
- Corrected an issue in ODM when having more than 5000 documents in the same view (#142445).
- The related links page picker now works as expected when having many pages (#142356).
- SharePoint Reindex now works with the delete option together with +5000 pages (#142356).
- Stack processes now highlight correctly.
- Updated edit teamwork flow to correctly ensure administrators (#142581).


6.11.33
========================================
(Omnia 6.11.31 / Workplace 6.11.18 / WCM 6.11.26 / MS 6.11.18)

- Using a token in the Action button to publish pages in another page collection now works as expected (#141725).
- End user filtering for channels now works as expected in the page rollup (#141831, #141968).
- Adjustment to avoid multiple review reminders (#141583, #142030)
- Automatic refresh of page rollup now works as expected.
- The WCM editor no longer incorrectly selects the channel tab by default in some cases (#141755).
- Fixed a client-side validation error for text properties in Teamwork templates (#141759, #141746, #141787).
- Fixed an issue that caused pages with a '#' character in the page title to not be possible to archive (#141770).
- Improved stability in the SharePoint page sync (#140680).
- Channel administrators can now change if a page should be published directly or be sent to others for approval.
- The WCM editor no longer enters "wizard mode" when a page is at a higher version than 0.1.
- Improved the merge logic of Controlled documents (#141299).
- Improved logic to calculate last activity of teamwork (#141376).
- Fixes to the Service Bus implementation to remedy ongoing instabilities due to MS changes.


6.11.26
========================================
(Omnia 6.11.26 / Workplace 6.11.14 / WCM 6.11.18 / MS 6.11.12)

- The WCM editor no longer renders in Wizard mode if the page version is larger than 0.1.
- The user profile cards now work as expected for external users (#141093).
- Fixed an issue that prevented all document types to show in the create document wizard (#141237, #124442).
- Internal scrollbar is no longer visible on the Dynamic Roller (#141321).
- Digital Signage queries using channels now works as expected (#141312).


6.11.24
========================================
(Omnia 6.11.24 / Workplace 6.11.12 / WCM 6.11.16 / MS 6.11.10)

- Image proxy now works as expected. 
- Export to excel in Document rollup now supports datetime properties. 
- The channel rollup block title can now be localized. 
- Improvements to Publishing Channels administrative interface.


6.11.19
========================================
(Omnia 6.11.19 / Workplace 6.11.10 / WCM 6.11.14 / MS 6.11.8)

- Advanced search now closes correctly on page navigation (#140408).
- Fixed an issue in the RTF editor when adding multiple images (#139947).
- Corrected an issue in Omnia Admin where Publishing apps would be incorrectly flagged as inactive.

6.11.18
========================================
(Omnia 6.11.18 / Workplace 6.11.9 / WCM 6.11.13 / MS 6.11.7)

- OnPrem: Internal user group now works as expected.
- Channel categories have received several improvements. 
- Fixed a rendering issue in the Dynamic Roller.
- Stability improvements to Document Rollup Excel export.

6.11.16
========================================
(Omnia 6.11.16 / Workplace 6.11.9 / WCM 6.11.12 / MS 6.11.6)

- Corrected spelling mistake in AzureAD sync instruction.
- Improved performance for comments search (#140765).
- Style updates for text ellipsis when using FireFox.
- Stability improvements to emails send from Document Management (#140662)
- Performance improvements of page rollup.


6.11.15
========================================
(6.11.15 / Workplace 6.11.8 / WCM 6.11.11 / MS 6.11.5)

- Improved support for several different locals for SharePoint Birthday. (#136858).
- The Summary field can now be used in results from Microsoft Search.
- To avoid confusion and minimize issues, all emails are now sent using the default business profile language.
- Scheduled publishing should now work as expected (#140374, #140744, #140460, #140722).
- Improved performance for image loading in Process Management(#140124).
- Improved performance for the page rollup and page dashboard.


6.11.14
========================================
(6.11.14 / Workplace 6.11.6 / WCM 6.11.9 / MS 6.11.4)

- Improved stability for attaching existing teamwork to Omnia.
- Improved stability for scenarios when several features are activated at the same time (#140099, #140153).
- Stability improvements when moving pages (#140451).
- Fixed an issue in the Document rollup card view.
- Fixed an issue with rendering of the search when used as a block on the page.
- Corrected the data migration for the action button for upgrades between 6.10 and 6.11. (#140150).
- Updates to Publishing Channel Administration interfaces. 
- Several DM email notifications have seen their content reviewed and now works correctly. (#140299, #140267).
- Fixed an issue when saving settings in the Microsoft Search configuration.
- Improved data loading on the user profile card (#139730).
- Teamwork naming policies now support text.
- Extra spaces are no longer added in naming policies for teamwork (#140379).
- The Birthday value on the people card now hides correctly if it has no value (#140470).
- Added back missing logic on the page rollup time when social dates are used, and the day is today (#140477).


6.11.9
========================================
(Omnia 6.11.9 / Workplace 6.11.4 / WCM 6.11.3 / MS 6.11.2)

- Corrected the calendar rollup multi day event display (#140042).
- Channels can now be saved on a draft page correctly.
- Updates to the User Sync to handle users without a User Type (#140052).
- The organization tree should now load as expected (#140268).
- Corrected an issue that would cause the wrong quick link to open when last visited sort is used (#140049).

6.11.4
========================================
(Omnia 6.11.4 / Workplace 6.11.2 / WCM 6.11.2 / MS 6.11.2)

- Reduced number of requests sent by ODM to reduce risk of throttling.
- Corrected an issue with the Workspace home title (#139988).
- Document links in the quick and advanced search now fallback to Path if the selected managed property is empty (#139998).
- Corrected an issue when changing a calculated filed property.
- All system emails now follow the Business Profile language; site language is ignored (#139793).
- Corrected an issue preventing approval of Processes (#140090, #140097).
- Corrected an issue that would open the wrong document on the second page in the page rollup (#140062, #140089, #140079).
- My links now opens the links as intended (#140049).
- Updated the SharePoint User Profile sync instruction to include information about App expiration times.


6.11
========================================

- Publishing channels can now be grouped into categories. 
- It is now possible to search in the Admin Channel UI.
- The Org tree block and people card display can now be filtered to exclude users based on a property. (#136830)
- Channel approval emails are now sent on saving the page, regardless if the page is published or not.
- Document links can now be configured to open directly in app on mobile.
- A Channel rollup block is now available for easier approvals of pages in channels.
- Related processes can now be shown in the document rollup.

6.10.7
========================================
(6.10.7 / Workplace 6.10.4 / WCM 6.10.7 / MS 6.10.4)

- Fixed an issue causing some pages to not show in the page rollup (#139785, #139776, #139726, #139733, #139724).
- Increased the upload file size limit for document properties on pages.
- Performance improvements to the create page flow (#139665).
- Performance improvements to the media picker (#139552).
- Corrected link in the teamwork approval email. (#139607).
- Corrected an issue that would cause process approval tasks to sometimes not load correctly (#139346, #139347).
- The admin page for teamwork now has the correct links to the apps (#139352).
- Corrected an issue with term driven approval in ODM (#139462).
- Updates to routing in SPFx to align with recent changes from MS (#139472).
- Fixed an issue in the page rollup calendar view related to time zones.
- Improved machine translation for complex content (#139306).
- Filters using taxonomy properties now work correctly in the teamwork rollup (#139596).
- Corrected an issue the yammer comment integration when login name and email are different.
- Corrected an issue in the create document wizard causing suggested sites to not work properly (#139727, #139681).
- The advanced search button in quick search now works as expected when no search has been made (#139242).
- Corrected several dialog theme issues.
- The link picker now works correctly when picking images as a document.
- Fixed an issue where a page rollup would not allow fixed values to be set in the query (#138609).


6.10
========================================

Teamwork
*********
- Using a new way to provision teams - approver who approves a team no longer becomes owner (#127793, #127652, #127793)
- Default values for properties on Teamwork is now available (#115969).
- Naming policies can now be configured on Teamwork.
- Additional general policies can now be configured on Teamwork (minimum length description, minimum number of members).
- Default property values can now be set on a teamwork template.
- Teamwork can now be created in app context. Allowing the possibilities of only having self-service of MS Teams through Omnia.
- The create Teamwork wizard has been completely remade and fixes (#136225, #126909).
- Teamwork provisioning now supports sensitivity labels.
- Corrected validation of group names already existing. 
- Corrected URL validation in all scenarios (#124846, #120614).
- Teamwork rollup now uses the correct date format configured (#120436, #120434).
- Better usage of space in the teamwork rollup in narrow columns (#122146).
- Teamwork image can now be set in Omnia and will be synchronized to the O365 Group or Site.
- Updated people picker to only allow picking valid options (#132420, #133052).
- Teamwork templates can now be targeted.
- Time zone can now be selected by the end user when provisioning a teamwork instance. 
- Fixed an issue where properties would not safe if placed after a custom step (#121168).
- Detaching a teamwork instance no longer sends email (#133240).
- Improved error message when editing a teamwork app that you do not have permissions on (#120426).
- Email send outs have been reviewed (#134224).
- Inactive teamwork can now be reviewed in Omnia Admin.
- Fixed an issue where the wrong feature UI could sometimes be loaded in Omnia Admin.
- Long word site titles will now work as expected (#123672).
- Teamwork layouts can now be created and included as a tab in MS Teams. (To display for example Controlled Documents Authoring).
- Its now possible to provision a MS Teams Teamwork from an existing MS Team.
- MS Teams standard templates are now supported in Omnia templates.
- A Planner board can now be provisioned together with the Teamwork.



Process Management
*****
- Using “Add as favorite” action button on processes now adds the process with the correct title (#135579).
- Processes can now be printed or exported to PDF.
- Mouse over no longer shows cursor:pointer if there is no link (#120202, #123510).
- Process search can now be combined with other kinds of data.

Workplace
************
- The User Profile Competition block now has configurable button labels (#116581).
-  Mega menu rendering in mobile and tablet improved (#125709).
- Corrected an issue with the action bar rendering when navigating via direct links (#119504).
- Corrected hover effect on links in the top navigation (#114578).
- App Instance Posts Block available. See main release notes.
- The Logo now correctly renders as unclickable if no link is configured (#133844).
- Its now possible to configure if "My subscriptions" will show up or not in the user profile card.
- Team channel feed now handles System events correctly.
- The calendar rollup no longer contains a broken link to the calendar item in Outlook.
- Publishing apps now have a contribute role, making it possible to control who can comment/like/rate etc.

Web Content Management
*************
- Label padding now aligns better (#138463).
- Possibility to move pages between page collections (#113462, #132221).
- Possibility to move page collections between publishing apps (#113462, #132221).
- Related links can now use more options on how to open links (#133631, #119645, #120098).
- Related links now handles long links better including line breaks (#113899).
- RSS Feed block can now handle more kinds of images (#115862, #116968).
- Media properties can now have default values (#116730).
- SVG files now provide correct thumbnails when picked from a SharePoint library (#136801)
- Show more button in the Quick Links block now have the correct color settings (#117529, #117911)
- Corrected an issue with color settings in the enterprise glossary (#136443).
- Sorting by columns now has a larger clickable area (#119772).
- Fixed a cache issue on the page collection settings page (#137099).
- The variation picker no longer shows drafts as selectable (#128061).
- Improved UI in the edit banner form for small screens (#136671).
- Corrected the design of bullet lists in the FAQ block (#114117). 
- Automatic translation options are now correct when inheriting from tenant (#115062).
- Added possibility to resync Omnia Search Index, stability improvements to sync of SharePoint data. (#137857). 
- Improved page view statistics gathering. 
- Fixed an intermittent error where the preview of pages would sometimes give access denied (#136471, #138372, #134866, #136157).
- Authors can no longer delete page collections.
- Reworked action menus, icons, and option placement.
- Performance improvements for automatic translations.
- Performance improvements for editing Channels.
- Improved support for right to left languages when using auto translate.
- Emails sent from Web Content Management now fallback to the Business profile language.
- “Controlled Documents” and “Process Library” can now be activated on the backend site of a publishing app. 
- Channels can now be categories in to one Default Channel and Additional Channels.
- Blocks from a Layout/Page Type can now be configured to be unlockable. Allowing the editor on the page to change its configuration.
- Updated link picker UX with more options.
- Page Versioned Documents allow the editor to tie a document to the page versioning. It also allows first line works / Kaizala users to download the document. 
- Automatically translated pages can now be edited. NOTE: The edit will be overwritten upon a new publish of the default page.
- When moving a page in the navigation structure to a childless node, the page is now selected after the move (#118661).
- A generic integration is now available to connect omnia to third party big screen providers. 
- Additional blocks supported for automatic translation.
- Publishing app settings tabs have been reorganized.
- Reusable content pages with many connections, now needs to be manually triggered.
- AD Groups can now be set as publishers on Channels. 

Search
*******
- Corrected rendering of links in search (#138299).
- Layout updates to search to better use the space when using promoted links and feedback (#136188, #136341, #136593).
- Improvements to the Omnia Free Text search generation (#136940, #136892).
- Corrected rendering of Teams Presence in Quick Search.
- Added missing shadow of dropdown.

Controlled documents
****
- Added support for icons on .msg files (#120880).
- Updating multiple draft documents properties will now work correctly (#138671).
- Added a missing space to the default text in the Feedback dialog (#120819, #122188).
- Document rollup now correctly resets filters when navigating between multiple rollups with different settings (#119636).
- All metadata in a document rollup can now be exported to Excel. 
- User Language ({UserLanguage}) can now be used as a token in the query of the document rollup.


System
**********
- The Azure AD Sync has received several updates to improve stability (#138948).
- Default content features can now be upgraded without error (#120974).
- Feature naming and categories have been updated. 
- User profile completeness now reaches 100% even when the user profile picture is included (#119425, #134770).
- Improved rendering of Icons in all system (#120369).
- Corrected the z-index of the “Your session has expired” message (#120381).
- General performance improvements for page loads and page rollups.
- The login flow has been simplified, leading to better performance on login.
- The setup Wizard is now available for all tenants.
- The Script block MSGraph client now refreshes its tokens automatically in case they expire.
- New definitions of built-in groups, see main release notes.
- Multiple targeting properties can now be linked to the same enterprise property (#116344).
- A Teamwork app generator is now available to make deployments to MS Teams easier.

Page Rollup
*********
- Possibility to view and sort by Most visited (#118520).
- Better overflow for the page rollup in narrow columns (#133906).
- Its now possible to sort on text in the page rollup (#119522, #127382, #128932, #124725).
- Possibility to show pages in a calendar view.
- Possibility to query on All pages (Tenant) or all pages in a Business Profile.
- Possibility to query on Language.
- Possibility to query on and show pages that has never been published.
- Possibility to query on Workflow status (Scheduled).
- Possibility to query on statistics. 
- Possibility to sort by most viewed. (#115241, #121723).
- The page rollup results can now be exported to Excel.
- Possibility to filter on Channels for all scopes. 
- Corrected background color from theming in the navigation view. (#131977).
- Its now possible to have custom labels in the List View.
- Social period has been renamed Time Period in settings. 
- The Page rollup can now be configured to open the target page in the editor. Allowing for editorial tools to be created using the page rollup.
- Corrected line height in the dynamic roller.



WCAG and UI/UX
***************
- alt text when hovering term picker icon corrected. (#115442).
- Better rendering of term picker with many terms at the top of the screen (#133753).
- When selecting multiple terms, the picker will not close between selections (#116627, #121832).
- Corrected color for the close button of the notification panel admin blade (#126112).
- aria-describedby is now used to connect error messages in user profile completeness to the correct form input.
- Configurable alt-text now available on the tenant and BP logos.
- Browser title updated to better comply with WCAG recommendations. 
- Updated aria-labels for navigation components.
- no-script message added if Omnia is started without JavaScript enabled. 
- Corrected heading structure to better comply with WCAG standard. 
- Better element IDs for the search panel.
- Improved keyboard control feedback.
- Several corrections to rendering in Safari.
- Teams presence is now available on all components where applicable. 
- Corrected background color on the skeleton loader.
- Close button and click out added to the tutorial.

Also fixes preview bugs (#138042, #138335, #138527, #138224, #138538, #138239, #138050, #137947, #138216)
