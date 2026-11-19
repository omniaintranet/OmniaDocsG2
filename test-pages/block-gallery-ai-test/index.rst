Block gallery
==============

(This is an AI generated test page).

The Block gallery controls the **Add content** dialog that authors use when editing a page layout. Tenant administrators can choose which blocks and reusable block templates appear in each dialog layout, organize them, and enable the modern dialog.

Access
***********
In the Admin experience, open **Tenant > Block gallery**. Access is controlled by the tenant **Block Template Editor** role (`SecurityRoles.Tenant.BlockTemplateEditor`).

The gallery has three areas:

- **Settings** — enables or disables the modern Add content dialog.
- **Block templates** — creates and manages reusable layout templates.
- **Block dialog** — configures the items available in each Add content dialog layout.

Enable the modern Add content dialog
*****************************************
1. Open **Settings**.
2. Turn on **Modern 'Add content' dialog**.
3. Save the setting.

When enabled, authors see the modern dialog when adding content to a layout. When disabled, Omnia uses the classic dialog. The setting is initially off if it has not previously been configured.

Configure a block dialog
****************************
1. Open **Block dialog** and choose a layout.
2. Use **Add blocks** to search for and select blocks to include. Already-added blocks are not offered again.
3. Optionally add headers to group items. Headers can be edited or removed.
4. Use **Manage list** to drag items into the desired order, then confirm the new order.
5. Save the dialog configuration.

The built-in layouts are **Default**, **SPFx**, and **Authentication**. Other layouts may be available if an extension registers a dialog layout provider. Each layout has its own configuration.

If a layout has no saved configuration, its initial list is populated from the blocks applicable to that layout and grouped by category. The **Layout** category is placed first when available.

Headers and ordering
***************************
Headers appear as group labels in the modern dialog; they are not blocks that authors can add. Header titles are required and can be entered in the tenant's configured languages.

The order configured here determines the order in which blocks, templates, and headers appear to authors. Use the remove action beside a block to take it out of the list.

Manage block templates
***************************
Block templates are reusable layout content that authors can insert from the modern Add content dialog.

1. Open **Block templates**.
2. Choose **Create template**, or select an existing template to edit it.
3. Enter the localized **Title** and **Description**, choose an **Icon**, and provide the template **Definition** as valid JSON.
4. Save the template.

To make a template available in an author's dialog, also add it through **Block dialog > [layout] > Add blocks** and save that layout. Creating a template alone does not add it to a dialog.

Deleting a template does **not** automatically remove its entry from existing block dialog configurations. After deleting a template, review each relevant dialog layout and remove the stale entry there.

What authors see
********************
In the modern dialog, authors can search the configured list and select a block or template to add it to the page layout. Blocks are filtered for the current layout and context; for example, the SPFx dialog only shows SPFx-compatible blocks, and top-container areas only show blocks allowed in that context. As a result, a block configured in the gallery may not appear in every authoring context.


