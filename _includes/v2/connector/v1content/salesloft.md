
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

First, login to your existing Salesloft account or [sign up for one.](https://integrations.salesloft.com/register/)

### OAuth2 Details

- [Login](https://accounts.salesloft.com/sign_in) to your Salesloft Account
- Click **Create App**
    - More details on how to create an app can be found [here](https://developers.salesloft.com/api.html#!/Topic/oauth).
- Enter a name and **Callback URL** `https://[Your Cyclr Service Domain]/connector/callback`
- Click **Save**
- Note the `client ID` and `Client Secret`

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Salesloft App within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose **Connector Library**
- Scroll down to **Salesloft**
- Click the **Setup** button

Enter the following values:

**Client ID**:  The client ID that we retrieved from the app that we made.

**Client Secret**:  The secret that we retrieved from the app that we made.

Your Salesloft Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>