
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Create an oAuth application on the Drift [developer portal](https://dev.drift.com/apps)

- Click *Build Your App*
- Enter an App Name
- Click the *Oauth & Scopes* menu option
- Add Redirect URL: enter a name and Callback URL `https://[Your Cyclr Service Domain]/connector/callback` for your app
- Select the required *Drift Scopes* based on the operations used to be intergration
- Copy `Client ID` and `Secret ID`

</div>

</section>

<section class="setup partner" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Drift Connector within Cyclr:

- Go to your *Cyclr Console*
- Click the *Connectors* menu option
- Choose Connector Library
- Search for  *Drift*
- Click the *Setup* button

Enter the values noted during the partner setup:

- `Client ID`:  The Client ID
- `Client Secret`:  The Secret ID

Your Drift Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>
