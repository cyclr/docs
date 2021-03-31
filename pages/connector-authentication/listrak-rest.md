---
title: Listrak REST Authentication
sidebar: cyclr_sidebar
permalink: listrak-rest-connector
tags: [connector]
---

## Partner Setup

#### Retrieving client ID and secret
*   Login to your Listrak front-end, and navigate to the **Integrations Page** by clicking **Manage** -> **Integrations**.
*   Create a new integration. The integration type should be set to **Email**.
*   Set the scope as **Contact** and **List** if you want to use all the methods in the connector. 
*   Make a note of the client ID and secret.

### Cyclr Setup

Setup your Listrak REST App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Listrak REST**
*   Click the **Setup** button

Enter the following values:

**Client ID**: Retrieved from the above steps.

**Client Secret**: Retrieved from the above steps.


Your Listrak REST Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
