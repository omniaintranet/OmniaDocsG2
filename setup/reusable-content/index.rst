Setup reusable sections
=========================

Prerequisite: "Enable reuse content" must be turned on in the publishing app settings, see: :doc:`Publishing app settings </pages/page-settings/index>`

Follow these steps to setup a reusable section:

1. **Create an enterprise property of type Data.**
2. **Create a page type.**
  + Add a section of type Reusable section. 
  + Map it to the property from step 1.
  + Publish the page type.
3. **Create a page using the page type from step 2.**
  + Add blocks to the reusable section.
  + Publish the page.
4. **Create another page using the page type from step 2.**
  + Configure reusable content. 
  + Select the page from step 3 as source. 
  + add the property from step 1. 
  + Publish the page.

When the content of the reusable section on the page from step 3 is updated it will be reflected on the page from step 4.

More information on reusable content
***************************************
See this pages for more information:

+ :doc:`Reusable content </pages/reusable-content/index>`
