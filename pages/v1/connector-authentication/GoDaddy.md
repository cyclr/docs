---
title: GoDaddy Authentication
sidebar: cyclr_sidebar
permalink: godaddy-connector
tags: [connector]
---

## Partner Setup

#### Retrieving API Key and Secret
* Login to your GoDaddy Developer Portal. 
* Click the API Keys tab at the top of the page.
* Click **Create New API Key**, if not key is shown underneath.

The first API Key that you create will be a test key and should be used for your development against our OTE environment which is hosted at https://api.ote-godaddy.com. Integrate first with the OTE environment to verify that you are calling the API properly before going live with calls to the Production environment.

When you are ready for production, create a new API Key and Secret to call our production environment which is hosted at https://api.godaddy.com.

### Cyclr Setup

Setup your Go Daddy connector within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **GoDaddy**
*   Click the **Setup** button

Enter the following values:

**Server Name**: One of these, OTE server: https://api.ote-godaddy.com, production: https://api.godaddy.com..

**API Key**: Retrieved from the Partner Setup steps.


Your GoDaddy Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
