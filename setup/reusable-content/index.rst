Setup reusable sections
=========================

Prerequisite: "Enable reuse content" must be turned on in the publishing app settings, see: :doc:`Publishing app settings </pages/page-settings/index>`

Follow these steps to setup a reusable section:

1. Create an enterprise property of type Data.
2. Create a page type.
	a. Add a section of type Reusable section. 
	b. Map it to the property from step 1.
	c. Publish the page type.
3. Create a page using the page type from step 2.
	a. Add blocks to the reusable section.
	b. Publish the page.
4. Create another page using the page type from step 2.
	a. Configure reusable content. 
	b. Select the page from step 3 as source. 
	c. add the property from step 1. 
	d. Publish the page.

When the content of the reusable section on the page from step 3 is updated it will be reflected on the page from step 4.

Important notes
*****************
+ A Reusable section can’t be moved or copied.
+ You can’t move a block within a reusable section if the sections has been used for reusable content at least once.
+ A Reusable section can’t contain a block that uses a property for some or all content.
+ Blocks and sections with reused content are locked on the target page. They can not be edited there. Reused content can only be edited on the source page.
+ The editor working with the reusable content on the source page must have editing permissions on the target pages as well.

More information on reusable content
***************************************
See these pages for more information:

+ :doc:`Reusable content </pages/reusable-content/index>`
