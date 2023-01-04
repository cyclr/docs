---
title: Boulevard Authentication
sidebar: cyclr_sidebar
permalink: boulevard-connector
tags: [connector]
---

## Boulevard setup

To connect with Cyclr, you need an **API Key** for the Boulevard application. You can find the API Keys for Boulevard your existing apps on the **Manage Apps** page in the Boulevard developer portal, or you can create a new app on this page.

You also need the following authentication details from your Boulevard account:

*  **Business ID**
*  **API Secret**

For more information on how to obtain these details, contact your Boulevard account manager.

>  **Note**: To allow Boulevard to access your business's data, an admin needs to install the Boulevard application with the **Application ID** shown on the **Manage Apps** page.


## Cyclr setup

To set up the Boulevard connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Boulevard connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Business ID** | The Boulevard account Business ID. |
   | **API Secret** | The Boulevard account API secret. |
   | **Base URL** | A dropdown box to select either the Boulevard production URL or the sandbox URL. |
   | **API Key** | The Boulevard app's API Key. |
   
5. Select **Save Changes**.

> **Note**: To use different settings for different accounts, leave the value blank. This means Cyclr asks for the value when you install the connector into an account.



