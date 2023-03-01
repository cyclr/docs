---
title: Disciple Media Information
sidebar: cyclr_sidebar
permalink: disciple-media-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Use webhooks

Webhook requests undergo a validation check before being accepted. Make sure you provide a secret for the webhook in Disciple Media: `(`https://<span>{AccountSubdomain}.</span>disciplemedia.com/admin/webhooks/`. You also need to enter the secret at connector setup. If you don't provide the secret, or the secret doesn't match the webhook, it rejects the webhook.

![disciple webhook setup](./images/disciple_webhook_1.png)

![connector setup](./images/disciple_webhook_2.png)

</section>
