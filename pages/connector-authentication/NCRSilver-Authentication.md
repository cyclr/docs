---
title: NCR Silver Authentication
sidebar: cyclr_sidebar
permalink: ncr-silver-connector
tags: [connector]
---

## NCR Silver setup

### Requirements

To connect with Cyclr, you need an **NCR Developer account**.

To get this account set up, follow the steps below:
1) Go to `https://developer.ncr.com/`.
2) Click the **Sign Up** button in the top right corner of the window.
3) Enter details, before continuing and accepting the developer agreement.
4) Verify email using the link sent to your account.

### Get authentication details

You will need a **Shared Key** and **Secret Key**, in order the access the connector.

To get these from your account, follow the steps below:
1) Go to `https://developer.ncr.com/`.
2) Log in to your account using the button in the top right corner of the window.
3) Now click your email at the top right corner of the window and select dashboard.
4) Select your application.
5) Click the `+` icon next to **Access Keys**. You have now generated your own **Shared Key** and **Secret Key**.

## Cyclr setup
Includes anything the partner needs to do in the Cyclr console and accounts in order to use the connector.

### Console setup

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

Documentation of the NCR API library can be found here: https://developer.ncr.com/portals/dev-portal/api-explorer