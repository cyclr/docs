<section class="authentication" markdown="1">

## Authentication

| **Type** | OAuth 2.0 |
| **OAuth 2.0 type** | AuthorisationCode |
| **Authorise URL** | https://zoom.us/oauth/authorize |
| **Access token URL** | https://zoom.us/oauth/token |
{: .table .vheader}

</section>

<section class="zoom-set-up" markdown="1">

## Zoom set up

You need an OAuth 2.0 client ID and client secret to install the Zoom connector in Cyclr. You need to create a Zoom OAuth App to obtain these. Zoom's documentation on creating an OAuth app can be found [here](https://marketplace.zoom.us/docs/guides/build/oauth-app).

<div class="section-creating-an-oauth-app-in-zoom" markdown="1">

### Create an OAuth app in Zoom

Use the following settings when creating your Zoom OAuth app, make note of the **Client ID** and **Client secret**:

-   **Choose app type**: Account-level app
-   **Would you like to publish this app on Zoom App Marketplace?**: False
-   **Redirect URL for OAuth**: `https://{{Your Cyclr Service Domain}}/connector/callback`
-   **Subdomain check**: True
-   **Add allow lists**: `https://{{Your Cyclr Service Domain}}/connector/callback`

**Note**: Your `Cyclr service domain` can be found in your Cyclr console under **Settings** > **General Settings** > **Service Domain**. Set scopes according to your use case of the API. Zoom's documentation on OAuth scopes can be found [here](https://marketplace.zoom.us/docs/guides/auth/oauth/oauth-scopes).

</div>
</section>

<section class="cyclr-set-up" markdown="1">

## Cyclr set up

To set up the Zoom connector in Cyclr, in your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the Snowflake connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:
    - **Client ID**: The client ID of your Zoom OAuth app.
    - **Client Secret**: The client secret of your Zoom OAuth app.
6. Select **Save Changes**.

Your Zoom connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>
