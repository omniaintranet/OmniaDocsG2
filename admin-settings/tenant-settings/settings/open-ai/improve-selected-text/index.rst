Improve selected text (OpenAI)
=============================================

This page describes how this works in Omnia 7.7. For information about how this option works in Omnia 7.8 and later, see: :doc:`Improve selected text (AI settings) </admin-settings/tenant-settings/settings/ai-engine/improve-selected-text-ai-engine/index>`

You can create a number of prompt settings here to be used by editors, with OpenAI, for example:

.. image:: improve-selected-text-75.png

Click the pen to edit, the dust bin to delete.

All settings are available for edit, see below.

Create a new prompt setting
******************************
The following are available for a new prompt setting:

.. image:: improve-selected-text-new-v75.png

+ **Title**: Add a title for this setting, in any available tenant language. Mandatory.
+ **Prompt**: Add the text (the instruction to OpenAI) for the prompt here. Note the message under the field. The token {Text} must be added here, within quotation marks. See below for an example.
+ **Open chat dialog**: If the chat dialog should open, select this option. This can be useful for editors, as they can continue communicating with OpenAI to make addtional changes.
+ **TRY OUT**: You can try out the settings by clicking this button.

Here's an example of a prompt:

.. image:: improve-selected-text-example.png

See the bottom of this page for information about how OpenAI can be used in the RTF editor: :doc:`Editing text with the RTF Editor </general-assets/rtf-editor/index>`

