---
title: AmeriCommerce authentication
sidebar: cyclr_sidebar
permalink: americommerce-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## AmeriCommerce setup

### Requirements

To connect with Cyclr, you need the following authentication details from your Admin console:
   
*  AmeriCommerce Client ID
*  Client Secret
*  Store Domain
*  Redirect URI.

For more information, see the AmeriCommerce documentation on [creating an Access Token](https://developers.cart.com/docs/rest-api/ZG9jOjU4NjM4-cart-com-online-store-api-authentication).

</section>
<section class="card">

## Cyclr setup

To set up the AmeriCommerce connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the AmeriCommerce connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**           | **Description**                                                                 |
   | :-----------------  | :------------------------------------------------------------------------------ |
   | **Client ID**       | The App ID given to you in the Admin console when you set up your application.  |
   | **Client Secret**   | The App Secret from the Admin console.                                          |
   | **Store Domain**    | The Domain of your AmeriCommerce Store.                                         |
   | **Redirect URI**    | The OAuth callback URL.                                                         |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
