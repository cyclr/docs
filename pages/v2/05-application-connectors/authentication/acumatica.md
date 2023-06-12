---
title: Acumatica Authentication
sidebar: cyclr_sidebar
permalink: acumatica-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Acumatica setup

To authenticate your connector, you need to get the client ID and secret of the Acumatica account.These can be created in your Acumatica account.

</section>
<section class="card">

## Cyclr setup

To set up the Acumatica connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Acumatica connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**          | **Description**                             |
   | :----------------- | :------------------------------------------ |
   | **Client ID**   | The client ID of the OAuth application created your Acumatica instance.                        |
   | **Client Secret**   | The client secret of the OAuth application created your Acumatica instance.                     |

5. Select **Next**.
6. Select **Sign In**.
7. Sign into Acumatica with the relevant username and password.
8. Select whether you would like to give the app **Offline Access** or not.
9. Select **Yes, Allow**.


> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
