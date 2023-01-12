---
title: Miva Authentication
sidebar: cyclr_sidebar
permalink: miva-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Miva setup

To authenticate your connector, you need to get these authentication details. Select the links to view the relevant Miva documentation. 

*  [Signature](https://docs.miva.com/json-api/#hmac-signature)
*  Store [URL domain](https://docs.miva.com/json-api/#api-endpoint)
*  [Folder](https://docs.miva.com/json-api/#api-endpoint)
*  Store Code
*  API access token

For more information on how to obtain these details, either view the Miva [API documentation](https://docs.miva.com/json-api/#api-endpoint) or contact your Miva account manager.


</section>
<section class="card">

## Cyclr setup

To set up the Miva connector in Cyclr, go to your console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Miva connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

| Value              | Description                                 |
| :----------------- | :------------------------------------------ |
| **Signature** | A Miva-generated private key, used in authentication. |
| **Domain** | The domain URL of the store you would like to access. |
| **Folder** | The folder in the instance you are trying to access. |
| **Store Code** | The code of the store you would like to access. To be used in request body. |

5. Select **Next**.

6. Enter the **API Access Token** provided to you and select **Save**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.


</section>
