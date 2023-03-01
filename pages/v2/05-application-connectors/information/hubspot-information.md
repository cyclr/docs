---
title: HubSpot information
sidebar: cyclr_sidebar
permalink: hubspot-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Webhook setup

Hubspot webhooks utilize a single webhook URL, which requires some configuration of your Hubspot application.

1.  Navigate to your Cyclr Console > **Connectors** > **Application Connector Library** > **Hubspot** > **Setup**.

2.  Copy the Webhook URL to your clipboard. For example, `https://<yourservicedomain>/api/partnerwebhook/xxxxxx`.
    > **Note**: Don't use the webhook URL from the builder. Make sure to get the URL from under the partner console.

To send webhooks, you need to setup the Hubspot application:

1.  Enter the URL.
2.  Alter scopes to select the events to subscribe to.
3.  Activate the events.

### Enter the URL

1.  Navigate to the Hubspot Developers App [Dashboard](https://app.hubspot.com/developer), and select the application you use with Cyclr.
2.  Within the application, navigate to **Webhooks**.
3.  Paste the **Webhook URL** from your clipboard, into the **target URL**.
4.  Select **Save** (at the bottom of the screen).

### Scopes

To set up your subscriptions, you might need to alter the scopes of the Hubspot application to allow the events to send. For more information, see Hubspot's [documentation on webhook scopes](https://developers.hubspot.com/docs/api/webhooks#scopes).

1. Select **Create Subscription**.
2. Choose the objects and events that you wish to send to Cyclr.
3. Select **Subscribe**.

### Activate the events

1.  Under event subscriptions, hover over the line with your mouse to show the **view subscriptions** button and select the button.
2.  Hover over the line with your mouse to show the **activate** button, and select this button to activate the sending of the webhook.

</section>
<section class="card">

## Add webhooks to your cycle or template

1.  Drag the Webhook step from the sidebar into the builder.
2.  Connect the Webhook to another step.
3.  Select **Run** to start the cycle.

</section>
<section class="card">

## Use custom objects

### Create a custom object schema

To create custom object categories in the HubSpot connector, you need a custom object schema. HubSpot allows you to create custom object schema on the [Custom objects page](https://developers.hubspot.com/docs/api/crm/crm-custom-objects) of their documentation.  You can create custom object schema on the **Object schema** tab under **Create a new schema**.

### Create a custom object method category

You can also create a custom object method category.

1. Go to the HubSpot connector Settings page:
   *  For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **HubSpot** > **Edit Connector**.
   *  For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **HubSpot** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Custom Objects** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Use the drop-down menu and select the custom object schema to use for the custom object method category.
5. Select **Copy**.

The new category then uses the custom object schema selected for all methods.

</section>
