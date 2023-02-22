---
title: UtilizeCore Authentication
sidebar: cyclr_sidebar
permalink: utilizecore-connector
tags: [connector]
---

## UtilizeCore Setup

### Requirements

To connect with Verint, you will need a **Client ID**, **Client Secret**, **Username** and **Password**.
The **Domain** of the instance you would like to access has selectable values, with the option of custom domain entry.
If the link you would like to access is: https://msnw.staging.utilizecore.com/api/v2/vendors
The **Domain** would be "msnw.staging.utilizecore.com".

## Cyclr setup
This section describes how to setup the connector in the console. No other setup is required.

### Console setup

To set up the Verint connector in Cyclr, go to your console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the UtilizeCore connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Client ID** | The Client ID, authorized to access the desired application. |
   | **Client Secret**     | The Client Secret, authorized to access the desired application. |
   | **Username** | The Username of the authorized user.              |
   | **Password** | The Password of the authorized user. |
   | **Domain** (Optional) | The domain and subdomain of the request, used to target the correct resource. |

7. Select **Save**.

## Additional information
### Documentation

The API reference documentation can be found here:
https://app.swaggerhub.com/apis-docs/utilizecore/utilizecore-mobile/2.0.0#/