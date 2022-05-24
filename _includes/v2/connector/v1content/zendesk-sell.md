<section class="authentication" markdown="1">

## Authentication

| **Type** | OAuth 2.0 |
| **OAuth 2.0 type** | AuthorisationCode |
| **Authorise URL** | https://api.getbase.com/oauth2/authorize |
| **Access token URL** | https://api.getbase.com/oauth2/token |
{: .table .vheader}

</section>

<section class="zendesk-sell-set-up" markdown="1">

## Zendesk Sell set up

<div class="retrieving-client-id-and-client-secret" markdown="1">

### Retrieving client ID and client secret

1. Login to your Zendesk Sell front-end.
2. Select the settings cog on the left side of the page.
3. Navigate to **Integrations** > **OAuth** > **Developer Apps**.
4. Select a new app, enter your Cyclr redirect URL `https://{{Your Cyclr Service Domain}}/connector/callback`.
5. Select **Save**, and then **Details** and note down the **Client ID** and **Client Secret**.

**Note**: Your `Cyclr service domain` can be found in your Cyclr console under **Settings** > **General Settings** > **Service Domain**.

</div>

</section>

<section class="cyclr-set-up" markdown="1">

## Cyclr set up

To set up the Zendesk Sell connector in Cyclr, in your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the Zendesk Sell connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:
    - **Client ID**: The client ID of your Zendesk Sell app.
    - **Client Secret**: The client secret of your Zendesk Sell app.
6. Select **Save Changes**.

Your Zendesk Sell connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>
