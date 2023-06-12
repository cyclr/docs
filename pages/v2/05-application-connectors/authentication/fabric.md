---
title: Fabric Authentication
sidebar: cyclr_sidebar
permalink: fabric-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Fabric setup

To connect with Cyclr, you need the following authentication details from your Fabric account:

*  A Client ID.
*  A Client Secret.
*  An Authorization URL.
*  A Tenant ID (Also known as Account ID).
*  The name of the environment (Also known as the **stage**).

There are also optional credentials that you may want to use for your connector:

*  A Sales Channel ID.
*  A Source value.

To find the **Client ID**, **Client Secret** and **Authorization URL**, go to your [application information page](https://live.copilot.fabric.inc/home/developer-tools/app/api/). To find the **Tenant ID**, go to your [account details page](https://live.copilot.fabric.inc/home/account-details).

For more information on how to authenticate with Fabric, see the Fabric documentation on [identity developer guide concepts](https://developer.fabric.inc/reference/identity-developer-guide-concepts).

</section>
<section class="card">

## Cyclr setup

To set up the Fabric connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.
2. Use the search box to find the Fabric connector.
3. Select the **Setup Required** icon.
4. Enter the below values:

| **Value**          | **Description**                             |
| :----------------- | :------------------------------------------ |
| **Client ID**   | The Client ID of your application.      |
| **Client Secret**   | The Client Secret of your application.   |
| **Auth URL**| The authorization URL, found in your application page. This allows you to target the correct authorization server.      |
| **Tenant ID**| Your account ID, found in the fabric console.       |
| **Environment**| The name of the environment you want to access, also known as a stage.       |
| **Sales Channel ID (Optional)**| The sales channel ID of the of the source you want to access.       |
| **Source (Optional)**| The source you want to access.       |
| **Scopes (Optional)**| This field allows you to use custom scopes when you authorize.      |

5. Select **Save Changes**.

> **Note**: If you leave any values (other than scopes) blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
