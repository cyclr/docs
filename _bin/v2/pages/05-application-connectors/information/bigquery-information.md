---
title: Google BigQuery Information
sidebar: cyclr_sidebar
permalink: bigquery
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

### Allowing Other Users Access To a Dataset

This section is for reference if another user is needed to access the dataset.

To allow other users access to the dataset and the tables, add the user permissions in the BigQuery console.

Click the "Share dataset" button next to the "Create dataset" button on the dataset, these buttons are below the "Query Editor" screen.

Enter in the email of the user. Choose which permissions to give the user, such as "Editor" or "Viewer".

Click "Add" 

For reference: [IAM access.](https://cloud.google.com/bigquery/docs/access-control)

### Inserting Table Data

When inserting table data, you will need to wait for it to populate in Google Big Query as they process and stream the data from their internal servers to the table instead of populating directly. As long as the call hasn't returned an error, you will see the data in your table in the next 24 hours.

</section>
