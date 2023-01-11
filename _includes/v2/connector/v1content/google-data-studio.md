
<section class="setup partner" markdown="1">

## Google Setup

<div class="section-content" markdown="1">

Google Data Studio turns your data into interactive dashboards and informative reports.

Using the Cyclr API, you can consume data from any Cyclr connectors you have installed and display them in Data Studio.

This demo shows how to set up Cyclr in Data Studio, creating a KPI report for a [Sentori](http://sentoriapp.com/) campaign.

### Apps Script Setup

Set up Google Apps Script. Apps Script defines how your users authenticate the requests and pull data from connectors installed in Cyclr. 

Cyclr has created an Apps Script project to help you bootstrap this. Contact Cyclr support to get the latest code.

Once you have the code, create a new project in [G Suite Developer Hub](https://script.google.com/home) and copy the code into the project.

![](../images/google-data-studio/apps-script.png)

In the project you created:

- Open **Publish** > **Deploy from manifest...** 
- Click the deployment link to go to the  Data Studio setup.

![](../images/google-data-studio/apps-script-deployment.png)

### Data Source Configuration

To get data from the Cyclr connectors you have installed, Cyclr needs to know which account they are in and which connector method to call.

![](../images/google-data-studio/data-sources.png)

Here are the parameters required to set up Cyclr Data Source:

- `Cyclr Domain`: Choose the Cyclr domain you are using
- `Client ID`: Find your `Client ID` in  **Console** > **Settings** > **OAuth Client Credentials**
- `Client Secret`: Find your `Client Secret` in  **Console** > **Settings** > **OAuth Client Credentials** and view the secret to copy
- `Account ID`: Find the account ID in the Cyclr Console or make a *List Accounts* API call to Cyclr
- Account Connector: Select the connector you would like to get data from. Tthe connector must be authenticated in Cyclr
- Method: Select the method to call
- Additional Parameters: additional parameters may be required, depending on the selected method   e.g. Email Campaign ID

### Data Source Fields

The Apps Script automatically populates method response fields. You can change the data types or create new aggregation fields here.

![](../images/google-data-studio/data-sources-fields.png)

Open the Explorer and generate a report using the response fields. The line chart here shows the number of first clicks ordered by date:

![](../images/google-data-studio/explorer.png)

### Apps Script Customisation

The sample code provided is partner agnostic. Customise the script to better fit your use cases.

- Include the Cyclr domain and `Client ID` in the code so your users don't need to set them up when creating the Data Source
- Embed the deployment link in your application
- Rename the Username and Password parameters e.g. Access ID and Access Secret, and display their values in your application. Before users open the Data Studio link from your application, they already know what values they should provide in the Data Source setup
