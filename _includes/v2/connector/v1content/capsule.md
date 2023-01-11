
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Capsule v2 uses OAuth 2. Sign up for an application on Capsule first and get an ``OAuth Client ID`` and ``Client Secret``.

See the [Capsule documentation](https://developer.capsulecrm.com/v2/overview/authentication#oauth-2) for details.

1. Register a free Capsule account; or log into your existing account if you already have one.
2. Go to [https://developer.capsulecrm.com/clients/new](https://developer.capsulecrm.com/clients/new)

    Below are the details you should provide:

    *Name*: Your Application Name

    *URL*: Your Cyclr service domain, e.g. https://app-h.cyclr.com/. This can be found in your Cyclr Console under Settings > General Settings > Service Domain.

    *Redirect URL* : you must add a callback URL to allow Capsule to be used in your Cyclr Console and its accounts.

    The URL is:

    `https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback`

    *Application Type*: Web Application

</div>

</section>

<section class="setup partner" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">


3. Go to Cyclr Console (https://yourCyclrInstance/console) > Connectors > Connector Library > Capsule v2 > Setup

    - *Client ID* : Client ID displayed after you create the Capsule app
    - *Client Secret* : Client Secret displayed after you create the Capsule app
    - *Authorise URL* : https://api.capsulecrm.com/oauth/authorise?scope=read+write
    - *Access Token URL* : https://api.capsulecrm.com/oauth/token

Your Capsule v2 connector is now set up! You can test it by installing it in one of your user accounts.

</div>

</section>

<section class="setup partner" markdown="1">

## API Integration

<div class="section-content" markdown="1">

Capsule v2 connector uses OAuth 2 Authorisation Code flow. 

Your end users must sign into Capsule and grant Cyclr access to their account.

To do this, call _/UpdateAccountConnectorOAuth_ with a one-time sign-in token.

</div>

</section>
