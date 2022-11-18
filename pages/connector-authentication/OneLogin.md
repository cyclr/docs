---
title: OneLogin Authentication
sidebar: cyclr_sidebar
permalink: onelogin-connector
tags: [connector]

---

## OneLogin setup
To authenticate this connector you will need a credential pair for OneLogin of `Client ID` and `Client Secret`. More information on how to obtain these credentials can be found in OneLogin's [Working with API credentials](https://developers.onelogin.com/api-docs/1/getting-started/working-with-api-credentials) documentation.

## Cyclr setup

To set up the OneLogin connector in Cyclr:

1. Go to your **Cyclr Console**.

2. Select **Connectors** > **Application Connector Library** at the top of the page.

3. Use the search box to find the **OneLogin** connector.

4. Select the **Setup Required** icon.

5. Enter the your `Client ID` and `Client Secret`. 

6. Enter your OneLogin **sub domain**. This can be found in your OneLogin frontend URL just before `.onelogin.com`. For example if your frontend URL is `https://testing-dev.onelogin.com/portal`, your **sub domain** would be `testing-dev`.

6. Select **Save Changes**.
