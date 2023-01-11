
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

To authenticate the Calendly connector, register an OAuth app.

1. Go to <https://calendly.com/integrations/api_webhooks>

2. Under OAuth click 'Register now'

   ![calendly oauth setup](./images/calendly_1.png)

3. Follow the steps on screen. When prompted for a redirect URL enter https://{Your Cyclr service domain e.g. <span>app-h.cyclr.</span>com}/connector/callback

4. Once you have completed your app registration you will receive your authentication credentials via LastPass. For this reason it is important that the email address you register for this app is the same as that of your LastPass account

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Once you have your OAuth credentials:

1. Locate the Calendly connector

   > Cyclr Console > Connectors > Connector Library > Calendly

2. From the Edit Connector interface click 'Setup'

3. Enter your Client ID and Client Secret, click 'Next'

4. Click 'Sign In' which will redirect you to a Calendly login page where you should log in with your google account

> Note: If you are already logged into Calendly you might not be prompted to log in at this point. This is due to the session cookie your browser stores

You will be redirected to Cyclr where the connector is now authenticated and ready to use.

</div>

</section>
