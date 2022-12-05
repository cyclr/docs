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

You need a **Shared Key** and **Secret Key** in order to access the connector. You also need an **NEP Organization** value.


To get these from your account, go to the [NCR website](https://developer.ncr.com/):
1.  Log in to your account.
2.  Select your email at the top right corner of the window and select dashboard.
3.  Select your application.
4.  Make note of the **NEP Organization** value under **Service User Name**. This is the value after `acct:` and before the `@` symbol.

    >  For example, if the **Service User Name** is `acct:test-drive-486bcc60-9426-4e46-bf9c-90l3e6e5883e@44423c74-6324-446b-97d2-e88538c3c926`, the **NEP Organization** you need is `test-drive-486bcc60-9426-4e46-bf9c-90l3e6e5883e`.

5.  Select the **+** icon next to **Access Keys**. 
6.  Make note of the **Shared Key** and **Secret Key**.

## Cyclr setup

To set up the NCR Silver connector in Cyclr, go to your console:

1. Go to **Connectors** > **Application Connector Library**.
2. Use the search box to find the NCR Silver connector.
3. Select the **Setup Required** icon.
4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Shared Key**      | The equivalent of an OAuth client ID.        |
   | **Secret Key**      | The equivalent of an OAuth client secret key.|
   | **NEP Organization**| The identifier for the organization.         |

7. Select **Save**.

> **Note**: To use different settings for different accounts, leave the value blank. This means Cyclr asks you to enter the value when you install the connector into an account.
## Additional information

### Documentation

For more information, see the [NCR API library documentation](https://developer.ncr.com/portals/dev-portal/api-explorer).
