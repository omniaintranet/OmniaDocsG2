Content analysis (OpenAI)
=============================================

This page describes how this works in Omnia 7.7.

You can set up a number of prompts for content analysis, to be used by editors. Here's an example:

.. image:: content-analysis.png

Click the pen to edit, the dust bin to delete.

All settings are available for edit, see below.

Create a new analysis
************************
When creating a new analysis, the following settings are available:

.. image:: content-analysis-new-75.png

+ **Title**: Add a title for this setting, in any available tenant language. Mandatory.
+ **Prompt**: Add the text (the instruction to OpenAI) for the prompt here. Note the message under the field. The prompt must contain the token {Text} within quotation marks.
+ **Criteria to pass check**: Can be Yes or No.
+ **Default enterprise properties**: Select one or more properties here.
+ **Prompt fix**: You can add a prompt to ask OpenAI to fix something in the content, for example to fix the spelling.
+ **TRY OUT** You can try out the settings by clicking this button.

Here's an exaple of content analysis prompt:

.. image:: content-analysis-example.png

