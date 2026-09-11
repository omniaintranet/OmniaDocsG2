Microsoft Search connectors
===========================

This guide describes how to show external items from Microsoft 365 Copilot
connectors (formerly Microsoft Graph connectors) in Omnia Search. It is intended
for partners and administrators who already have a connector that ingests
external items into Microsoft 365.

Omnia queries the Microsoft Graph Search API as the signed-in user. Microsoft
Search therefore applies the connector item's access control list (ACL) and
security trims the result for that user. Omnia does not use an app-only search
context for this scenario.

.. note:: This functionality is available only with a Microsoft 365 backend.
   A Tenant Administrator must activate the tenant feature **Microsoft Search
   connectors** and grant the delegated Microsoft Graph permission
   ``ExternalItem.Read.All``.

Before configuring Omnia
************************

Complete the following preflight in Microsoft Graph Explorer. Use the actual
connection ID, external item ID, property names, and values from your connector.
Do not continue with Omnia configuration until the deterministic search test in
step 5 succeeds.

1. Verify the connection
------------------------

Run:

.. code-block:: text

   GET https://graph.microsoft.com/v1.0/external/connections/{connection-id}

The response should be ``200 OK`` and the connection ``state`` should be
``ready``. A draft or failed connection is not ready to serve external items.

2. Verify an asynchronous schema operation
------------------------------------------

If creating or updating the schema returned ``202 Accepted`` and an operation
URL in the ``Location`` response header, send a GET request to that URL. For
example:

.. code-block:: text

   GET https://graph.microsoft.com/v1.0/external/connections/{connection-id}/operations/{operation-id}

The operation must be completed successfully. If it failed, correct the schema
error before testing search. Microsoft states that schema changes can take 5-15
minutes to take effect, so allow for propagation before assuming that a new
schema configuration has failed.

3. Verify the schema
--------------------

Run:

.. code-block:: text

   GET https://graph.microsoft.com/v1.0/external/connections/{connection-id}/schema

Review every property that Omnia should search, display, sort, or use as a
refiner:

+ ``isSearchable`` adds text to the full-text index so a free-text query can
  match it.
+ ``isRetrievable`` allows the property value to be returned in search results.
  A property used in a result template must be retrievable.
+ ``isQueryable`` allows an explicit property restriction in a KQL query, for
  example ``{schema-property}:{value}``.
+ ``isRefinable`` allows aggregations and filters. A property cannot be both
  searchable and refinable.

Properties assigned to semantic labels must be retrievable. Map the ``title``
and ``url`` labels to properties that genuinely contain the item title and
target URL. Accurate labels improve Microsoft Search and Microsoft 365 Copilot
behavior.

The connector schema is configured in Microsoft 365, not in Omnia. The
Retrievable, Queryable, Refinable, and Sortable options on an Omnia Enterprise
Property do not change the Microsoft connector schema.

4. Verify a known item and its ACL
----------------------------------

Run:

.. code-block:: text

   GET https://graph.microsoft.com/v1.0/external/connections/{connection-id}/items/{external-item-id}

Confirm that:

+ ``properties`` contains the expected schema property names and values.
+ ``content`` contains the text or HTML that should be indexed.
+ ``acl`` grants the authorized test user access, either directly or through an
  applicable group.

An ACL entry with ``accessType`` set to ``deny`` takes precedence over a
``grant`` entry.

5. Run a deterministic search as an authorized user
---------------------------------------------------

In Graph Explorer, sign in as a user who should be allowed to see the known
item. Consent to the delegated ``ExternalItem.Read.All`` permission, then run:

.. code-block:: json

   POST https://graph.microsoft.com/v1.0/search/query
   Content-Type: application/json

   {
     "requests": [
       {
         "entityTypes": [
           "externalItem"
         ],
         "contentSources": [
           "/external/connections/{connection-id}"
         ],
         "query": {
           "queryString": "{known-unique-phrase}"
         },
         "from": 0,
         "size": 25,
         "fields": [
           "{schema-title-property}",
           "{schema-url-property}",
           "{schema-extra-property}"
         ]
       }
     ]
   }

Use a unique phrase known to occur in the item and use actual connector schema
property names in ``fields``. Do not assume that every schema uses properties
named ``title``, ``url``, or ``status``.

A successful preflight returns ``200 OK`` and:

+ ``value[0].hitsContainers[0].total`` is greater than zero.
+ The expected hit has
  ``contentSource`` equal to ``/external/connections/{connection-id}``.
+ ``resource.properties`` contains the requested property values.

Also check the property names that Omnia will consume. Omnia's direct title and
path mapping requires a returned ``resource.properties.title`` and either
``resource.properties.url`` or ``resource.properties.webUrl``. If the connector
uses differently named schema properties for its title or URL, even when they
have the Microsoft ``title`` or ``url`` semantic label, plan an explicit
per-category template mapping in Omnia.

6. Verify security trimming
---------------------------

Repeat the same POST request while signed in as a user who is not authorized
for the known item. The known item must not be returned. When the unique phrase
matches only that item, the expected total is zero.

This test reflects the Omnia runtime context because Omnia also calls
``POST /v1.0/search/query`` as the current user.

7. Optionally verify the Microsoft 365 experience
-------------------------------------------------

You can also test the connection in a Microsoft 365 search experience. A custom
vertical for connector content requires both a vertical and a result type.
Configuration and index changes can take time to propagate, so this check is
useful but is less deterministic than the Graph request above.

Configure Omnia
***************

Activate the tenant feature
---------------------------

1. In Omnia Admin, open **Tenant > Features**.
2. Under **Integration**, expand **Microsoft Search connectors**.
3. Activate the feature and complete consent for the delegated Microsoft Graph
   permission ``ExternalItem.Read.All``.

The feature is tenant-scoped and requires the Tenant Administrator role. The
**External Item** search result source is shown in Search config only while this
feature is active.

Map extra template fields with Enterprise Properties
----------------------------------------------------

Standard external-item title and link values do not require an Enterprise
Property solely to populate Omnia's result model. Omnia maps the title from
``resource.properties.title`` and the path from
``resource.properties.url`` or ``resource.properties.webUrl`` when those
properties are present.

Create or edit Enterprise Properties for additional values required by the
selected Omnia search template:

1. Open **Tenant > Properties > Enterprise properties**.
2. Open or create the Enterprise Property used by the template.
3. Expand **Microsoft Searchable** and select **Microsoft Searchable**.
4. In **Managed Property**, enter the full response path:
   ``resource.properties.{schema-property}``.
5. If a separate **Retrievable Managed Property** is used, enter the same style
   of full path there.
6. Save the property and map the template field to this Enterprise Property in
   the search category.

For example, if the connector schema property is ``ticketState``, use:

.. code-block:: text

   resource.properties.ticketState

Use the exact property name and casing from the connector schema. Omnia
currently includes a configured field in the Graph ``fields`` request only
when its configured path contains ``resource``. It sends only the final segment
of the path, such as ``ticketState``, to Graph, and then reads the response by
traversing the original dotted path.

Omnia applies the Enterprise Property mappings as follows:

+ Field retrieval uses **Retrievable Managed Property**, or **Managed
  Property** when the retrievable value is empty.
+ Sorting uses **Sortable Managed Property**, or **Managed Property** when the
  sortable value is empty.
+ Refiners use **Refineable Managed Property**, or **Managed Property** when
  the refinable value is empty.
+ **Queryable Managed Property** is not automatically added to the search
  category query. Add any required property restriction explicitly to
  **Search Query**.

These settings tell Omnia which Graph property names and response paths to use.
They do not make a Microsoft connector schema property searchable, retrievable,
queryable, refinable, or sortable. Configure those capabilities separately in
Microsoft 365.

Create the search category
--------------------------

1. Open **Business profile > Search > Search config**.
2. Add a search category and enter a **Title**.
3. Set **Search providers** to **Microsoft Search**.
4. Set **Search result source** to **External Item**.
5. In **Content Sources**, enter one connection per line using exactly this
   format:

   .. code-block:: text

      /external/connections/{connection-id}
      /external/connections/{another-connection-id}

6. In **Search Query**, use ``*`` when no category-specific restriction is
   needed. To restrict the category, enter valid KQL that uses an actual
   queryable connector schema property, for example
   ``{schema-property}:{value}``.
7. Keep **Sort by** set to **Relevance** unless the connector schema and Omnia
   Enterprise Property mapping support the intended sort.
8. Select a compatible explicit **Search template** and map any extra template
   fields to their Enterprise Properties.
9. Save the category and test it as both an authorized and unauthorized user.

.. warning:: Omnia stores **Content Sources** as newline-delimited text, reads
   it one line at a time, and sends every line verbatim to Microsoft Graph. It
   does not trim, normalize, or validate the values. Do not add blank lines,
   leading spaces, or trailing spaces. Microsoft requires the full
   ``/external/connections/{connection-id}`` value, not only the connection ID.

Omnia combines **Search Query** with the user's search text using ``AND``. It
does not automatically use **Queryable Managed Property** to rewrite the
category query. **Enable partial word search** appends a wildcard to the user's
search text; enable it only when that behavior is wanted.

Current template limitation
***************************

In current affected versions, registration for the stock default search
template expects Microsoft Search values under ``resource.properties.*``, but
the DefaultSearchTemplate rendering logic checks ``Title`` and
``resource.fields.*``. This version-sensitive mismatch can produce an
icon-only or incomplete external-item card even when Graph returned the
correct values.

Until a product fix is available in your Omnia version, select a compatible
explicit template for the external-item category. The template should consume
the external item's direct title and path values, or use explicit per-category
template mappings backed by Enterprise Properties. Do not treat the current
stock-template mismatch as a permanent supported contract.

Troubleshooting
***************

Graph returns 200 but zero results
----------------------------------

+ Confirm that the connection state is ``ready`` and allow for schema and index
  propagation.
+ Use a known unique phrase and the exact
  ``/external/connections/{connection-id}`` content source.
+ Confirm that at least one searched property or the item content is indexed as
  searchable.
+ Check the known item's ACL for the signed-in user. Remember that deny
  overrides grant.

Expected fields are missing
---------------------------

+ Confirm that the fields use actual connector schema property names and are
  retrievable in the Microsoft schema.
+ Confirm that the item contains values for those properties.
+ In Omnia, use
  ``resource.properties.{schema-property}`` for the Enterprise Property
  Microsoft Search path.
+ Confirm that the selected template maps its extra fields to the intended
  Enterprise Properties.

Graph or Omnia returns 400
--------------------------

+ Remove blank or whitespace-padded lines from **Content Sources**.
+ Confirm that every source uses
  ``/external/connections/{connection-id}``.
+ Validate **Search Query** as KQL and use only properties configured as
  queryable in the Microsoft schema.
+ Check field, sort, and refiner names against the current connector schema.

Graph or Omnia returns 403
--------------------------

+ For the search query, confirm delegated ``ExternalItem.Read.All`` consent and
  sign in again to refresh the token if consent was just granted.
+ Confirm that the Omnia tenant feature is active and consent was completed.
+ For connection, schema, or item management GET requests, grant the appropriate
  connector management permission documented by Microsoft.

Graph succeeds but Omnia does not
---------------------------------

Confirm the Omnia tenant feature and delegated consent, the exact content source
lines, the category query, Enterprise Property paths, per-template mappings, and
the selected template. Test with the same signed-in user used for the successful
Graph request.

The decision boundary is:

+ If the deterministic Graph search fails, fix the Microsoft connector, schema,
  indexed item, permission, or ACL first.
+ If Graph succeeds for the same user and request values but Omnia fails,
  investigate the Omnia feature, consent, content source, query, mapping, and
  template configuration.

Microsoft documentation
***********************

+ `Search custom external item types with Microsoft Graph
  <https://learn.microsoft.com/en-us/graph/search-concept-custom-types>`_
+ `Manage the Microsoft 365 Copilot connector schema
  <https://learn.microsoft.com/en-us/graph/connecting-external-content-manage-schema>`_
+ `Manage external items, content, and ACLs
  <https://learn.microsoft.com/en-us/graph/connecting-external-content-manage-items>`_
+ `Microsoft Graph search query API
  <https://learn.microsoft.com/en-us/graph/api/search-query?view=graph-rest-1.0>`_
+ `Manage Microsoft Search verticals
  <https://learn.microsoft.com/en-us/microsoftsearch/manage-verticals>`_
+ `Manage Microsoft Search result types
  <https://learn.microsoft.com/en-us/microsoftsearch/manage-result-types>`_
