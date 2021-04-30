---
title: Stripe (OAuth) Authentication
sidebar: cyclr_sidebar
permalink: stripe-oauth-connector
tags: [connector]
---

## Partner Setup

#### Retrieving Client ID
* Navigate to connect settings in the dashboard: https://dashboard.stripe.com/settings/applications.
* Add your Cyclr redirect URL: https://``Your Service Domain``/connector/callback
* Tick "OAuth for Standard Accounts".
* Note down the generated Client ID.

#### Retrieving API Key
* Navigate to the API settings page in the dashboard: https://dashboard.stripe.com/apikeys.
* Create a new secret key and note it down.

### Cyclr Setup

Setup your ConnectWise Manage App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Stripe (OAuth)**
*   Click the **Setup** button

Enter the following values:

**Client ID**: Retrieved from the above steps.

**Client Secret**: Leave this empty.

**API Key**: Retrieved from the above steps.


Your Stripe (OAuth) Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
