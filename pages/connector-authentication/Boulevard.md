---
title: Boulevard Authentication
sidebar: cyclr_sidebar
permalink: boulevard-connector
tags: [connector]
---

## Partner Setup

#### Create App
* Go to **Manage Apps** on the dev-portal
* Click on **Create New App**
* Enter the required information and save.

#### App Installation
* To gain access to a businesses data an admin at the business must install your application. 
* The first step to enabling this is to provide your **Application ID** to the business admin. 
* The **Application ID** can be found on the **Manage Apps** section of the **Dev Portal**. Your business admin can then follow the steps below to install the application.
* At the bottom of the page, in the **Custom Apps** section click on the **Install** button. This will open the **App installation** dialog.
* After entering the provided **Application ID** (that can be found on the **Manage Apps** page on the **dev-portal**) and clicking on **Install**, you will be presented with a confirmation dialog that will display additional information about the Application.
* Click **Confirm** to install the application and it will be listed in your **Custom Apps** section of the page.

### Cyclr Setup

Setup your Boulevard App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Boulevard**
*   Click the **Setup** button

Enter the following values:
(Use API Key as the username and leave the password blank (or you can put any value as password if your HTTP client requires it)).

**Business ID**: **Business ID** provided by Boulevard when account created.
**API Secret**: **API Secret** provided by Boulevard when account created.
**API Version**: Enter API Key retrieved from Partner Setup.
**Base URL**: Production URL: https://dashboard.boulevard.io/api/2020-01/admin, or Sandbox URL: https://sandbox.joinblvd.com/api/2020-01/admin.
**API Key**: Enter API Key retrieved from Partner Setup, or go to **Manage Apps** section of the **Dev Portal**.




Your Boulevard Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
