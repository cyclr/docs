---
title: eBay Authentication
sidebar: cyclr_sidebar
permalink: ebay-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
<a name="ebay-setup"></a>


</section>
<section class="card py-5 my-5">
## eBay setup

You need the following to setup the eBay connector in Cyclr:

-   An eBay [developer account](#register-a-developer-account).
-   A set of [application keys](#create-application-keys) created for a production account.
-   An [app ID (client ID) and cert ID (client secret)](#get-a-client-id-and-client-secret) associated with the production application keys.
-   An [application](#create-an-application) set with your Cyclr account redirect URL.

<a name="register-a-developer-account"></a>

### Register a developer account

Register an account with the eBay developer program [here](https://developer.ebay.com/). Find eBay's guide on how to do this [here](https://developer.ebay.com/api-docs/static/gs_join-the-ebay-developers-program.html).

<a name="create-application-keys"></a>

### Create application keys

Create a set of application keys [here](https://developer.ebay.com/my/keys). You need a production set of keys to use the connector with a live eBay account. Sandbox keys can only be used with sandbox accounts. eBay's guide on how to do this can be found [here](https://developer.ebay.com/api-docs/static/gs_create-the-ebay-api-keysets.html).

> **Note**: To use production application keys, you need to subscribe to or opt-out of eBay's marketplace account deletion/closure notifications. Opting in requires a setup outside of Cyclr to respond to eBay's GET requests. Opting out may be possible depending on your usage because Cyclr doesn't persist data. You can find more information [here](https://developer.ebay.com/marketplace-account-deletion).

<a name="obtain-client-id-and-client-secret"></a>

### Obtain client ID and client secret

Once you have created a set of application keys, you can obtain your client ID and client secret associated with your application keys [here](https://developer.ebay.com/my/keys). Your client ID is listed as **App ID (Client ID)** and your client secret is listed as **Cert ID (Client Secret)**.

<a name="create-an-application"></a>

### Create an application

Once you have obtained your client ID and client secret, you need to create an application from the **User Tokens (eBay Sign-In)** page of your application. Under the **Find the Get a Token from eBay via Your Application** heading, do the following:

1. Select **Add eBay Redirect URL**.
2. Enter an application name for the **Display Title**.
3. Enter your Cyclr account redirect URL for the **Your auth accepted URL**.
4. Select **OAuth**.
5. Select **Save**.

> **Note**: You can find your Cyclr account redirect URL in your Cyclr console under **Settings** > **General Settings** > **Service Domain**. It has the format `https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback`.

<a name="cyclr-set-up"></a>


</section>
<section class="card py-5 my-5">
## Cyclr setup

<a name="sandbox-or-production"></a>

### Sandbox or Production

If you want to use the eBay developer sandbox for testing, set the **Is Sandbox?** field to `true` during setup, and use the sandbox application keys you generated in the previous steps. For production keys,  set **Is Sandbox?** to `false`.

<a name="console-setup"></a>

### Console setup

To setup your eBay connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the eBay connector.
4. Select the **Setup Required** icon.
5. Enter the below valuess:

    | **Value**     | **Description**                                                                  |
    |:--------------|:-------------------------------------------------------------------------------- |
    | **Client ID** | Your eBay application [App ID (Client ID)](#obtain-client-id-and-client-secret). |
    | **Client Secret** | Your eBay application [Cert ID (Client Secret)](#obtain-client-id-and-client-secret). |
6. Set **Is Sandbox?** to true or false depending on which type of authentication keys you are using.  
7. Select **Save Changes**.

> **Note**: To use different settings for different accounts, leave the value blank. This means Cyclr asks you to enter the value when you install the connector into an account.

<a name="account-setup"></a>

### Account setup

Cyclr asks for the following values when you install the eBay connector into an account:

| **Value**     | **Description**                                                                  |
|:--------------|:-------------------------------------------------------------------------------- |
| **Client ID** | Your eBay application [App ID (Client ID)](#obtain-client-id-and-client-secret) if you left the field blank in the console setup. |
| **Client Secret** | Your eBay application [Cert ID (Client Secret)](#obtain-client-id-and-client-secret)if you left the field blank in the console setup. |
| **Account Identifier** | Your eBay application [environment](#create-application-keys). |

To test your eBay connector, you can execute one of the methods to confirm it can return data.

</section>
