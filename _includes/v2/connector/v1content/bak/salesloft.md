
## Partner Setup

First, login to your existing Salesloft account or [sign up for one.](https://integrations.salesloft.com/register/)

#### Retrieving OAuth2 Details

*   [Login](https://accounts.salesloft.com/sign_in) to your Salesloft Account.
*   Click Create App.
    *   More details on how to create an app can be found [here](https://developers.salesloft.com/api.html#!/Topic/oauth).
*   Enter a name and Callback URL (https://[Your Cyclr Service Domain]/connector/callback) for your app.
*   Click Save.
*   Note the **client ID** and **secret**.

### Cyclr Setup

Setup your Salesloft App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Salesloft**
*   Click the **Setup** button

Enter the following values:

**Client ID**:  The client ID that we retrieved from the app that we made.

**Client Secret**:  The secret that we retrieved from the app that we made.


Your Salesloft Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
