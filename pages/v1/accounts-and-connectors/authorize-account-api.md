---
title: Authorize account API calls
sidebar: cyclr_sidebar
permalink: authorize-account-api
tags: [accounts]
---

You can use the Cyclr API to make calls within specific user accounts.

For each call, replace `{YourCyclrDomain}` with your Cyclr api domain. You also need to include the following values in the header parameters:

| **Parameter**   | **Description**                                                      |
|-----------------|----------------------------------------------------------------------|
| `Authorization`   | Your Cyclr access token. Use the format: `Bearer {access_token}`.      |
| `X-Cyclr-Account` | The `{AccountID}` of the account you want to install a connector into. |

>  **Note**: For information on how to obtain these values, see the [Cyclr authentication](api-authentication) page.
