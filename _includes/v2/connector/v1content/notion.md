
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Login to your existing Notion account.

### OAuth2 Application

- Go to [My Integrations](https://www.notion.so/my-integrations) within Notion
- Click **New Integration** - see the [Notion documentation](https://developers.notion.com/docs/authorization#authorizing-public-integrations) for more details of app creation
- Enter a name and select the workspace you wish to integrate with
- Click **Submit**
- Select **Public Integration Option**
- Enter your app **Redirect URL** , `https://[Your Cyclr Service Domain]/connector/callback` 
- When prompted enter other details such as privacy policy, support email etc
- Click on **Save** 
- Note the `OAuth client ID` and `OAuth Client Secret`

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Notion Connector within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose **Connector Library*
- Search for Notion
- Click the **Setup** button

Enter the following values:

**Client ID**:  The client ID that we retrieved from the app that you made.

**Client Secret**:  The secret that we retrieved from the app that you made.

Your Notion Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>
