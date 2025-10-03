Email service
=======================================

Use these settings to decide if Emails should be sent from Omnia or not.

+ **Turn off all Email notifications**: If you select this option, no Emails are sent from Omnia at all. If this option is enabled (ie not turned off) Emails will be sent using the provider you choose. 
+ **Email Provider**: Normally, three options can be available here: "Exchange online mailbox", "SharePoint outgoing mail" or "Smtp server". If you select "Smtp server", additional settings are shown, see below.
+ **User mailbox**: If you choose Exchange online mailbox as the provider, select the actual user mailbox that will used. Below this the mailadress for the sender, that users will see, is noted. If you select "SharePoint outgoing mail", this field is not shown as the Sharepoint mailbox is used, which no answers can be sent to. 

**Note!** The selected user account need to have a cloud Exchange mailbox.

**Note!** This option is not available in Omnia on-prem.

Restrict who Omnia can send Emails as through Exchange
*******************************************************
To use Exchange for sending Emails from Omnia, the Microsoft permission model currently requires Omnia to be granted permission to send Emails on behalf of any user in the organization. This approach may raise security concerns. To address this, a guide for the Exchange admin to restrict Omnia to only send emails as a specified user, is included:

.. image:: custom-email-settings-v8-restrict.png

Additional Smtp server settings
************************************
If you select Smtp server as Email provider, the settings needed are made available:

.. image:: custom-email-settings-v8-smtp.png





