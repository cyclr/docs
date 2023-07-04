---
title: Pipedrive (OAuth2.0) Connector Guide
sidebar: cyclr_sidebar
permalink: pipedrive-oauth-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Pipedrive setup

## Requirements

Pipedrive uses OAuth 2.0 authentication for remote API access, so to connect with Cyclr, you need to create an application within Pipedrive.

To create an app, you need to request a [developer sandbox account](https://pipedrive.readme.io/docs/developer-sandbox-account), 

To obtain the authentication values, you need to [register the application](https://pipedrive.readme.io/docs/marketplace-registering-a-private-app) in the Pipedrive Developer Hub. 

To connect with Cyclr, you need to set the correct callback and scopes in the **App registration form**:

*  Enter the Cyclr Callback URL in the **Callback URL** field. The URL has the format: `https://{YourServiceDomain e.g. app-h.cyclr.com}/connector/callback`
*  Enable the **Access scopes** as either **Read only** or **Full access**. For more information, see the Pipedrive documentation on [scopes](https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations).


### Get authentication details

To connect with Cyclr, you need the following authentication values:

*  Client ID
*  Client Secret

To view the authentication details, open up the app in the Pipedrive Developer Hub. In the settings, go to the **OAuth and Access Scopes** tab to see the Client ID, and select **Show** to view the Client Secret.

</section>
<section class="card">

## Cyclr setup

To set up the Pipedrive OAuth 2.0 connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Pipedrive OAuth 2.0 connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**          | **Description**                             |
   | :----------------- | :------------------------------------------ |
   | **Client ID**   | The Client ID from the Pipedrive application.                           |
   | **Client Secret**   | The Client Secret from the Pipedrive application.                   |
   | **Callback URL**| Cyclr fills this field by default.          |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.





# Partner Setup
-------------
Cyclr requires Pipedrive to use OAuth 2.0 authentication for remote API access. You must register Cyclr within Pipedrive as its own App to receive a Client ID and Client Secret. This enables Cyclr to authenticate and connect with Pipedrive.

> Note: Due to how Pipedrive authentication works, customers themselves will need to follow the below Pipedrive setup process.  You may wish to use the standard (non-OAuth) Pipedrive Connector if you don't want your customer to have this responsibility.  With the standard Connector only their personal API Key is required for installation. (https://support.pipedrive.com/en/article/how-can-i-find-my-personal-api-key)

</section>
