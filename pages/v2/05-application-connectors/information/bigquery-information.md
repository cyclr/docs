---
title: Google BigQuery information
sidebar: cyclr_sidebar
permalink: bigquery-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Allow other users access to a dataset

To allow other users access to the dataset and the tables, you can add the user permissions in the BigQuery console:

1. Below the "Query Editor" screen, select the **Share dataset** button on the dataset.
2. Enter the email of the user. 
3. Select the permissions you want to give to the user, for example, **Editor** or **Viewer**.
4. Select **Add**. 

For reference, see the Bigquery documentation on [IAM access.](https://cloud.google.com/bigquery/docs/access-control)

</section>
<section class="card">

## Insert Table Data

When you insert table data, you need to wait for it to populate in Google Big Query as they process and stream the data from their internal servers to the table instead of populating directly. If the call doesn't return an error, the data appears in your table within 24 hours.

</section>
