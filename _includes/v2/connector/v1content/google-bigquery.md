
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Install a new connector instance for each table to be accessed.

### Google OAuth2 Credentials 

1. Login to an existing account or create an new one on Google Developer Console
2. Go to https://console.developers.google.com/apis/credentials
3. Create an application:

   __Application Type:__ Web Application
   
   __Name:__ Application Name
   
   __URL:__ Cyclr service domain, e.g. https://app-h.cyclr.com/. Find this in the **Cyclr Partner Console** at **Settings** > **General Settings** > **Service Domain**
   
   __Redirect URL:__ Add a callback URL

   The URL is: https://app-h.cyclr.com/connector/callback

4. Note the `Client ID` and `Client Secret` to be used in the Cyclr Setup

### Google Big Query Settings

The Connector requires `Project ID`, `Table ID` and `Dataset ID`. 

#### Project ID

Go to [BigQuery console](https://console.cloud.google.com/bigquery), click the drop-down button to the right of the **Google Cloud Platform** button

![BigQuery - Project ID](./images/bigquery_project_id.png)

The `Project ID` is to the right of the project name.

#### Dataset ID

Select the project:

- Click on the drop down menu on the left side of the page to see datasets 
- Click on the dataset and find the ID in the "Dataset Info" area: the Dataset ID is the second part of the ID

![BigQuery - Dataset ID](./images/bigquery_dataset_id.png)

In this example `Project ID` is "round-bounty-259512" and dataset ID is "testDataset".

#### Table ID

Select **Table info** on the **Details** tab.

![BigQuery - Table ID](./images/bigquery_table_id.png)

In this example  `Table ID` is "testTable".

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Install a new connector instance for each table that you wish to access.
 
Click **Setup ** and then enter `Client ID`, `Client Secret`, `Project ID`, `Table ID` and `Dataset ID`.

The connector is now setup.

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

### Enable other users access to a Dataset

To allow other users access to the dataset and the tables, add the user permissions in the BigQuery console.

- Click the **Share dataset** button next to the **Create dataset** button on the dataset. These buttons are below the **Query Editor** screen.
- Enter the user's email. Choose which permissions to give the user, such as **Editorv or **Viewer**.
- Click **Add** 

See [IAM access.](https://cloud.google.com/bigquery/docs/access-control) for more information.

</div>

</section>