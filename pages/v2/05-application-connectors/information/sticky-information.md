---
title: Sticky information
sidebar: cyclr_sidebar
permalink: sticky-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Webhook setup

Sticky webhooks utilize a single webhook URL. To use the webhooks, you need Sticky to configure your Sticky application. This means you need to provide Sticky with the URL to send webhook events to.

To find the webhook URL, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.
2. Search for the Sticky connector and select the **Authentication Setup** padlock icon.
3. Copy the **Webhook URL** and send this to Sticky.

> **Warning**: Do not use the Webhook URL that the Webhook step displays. Use the URL on the Sticky connector's **Authentication Setup** page.

### Add webhooks to your cycle or template

If you Sticky account has the correct webhook URL, you can add webhooks through the template builder:

1.  Drag the **Webhook** step from the sidebar into the builder.
2.  Connect the Webhook to another step.
3.  Select **Run** to start the cycle.

</section>