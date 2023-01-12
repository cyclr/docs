---
title: Miva Authentication
sidebar: cyclr_sidebar
permalink: miva-connector
tags: [connector]
---

## Cyclr setup
Includes anything the partner needs to do in the Cyclr console and accounts in order to use the connector.

### Console setup

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

## Additional information
### Documentation

Documentation of the Miva API can be found here: https://docs.miva.com/json-api/#api-endpoint