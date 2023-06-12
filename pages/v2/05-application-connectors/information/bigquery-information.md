---
title: Google BigQuery information
sidebar: cyclr_sidebar
permalink: bigquery-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
  
## Create a table custom object

To access each table within a project and dataset, you can create a custom object. If you create multiple custom objects, then you can have multiple tables under a single connector installation.

> **Warning**: You need to install the Google BigQuery connector with a [**Project ID** and **Dataset ID**](bigquery-connector) for table custom objects to function. 

You can create a table custom object from the Edit Connector page of the Google BigQuery connector:

1. Under the **Methods & Fields** heading, select the **Tables** methods category.
2. Select the pink **Copy this Category to create a Custom Category Object** icon.
3. Select the **Select object** dropdown.
4. Select the table you want to create a custom object for.
5. Select **Copy**.

This creates a new method category in which the methods now target the selected table.

</section>
<section class="card">

## Give dataset access to another user

You can give other users access to a dataset. For more information, see Google BigQuery's documentation on [IAM access control](https://cloud.google.com/bigquery/docs/access-control).

You can add access for another user from the [Google BigQuery console](https://console.cloud.google.com/bigquery):

1. Using the **Explorer** pane, navigate and select the dataset.
2. From the dataset navigation menu bar, select **Sharing** > **Permissions**.
3. Select **Add Principal**.
4. Under the **Add principals** heading, in the **New principals** field, enter users, groups, domains, or service accounts to give access to.
5. Under the **Assign roles** heading, select the **Select a role** dropdown box to assign roles.
6. Select **Save**.

</section>
<section class="card">

## Insert table data delay

When you insert table data, there may be a delay before you can access data in the table. This is because Google BigQuery needs to process and stream the data from their internal servers to the table before you can access it.

If the insert call doesn't return an error, the data appears in your table within 24 hours.

</section>
