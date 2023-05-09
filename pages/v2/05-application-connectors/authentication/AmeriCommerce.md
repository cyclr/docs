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

To connect with Cyclr, you need an AmeriCommerce Client ID, Client Secret, Store Domain and Redirect URI.

For more information, see the AmeriCommerce documentation on [creating an Access Token]([<link to connector docs>](https://developers.cart.com/docs/rest-api/ZG9jOjU4NjM4-cart-com-online-store-api-authentication)).


### Get authentication details

To authenticate your connector, you need to get the authentication details. 

Go to the Admin Console and make note of the Application ID and Secret.

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
   | **Client ID**       | The APP ID given to you in the admin console when you set up your application.  |
   | **Client Secret**   | The App Secret from the admin console.                                          |
   | **Store Domain**    | The Domain of your AmeriCommerce Store.                                         |
   | **Redirect URI**    | The OAuth callback URL.                                                         |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
