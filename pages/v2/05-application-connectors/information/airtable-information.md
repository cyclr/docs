---
title: Airtable information
sidebar: cyclr_sidebar
permalink: airtable-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Airtable custom objects

The Airtable connector uses Cyclr custom objects to make methods dynamic based on module names. Each custom object name requires:

*   The BaseID of the table that you want to work with.
*   The table name of the table you want to interact with.

> **Note**: The BaseID and table name can be different for each client account.

### Set up a custom object

If you set up a custom object, you create a new method category with the parameters you enter. To set up a custom object:

1. Go to the Airtable connector **Settings** page:
    - For template connectors, go to **Templates** > **Template Connectors** > **Airtable** > **Edit Connector**.
    - For connectors within a cycle, go to the **Template Builder** > **Application Connectors** > **Airtable** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Records (Custom Object)** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Enter `{BaseID}.{table name}` into the **Specify object name** field. For example, `appTCumMdMOC1Zcqz.TestTable`.
5. Select **Copy**.


</section>
