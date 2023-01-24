---
title: Pipedrive (OAuth2.0) Connector Guide
sidebar: cyclr_sidebar
permalink: pipedrive-oauth-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
# Partner Setup
-------------
Cyclr requires Pipedrive to use OAuth 2.0 authentication for remote API access. You must register Cyclr within Pipedrive as its own App to receive a Client ID and Client Secret. This enables Cyclr to authenticate and connect with Pipedrive.

> Note: Due to how Pipedrive authentication works, customers themselves will need to follow the below Pipedrive setup process.  You may wish to use the standard (non-OAuth) Pipedrive Connector if you don't want your customer to have this responsibility.  With the standard Connector only their personal API Key is required for installation. (https://support.pipedrive.com/en/article/how-can-i-find-my-personal-api-key)


</section>
<section class="card">
## Pipedrive Setup

To obtain Client ID and Client Secret values from within Pipedrive:

### Enable a Developer Sandbox Account

To create a Developer Sandbox Account, Pipedrive requires you to complete the following [form](https://developers.pipedrive.com/start-here). This allows you to access the **Marketplace Manager**. Without this, you will be unable to create the Pipedrive App required for authentication with Cyclr. The official Pipedrive documentation on this process can be found [here](https://pipedrive.readme.io/docs/developer-sandbox-account).

### Create an app within the Marketplace Manager

Create a new App and obtain the Client ID and Client Secret using the steps below. The official Pipedrive documentation for creating an App can be found [here](https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app).

1. Go to the **Marketplace Manager** found [here](https://cyclrdevs.pipedrive.com/settings/marketplace_manager). This is only accessible if you have a Developer Sandbox Account as explained above.
2. Click `Create New App`.
3. Select `No` to set the App to unlisted and internal/private, then click `Next`. Pipedrive's documentation on app types can be found [here](https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app#types-of-apps).
4. Complete the App form as required by Pipedrive.
5. Cyclr authentication is handled under the **OAuth & Access scopes** heading. Enter the callback URL in the **Callback URL** field. The callback URL has the following format:
   https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback
6. Enable the required **Access scopes** as either **Read only** or **Full access**. The official Pipedrive documentation on access scopes can be found [here](https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations).
7. Click `Save` to create the App. This will take you back to the Marketplace Manager.
8. Click the newly created App within the **Marketplace Manager** to be taken to the settings again. Under the **OAuth & Access scopes** heading you will now find the **Client ID** and can click `Show` to reveal the **Client secret**. Make a note of these as they will be required by Cyclr to set up the Pipedrive Connector.


</section>
