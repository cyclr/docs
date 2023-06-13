---
title: Acumatica Authentication
sidebar: cyclr_sidebar
permalink: acumatica-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Acumatica setup

To authenticate your connector, you need to get the client ID and secret of the Acumatica account you want to connect with. You can generate these credebtials from the Acumatica account.

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
| **Client ID**   | The client ID of the OAuth application in your Acumatica instance.                        |
| **Client Secret**   | The client secret of the OAuth application in your Acumatica instance.                     |

5. Select **Next**, and then select the **Sign In** button.
   
6. Sign into Acumatica with the relevant username and password.

7. Select whether you want give the app **Offline Access** or not.

8. Select **Yes, Allow**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
