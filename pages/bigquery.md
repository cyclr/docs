---
title: Google BigQuery Authentication
sidebar: cyclr_sidebar
permalink: bigquery
tags: [connector]
---

## Partner Setup ##

You must first setup OAuth2 so that Cyclr can connect to your Google account. This can be done by following the [Google Connector guide.](https://docs.cyclr.com/google-connector)

Once you have authenticated your Google account with Cyclr by entering in your client ID and secret, you must now find out your project ID, table ID and dataset ID. 

To find your Project ID, navigate to your [BigQuery console.](https://console.cloud.google.com/bigquery) and click the drop-down button to the right of the "Google Cloud Platform" button.

![BigQuery - Project ID](./images/bigquery_project_id.png)

You will now be greeted with a screen that contains all of your projects. To the right of the project name, you will see a Project ID, which we will use to identify the project that you wish to work with.

To find the dataset ID, first make sure that you have selected the project that you are going to work with from the previous step. Find your project, which is located on the left side of the page, and drop down the menu. You can now see the hierarchy that BigQuery uses, and you will see your datasets that are contained in your project. Click on your dataset and find the ID, which is seen in the "Dataset Info" area. The dataset ID that we use is only the second part of the ID, we do not need the whole identification code.

![BigQuery - Dataset ID](./images/bigquery_dataset_id.png)

In the example above, our project ID is "round-bounty-259512" and dataset ID is "testDataset".

Finally, to find the table ID you can select the table that you wish to work with that will be visible from the previous step. The tables are inside the dataset hierarchy, and to obtain the ID of a table you must click on the table and read the "Table Info" in the "Details" tab in the same area we got the dataset ID from.

![BigQuery - Table ID](./images/bigquery_table_id.png)

In the example above you can see our table ID is "testTable", which is inside of our dataset.
 
Now that you have all of the required data, you can head to your Cyclr console, then to connectors, and then onto connector library which will contain Google BigQuery. Click "Setup" and then enter your "Client ID", "Client Secret", "Project ID", "Table ID" and "Dataset ID".

Your connector is now all setup and ready for your users.