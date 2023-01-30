---
title: Marketo information
sidebar: cyclr_sidebar
permalink: marketo-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Bulk Import/Export

You can import and export CSV, TSV or SSV files  with methods from the **Bulk Imports** and **Bulk Exports** categories.

## Import

To import data as a CSV or TSV file, you need to add custom fields for each column headers that you want to create to the method **Create Import Job**.

For example, if the desired outcome for the import file is as follows:

![marketo csv raw](./images/marketo_import_3.png)

Your custom request fields should be created as:

![marketo import custom fields](./images/marketo_import_custom_fields.png)

> **Note: the [data]. prefix is required**

Once the you configure your fields, you can map them.

## Export

The following example shows the process for an export of type **leads**. The process for activities is identical but with export type changed to **activities**.

For this process, you need to install both the [Generic Webhook](https://docs.cyclr.com/generic-webhook) and [Generic File](https://docs.cyclr.com/generic-file) connectors from the **Utility Connectors** library.
![create export job configuration](./images/marketo_export_19.png)

To create a bulk export from Marketo, you need to create two cycles:

1. Create **Cycle 1** to create the export job, add that job to the processing queue, and send the Export ID to **Cycle 2**
2. Create **Cycle 2** with the first step as a webhook step so the cycle starts when it receives the Export ID from **Cycle 1**. Configure **Cycle 2** to check the status of the export job, so if the status is `completed`, the cycle continues down the `true` branch to retrieve the file content. If the status isn't `completed`, the cycle continues down the `false` branch, waits for a specified amount of time, and then calls the starting webhook again to repeat the process of Cycle 2.

Follow the steps below for more detailed information on how to create the export cycles.

### Set up Cycle 1

![create export job configuration](./images/marketo_export_11.png)

1. Select the **Create Export Job** method that you want to use, such as **Activities**, **Leads**, **New Activities**, or **New Leads**.

   ![create export job configuration](./images/marketo_export_1.png)

2. Define the fields you want the export file to include, such as `firstName`, `lastName`, or `email`.

   > **Note**: The method **List Lead Fields** from the **Leads** category retrieves a list of all fields available for interaction via the REST API, with their correct formatting.

3. Either select a file format, or leave the file format to default to CSV.

   ![create export job configuration](./images/marketo_export_2.png)

   > **Note**: The response from this method includes the status and the Export ID for use in subsequent methods

      ![create export job configuration](./images/marketo_export_6.png)

4. Add the export job you created to the processing queue with the method **Enqueue Export Job**, select the **Export Type** (`leads` or `activities`), and enter the Export ID. This changes the export job status to `Queued`.

   ![create export job configuration](./images/marketo_export_4.png)

5. From the **Generic Webhook** > **HTTP Methods**, drag **POST** onto the cycle builder.

   ![create export job configuration](./images/marketo_export_9.png)

6. The **POST** (and **Webhook**) method needs to be configured. To do so, go into the **Generic Webhook**'s connector settings

   ![create export job configuration](./images/marketo_export_10.png)

7. Locate the **POST** method and add a [custom request field](https://docs.cyclr.com/adding-custom-fields), and set the **Field Location** and **Display Name**.  This example uses `ExportId` as the Export ID is assigned to the field.

   ![create export job configuration](./images/marketo_export_13.png)

8. Locate the **Webhook** method and add an identical custom request field.

    ![create export job configuration](./images/marketo_export_17.png)

In the cycle builder, select **step setup** on the **POST** step to see the field that you can map the custom request field to:

    ![create export job configuration](./images/marketo_export_14.png)

You also need a URL. The URL you can post the custom request field to is the URL of the webhook in Cycle 2.

### Set up Cycle 2

![create export job configuration](./images/marketo_export_12.png)

1. Open the **step setup** for the webhook step to find the URL, and copy the URL into the **POST** step's **URL** field in Cycle 1

   ![create export job configuration](./images/marketo_export_15.png)

   ![create export job configuration](./images/marketo_export_16.png)

2. Map the custom request field to **Get Export Job Status** and **Get Export File**. You need to set the **Export Type** (`leads` or `activities`) for these methods.

3. Use the **Decision** step, named **Completed?** in this example, to chedck the status of the export job. If the status is `completed`, the cycle continues down the `true` branch, and if it's not complete, the cycle continues down the `false` branch.

   ![create export job configuration](./images/marketo_export_21.png)

   ![create export job configuration](./images/marketo_export_18.png)

4. To make the `true` branch lead to **Read Delimited Text File** from the **Generic File** connector, configure **Read Delimited Text File** so the **Delimiter** matches that of the export file. Set **Has Headers** to `true` and map **Content** from the **Content** field of **Get Export File**.

   ![create export job configuration](./images/marketo_export_20.png)

   > Once the data has been retrieved and converted to JSON by **Read Delimited Text File** it's contents can be mapped to subsequent steps. (eg. MailChimp etc.)

   ![create export job configuration](./images/marketo_export_24.png)

5. To make the `false` branch repeat **Cycle 2**, add a **Delay** step from **Logic Tools**. The value should be greater than 60 seconds

   ![create export job configuration](./images/marketo_export_22.png)

6. Add another **POST** method and map it to the custom request field and the URL of the webhook at the beginning of **Cycle 2**.

   ![create export job configuration](./images/marketo_export_23.png)

### Run the cycles

Now that both cycles are configured we can run them:

1. Run **Cycle 2** first. Nothing happens because the cycle is on standby, ready to run when the webhook is triggered.
2. Run **Cycle 1**. This creates an export job, adds it to the processing queue, and sends the custom request field to the webhook of **Cycle 2**, to start the cycle.

</section>
