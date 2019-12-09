---
title: Google Data Studio
sidebar: cyclr_sidebar
permalink: google-data-studio-connector
tags: [connector]
---

## Google Data Studio

Google Data Studio is designed to turn your data into interactive dashboards and informative reports.

Using the Cyclr API, you can consume data from any Cyclr connectors you have installed and display them in Data Studio.

Let's take a look at how to set up Cyclr in Data Studio. In this example, we will create a KPI report for a [Sentori](http://sentoriapp.com/) campaign.

### Apps Script Setup

The first step is to set up Google Apps Script. Apps Script defines how your users authenticate the requests and pull data from connectors they installed in Cyclr. We have written an Apps Script project to help you bootstrap this. Contact our support to get the latest code.

Once you have the code, create a new project in [G Suite Developer Hub](https://script.google.com/home) and copy the code into the project.

![](../images/google-data-studio/apps-script.png)

From the project you created, open Publish -> Deploy from manifest... and select the deployment link which will take you to the Data Studio setup.

![](../images/google-data-studio/apps-script-deployment.png)

### Data Source Configuration

To get data from the Cyclr connectors you have installed, Cyclr needs to know which account they are in and which connector method to call.

![](../images/google-data-studio/data-sources.png)

Here are the parameters for setting up the Cyclr Data Source:

- Cyclr Domain: Choose the Cyclr domain you are using
- Client ID: Find your client ID in the Console -> Settings -> OAuth Client Credentials
- Account ID: Find the account ID in the Cyclr Console or by making a *List Accounts* API call to Cyclr
- Username: Username for the user who has access to the account. You can create users and add them to a specified account in the Cyclr Console or by calling the Cyclr API
- Password: Password for the user who has access to the account. You can set up a password using the Cyclr API
- Account Connector: Select the connector you would like to get data from. Make sure the connector you selected is authenticated in Cyclr
- Method: Select the method to call
- Additional Parameters: Depending on the method you selected, you may need to set up additional parameters e.g. Email Campaign ID

### Data Source Fields

The Apps Script will automatically populate method response fields. You can change the data types or create new aggregation fields here.

![](../images/google-data-studio/data-sources-fields.png)

Now you can open the Explorer and generate a report using the response fields. The line chart here shows the number of first clicks ordered by date:

![](../images/google-data-studio/explorer.png)

### Apps Script Customisation

The sample code we've provided is partner agnostic. You can customise the script to better fit you use cases.

- Include the Cyclr domain and client ID in the code so your users don't need to set them up when creating the Data Source.
- Embed the deployment link in your application.
- Rename the Username and Password parameters to e.g. Access ID and Access Secret, and display their values in your application. Before users open the Data Studio link from your application, they already know what values they should provide in the Data Source setup.