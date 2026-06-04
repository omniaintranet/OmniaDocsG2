Setup reusable content for blocks and sections
==================================================

We are still working on this description. Will be finished soon.

Prerequisite: "Enable reuse content" must be turned on in the publishing app settings, see: :doc:`Publishing app settings </pages/page-settings/index>`


Setting up reusable sections
******************************
Follow these steps:

1. Create an enterprise property of type Data.
2. Create a page type.
	2a. Add a section of type Reuseable section. 
	2b. Map it to the property from step 1.
	2c. Publish the page type.
3. Create a page using the page type from step 2.
	3a. Add blocks to the reusable section.
	3b. Publish the page.
4. Create another page using the page type from step 2.
	4a. Configure reuseable content. 
	4b. Select the page from step 3 as source. 
	4c. add the property from step 1. 
	4d. Publish the page.

When the content of the reusable section on the page from step 3 is updated it will be reflected on the page from step 4.

Important notes
*****************
+ A Reusable section can’t be moved or copied.
+ You can’t move a block within the section if the sections has been used for reusable content at least once.
+ A Reusable section can’t contain a block that uses a property for some or all content.
+ Blocks and sections with reused content are locked on the target page. They can not be edited there. Reused content can only be edited on the source page.
+ The editor working with the reusable content on the source page must have editing permissions on the target pages as well.
