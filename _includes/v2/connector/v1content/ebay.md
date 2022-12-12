
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

You need the following to setup the eBay connector in Cyclr:

-   An eBay [developer account](#register-a-developer-account).
-   A set of [application keys](#create-application-keys) created for a production account.
-   An [app ID (client ID) and cert ID (client secret)](#get-a-client-id-and-client-secret) associated with the production application keys.
-   An [application](#create-an-application) set with your Cyclr account redirect URL.

### Register a developer account

Register an account with the eBay developer program [here](https://developer.ebay.com/). eBay's guide on how to do this can be found [here](https://developer.ebay.com/api-docs/static/gs_join-the-ebay-developers-program.html).

### Create application keys

Create a set of application keys [here](https://developer.ebay.com/my/keys). You need a production set of keys to use the connector with a live eBay account. Sandbox keys can only be used with sandbox accounts. eBay's guide on how to do this can be found [here](https://developer.ebay.com/api-docs/static/gs_create-the-ebay-api-keysets.html).

**Note**: To use production application keys, you must subscribe to or opt-out of eBay's marketplace account deletion/closure notifications. Opting in requires a setup outside of Cyclr to respond to eBay's GET requests. Opting out may be possible depending on your use case as Cyclr does not persist data. You can find more information [here](https://developer.ebay.com/marketplace-account-deletion).


### Obtain client ID and client secret

Once you have created a set of application keys you can obtain your client ID and client secret associated with your application keys [here](https://developer.ebay.com/my/keys) . Your client ID is listed as **App ID (Client ID)** and your client secret is listed as **Cert ID (Client Secret)**.

### Create an application

Once you have obtained your client ID and client secret you need to create an application from the **User Tokens (eBay Sign-In)** page of your application. Under the **Find the Get a Token from eBay via Your Application** heading, do the following:

1. Select **Add eBay Redirect URL.**
2. Enter an application name for the **Display Title**.
3. Enter your Cyclr account redirect URL for the **Your auth accepted URL**.
4. Select **OAuth**.
5. Select **Save**.

**Note**: Your Cyclr account redirect URL can be found in your Cyclr console under **Settings** > **General Settings** > **Service Domain**. It has the format: `https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback`.

</div>

</section>

<section class="setup partner" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

To setup your eBay connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the eBay connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:
    - **Client ID**: Your eBay application [App ID (Client ID)](#obtain-client-id-and-client-secret).
    - **Client Secret**: Your eBay application [Cert ID (Client Secret)](#obtain-client-id-and-client-secret).
6. Select **Save Changes**.

### Account setup

You will be asked for the following values when installing the eBay connector within an account:

-   **Client ID**: Your eBay application [App ID (Client ID)](#obtain-client-id-and-client-secret), if you did not enter this in step 5 above.
-   **Client Secret**: Your eBay application [Cert ID (Client Secret)](#obtain-client-id-and-client-secret), if you did not enter this in step 5 above.
-   **Account Identifier**: Your eBay application [environment](#create-application-keys).

Your eBay connector is now set up! You can test it by executing one of the methods to confirm it can return some data.

</div>

</section>
