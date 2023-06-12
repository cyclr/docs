---
title: Google BigQuery Authentication
sidebar: cyclr_sidebar
permalink: bigquery
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Google BigQuery setup

### Requirements

To connect with Cyclr, you need a Google Cloud Platform account.

### Get OAuth 2.0 credentials

To authenticate your connector, you need to create a web application inside your Google Cloud Platform account to get OAuth 2.0 credentials: 
   
1.  From the [Google Cloud Platform Credentials](https://console.cloud.google.com/apis/credentials) page, select **CREATE CREDENTIALS** > **OAuth client ID**. Create the app with the following settings:

| Setting                      | Value                                                        |
| :--------------------------- | :----------------------------------------------------------- |
| **Application type**         | `Web application`                                            |
| **Authorised redirect URIs** | `https://{{ServiceDomain}}/connector/callback`<br>Your service domain can be found in your Cyclr Console under **Settings** > **General Settings** > **Service Domain**. |

2.  Make note of the **Client ID** and **Client secret**.
   
For more information, see Google's guide on how to [create client credentials](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id).

### Get project ID

You need a project ID to use methods in the **Tables** method category. From the [Google Cloud Platform](https://console.cloud.google.com/) dashboard:

1. Select the project name from drop down button in the navigation bar.
![BigQuery project ID 1]((./images/google-bigquery-project-id-1.png)

2. T=Make a note of the project ID listed under the **ID** heading. In this example, the project ID of the `cyclr` project is `cyclr-389110`.
![BigQuery project ID 2]((./images/google-bigquery-project-id-2.png)

> **Note**: You can also find the project ID if you install the Google BigQuery connector without a project ID or dataset ID set, then use the **Utilities** > **Projects** > **List Projects** method. After you use this method, you need to re-authenticate the connector.

### Get dataset ID

You also need a dataset ID in order to use methods in the **Tables** method category. From the [Google BigQuery](https://console.cloud.google.com/bigquery) dashboard:

1. In the **Explorer** pane, select the arrow to the left of the project ID to expand it.
   
2. Select the arrow to the left of each dataset to view the tables within it and make a note of the dataset ID. In this example, the dataset ID that contains `table_1` is `dataset_1`.
![BigQuery dataset ID 1]((./images/google-bigquery-dataset-id-1.png)

>  **Note**: You can also find the dataset ID if you install the Google BigQuery connector without a project ID or dataset ID set, then use the **Utilities** > **Datasets** > **List Datasets** method. After you use this method, you need to re-authenticate the connector.

</section>
<section class="card">

## Cyclr setup

To set up the Google BigQuery connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Google BigQuery connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

| **Value**         | **Description**                                              |
| :---------------- | :----------------------------------------------------------- |
| **Client ID**     | The default client ID to use.                                |
| **Client Secret** | The default client secret to use.                            |
| **Scopes**        | The scopes you want to use. Cyclr uses the default scope of `https://www.googleapis.com/auth/bigquery` if you don't set this value. |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

### Account setup

Cyclr also asks for the below values when you install the Google BigQuery connector into a specific account:

| **Value**      | **Description**                                              |
| :------------- | :----------------------------------------------------------- |
| **Project ID** | The project ID of the project to use. This must be entered to use methods in the **Tables** method category. |
| **Dataset ID** | The dataset ID of the dataset to use.  This must be entered to use methods in the **Tables** method category. |

> **Note**: You can use different details for different accounts.

</section>
