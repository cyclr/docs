<section class="authentication" markdown="1">

## Authentication

| **Type** | OAuth 2.0 |
| **OAuth 2.0 type** | AuthorisationCode |
| **Authorise URL** | {{Domain}}/oauth/v2/auth?scope={{Scopes}}&access_type=offline&prompt=consent |
| **Access token URL** | {{Domain}}/oauth/v2/token |
{: .table .vheader}

</section>

<section class="zoho-crm-set-up" markdown="1">

## Zoho CRM set up

You need an OAuth 2.0 client ID and client secret to install the Zoho CRM connector in Cyclr. You need to create an application in your [Zoho CRM API console](https://accounts.zoho.com/developerconsole) to obtain these. Zoho CRM's documentation on creating an application in your Zoho API console can be found [here](https://www.zoho.com/accounts/protocol/oauth-setup.html).

<div class="create-a-client-in-your-zoho-crm-api-console" markdown="1">

### Create an application in your Zoho CRM API console

Use the following settings when creating an application in your Zoho CRM API console, make note of the **Client ID** and **Client Secret**:

-   **Choose a Client Type**: Server-based Applications
-   **Authorized Redirect URIs**: `https://{{Your Cyclr Service Domain}}/connector/callback`

**Note**: Your `Cyclr service domain` can be found in your Cyclr console under **Settings** > **General Settings** > **Service Domain**.

</div>

<section class="cyclr-set-up" markdown="1">

## Cyclr set up

To set up the Zoho CRM connector in Cyclr, in your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the Zoho CRM connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:
    - **Client ID**: The client ID of your Zoho CRM application.
    - **Client Secret**: The client secret of your Zoho CRM application.
6. Select **Save Changes**.

Your Zoho CRM connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>

<div section="additional-information" markdown="1">

## Additional Information

<div class="scopes" markdown="1">

### Scopes

The default scopes on installation are: `ZohoCRM.modules.ALL,ZohoCRM.users.ALL,ZohoCRM.org.ALL,ZohoCRM.settings.roles.ALL`. You can manually enter scopes to restrict the connectors access. Zoho's documentation on available scopes can be found [here](https://www.zoho.com/crm/developer/docs/api/v2/scopes.html).

</div>

</section>
