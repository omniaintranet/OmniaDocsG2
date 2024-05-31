Release 7
========================================

User Management
----------------------------------------

Omnia now offers the ability to create and manage users within the platform, allowing for seamless user onboarding without requiring a Microsoft 365 license.

.. image:: usermgmt-users.png

In addition to user management, Omnia provides the capability to create and manage security groups that can be utilized to safeguard content and features throughout the platform.

.. image:: usermgmt-groups.png

All users in Omnia will be assigned a user type. Examples of a user type can be Office worker, Production worker, Partner, Customer etc.
Customized user profile cards can be created for each user type, featuring unique sets of properties.

.. image:: usermgmt-usertypes.png

Omnia supports dynamic security groups based on user types. The dynamic security groups will replace and expand on the built-in groups "Internal users" and "External users".

.. image:: usermgmt-dynamicgroups.png

It is possible to create user properties in Omnia. These properties can be shown on the customized user profile cards together with properties from Azure AD and SharePoint.
The user properties in Omnia will also be used to manage targeted mobile push notifications and statistics going forward.

.. image:: usermgmt-userproperties.png

Omnia supports any custom user directory provider to synchronize groups and users into the system. Built-in providers are Microsoft Graph (Azure AD) and Active Directory (On-prem).

.. image:: usermgmt-sync.png

Omnia supports any custom authentication provider to be plugged into the system. Built-in authentication providers are Azure AD, Active Directory (On-prem) and Omnia.
Omnia provides support for a range of authentication options, including passwords, one-time passwords (OTPs), magic links, and combinations of these methods.

.. image:: usermgmt-authentication.png


Process Management improvements
----------------------------------------

Enhancements have been made to process templates, now encompassing a process layout along with default canvas size and available shapes settings.

.. image:: pm-processlayout.png

.. image:: pm-processlayout-shapes.png

The process editor has undergone a division into two distinct modes, namely Design and Content. In Design mode, you are able to work with the process drawing and the layout.
The layout for each process step can either be inherited from the overall process or customized specifically for that particular step.

.. image:: pm-process-design.png

.. image:: pm-process-design-layout.png

The process drawing tool has been improved:

* Move shapes with keyboard.
* Select multiple shapes.
* Snap to grid when rotating.
* Full support to clone all properties of a shape.
* Option to determine the priority of layers when overlaying shapes on top of one another.
* Input boxes to adjust width and height of a shape.
* Enable image cropping on background image.
* Default canvas size.

.. image:: pm-process-shapes.png


Document Management improvements
----------------------------------------

The Documents Bulk Update feature now includes the ability to find and replace inactive user accounts for employees who have left the company.

.. image:: dm-batchupdate.png

The create document wizard will now display a tooltip for document types that include a description.

.. image:: dm-doctypedescription.png

It is now possible to restore controlled document drafts from the SharePoint recycle bin.

.. image:: dm-restoredrafts.png

Teamwork governance as Microsoft Teams app
------------------------------------------

Teamwork governance can now be deployed as a Microsoft Teams app.

.. image:: msteamsapp-teamworkgovernance.png

Improved end user filters
----------------------------------------

The end user filters for all rollups have undergone significant enhancements.

.. image:: new-filters-1.png

.. image:: new-filters-2.png

The refiners section in the settings have been removed and merged into the filters section.
Rollups that support refiners (all rollups based on SharePoint Search) will have a new filter setting
to allow the possiblity to "Show result count".

.. image:: new-filters-3.png

Least privilege app permission model
----------------------------------------

Omnia now use a least privilege app permission model. Any app permissions required to run Omnia will be consent based on tenant features that are activated.
All application access to SharePoint sites will utilize the SharePoint Site Selected permission model.

Reusable content cross tenants
----------------------------------------

It is now possible to connect one or more tenants together (both on-premise and online) to allow cross tenant publishing.
The automatic page creation feature has been enhanced to allow a page created in one tenant to be automatic published in another tenant.

.. image:: crosstenant-automaticpagecreation.png

Security-trimmed apps
----------------------------------------

All rollups of apps (Publishing, Community, Teamwork) has been enhanced to support security trimming. The security trimming can be configured to be based on five different types of permission:

* Administrator: Administrator of the app, for example a publishing app administrator or an M365 group owner.
* Author: Author role in the app, for example a publishing app editor/author or a controlled documents author.
* Contributor: Contributor role in the app, for example a community member or an M365 group member.
* Reader: Reader role in the app, for example reader in a page collection or SharePoint site reader.
* Viewer: Viewer role in the app, possibility to read meta information about an app and public teamwork information.

.. image:: approllup-securitytrimming.png

Multi-lingual improvements
----------------------------------------

Enhanded multi-lingual support:

* Tenant and Business Profile names.
* Publishing App title and description.
* Navigation node titles.
* Page Types titles.

(7.1) Media gallery
--------------------------------------------

The media block and RTF editor now offer the option to enable the multi-selection of images and videos in the media picker.
When multiple images or videos are selected, a media gallery is displayed to the end user, allowing them to open the gallery
and navigate through each image or video for additional details.

.. image:: media-gallery-add-edit-media.png

.. image:: media-gallery-wall.png

Each image or video can also include a caption, which will be displayed beneath it in the details dialog.

.. image:: media-gallery-dialog-video.png


(7.1) Media provider for Mediaflow
--------------------------------------------

A new out-of-the-box media provider, that integrates with Mediaflow, is now available in the media picker.

.. image:: media-flow-administration.png

.. image:: media-flow-mediapicker.png

Please find more information about Mediaflow here: https://www.mediaflow.com/.

(Note! This feature requires a subscription to the Mediaflow service.)

(7.1) Media provider for Dall-E 
--------------------------------------------

A new out-of-the-box media provider, that integrates with Dall-E (Azure Open AI), is now available in the media picker.
DALL-E is an AI model developed by OpenAI. It is a variation of the GPT architecture and is designed specifically for generating images from textual descriptions.

.. image:: openai-dalle-mediapicker.png

(Note! Open AI requires an Azure Open AI subscription)

(7.1) Multi-level approval on pages
--------------------------------------------

It is now possible to enable multi-level approval on pages in a page collection.

.. image:: multistep-approval-settings-2.png

The approval process is sequential, with each step governed by a set of business rules determining
the appropriate approver for that step and specifying the tasks that the approver is authorized to perform.

.. image:: multistep-approval-dialog-2.png

(7.1) Dynamic 401/404 pages
--------------------------------------------

It is now possible to design your own 401/404 error pages. Instead of generic and unhelpful error messages,
you can make these pages more engaging, maintain brand consistency, and guide users back to valuable content.
It's a simple yet effective way to enhance the overall user experience and build trust with your audience.

.. image:: system-layouts-404-edit.png

(7.1) Broken links detection and metrics
--------------------------------------------

Omnia now features a built-in broken link detector. It identifies all 404 errors within the solution and provides
comprehensive metrics, showing the frequency of user encounters with broken links each month.
Additionally, you can access in-depth information regarding these broken links, including their referring page.

.. image:: broken-links-dashboard-metrics.png

.. image:: broken-links-details.png

(7.1) Colors in calendar view
--------------------------------------------

We have added 'Page Type' and 'Workflow Status' to the Enterprise Glossary, allowing them to be customized with colors and icons.

.. image:: calendar-colors-enterprise-glossary.png

Now, these properties can be chosen within the page rollup calendar view and used as the foundation
for the icon and background color assigned to each page on the calendar.

.. image:: pagerollup-calendar-colors-edit.png

(7.1) Process management shape descriptions
--------------------------------------------

It is now possible to add a rich text description to shapes on a process template.

.. image:: shape-descriptions-administration.png

This will assist the process designer in making decisions on which shape to use when adding shapes to a process.

.. image:: shape-descriptions-add-shape.png

(7.1) Generate page content with AI
--------------------------------------------

You can enable authors in a page collection to utilize AI when generating content for a page.
The author describes which content to create...

.. image:: openai-generatedcontent-createpagedialog-1.png

.. image:: openai-generatedcontent-createpagedialog-2.png

...and AI generates a draft that the author can further refine and edit.

.. image:: openai-generatedcontent-draft.png

A text block can also be set up to automatically generate a summary based on another text property on the page.
This allows the page author to concentrate on the narrative, while AI handles the summary creation.

.. image:: openai-automaticsummary-edit.png

(Note! Open AI requires an Azure Open AI subscription)

(7.1) Improve text with AI
--------------------------------------------

Now, it's possible to centrally configure AI prompts within Omnia Admin, offering support to page authors as they enhance their content during the writing process.

.. image:: openai-improvetext-dialog.png

(Note! Open AI requires an Azure Open AI subscription)

(7.1) Analyze content with AI
--------------------------------------------

AI can assist editors in analyzing content within a publishing app, generating a well-structured report of the results.
The reports are generated based on the assumption that a page will either meet or not meet specific criteria.

.. image:: openai-contentanalysis-report.png

AI will also show a detailed description on why a certain page doesn't meet the criteria.

.. image:: openai-contentanalysis-details.png

(Note! Open AI requires an Azure Open AI subscription)

(7.5) Improved user management
--------------------------------------------

Business profile users and groups
********************************************

Users and groups can now be specifically scoped to a business profile, enabling seamless management by a business profile administrator.
This functionality empowers administrators to oversee users with access limited to designated sections of the solution, such as front-line workers or partners.

.. image:: usermgmt-businessprofileusers.png

Self-service account creation and on-boarding
**********************************************

You can now activate self-service account creation for a business profile, with the option to configure whether approval is necessary or not.

.. image:: usermgmt-selfservice.png

The account request form can be configured to allow users to submit account information in advance for an administrator to validate.

.. image:: usermgmt-requestformsettings.png

You can configure anonymous access to a specific section of a business profile to set up a welcome page providing information about the account request procedure.

.. image:: usermgmt-loginscreen-anonymous.png

A user type with password as authentication mechanism can be setup to force password change on first login.

.. image:: usermgmt-forcepasswordchange.png

A unique onboarding URL can be configured for each user type, enabling users to be redirected to a specific portal once their new account has been set up.

.. image:: usermgmt-onboardingurl.png

  
Improved identity picker
*********************************************

In response to customer feedback, we have revamped the identity picker UI. Now, users and groups are conveniently listed in a single interface,
offering the option to filter based on specific user and group types.

.. image:: usermgmt-identitypicker.png

Improved user profile cards
*********************************************

The user profile card can now feature two distinct layouts. A public layout is displayed when someone else views your profile card,
while a private layout can be configured for your own viewing. This customization allows for a focus on different properties and roll-ups depending on the target audience.

.. image:: usermgmt-publicprivate-profilecard.png

User properties can be configured as either public or private. Private properties are exclusively accessible by the user and can be utilized to
store information meant solely for the user's eyes, ensuring that it is only displayed on the private profile layout.

.. image:: usermgmt-publicprivate-properties.png

Both public and private properties can be used to aggregate information on a profile card.
A new dynamic value in rollups is now available, allowing for the aggregation of information about the selected user in focus when opening a profile card.

.. image:: usermgmt-queryonselecteduser.png

The profile card settings can be adjusted to enable users to update their profile photos.
Additionally, for users with an M365 license, the profile photo will automatically synchronize across all M365 services.

.. image:: usermgmt-editprofilephoto.png

New scope in the People rollup block
**********************************************

A new scope in the People rollup block makes it possible to find all users that are synchronized to Omnia or created as Omnia accounts.

.. image:: usermgmt-peoplerollup-users.png

Improved user management governance
**********************************************

We have introduced a login log feature to track all successful and unsuccessful login attempts made by Omnia accounts within the system.

.. image:: usermgmt-loginlog.png

There is also a possibility to create custom authentication layouts for the following activities: Request account, Setup account, Login and Logout.

.. image:: usermgmt-authenticationscreens.png

Accounts can now be setup to be time-limited. It is also possible for an administrator to disable an account at any time.

.. image:: usermgmt-timelimited-and-disabled.png


(7.5) Analytics powered by Matomo
--------------------------------------------

The analytics features have transitioned to being powered by Matomo. A local instance of Matomo will be automatically established in the tenant,
offering access to over 100 widgets for analyzing usage and behavior within your solution.

.. image:: analytics-widget-settings.png

.. image:: analytics-widget-read.png

(7.5) Anchor navigation
--------------------------------------------

We've added a new block to enhance anchor navigation, making it easier and more efficient for users to navigate through content.
This improvement ensures a smoother and more user-friendly experience when moving through different sections of a page.

.. image:: anchornavigation-settings.png

.. image:: anchornavigation-read.png

(7.5) Publishing campaigns
--------------------------------------------

We've simplified the process of creating publishing campaigns in the solution. Two new features have been added to enhance this functionality further, making it more powerful.

You can set up a calendar view in the page rollup to allow page creation directly from the calendar.

.. image:: publishingcampaigns-createarticlefromcalendar-settings.png

.. image:: publishingcampaigns-createarticlefromcalendar.png

You can now configure promotion channels to send teasers to Microsoft Teams, Viva Engage, and via email.

.. image:: promotionchannels-settings.png

.. image:: promotionchannels-email.png

(7.5) Improved metrics
--------------------------------------------

The possibility to configure metrics have now been added to the publishing, community and teamwork rollup blocks.

.. image:: approllups-metric.png

We've introduced a new custom date query builder, allowing users to perform advanced date queries for creating metrics.

.. image:: datequery-custom.png

(7.5) Improved page feedback
--------------------------------------------

It is now possible to use an action button to provide feedback on a page.

.. image:: feedback-action.png

Accessing feedback is now made simple through the menu in the content editor.

.. image:: feedback-list.png


(7.6) Improved mobile and frontline
------------------------------------------------------

A new feature has been added to the user management section that empowers group owners with enhanced administrative capabilities within their groups.
Group owners can now create and manage individual users directly within their groups. This feature provides greater flexibility and control, allowing group owners to tailor the user management process to their specific needs.

.. image:: usermanagement-create-user-in-group.png

We have also added the possibility to add Entra ID users to Omnia groups as part of this feature.

Administrators can now create local forms directly within an Omnia publishing app. Additionally, we've introduced a streamlined method for form creation using an action button.
This simplified form creation allows for the rapid development and publishing of quick polls or similar forms to specific target audiences.
Users can also assign properties to these forms, which can be utilized for targeting purposes and incorporated into a new Forms rollup block.

.. image:: forms-create-quick-poll.png

The Forms rollup block offers both an end-user view, enabling users to respond to one or multiple forms, and an administrative view that provides an overview of all
open forms within the solution.

.. image:: forms-formsrollupblock.png

Moreover, the Omnia Feed mobile app now features a setting that enables new forms to be published with a push notification.
These forms will be displayed natively in the master feed within the mobile app.


(7.6) Improved communication
--------------------------------------------

You can now utilize the newly introduced Media rollup block to showcase images, videos, and audio files sourced from a SharePoint library.
This versatile block offers two distinct views: a visually engaging Photowall view and a straightforward list view.

.. image:: mediarollup.png

For end users, navigating through the various media items is intuitive and user-friendly. They can easily browse the content in a dialog format,
facilitating quick actions such as downloading the desired media files with ease.

.. image:: forms-formsrollupblock.png


The sign-off request feature has been significantly improved to offer greater flexibility and functionality.
Now, users can create both one-time scheduled sign-off requests and recurring sign-off requests that are automatically sent out at specified intervals.
This enhancement streamlines the sign-off process, enabling more efficient management of approvals and ensuring timely responses from recipients.

.. image:: sign-off-requests-recurring.png

The mobile experience for authors has been enhanced to provide a more seamless and user-friendly interface.
Now, when authors upload images from their mobile devices in portrait format, the images will retain their original orientation. 

.. image:: mobile-author-experience.png

The RTF editor has been enhanced to include support for subscript and superscript formatting options. 

.. image:: rtf-editor-sub-super-script.png


(7.6) Improved governance and analytics
------------------------------------------------------

The analytics solution, powered by Matomo, has been enhanced to incorporate an Analytics report block.
This feature enables widgets from Matomo to be displayed in a table style with Omnia look and feel.

It is now possible in Omnia Admin to centrally reassign tasks for controlled documents in bulk.

.. image:: dm-tasks-bulk-update.png



Versions
-----------------------------------------

.. toctree::
   :titlesonly:

   versions