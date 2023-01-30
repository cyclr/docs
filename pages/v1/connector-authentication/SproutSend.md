---
title: Sprout Send Authentication
sidebar: cyclr_sidebar
permalink: SproutSend-connector
tags: [connector]
---

## Partner Setup

First, login to your existing Sprout Send account or [sign up for one.](https://myguestlist.com/mgl/contact_forms/covid-sprout/get_started.php)

#### Retrieving OAuth2 Details

*   [Login](https://app.sproutsend.com/) to your Sprout Send Account.
*   Click Create App.
*   Enter a name and Callback URL (https://[Your Cyclr Service Domain]/connector/callback) for your app. 
*   Click Save.
*   Note the **client ID** and **secret**.

### Cyclr Setup

Setup your Sprout Send App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Sprout Send**
*   Click the **Setup** button

Enter the following values:

**Client ID**:  The client ID that we retrieved from the app that we made.

**Client Secret**:  The secret that we retrieved from the app that we made.


Your Sprout Send Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
