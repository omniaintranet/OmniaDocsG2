Welcome block
==================================

This block is available in Omnia 7.8 and later. It can be used for various messages, on specific dates or occasions, to the logged in user.

Here's a simple example:

.. image:: welcome-block.png

For information aboiut how this is set upp, see below.

Settings
************
Available settings are these:

.. image:: welcome-block-settings.png
 
General
-------------
You can add a name for the block here, if needed.

.. image:: welcome-block-settings-general.png 

Profile image
---------------
Here you can choose to show an avatar (meaning a profile image), and if you do, the following settings are available:

.. image:: welcome-block-settings-profile.png 

You can see a preview in the block while testing different settings.

+ **Position**: Set the position for the avatar, in relation to the message(s); Left, Right, Top or Bottom.
+ **Size**: Set the size of the avatar; Small, Medium, Large or Extra large,
+ **Elevation and Border width**: Use the sliders to set avatar elevation and a border in pixels, if you want.
+ **Border color**: If you opt to use a border (meaning setting it to more than 0 pixels), you can set the color of the border here.

Messages
-----------
You can use this section to add one or more messages and to set the name to be shown. The following settings are available here:

.. image:: welcome-block-settings-messages.png 

+ **Message template**: Here you add the message. If you would like to display a name for the user, add a token. For available tokens, see below.
+ **Message type**: The message type can be Time in day, Date time, Day of week, Birthday or Default. Note that different settings are available for the message types. See below for more information. (Also see below for a message).
+ **Font size**: Use the slider to set the font size. Default font size is 14. You can't set the size smaller than that.
+ **Text color**: The text color for the message can be set here.
+ **Bold, italic or underscore**: The text can also be bold, italic or underscored.

You must save each message before adding another one.

When one message is added, click the plus to add another text:

.. image:: welcome-block-settings-messages-more.png 

You can use the pen and the dustbin for each message, to edit or delete it.

Available tokens for the name
-------------------------------
In the Welcome block you can use the User properties as token to show the users name, for example Username or Display name. Here's how you add these tow tokens in the Message template field (note the difference):

+ {[Username]}
+ {[Display name]}!

Message types
----------------
You can use the message types this way:

+ Time in day: Select a day and time when the message should be shown. It's then shown, that time in day, until you delete it.
+ Date time: Set a period for when the message should shown; a start date and time and en end day and time.
+ Day of week: Set which day of the week the message should be shown. It's then shown, that day of the week, until you delete it.
+ Birthday: Select the data source for the birthday date. There must be a data source for birthday set up for this to work.
+ Default: The message is shown from now on, til you delete it.

Style
---------------
Just settings for padding available here.

.. image:: welcome-block-settings-style.png 

Welcome block implementation example
************************************
In this example (also shown at the top of the page):

.. image:: welcome-block.png

These settings are used:

(No block title used and no padding added).

For Profile image, the following settings are used:

.. image:: profile-image-example.png

As for Messages, it's set up to show three different messagesm depending on time of day, and the user's name:

.. image:: Message-example.png

Note that the token "Display name" is used (last "message"). The message type "Time of day" is used for all three messages, and then Morning, Afternoon and Evening as "Display time". Here's eth settings for Morning as an example:

.. image:: Morning-example.png


