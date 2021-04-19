---
title: Wix Authentication
sidebar: cyclr_sidebar
permalink: wix-connector
tags: [connector]
---

## Partner Setup

#### Retrieving public and private key
*   Navigate to the [development area](https://dev.wix.com/dc3/my-apps/) of Wix.
*   Create a new app if you have not already done so.
*   Click **OAuth** on the menu on the left side of the page.
*   Enter your Redirect URL (https://``Your Service Domain``/connector/callback ).
*   Note down your **App ID** and **App Secret Key**.
*   Navigate to the **Permissions** area on the menu on the left side of the page.
*   Add the appropriate permissions needed for the integration. At the moment the only permission needed is **Wix Stores** > **Read Orders**. More information can be found here: https://devforum.wix.com/en/article/available-permissions

### Cyclr Setup

Setup your Wix App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Wix**
*   Click the **Setup** button

Enter the following values:

**Client ID**: Retrieve from the above steps.

**Client Secret**: Also retrieved from the above steps.


Your Wix Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
