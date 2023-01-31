---
title: Drift Authentication
sidebar: cyclr_sidebar
permalink: drift-connector
tags: [connector]
---

## Partner Setup

First you will need to create an oAuth application on the Drift [developer portal](https://dev.drift.com/apps)


#### Retrieving OAuth2 Details

*   Click Buiild Your App.
*   Enter an App Name
*   Click in Oauth & Scopes in the menu
*   Add Redirect URL - Enter a name and Callback URL (https://[Your Cyclr Service Domain]/connector/callback) for your app.
*   Select the required Drift Scopes based on the opreations you will be performing with your intergration
*   Copy Client ID and Secret ID


### Cyclr Setup

Setup your Drift Connector within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Search for  **Drift**
*   Click the **Setup** button

Enter the following values:

**Client ID**:  The client ID obtatined in above steps.

**Client Secret**:  The secret ID obtatined in above steps.


Your Drift Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
