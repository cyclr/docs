---
title: Notion Authentication
sidebar: cyclr_sidebar
permalink: notion-connector
tags: [connector]
---

## Partner Setup

First, login to your existing Notion account .

### Creating OAuth2 Application


*   Go to [My Integrations](https://www.notion.so/my-integrations) within Notion
*   Click "New Integration".
    *   More details on how to create an app can be found [here](https://developers.notion.com/docs/authorization#authorizing-public-integrations).
*   Enter a name and select the workspace you wish to integrate with
*   *   Click Submit.
*   Select Public Integration Option
*   Enter the Redirect URL (https://[Your Cyclr Service Domain]/connector/callback) for your app.
*   You will be asked for other details such as privacy policy support email etc.
*   Click on "Save" 
*   Copy and store securely bothe the **OAuth client ID**, and **OAuth client secret**

### Cyclr Setup

Setup your Notion Connector within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Search for **Notion**
*   Click the **Setup** button

Enter the following values:

**Client ID**:  The client ID that we retrieved from the app that you made.

**Client Secret**:  The secret that we retrieved from the app that you made.

Your Notion Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
