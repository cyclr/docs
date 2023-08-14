---
title: Akeneo Authentication
sidebar: cyclr_sidebar
permalink: Akeneo-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Akeneo setup
To connect with Cyclr, you need the following authentication details from your Akeneo PIM account:
*  Client ID
*  Client Secret
*  PIM URL

To access these authentication values from your Akeneo PIM account, you need to create an Akeneo Data Source connection:
1.  On the left side panel, select the **Connect** tab.
2.  Select the green **Create** button in the top right corner.
3.  Enter a **Label** and **Code**, then select **Data Source** and select **Save**.
4.  Go to the **Credentials** section and make a note of the Client ID and Secret.

You also need to set the following permissions for your Akeneo Data Source connection:
*  Set **Role** to **API**.
*  Set **Group** to **API Connections**

</section>
<section class="card">

## Cyclr setup

To set up the Akeneo connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Akeneo connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**          | **Description**                             |
   | :----------------- | :------------------------------------------ |
   | **Client ID**   | The Client ID from your application.      |
   | **Client Secret**   | The Client Secret from your application.   |
   | **Username**   | The username of the authorized user.     |
   | **Password**   | The password of the authorized user.   |
   | **PIM URL**   | The PIM URL from your Akeneo account.   |

6. Select **Save Changes**.

> **Note**: You can use different details for different accounts.

</section>
