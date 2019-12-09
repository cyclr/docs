---
title: Google BigQuery Authentication
sidebar: cyclr_sidebar
permalink: bigquery
tags: [connector]
---

## Google BigQuery ##

### Setup OAuth2 ###

You must first setup OAuth2 so that Cyclr can connect to your Google account.

Here are the steps that you need to take.

1.  Sign up for a Google account; or log into your existing account if you already have one.
2. Go to https://console.developers.google.com/apis/credentials
3. Below are the details you should provide:

   Application Type: Web Application
   
   Name: Your Application Name
   
   URL: Your Cyclr service domain, e.g. https://app-h.cyclr.com/. This can be found in your Cyclr Console under Settings > Integration Settings > Service Domain.
   
   Redirect URL: you must add a callback URL to allow Google to be used in your Cyclr Console and its accounts.
   
   The URL is:
        https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback

You should now have your client ID and client secret.

### Get Project ID, Table ID and Dataset ID ###

You must now find out your project ID, table ID and dataset ID. 

1. Navigate to your [BigQuery console.](https://console.cloud.google.com/bigquery) and click the drop-down button to the right of the "Google Cloud Platform" button.

![BigQuery - Project ID](./images/bigquery_project_id.png)

To the right of the project name is the project ID.

2. To find the dataset ID, first make sure that you have selected the project that you are going to work with from the previous step. Click on the drop down menu on the left side of the page to see your datasets. Click on the dataset and find the ID, which is seen in the "Dataset Info" area. The dataset ID that is needed is only the second part of the ID.

![BigQuery - Dataset ID](./images/bigquery_dataset_id.png)

In the example above, our project ID is "round-bounty-259512" and dataset ID is "testDataset".

3. To find the table ID you can select the table from the previous step. You can see the ID in the "Table info" on the "Details" tab.

![BigQuery - Table ID](./images/bigquery_table_id.png)

In the example above you can see our table ID is "testTable", which is inside of our dataset.
 
4. Now that you have all of the required data, you can head to your Cyclr console, then to connectors, and then onto connector library which will contain Google BigQuery. Click "Setup" and then enter your "Client ID", "Client Secret", "Project ID", "Table ID" and "Dataset ID".

Your connector is now all setup and ready for your users.

## Allowing Other Users Access To Your Dataset ##

If you would like to allow other users access to operate on your dataset and the tables in said dataset, you can change the permissions of users from the BigQuery console.

To do this, simply click the "Share dataset" button next to the "Create dataset" button when you have the dataset that you would like to share selected. These buttons can be seen below the "Query Editor" screen.

Once you have selected share, you can enter in the email of the user that you would like to share the dataset with. To the right of the input box, you can choose which permissions you would like to give the user, such as "Editor" or "Viewer".

Once you have decided on the users permissions, simply click "Add" and the changes will be made.

To allow further access, you must allow the users [IAM access.](https://cloud.google.com/bigquery/docs/access-control)
