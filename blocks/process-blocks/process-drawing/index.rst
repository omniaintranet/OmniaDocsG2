Process drawing block
======================

Use this block to display the process drawing for the process. The process is not set in the block, it's set on the Properties tab of the page, see this page for more information: :doc:`Displaying processes for users </working-with-processes/displaying-processes-for-users/index>`

Settings
***********
The block has the following settings:

.. image:: process-drawing-block-v78.png

+ **Title**: You can add a title, if nedded.
+ **Padding**: Add some padding between the block frame and the content, if needed.
+ **Enable process status colors**: Applicable for a Teams environment. If selected, the background colors of process steps will change depending on status.
+ **Stack process**: Normally when you select a sub process, the drawing for the main process is closed. Select this option if you want the main process's drawing, and all the drawings for the selected steps, to be shown at the same time. 

When you select "Stack process" additional options are available:

.. image:: process-drawing-block-stack-78.png

Use them to set the postion for the close button and to set colors.

Here's an example when Stack process is selected. Develop products is selected in the main process and both that drawing and the drawing for Develop product are shown.

.. image:: stack-process-example-v7.png

The user can close the drawing for a sub process by clicking the x.

.. image:: stack-process-close-v7.png

Layout and Write
*********************
The WRITE TAB is not used here. The LAYOUT tab contains general settings, see: :doc:`General block settings </blocks/general-block-settings/index>`

