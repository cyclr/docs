---
title: DevicePilot information
sidebar: cyclr_sidebar
permalink: devicepilot-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Update and Insert device data

DevicePilot allows users to submit any data that is relevant to their devices. Because of this, Cyclr lets you choose your own fields that you want to submit. To choose your own field, you can create request **custom fields**.

</section>
<section class="card">

## Webhook Support

DevicePilot manages webhooks, so you need to set webhooks up through the DevicePilot admin portal:

1. In Cyclr, add the webhook method that's present in the connector. 
2. Select **Step setup** and note the webhook URL. It looks similar to `https://my.cyclr.com/api/webhook/ABC123`, depending on your region.
3. Navigate to the [connections](https://app.devicepilot.com/#/connect/manage) area in DevicePilot.
4. Select **Get Started** underneath the "Webhooks" category to create a new webhook.
5. Enter in the appropriate details:
    * Set the URL to the Cyclr webhook URL (see step 1).
    * Set Method to `POST`.
    * In the header, set `Authorization` to the API key that you entered in connector setup, and `content-type` is set to `application/json`.
    * The Body represents the response and data.
The webhook setup should look similar to the following:<br>
![Example webhook setup](./images/devicepilot-webhook.png)

6. Save the changes.

You can find more information on the [DevicePilot help page](https://help.devicepilot.com/webhook).

</section>
