---
title: PassKit authentication
sidebar: cyclr_sidebar
permalink: passkit-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## PassKit setup

### Requirements

To connect with Cyclr, you need to sign up for a [PassKit account](https://app.passkit.com/signup).

### Get authentication details

To authenticate your connector, you need to get the authentication details. 

1. From the Dashboard, select the arrow by your account name in the top right of the page.
 
2. Go to **Developer Tools** > **REST Credentials**.
  
3. Enter your password and then select **Get Credentials**.
  
4. Make note of the **Key** and **Secret**.

</section>
<section class="card">

## Cyclr setup

To set up the PassKit connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the PassKit connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**    | **Description**                                                        |
   | :----------- | :----------------------------------------------------------------------|
   | **Base URL** | Your base PassKit API URL, for example, `https://api.pub1.passkit.io`.               |
   | **Key**      | The key for the specific app on you created in the PassKit Portal.   |
   | **Secret**   | The secret' for the specific app on you created in the PassKit Portal |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
