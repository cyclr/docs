---
title: Phrase Authentication
sidebar: cyclr_sidebar
permalink: phrase-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Phrase setup

To authenticate your connector, you need to get the authentication details. You can generate the API credentials from your Phrase application:

1. Go to Phrase frontend and login to your account.
2. Go to **Settings** in the left side menu.
3. Find the **Integrations** section and select **Registered OAuth apps**.
4.  Select **New**.
5. Enter a name and your callback URL (`https://{YourCyclrServiceDomain}/connector/callback`).
6.  Select **Save** and make a note of your **Client ID**.

</section>
<section class="card">

## Cyclr Setup
To set up the Phrase connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Phrase connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Client ID**      | The Client ID generated from your Phrase account. |
   | **Client Secret**  | Leave this value empty.                           |
   | **US Instance?**   | If your account was created within Phrase's US data center, set this to **true**. |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
