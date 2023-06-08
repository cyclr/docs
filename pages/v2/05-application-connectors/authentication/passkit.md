---
title: PassKit authentication
sidebar: cyclr_sidebar
permalink: passkit-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## PassKit setup

### Requirements

To connect with Cyclr, you need to sign up for a [PassKit Account](https://app.passkit.com/signup).

### Get authentication details

To authenticate your connector, you need to get the authentication details. 

1. From the Dashboard, select the arrow by your account name in the top right
 
2.Select 'Developer Tools' > 'REST Credentials' > enter password > Select 'Get Credentials'
  
3. Make note of the 'Key' and 'Secret'.

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
   | **Base URL** | Base PassKit API URL e.g. "https://api.pub1.passkit.io".               |
   | **Key**      | The 'Key' for the specific app on you created on the PassKit Portal.   |
   | **Secret**   | The 'Secret' for the specific app on you created on the PassKit Portal |

5. Select **Next**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
