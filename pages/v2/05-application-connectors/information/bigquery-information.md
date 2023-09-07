---
title: Google BigQuery information
sidebar: cyclr_sidebar
permalink: bigquery-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Create a Table Custom Object Category

You can create a Custom Object Category to access each table within a project and dataset as it's own method category. Create multiple Custom Object Categories to access multiple tables under a single connector installation.

> **Warning**: You need to install the Google BigQuery connector with a [**Project ID** and **Dataset ID**](bigquery-connector) for table custom objects to function. 

To create a table Custom Object, from the **Edit Connector** page of the Google BigQuery connector:

1. Under the **Methods & Fields** heading, select the **Tables** methods category.
2. Select the pink **Copy this Category to create a Custom Category Object** icon.
3. Select the **Select object** dropdown.
4. Select the table you want to create a Custom Object Category for.
5. Select **Copy**.

The methods within the new method category you created now target the selected table.

</section>
<section class="card">

## Create a Cycle to request a large set of data

Use the **List New Table Data Incrementally** or **List Partial Table Data** method to incrementally list data in a Cycle. You can use **Generic Webhook Connector** methods to allow the cycle to send a request to itself to continually run. This approach is useful for very large sets of data.

When you use the **List Partial Table Data** method, you need to track the last index of the table data returned in the current request and send it in the next request. To do this, [add request fields for the Generic Webhook Connector](#add-request-fields-for-the-generic-webhook-connector) then [map the last index of the table data returned](#map-the-last-index-of-the-table-data-returned) as additional steps.

### Prerequisites

#### Install the Google BigQuery Connector

Install the Google BigQuery connector using the [Google BigQuery Authentication Guide](bigquery-connector).

#### Create a Tables Custom Object Category

[Create a Tables Custom Object](#create-a-table-custom-object-category) that targets the required table.

#### Install the Generic Webhook Connector

1. To install the Generic Webhook Connector, navigate to the **Utility Connectors** page:
   * From the console, select **Templates > Template Connectors > + Install New Utility**.
   * From an account, select **Connectors > + Install New Utility**.
3. Select **Install** under the **Generic Webhook** Connector.
4. Update the **Name** field to a recognisable name.
5. Select **Next**.

#### Add request fields for the Generic Webhook Connector

> **Note**: You only need to do this step for the **List Partial Table Data** method.

To allow the next request to use the last index of the table data returned in the current request, you must add request fields to the Generic Webhook connector that track the index:

Navigate to the **Edit Connector** page for the Generic Webhook Connector:
 * From the console, select **Templates > Template Connectors**. Under the **Installed Utility Connectors** heading, select the **Edit Connector** icon next to the the **Generic Webhook Connector**. This will have the name entered in [Install the Generic Webhook Connector](#install-the-generic-webhook-connector).
 * From an account, select **Connectors**. Under the **Installed Utility Connectors** heading, select the **Edit Connector** icon next to the the **Generic Webhook Connector**. This will have the name entered in [Install the Generic Webhook Connector](#install-the-generic-webhook-connector).

##### Add a request field to the POST method

1. Under the **Methods and Fields** heading, select **HTTP Methods**.
2. Select **POST**.
3. Under the **Request Fields** heading, select the **Add Field** icon.
4. Set the **Field Location** to `lastIndex`.
5. Set the **Display Name** to `Last Index`.
6. Set the **Data Type** to `Integer`.
7. Select **Create**.

##### Add a request field to the Webhook method

1. Under the **Methods and Fields** heading, select **Webhooks**.
2. Select **Webhook**.
3. Under the **Request Fields** heading, select the **Add Field** icon.
4. Set the **Field Location** to `lastIndex`.
5. Set the **Display Name** to `Last Index`.
6. Set the **Data Type** to `Integer`.
7. Select **Create**.

### Create a Cycle

From the console:
  1. Select **Templates > Template Library**.
  2. Select **Create New Template**.
  3. Enter a template name.
  4. Select **Create**.

From an account:
  1. Select **Cycles**.
  2. Select **Design New Cycle**.
  3. Enter a Cycle name.
  4. Select **Create**.

#### Add methods to the Cycle

Add following methods to the Cycle:

* **Generic Webhook** > **HTTP Methods > POST**
* **Generic Webhook** > **Webhooks** > **Webhook**
* **Google BigQuery** > **Tables** > **List New Table Data Incrementally** or **List Partial Table Data**
* **Tools** > **Delay**: You can use the **Delay** tool to set the time between requests once all current table data has been retrieved.

#### Connect the methods

Connect the methods as follows:

![Google BigQuery Cycle 1](./images/google-bigquery-cycle-1.png)

> **Note**: In this example, add any additional Cycle methods between the true exit of the **List Partial Table Data** method and the **POST** method.

### Configure a Cycle

#### Setup the POST to webhook loop

The POST method must target the Webhook method to allow the Cycle to send a request to itself to continually run:

1. Select the **Step setup** of the **Webhook** method.
2. Copy the webhook URL and close the window.
3. Select the Step setup of the **POST** method.
4. Select **Select...** next to the **URL** field.
5. Select **Type a Value**.
6. Enter the webhook URL into the text box and close the window.

#### Map the last index of the table data returned

> **Note**: This step is only required for the **List Partial Table Data** method.

1. Select the **Step setup** of the **List Partial Table Data** method.
2. Select **Ignore** next to the **Start Index** field.
3. Select **Webhook**.
4. Select **Nothing Selected**.
5. Select **Last Index**. This is the field added in the [add a request field to the Webhook method](#add-a-request-field-to-the-webhook-method) step.
6. Close the window.
7. Select the **Step setup** icon of the **POST** method.
8. Select **Ignore** next to the **Last Index** field. This is the field added in the [add a request field to the POST method](#add-a-request-field-to-the-post-method) step.
9. Select the **List Partial Table Data** method.
10. Select **Nothing Selected**.
11. Select **Last Row Index**.
12. Close the window.

#### Configure the Rows Per Execution setting

The rows per execution setting determines how many table rows are returned per Cycle execution. You need to manually set the rows per execution, which is dependant on the width of your table data. For example, a starting point of `10000` might be useful.

1. Select the **Step setup** of the **List Partial Table Data** or **List New Table Data Incrementally** methods.
2. Select **Ignore** next to the **Rows Per Execution** field.
3. Select **Type a Value**.
4. Enter the enter the rows per execution into the text box.
5. Close the window.

#### Configure the delay time

Use the delay step to set the time between cycle executions once the cycle retrieves all of the table data. When new table data is found, the cycle continues to run until it retrieves all table data and then reverts back to the delay.

For example, a delay duration of 12 hours makes the Cycle check for new table data once every 12 hours once it retrieves all of the table data.

1. Select the **Step setup** of the **Delay** method.
2. Set the duration and close the window.

</section>
<section class="card">


## Give dataset access to another user

You can give other users access to a dataset. For more information, see Google BigQuery's documentation on [IAM access control](https://cloud.google.com/bigquery/docs/access-control).

Add access for another user from the [Google BigQuery console](https://console.cloud.google.com/bigquery):

1. From the **Explorer** pane, navigate and select the dataset.
2. From the dataset navigation menu bar, select **Sharing** > **Permissions**.
3. Select **Add Principal**.
4. Under the **Add principals** heading, in the **New principals** field, enter users, groups, domains, or service accounts to give access to.
5. Under the **Assign roles** heading, select the **Select a role** dropdown box to assign roles.
6. Select **Save**.

</section>
<section class="card">

## Insert table data delay

Because Google BigQuery needs to process and stream the data from their internal servers to the table before you can access it, there might be a delay when you insert table data, before you can access the data.

If the insert call doesn't return an error, the data appears in your table within 24 hours.

</section>
