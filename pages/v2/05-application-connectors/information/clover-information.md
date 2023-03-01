---
title: Clover information
sidebar: cyclr_sidebar
permalink: clover-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Webhooks

Clover only supports sending webhooks to one webhook step per Clover application. To use webhooks with Cyclr, you need to create a separate Application in [clover.com/developers](https://www.clover.com/developers/) for each connector install.

### Set up webhooks

1.  Add the **Clover Event Webhook** step to the cycle.
2.  Run the cycle.
3.  Copy the URL from the webhook step and paste it into the **Clover setting** for clover webhook
4.  Clover sends a verification message to the webhook cycle, so open the step data for the webhook and copy the **verification code**.
5.  Paste the **verification code** into the Clover application to authenticate the URL.

![Clover Webhooks](./images/clover-webhooks-1.png)

Enable the subscriptions that you want to receive events for.

**Note**: Each subscription requires a corresponding read permission. If you change permissions after a merchant installs your app, the permissions won't update for that merchant until the merchant uninstalls and reinstalls the app.

</section>
