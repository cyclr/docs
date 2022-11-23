---
title: Calendly Connector Guide
sidebar: cyclr_sidebar
permalink: calendly-connector
tags: [connector]
---

## Setup

To authenticate the Calendly connector you first need to register an OAuth app.

1. Go to <https://calendly.com/integrations/api_webhooks>

2. Under OAuth click 'Register now'

   ![calendly oauth setup](./images/calendly_1.png)

3. Follow the steps on screen. When prompted for a redirect URL enter https://{Your Cyclr service domain e.g. <span>app-h.cyclr.</span>com}/connector/callback

4. Once you have completed your app registration you will receive your authentication credentials via LastPass. For this reason it is important that the email address you register for this app is the same as that of your LastPass account

### Connector Setup

Once you have your OAuth credentials:

1. Locate the Calendly connector

   > Cyclr Console > Connectors > Connector Library > Calendly

2. From the Edit Connector interface click 'Setup'

3. Enter your Client ID and Client Secret, click 'Next'

4. Click 'Sign In' which will redirect you to a Calendly login page where you should log in with your google account

> Note: If you are already logged into Calendly you might not be prompted to log in at this point. This is due to the session cookie your browser stores

You will be redirected to Cyclr where the connector is now authenticated and ready to use.
