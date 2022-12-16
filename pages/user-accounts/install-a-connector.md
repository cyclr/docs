---
title: Install account connectors (API)
sidebar: cyclr_sidebar
permalink: install-a-connector
tags: [accounts]
---

You can install a connector into an account through the Cyclr API.

For each call, replace `{YourCyclrDomain}` with your Cyclr api domain. You also need to include the following values in the header parameters:

| **Parameter**   | **Description**                                                      |
|-----------------|----------------------------------------------------------------------|
| `Authorization`   | Your Cyclr access token. Use the format: `Bearer {access_token}`.      |
| `X-Cyclr-Account` | The `{AccountID}` of the account you want to install a connector into. |

>  **Note**: For information on how to obtain these values, see the [Cyclr authentication](api-authentication) page.
