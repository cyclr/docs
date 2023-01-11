---
title: Sage 50 Authentication
sidebar: cyclr_sidebar
permalink: sage50-connector
tags: [connector]
---

## Partner Setup

First, login to your existing Sage Developer account or [sign up for one.](https://developerselfservice.sageone.com/)

Also login to your existing Sage Business Cloud Accounting account or [sign up for a free trial.](https://www.sageone.com/?clear&filter=apiv3.1)

#### Retrieving OAuth2 Details

*   [Login](https://developerselfservice.sageone.com/) to your Sage Developer Account.
*   Click Create App.
    *   More details on how to create an app can be found [here](https://developer.sage.com/api/accounting/guides/client_app_registration/).
*   Enter a name and Callback URL (https://[Your Cyclr Service Domain]/connector/callback) for your app. You can optionally provide an alternative email address and homepage URL for your app, but this isn’t required at this stage.
*   Click Save.
*   Note the **client ID** and **secret**.

### Cyclr Setup

Setup your Scoro App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Sage 50**
*   Click the **Setup** button

Enter the following values:

**Client ID**:  The client ID that we retrieved from the app that we made.

**Client Secret**:  The secret that we retrieved from the app that we made.


Your Sage 50 Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
