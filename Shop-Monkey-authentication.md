---
title: Shopmonkey authentication

sidebar: cyclr_sidebar
permalink: shop-monkey-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Shopmonkey setup



### Get authentication details

To authenticate your connector, you need the Public Key and a Private Key for your Shopmonkey account.


### Get a Public Key and Private Key

The keys can be obtained through this method:

- Login to Shopmonkey.
- Go to Settings / API & Webhooks and enable the API
- Select your user profile name in the upper-right and then select "Update Personal Info"
- Collect both the Public and Private Keys

If you have any trouble obtaining a Public and Private key, follow this guide or contact your Shop Monkey account manager.

</section>

<section class="card">

## Cyclr setup

To set up the Shopmonkey connector in Cyclr, go to your Cyclr console:


1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Shopmonkey connector.


3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**   | **Description**                            |
   | :---------- | :----------------------------------------- |
   | Public Key  | The Public Key obtained from Shopmonkey.  |
   | Private Key | The Private Key obtained from Shopmonkey. |

   
5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.


### Account setup

Cyclr asks you for the below values when you install the Shopmonkey connector into an account:


| **Value**  | **Description**                                            |
| :--------- | :--------------------------------------------------------- |
| URL        | The Base URL of your Shopmonkey integration to call from. |
| API Version | The version of the Shopmonkey API being used.             |


> **Note**: You can use different details for different accounts.

</section>