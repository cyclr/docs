---
title: Zoom Authentication
sidebar: cyclr_sidebar
permalink: zoom-connector
tags: [connector]
---

## Partner Setup

First, [login](https://zoom.us/signin) to your Zoom account.

#### Retrieving OAuth2 Details

*   Navigate to the [Zoom Marketplace](https://marketplace.zoom.us/develop/create).
*   Click on "OAuth" as the new app type.
*   Enter an appropriate name, and the app type is "Account-level app". Do not publish the app to the Marketplace. Click "Create".
*   Note down the **Client ID** and **Client Secret**.
*   Enter a redirect URL (https://[Your Cyclr Service Domain]/connector/callback) and whitelist URL (will be the same as the redirect URL) for your app.
*   Fill out the rest of the information appropriately. Set the scopes according to your use case of the API. Scope details can be found [here](https://marketplace.zoom.us/docs/guides/auth/oauth/oauth-scopes).

### Cyclr Setup

Setup your Zoom App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Zoom**
*   Click the **Setup** button

Enter the following values:

**Client ID**:  The client ID that we retrieved from the app that we made.

**Client Secret**:  The secret that we retrieved from the app that we made.


Your Zoom Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
