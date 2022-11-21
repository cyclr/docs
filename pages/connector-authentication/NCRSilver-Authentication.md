---
title: NCR Silver Authentication
sidebar: cyclr_sidebar
permalink: ncr-silver-connector
tags: [connector]
---

## NCR Silver setup

### Requirements

To connect with Cyclr, you need an **NCR Developer account**.

To set up an account, go to the [NCR website](https://developer.ncr.com/):

1.  Select the **Sign Up** button in the top right corner of the window.
2.  Enter your details, then continue and accept the developer agreement.
3.  Verify your email with the link sent to your account.

### Get authentication details

You need a **Shared Key** and **Secret Key** in order to access the connector.

To get these from your account, go to the [NCR website](https://developer.ncr.com/):
1.  Log in to your account.
2.  Select your email at the top right corner of the window and select dashboard.
3.  Select your application.
4.  Select the **+** icon next to **Access Keys**. 
5.  Make note of the **Shared Key** and **Secret Key**.

## Cyclr setup

To set up the NCR Silver connector in Cyclr, go to your console:

1. Go to **Connectors** > **Application Connector Library**.
2. Use the search box to find the NCR Silver connector.
3. Select the **Setup Required** icon.
4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Shared Key**   | The equivalent of an OAuth client ID.                               |
   | **Secret Key**   | The equivalent of an OAuth client secret key.                               |

7. Select **Save**.

## Additional information

### Documentation

For more information, see the [NCR API library documentation](https://developer.ncr.com/portals/dev-portal/api-explorer).
