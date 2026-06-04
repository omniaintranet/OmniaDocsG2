Setup reusable sections
=========================

In Omnia 7.11 and later, you can use reusable sections to reuse content across pages.

Prerequisite
***************
Before you start, make sure Enable reusable content is turned on in Publishing app settings.

See: Publishing app settings

Set up a reusable section
**************************
Follow these steps:Follow these steps to setup a reusable section:

1. **Create an enterprise property of type Data.**
2. **Create a page type.**
  + Add a section of type Reusable section. 
  + Map it to the property from step 1.
  + Publish the page type.
3. **Create a source page using the page type from step 2.**
  + Add blocks to the reusable section.
  + Publish the page.
4. **Create a target page using the same page type.**
  + Open reusable content configuration. 
  + Select the source page from step 3. 
  + add the property from step 1. 
  + Publish the page.

When content in the reusable section on the source page is updated and published, the same content is reflected on the target page.

.. image:: reusable-content-new.png

Important notes
*****************
+ Reused content is locked on the target page and can only be edited on the source page.
+ The editor who updates source content must have edit permissions on the target pages.
+ The reusable section cannot be moved or copied.
+ If a reusable section has been used at least once, blocks in that section cannot be rearranged.
+ A reusable section cannot contain blocks that use a property for some or all content.

Troubleshooting
*********************
If you see an error such as “the page is not reusable”:

+ Verify that reusable content is enabled in Publishing app settings.
+ Verify that the page type includes a Reusable section mapped to the correct Data property.
+ Verify that the source and target pages use the expected page type.

Verification
***************
To confirm setup is correct:

+ Edit content in the source page reusable section.
+ Publish the source page.
+ Open the target page and verify the updated content is shown.
More information
