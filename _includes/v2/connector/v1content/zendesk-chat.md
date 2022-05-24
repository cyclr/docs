<section class="authentication" markdown="1">

## Authentication

| **Type** | OAuth 2.0 |
| **Description** | Go to Settings > > Account > API & SDKs on the Zendesk Portal to setup an oAuth application. |
| **OAuth 2.0 type** | AuthorisationCode |
| **Authorise URL** | https://www.zopim.com/oauth2/authorizations/new?scope=read%20write%20chat&subdomain={{SubDomain}} |
| **Access token URL** | https://www.zopim.com/oauth2/token |
{: .table .vheader}

</section>

<section class="zendesk-chat-set-up" markdown="1">

## Zendesk Chat set up

You need an OAuth 2.0 client ID and client secret to install the Zendesk Chat connector in Cyclr. You need to create an API client in Zendesk to obtain these. Zendesk's documentation on creating an API client can be found [here](https://support.zendesk.com/hc/en-us/articles/4408828740762-Chat-API-tutorial-Generating-an-OAuth-token-integrated-Chat-accounts).

<div class="creating-an-api-client-in-zendesk" markdown="1">

### Creating an API client in Zendesk

Use the following settings when creating an API client in Zendesk, make note of the **Client ID** and **Client secret**:

-   **Redirect URLs**: `https://{{Your Cyclr Service Domain}}/connector/callback`

**Note**: Your `Cyclr service domain` can be found in your Cyclr console under **Settings** > **General Settings** > **Service Domain**.

</div>

</section>

<section class="cyclr-set-up" markdown="1">

## Cyclr set up

To set up the Zendesk Chat connector in Cyclr, in your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the Zendesk Chat connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:
    - **Client ID**: The client ID of your Zoom OAuth app.
    - **Client Secret**: The client secret of your Zoom OAuth app.
6. Select **Save Changes**.

Your Zendesk Chat connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>
