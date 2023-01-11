
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Login to your Marketo installation as an admin to get your `Client ID` and `Client Secret`.

- Go to **Admin > LaunchPoint** under the **Integration** menu.
- Click  **View Details** under the service that you want to use
- If no services are shown, create a new one
- Copy the `Client ID` and `Client Secret` from the prompt

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Marketo App within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Scroll down to **Marketo**
- Click the **Setup** button

Enter the following values:

**Client ID**: Enter the client ID that we retrieved from LaunchPoint.

**Client Secret**: Enter the client secret that we retrieved from LaunchPoint.

**API Subdomain**: The subdomain from your api instance endpoint. For example, "https://{{subdomain}}.mktorest.com".

Your Marketo Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### Bulk Import/Export

The ability to import and export CSV, TSV or SSV files is supported with methods from the **Bulk Imports** and **Bulk Exports** categories.

#### Import

To import data as a CSV or TSV file you will first need to add custom fields for the column headers that are to be created to the method **Create Import Job**.

For example, if the desired outcome for the import file was as follows:

![marketo csv raw](./images/marketo_import_3.png)

Your custom request fields should be created as:

![marketo import custom fields](./images/marketo_import_custom_fields.png)

**Note:** the [data]. prefix is required

The request fields are now configured and ready to be mapped.

#### Export

**Note:** The following example shows the process for an export of type **leads**. The process for activities is identical but with export type changed to **activities**.

![create export job configuration](./images/marketo_export_19.png)

To create a bulk export from Marketo we must create 2 cycles:

- **Cycle 1** will be used to Create the export job, add that job to the processing queue and then send the Export ID to the Cycle 2

- **Cycle 2** will start when it's first step, a webhook, receives the Export ID from Cycle 1. Cycle 2 will then check the status of the export job. If the status is **completed** we will continue down the true branch to retrieve the file content. If the status is not **completed** we will continue down the false branch, wait for a specified amount of time and then call the starting webhook again, thus repeating the process of Cycle 2

**Generic Webhook** and **Generic File** will both need to be installed from our Utility Connectors library.

More information on these connectors can be found [here](https://docs.cyclr.com/generic-webhook) and [here](https://docs.cyclr.com/generic-file).


Now lets look at the export process in more detail.

##### Cycle 1

![create export job configuration](./images/marketo_export_11.png)

1. Select the **Create Export Job** method that suits your requirements (Activities, Leads, New Activities or New Leads)

   ![create export job configuration](./images/marketo_export_1.png)

2. Define the fields the export file should include (eg. firstName, lastName, email).

   > Note: The method **List Lead Fields** from the **Leads** category will retrieve a list of all fields available for interaction via the REST API, with their correct formatting.

3. Optionally select the file format (if not selected this will default to CSV)

   ![create export job configuration](./images/marketo_export_2.png)

4. The response from this method will include the status and the Export ID for use in subsequent methods

   ![create export job configuration](./images/marketo_export_6.png)

5. Add the created export job to the processing queue with the method **Enqueue Export Job**. Select the Export Type (**leads** or **activities**) and enter the Export ID

   ![create export job configuration](./images/marketo_export_4.png)

6. The export job will now have a status of **Queued**

7. From the **Generic Webhook** > **HTTP Methods** drag **POST** onto the cycle builder

   ![create export job configuration](./images/marketo_export_9.png)

8. The **POST** (and **Webhook**) method needs to be configured. To do so, go into the **Generic Webhook**'s connector settings

   ![create export job configuration](./images/marketo_export_10.png)

9. Locate the **POST** method and add a custom request field. A guide to adding custom fields can be found [here](https://docs.cyclr.com/adding-custom-fields). The Field Location and Display Name can be whatever you want. In this case we've chosen **ExportId** as that is what will be assigned to the field

   ![create export job configuration](./images/marketo_export_13.png)

10. Locate the **Webhook** method and add an **identical** custom request field

    ![create export job configuration](./images/marketo_export_17.png)

11. You can now exit the connector's settings and navigate back to the cycle builder. In the **POST** step's **step setup** (cog icon) you can see we now have a field that we can map the Export ID to

    ![create export job configuration](./images/marketo_export_14.png)

12. As you can also see, a URL is required. The URL we are posting the Export ID to will be that of the webhook in Cycle 2

##### Cycle 2

![create export job configuration](./images/marketo_export_12.png)

1. Open the **step setup** for the webhook where you will find it's URL. Copy and paste this into the **POST** step's URL field in Cycle 1

   ![create export job configuration](./images/marketo_export_15.png)

   ![create export job configuration](./images/marketo_export_16.png)

2. Map the Export ID to **Get Export Job Status** and **Get Export File**. Those methods also require Export Type (**leads** or **activities**) to be set

3. Our **Decision** step (from **Logic Tools**), in this case renamed **Completed?** is checking for precisely that; If the status of the export job is **completed** we'll continue down the true branch, if not we'll continue down the false branch

   ![create export job configuration](./images/marketo_export_21.png)

   ![create export job configuration](./images/marketo_export_18.png)

4. The true branch will eventually lead to **Read Delimited Text File** from the **Generic File** connector. Make sure to configure this with the **Delimiter** matching that of the export file, **Has Headers** as **true** and **Content** mapped from the **Content** field of **Get Export File**

   ![create export job configuration](./images/marketo_export_20.png)

   > Once the data has been retrieved and converted to JSON by **Read Delimited Text File** it's contents can be mapped to subsequent steps. (eg. MailChimp etc.)

   ![create export job configuration](./images/marketo_export_24.png)

5. The false branch leads us to eventually repeat the process of Cycle 2. Firstly add a **Delay** step from **Logic Tools**. The value should be greater than 60 seconds

   ![create export job configuration](./images/marketo_export_22.png)

6. Then add another **POST** method. This should again be mapped the Export ID and the URL of the webhook at the beginning of Cycle 2

   ![create export job configuration](./images/marketo_export_23.png)

Now that both cycles are configured we can run them:

1. Run **Cycle 2** first. As you will see, nothing will happen at this point. The cycle is essentially on standby, ready to run when the webhook is triggered

2. Run **Cycle 1**. This will create an export job, add it to the processing queue and send the Export ID to the webhook of **Cycle 2**, thus starting that cycle

</div>

</section>
