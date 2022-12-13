---
title: Filevine authentication
sidebar: cyclr_sidebar
permalink: filevine-connector
tags: [connector]

---

## Filevine setup

You need to log into your server's developer portal and obtain the necessary authentication values. Please refer to Filevine's [documentation](https://developer.filevine.io/docs/v2/ZG9jOjM4ODc3NTE-authentication) on how to obtain an **API key**, **API secret**, a **User ID**, and an **Org ID**.

## Cyclr setup

To set up the Filevine connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Filevine connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value          | Description                                                  |
   | -------------- | ------------------------------------------------------------ |
   | **API Key**    | The API Key from your Filevine account. |
   | **API Secret** | The API Secret from your Filevine account.                   |
   | **Domain**     | The server where the account is hosted. For example, if you have a personalised url: `{company-name}.api.filevineapp.com` |
   | **User ID**    | The User ID of your Filevine account.                        |
   | **Org ID**     | The Org ID of your Filevine account.                         |

5. Select **Save Changes**.

> **Note**: To use different settings for different accounts, leave the value blank. This means Cyclr asks for the value when you install the connector into an account.
