---
title: Akeneo Authentication
sidebar: cyclr_sidebar
permalink: Akeneo-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Create Akeneo Data Source connection
- Login into your **Akeneo PIM account**
- On the left hand side panel, click on **Connect** tab.
- Navigate to the top right hand corner and click on the green **Create** button.
- Add some inputs to the required fields **Label** and **Code**. In the **Flow type** select **Data Source** and click **Save**.
- From the **Credentials** section, copy **Client ID**, **Secret**, **Username** and **Password**. These values will be needed when setting up connector.
- Navigate to the **Permissions** section and set **Role** to **API** and **Group** to **API Connections**. Click **Save**

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
   | **Client ID**   | The Client ID of your application.      |
   | **Client Secret**   | The Client Secret of your application.   |
   | **Username**   | The username of the authorized user.     |
   | **Password**   | The password of the authorized user.   |
   | **PIM URL**   | The PIM URL obtained when Akeneo account was created.   |

6. Select **Save Changes**.

> **Note**: You can use different details for different accounts.

</section>
