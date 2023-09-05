---
title: Revel authentication
sidebar: cyclr_sidebar
permalink: revel-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Revel setup

### Requirements

In order to get an API Key you need to contact your Revel sales rep to get a Partner Connect subscription. 
Once subscription is online, Revel Operations team will set up the keys and email them to specified email. 

To connect with Cyclr, you need the following authentication details:
   
*  API Key
*  API Secret

For more information, see the Revel documentation on [Authentication](https://developer.revelsystems.com/revelsystems/docs/how-to-make-an-api-call).

</section>
<section class="card">

## Cyclr setup

To set up the Revel connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Revel connector.

3. Select the **Setup Required** icon.

4. Enter the Sub Domain then click Next. Then enter API key and the API secret, they have to be joined by a colon (e.g. key:secret):

   | **Value**           | **Description**                                                                 |
   | :-----------------  | :------------------------------------------------------------------------------ |
   | **Sub Domain**      | The unique domain for the given client.                                         |
   | **API Key**         | The API key from the Parter Connect subscription email.                         |
   | **API Secret**      | The API secret from the Parter Connect subscription email.                      |


5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
