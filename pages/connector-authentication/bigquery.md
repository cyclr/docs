---
title: Google BigQuery Authentication
sidebar: cyclr_sidebar
permalink: bigquery
tags: [connector]
---

## Google BigQuery ##

This document will explain what is needed to setup access to Google Big Query and install the connector.

You should install a new connector instance for each table that you wish to access.

### Setup Google OAuth2 Credentials ###

First setup OAuth2 within Google Developer Console. 

1. Sign up for a Google account; or log into an existing account.
2. Go to https://console.developers.google.com/apis/credentials
3. Create an application:

   __Application Type:__ Web Application
   
   __Name:__ Application Name
   
   __URL:__ Cyclr service domain, e.g. https://app-h.cyclr.com/. This can be found in the Cyclr Partner Console under Settings > Integration Settings > Service Domain.
   
   __Redirect URL:__ Add a callback URL.
   
   The URL is:
        https://app-h.cyclr.com/connector/callback

Now save the Client ID and Client Secret, these settings will be needed later.

### Google Big Query Settings ###

The Connector requires Project ID, Table ID and Dataset ID. These can be found by:

1. Navigate to [BigQuery console](https://console.cloud.google.com/bigquery), click the drop-down button to the right of the "Google Cloud Platform" button.

![BigQuery - Project ID](./images/bigquery_project_id.png)

To the right of the project name is the Project ID.

2. To find the Dataset ID, select the project. 
  * Click on the drop down menu on the left side of the page to see datasets. 
  * Click on the dataset and find the ID, this is in the "Dataset Info" area. The Dataset ID is only the second part of the ID.

![BigQuery - Dataset ID](./images/bigquery_dataset_id.png)

In the example above, the project ID is "round-bounty-259512" and dataset ID is "testDataset".

3. To find the Table ID select the "Table info" on the "Details" tab.

![BigQuery - Table ID](./images/bigquery_table_id.png)

In the example above table ID is "testTable".

### Connector Setup ###

You should install a new connector instance for each table that you wish to access.
 
Click "Setup" and then enter "Client ID", "Client Secret", "Project ID", "Table ID" and "Dataset ID".

The connector is now setup.

### Allowing Other Users Access To a Dataset ###

This section is for reference if another user is needed to access the dataset.

To allow other users access to the dataset and the tables, add the user permissions in the BigQuery console.

Click the "Share dataset" button next to the "Create dataset" button on the dataset, these buttons are below the "Query Editor" screen.

Enter in the email of the user. Choose which permissions to give the user, such as "Editor" or "Viewer".

Click "Add" 

For reference: [IAM access.](https://cloud.google.com/bigquery/docs/access-control)
