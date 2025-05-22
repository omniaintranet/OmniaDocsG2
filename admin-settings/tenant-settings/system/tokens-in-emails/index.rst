Tokens in Omnia emails
=========================

Here you will find a list of Omnia Emails that contain tokens, and the tokens supported in each Email. Also note that tokens must not be translated.

**Note!** In some files Subject is called "EmailTitle" and Body can be called "Description". In this document Subject and Body are always used.

Announcements emails
-------------------------
There are three different Emails that can be sent, regarding comments to announcements. In all three Emails, just one token is supported in Subject:

+ {{title}}

Sign-off requests
---------------------
In Emails for sign-off requests the following token is supported in Subject:

+ {{title}}

In the body of the Emails, the following tokens are supported:

+ {{requestreceiver}}
+ {{requestfrom}}
+ {{requestdescription}}

User profile completion
-------------------------
In the User profile completion feedback Emails, the following token is supported in Subject:

+ {{userprofileproperty}}

In the body of the Emails, this token is supported:

+ {{feedback-email}}

Document management - Controlled documents
--------------------------------------------
The following tokens are supported in Emails regarding Controlled documents:

**Review task Emails**: In these Emails for Document management, the following token is supported in Subject:

In **ReviewerEmailSubjectTemplate** and **CancelSubjectTemplate**:

+ {{DocumentTitle}}

(In ReviewEndNotifyEmailSubjectTemplate no token is supported).

In the body, the following tokens are supported:

In **ReviewerEmailBodyTemplate**: 

+ {{Reviewer}}
+ {{Author}}
+ {{DueDate}}
+ {{DocumentUrl}}
+ {{DocumentTitle}}
+ {{TaskUrl}}
+ {{TaskTitle}}
+ {{Message}}

In **ReviewEndNotifyEmailBodyTemplate**:

+ {{Author}}
+ {{DocumentUrl}}
+ {{DocumentTitle}}

In **CancelBodyTemplate**:

+ {{Reviewer}}
+ {{DocumentTitle}}

In **ReviewerCompleteInfo** and **ReviewerIncompleteInfo**:

+ {{*}}

**Review reminder Email**: In this Email for Document Management, this token is supported in Subject:

+ {{DocumentTitle}}

and these tokens are supported in Body:

+ {{Recipient}}
+ {{DocumentUrl}}
+ {{DocumentTitle}}
+ {{SiteUrl}}
+ {{SiteTitle}}
+ {{PublishDate}}
+ {{ReviewDate}}

**Publishing Notification e-mail**: In this Document management Email, this token is supported in Subject:

+ {{DocumentTitle}}

In the body of **EmailBodyTemplate**, the following tokens are supported:

+ {{Recipient}}
+ {{DocumentUrl}}
+ {{DocumentTitle}}

If Read Receipt is selected **EmailBodyWithReadReceiptTemplate**, these tokens are supported:

+ {{Recipient}}
+ {{DocumentUrl}}
+ {{DocumentTitle}}
+ {{ReadReceiptUrl}}

**Send for approval Emails**: In these Document managment Emails, this token is supported in Subject (in **EmailSubjectTemplate**, **SubjectApproval**, **SubjectReject** and **CancelSubjectTemplate**):

+ {{Name}}

The folllowing tokens are supported in Body for these Emails:

In **EmailBodyTemplate**:

+ {{Approver}}
+ {{Author}}
+ {{Name}}
+ {{DueDate}}
+ {{DocumentLink}}
+ {{TaskTitle}}

In **ApprovalEditionCommentTemplate**:

+ {{Author}}
+ {{StartDate}}
+ {{Message}}

In **BodyApproval** and in **BodyReject**:

+ {{Author}}
+ {{Name}}
+ {{Approver}}
+ {{ApproverComment}}

In **BodyApprovalNoComment**:

+ {{Author}}
+ {{Name}}
+ {{Approver}}

In **CancelBodyTemplate**: 

+ {{Approver}}
+ {{Name}}

**Feedback e-mail**:
In this Document management Email, these tokens are supported in Subject:

+ {{DocumentName}}
+ {{DocumentId}}

In Body for that Email, the following tokens are supported:

+ {{Sender}}
+ {{Feedback}}
+ {{DocumentLink}}

**Related document Emails**: Here, no tokens are supported in Subject. The following tokens are supported in Body:

+ {{Recipient}}
+ {{RelatedDocument}}
+ {{Publisher}}
+ {{ControlledDocuments}}

**Retention policy Email**: In this Email, no tokens are supported in Subject. The following tokens are supported in Body:

+ {{RetentionManager}}
+ {{RetentionDocuments}}

**Review workflow tasks Email**: In these Document management Emails, no tokens are supported in Subject. The following tokens are supported in Body:

+ {{Author}}
+ {{DocumentUrl}}
+ {{DocumentTitle}}

Emails for processes
------------------------
**Feedback Email**: In the feedback Email for processes, these two tokens are supported in Subject:

+ {{ProcessTitle}}
+ {{ProcessStepId}}

In the Body for this Email, these tokens are supported:

+ {{Sender}}
+ {{Feedback}}

**Send for approval Email**: This token is supported in Subject for this processes Email:

+ {{ProcessTitle}}

And these tokens are supported in Body:

+ {{ApproverName}}
+ {{AuthorName}}
+ {{ProcessTitle}}
+ {{DueDate}}
+ {{ProcessLink}}
+ {{TaskLink}}
+ {{TaskTitle}}
+ {{StartDate}}
+ {{Message}}

**Cancel approval Email**: This token is supported in Subject in this processes Email:

+ {{ProcessTitle}}

And these two tokens are supported in Body:

+ {{ApproverName}}
+ {{ProcessTitle}}

**Complete approval Emails**: Used for both approval message and rejected message, for processes, this token is supported in Subject:

+ {{ProcessTitle}}

The following tokens are supported in Body for **ApproveBodyTemplate** and **RejectBodyTemplate**:

+ {{AuthorName}}
+ {{ProcessTitle}}
+ {{ApproverName}} 
+ {{ApproverComment}}

The following tokens are supported in Body for **ApproveBodyTemplateApproveBodyNoCommentTemplate**:

+ {{AuthorName}}
+ {{ProcessTitle}}
+ {{ApproverName}} 

**Review reminder Email**: this token is supported in Subject for this Processes e-mail:

+ {{ProcessTitle}}

The following tokens are supported in Body:

+ {{Recipient}}
+ {{ProcessLink}}
+ {{ProcessTitle}}
+ {{SiteUrl}}
+ {{SiteTitle}}
+ {{PublishDate}}
+ {{ReviewDate}}

App approval emails
----------------------
In the app approval Emails (for Communities, Publishing and Teamwork), the following tokens are supported:

**AppRequestToApprove**: In this Email, sent to the approver, no token is supported in Subject. The following token is supported in Body:

+ {{pendingRequestUrl}}

**App provisioning complete Email**: In this email, sent to the requester, no token is supported in Subject. The following tokens are supported in Body:

+ {{userDisplayName}}
+ {{appUrl}}
+ {{title}}

**AppRequestRejectedToRequester email**: Sent when creation of the community, publishing app or teamwork is rejected, no tokens are supported in Subject. The following tokens are supported in Body:

+ {{UserDisplayName1}}
+ {{rejectedComment}}
+ {{UserDisplayName2}}
+ {{rejectedTime}}

Emails for events
-------------------
In the **AddParticipant email**, this token is supported in Subject:

+ {{eventName}}",

and the following tokens are supported in Body:

+ {{eventName}}
+ {{startDate}}

Various Emails connected to action buttons
---------------------------------------------
A number of short Emails can be sent after action button actions. The token {{title}} is supported in Subject in some of these Emails:

AddComment, BestReplyComment, SubmitFeedback, PublishingApproval (six different emails - Approve, Reject, CancelApproval, ScheduleApprove, ScheduleReject, CancelScheduleApproval).

No tokens are supported in Body for these Emails.

Emails to variation authors
------------------------------
In Subject for these Emails (NewPageSubject and NewVersionSubject), this token is supported:

+ {{title}}

In the body called **Author**, the following token is supported:

+ {{name}}

Email for invitation of co-author
-----------------------------------
In the Email **InvitationOfCoAuthors**, no tokens are supported in Subject. These three tokens are supported in Body:

+ {{pageUrl}}
+ {{title}}
+ {{content}}


