Email service
=======================================

Use these settings to control whether emails are sent from Omnia, and how they are sent.

+ Turn off all email notifications – When enabled, no emails are sent from Omnia. If this option is not turned off, emails are sent using the selected provider. 
+ Email Provider**: Normally, three options can be available – Exchange online mailbox**, **SharePoint outgoing mail** or **SMTP server**. If you select **SMTP server**, additional settings become available (see below).
+ User mailbox – If you choose **Exchange Online mailbox** as the provider, select the user mailbox to be used. The sender address (as seen by recipients) is displayed below. If you select **SharePoint outgoing mail**, this field is not shown, as the SharePoint mailbox is used — replies cannot be sent to this address. 

**Notes**:

+ The selected user account must have a cloud Exchange mailbox.
+ This option is not available in Omnia OnPrem.

Restricting who Omnia can send emails as (Exchange)
*******************************************************
When using Exchange to send emails from Omnia, Microsoft’s permission model requires Omnia to be granted permission to send emails on behalf of any user in the organization.

This broad permission may raise security concerns. To address this, a guide for Exchange administrators is provided — it explains how to restrict Omnia so it can only send emails as a specified user.

Additional SMTP Server aettings
************************************
If **SMTP server** is selected as the email provider, the necessary configuration fields are displayed here.





