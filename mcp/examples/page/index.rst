Pages
=====

Pages are the content itself - a news article, a policy, a guide. Through the connector you can create a page inside a page collection, read one, change its title and properties, publish it, discard a draft and archive it.

Writing a page in a conversation works best when you bring the material: an article, a set of notes, a mail thread. The connector fills in the page's properties from what you agree on, and asks about anything it cannot know.

.. TODO screenshot: a page created through the connector, seen in the Omnia interface

What you can ask for
********************

+ Create a page in a page collection.
+ Read a page - its title, address, page type, property values, checkout state and version.
+ Change a page's title or property values.
+ Publish the current draft.
+ Discard the current draft and go back to the published version.
+ Archive a page.

Creating a page
***************

::

   Create a page called "Travel policy 2026" in the Policies page collection
   of https://contoso.omniacloud.net/sites/hr, based on this document

The **page type** decides which properties the page has. If the page collection allows only one page type it is used automatically; otherwise you pick from the ones it allows.

Every one of the page type's properties then has to be **answered** - either with a value, or explicitly left empty. That is deliberate: it is how you find out what the page type expects instead of publishing a page with silent gaps.

Finally you choose whether to **publish the page now or leave it as a draft**.

.. TODO screenshot: Claude asking for the page type and property values

Images
******

An image property is the one property that needs a short conversation of its own, because two things must be true: **you** choose where the image comes from, and **you** see it before it is stored.

1. You are offered the available sources. **Direct image URL** is for when you have the image's own address; **article link** is for when you have a web page and want to pick one of the images in it.
2. You give the link. The connector fetches what is behind it and returns the candidates **as thumbnails**.
3. You pick or confirm one, and only then is the image fetched, scaled and stored on the page.

.. TODO screenshot: image candidates shown as thumbnails to pick from

+ **Alt text is required.** You are asked for it and it is never invented, because a wrong description is worse for someone using a screen reader than none at all. For an image that carries no information, say it is decorative and an empty alt text is stored.
+ Only ``https`` links work, and the format is identified from the file itself - JPEG, PNG, GIF, BMP and WebP are supported; SVG and ICO are not.
+ If the image is larger than the tenant's limit, the tenant's image scalings are offered and you choose one - including keeping the original size.
+ Cropping and ratio renditions are not supported through the connector.
+ The tenant's central image library is not supported yet.

Working with an existing page
*****************************

::

   Show me the page at https://contoso.omniacloud.net/sites/hr/travel-policy

::

   Update the summary of the travel policy page and set the review date
   to the first of March next year, then publish it

Changing a page **checks it out for you** if needed, and only the fields you mention change. A property is cleared by saying so explicitly; a required property cannot be cleared.

::

   Discard the draft on the travel policy page

.. TODO screenshot: Claude publishing a page and reporting the result

Archiving
*********

::

   Archive the page "Travel policy 2024", comment "Replaced by the 2026 policy"

Good to know
************

+ Creating needs a **page collection** scope; everything else needs the **page**.
+ A new page is created as a **direct child of the page collection**. Nesting it under another page is not supported yet.
+ The page collection's allowed page types are read from its **last published** configuration, so a page collection that has never been published cannot take new pages yet.
+ A new page gets **no layout** - it is not copied from the page type.
+ The page's **address is generated from the title** and is never changed afterwards by the connector, because changing a live page's URL has consequences a chat message should not carry.
+ **Publishing sends no notification.** Publishing twice with nothing changed in between is refused, because there is no draft to publish.
+ **Discarding a draft** needs a draft to exist, and needs the page to have been published at least once - there is nothing to go back to otherwise.
+ **Omnia has no page deletion.** Archiving is the equivalent, it is reversible, and it **cascades to the page's children** - every archived page is listed back to you, so confirm before archiving a page that has children. Images are left in place so a restore brings the page back intact.

Actions
*******

+ ``Page.Create`` - create a page in a page collection.
+ ``Page.Get`` - read a page.
+ ``Page.Save`` - change a page's title or property values.
+ ``Page.Publish`` - publish the current draft.
+ ``Page.Undo`` - discard the current draft.
+ ``Page.Archive`` - archive the page and its children.
