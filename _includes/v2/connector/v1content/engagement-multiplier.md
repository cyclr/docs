
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

The Engagement Multiplier connector is authenticated with OAuth2.0.

The required credentials are `Client ID` and `Client Secret`

1. Login to your Engagement Multiplier *Developer* account [here](http://em.envisionitmedia.com)

2. Go to *Integrations* > *API Clients* on the dashboard menu

   ![engagement multiplier interface](./images/engage_multi_1.png)

3. If you have a client enabled you will see the *Client ID*, *Name* and *Secret*. If not, *Create New Client*

   ![engagement multiplier interface](./images/engage_multi_2.png)

4. Enter your application's *Name* and for *Redirect URL* enter `https://{service domain}/connector/callback`

   > Replace {service domain} with your service domain, which is available in your Cyclr console under Settings > General Settings > Service Domain

   ![engagement multiplier interface](./images/engage_multi_3.png)

</div>

</section>

<section class="setup partner" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. Go to the Engagement Multiplier connector

   > Cyclr Console > Connectors > Connector Library > Engagement Multiplier

2. Click *Setup* on the Edit Connector interface

3. Enter the `Client ID` and `Client Secret` from your Engagement Multiplier *Developer* account

4. Click *Next*

5. Click *Sign In*

   ![engagement multiplier interface](./images/engage_multi_5.png)

6. Login to your Engagement Multiplier account with your Engagement Multiplier *User* account credentials

7. Click *Authorize* when prompted to allow or deny access to your account

   ![engagement multiplier interface](./images/engage_multi_4.png)

A successful authorization redirects you to Cyclr. The connector is now authenticated and ready to use.

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

If you are unable to locate your `Company ID`, you can use the method *Get Authenticated User*. It retrieves  the `Company ID` for the currently authenticated user.

</div>

</section>
