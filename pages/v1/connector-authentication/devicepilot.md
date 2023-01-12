---
title: DevicePilot Authentication
sidebar: cyclr_sidebar
permalink: devicepilot
tags: [connector]
---

# Device Pilot #

## Partner Setup ##

This document will explain what is needed to setup access to Device Pilot and install the connector.

### API Key Setup ###

1. Go to the token settings in DevicePilot and create a new token. Select "POST" as the token type and enter an appropriate name.
2. Temporarily display the token by clicking "Show token" and note this down. It should start with "TOKEN".

### Connector Setup ###

In the connector setup enter the full API Key in the API Key textbox.

### Updating and Inserting Device Data ###

DevicePilot allows users to submit any data that is relevant to their devices. Because of this, Cyclr lets you choose your own fields that you want to submit. This is done by creating request "custom fields".

### Webhook Support ###

Webhooks are managed by DevicePilot, so will need to be setup through the admin portal. To do this:

1. Add the webhook method that is present in the connector. Enter "Step setup" and note the webhook URL. It should look similar to "https://my.cyclr.com/api/webhook/ABC123" depending on your region.
2. Navigate to the [connections](https://app.devicepilot.com/#/connect/manage) area  in DevicePilot.
3. Create a new webhook by clicking "Get Started" underneath the "Webhooks" category.
4. Enter in the appropriate details.
    1. Set URL to the Cyclr webhook URL (see step 1).
    2. Set Method to "POST".
    3. Headers should contain "Authorization" which is set to the API key entered in during connector setup, and "content-type" is set to "application/json".
    4. Body represents the response and data.
5. The webhook setup should look similar to the following:<br>
![Example webhook setup](./images/devicepilot-webhook.png)
6. Save the changes.

More information can be seen on the [DevicePilot help page](https://help.devicepilot.com/webhook).
