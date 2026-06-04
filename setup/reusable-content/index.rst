Setup reusable sections
=========================

Prerequisite: "Enable reuse content" must be turned on in the publishing app settings, see: :doc:`Publishing app settings </pages/page-settings/index>`

Follow these steps to setup a reusable section:

1. **Create an enterprise property of type Data.**
2. **Create a page type.**
1. Add a section of type Reusable section. 
2. Map it to the property from step 1.
3. Publish the page type.
3. **Create a page using the page type from step 2.**
1. Add blocks to the reusable section.
2. Publish the page.
4. **Create another page using the page type from step 2.**
1. Configure reusable content. 
2. Select the page from step 3 as source. 
3. add the property from step 1. 
4. Publish the page.

When the content of the reusable section on the page from step 3 is updated it will be reflected on the page from step 4.

More information on reusable content
***************************************
See this pages for more information:

+ :doc:`Reusable content </pages/reusable-content/index>`
