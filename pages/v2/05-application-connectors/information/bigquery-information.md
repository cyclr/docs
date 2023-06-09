---
title: Google BigQuery information
sidebar: cyclr_sidebar
permalink: bigquery-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
  
## Create table custom object

Each table within a project and dataset can be accessed by creating a custom object. Multiple tables can exist under a single connector installation by creating multiple custom objects. 

> **Warning**: You must install the Google BigQuery connector with a Project ID and Dataset ID entered for table custom objects to function. 

To create a table custom object, from the Edit Connector page of the Google BigQuery connector:

1. Under the **Methods & Fields** heading, select the **Tables** methods category.
2. Select the pink **Copy this Category to create a Custom Category Object** icon.
3. Select the **Select object** dropdown.
4. Select the table to create a custom object for.
5. Select **Copy**.

A new method category will be created in which the methods now target the selected table.

</section>

<section class="card">

## Give dataset access to another user

Other users can be given access to a dataset. See Google BigQuery's documentation on IAM access [here](https://cloud.google.com/bigquery/docs/access-control).

Add access for another user from the [Google BigQuery console](https://console.cloud.google.com/bigquery):

1. Using the **Explorer** pane, navigate and select the dataset.
2. From the dataset navigation menu bar, select **Sharing** > **Permissions**.
3. Select **Add Principal**.
4. Under the **Add principals** heading, in the **New principals** field, enter users, groups, domains, or service accounts to give access to.
5. Under the **Assign roles** heading, select the **Select a role** dropdown box to assign roles.
6. Select **Save**.

</section>

<section class="card">

## Insert table data delay

When you insert table data, there may be a delay before the data is accessible in the table. This is because Google BigQuery must process and stream the data from their internal servers to the table before is can be accessed.

If the insert call does not return an error the data will appear in your table within 24 hours.

</section>
