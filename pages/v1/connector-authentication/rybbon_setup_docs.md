---
title: Rybbon Connector Guide
sidebar: cyclr_sidebar
permalink: rybbon-connector
tags: [connector]
---

## Connector Setup

### Obtaining Authentication Credentials

If you haven't done so already you will need to generate an API Key in the Rybbon portal:

1. Go to https://<span>{yourAccount}.rybbon</span>.net/ui/settings/api

2. From the API ACCESS KEYS section click **Edit**

   ![api key dashboard](./images/rybbon_api_key_dashboard.png)

3. On the next page click **Generate New API Key**

4. You will be prompted to give the key a name. This will be the Username entered at connector setup

5. Once created, you can view the API Key by clicking the eye icon to the right of the screen. This API Key will be the Password entered at connector setup

   ![api key](./images/rybbon_api_key.png)

### Authenticate The Connector

1. Locate the Rybbon connector

   > Cyclr Console > Connectors > Connector Library > Rybbon

2. From the Edit Connector interface click Setup

3. Select either Production or Sandbox for your Account Type, click Next

4. Enter your API Key's username as the Username

5. Enter your API Key as the Password, click Next

The connector is now authenticated and ready to use.
