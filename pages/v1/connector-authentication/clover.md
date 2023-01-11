---
title: Clover Authentication
sidebar: cyclr_sidebar
permalink: clover-connector
tags: [connector]
---

# Clover #

This guide is for setting up and installing the [Clover](https://cyclr.com/integrate/clover) connector.

#### Setup in Clover

Go to [clover.com/developers](https://www.clover.com/developers/) and create a new application.  
In the new application go to Settings and:

*   Update the Web Configuration setting Site URL to be your Cyclr Service Domain. Available from Cyclr Console > Settings > General Settings
*   Update the permissions setting checking everything other than "Process Credit Cards"
*   The App ID is the Client ID and the App Secret is the Client Secret.  Copy them as they are needed later.

#### Setup in Cyclr

If you don't need to use webhooks, login to your Cyclr Console and in the top menu go to Connectors > Connector Library. Find the Clover connector in the list and click its Setup button.

*   Set the Client ID as the App ID
*   Set the Client Secret as the App Secret

#### Install/Authenticate a connector

*   Enter the domain for Clover, either US or Europe
*   Click the sign in button
*   If required in the popup, install the application, then close the popup and the sign in button again.

#### Webhooks

Clover only supports sending webhooks to one webhook step per Clover application. To use webhooks with Cyclr you will need to create a separate Application in [clover.com/developers](https://www.clover.com/developers/) for each connector install.

Setup Webhook
-------------

1.  Add the Clover Event Webhook step to the cycle
2.  Run the cycle
3.  Copy the URL from the webhook step and paste it into the Clover setting for clover webhook
4.  Clover will now send a verification message to the webhook cycle, open the step data for the webhook and copy the verification code
5.  Paste the verification code into the Clover application to authenticate the URL.

![Clover Webhooks](./images/clover-webhooks-1.png)

Enable the subscriptions that you wish to receive events for.

**Each subscription requires the corresponding read permission. If you change permissions after a merchant installs your app, the permissions won't update for that merchant until the merchant uninstalls and reinstalls the app.**
