---
title: Boulevard Authentication
sidebar: cyclr_sidebar
permalink: boulevard-connector
tags: [connector]
---

## Boulevard setup

To connect with Cyclr, you need a Boulevard app that is installed by a business and the following authentication values:

*  Business ID
*  API Secret
*  API Version
*  Base URL
*  API Key

To obtain these values, go to the **Manage Apps** page in the Boulevard developer portal. For more information, contact your Boulevard account manager.

>  **Note**: To gain access to a business's data, an admin at the business needs to install your application. To allow them to do this, you need to provide them with your **Application ID**. You can see your application ID on the **Manage Apps** page in the Boulevard developer portal.


1.  Provide your **Application ID** to the business admin. 
* The **Application ID** can be found on the **Manage Apps** section of the **Dev Portal**. Your business admin can then follow the steps below to install the application.
* At the bottom of the page, in the **Custom Apps** section click on the **Install** button. This will open the **App installation** dialog.
* After entering the provided **Application ID** (that can be found on the **Manage Apps** page on the **dev-portal**) and clicking on **Install**, you will be presented with a confirmation dialog that will display additional information about the Application.
* Click **Confirm** to install the application and it will be listed in your **Custom Apps** section of the page.

## Cyclr setup

To set up the Boulevard connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Boulevard connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Username**   | The Boulevard API Key                            |
   | **Password**   | You can leave this blank, or enter a value if your HTTP client requires it.                              |
   | **Business ID** | The Boulevard business ID. |
   | **API Secret** | The Boulevard account API secret. |
   | **API Version** | The Boulevard API Key. |
   | **Base URL** | Either the Boulevard production URL or the sandbox URL. |
   | **API Key** | The Boulevard API Key. |
   
5. Select **Save Changes**.

> **Note**: To use different settings for different accounts, leave the value blank. This means Cyclr asks for the value when you install the connector into an account.


Enter the following values:
(Use API Key as the username and leave the password blank (or you can put any value as password if your HTTP client requires it)).

**Business ID**: **Business ID** provided by Boulevard when account created.
**API Secret**: **API Secret** provided by Boulevard when account created.
**API Version**: Enter API Key retrieved from Partner Setup.
**Base URL**: Production URL: https://dashboard.boulevard.io/api/2020-01/admin, or Sandbox URL: https://sandbox.joinblvd.com/api/2020-01/admin.
**API Key**: Enter API Key retrieved from Partner Setup, or go to **Manage Apps** section of the **Dev Portal**.



