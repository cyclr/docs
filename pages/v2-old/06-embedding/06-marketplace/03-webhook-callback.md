---
title: Marketplace webhook callbacks
sidebar: cyclr_sidebar
permalink: marketplace-webhook-callback
tags: [marketplaces]
menus:
    marketplace:
        title: Marketplace webhook callbacks
        identifier: marketplace-webhook-callback
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">
When integrating with a Cyclr Marketplace you can specify a Webhook URL for Cyclr to send notifications to after your users have performed a Marketplace action.


</section>
<section class="card">
## Setting Marketplace URL

In the Cyclr Console goto Embedding > Marketplace and select the Settings Cog. Set the Marketplace Notification URL to the location where Cyclr should send notifications.

![Marketplace Notification URL](/images/marketplace_notification_url.png)


</section>
<section class="card">
## Installed Payload Example
```json
 {
    "Status": "installed",
    "AccountId": "00000000-0000-0000-0000-000000000000",
    "AccountApiId": "ExampleAccount",
    "MarketplaceIntegrationPackageId": 1234,
    "MarketplaceInstallDetails": [
        {
            "CycleId": "00000000-0000-0000-0000-000000000000",
            "CycleStatus": "Active",
            "Webhooks": [
                {
                    "Url": "https://example.com/api/webhook/abcdefg",
                    "StepName": "Example Webhook"
                }
            ],
            "TemplateId": "00000000-0000-0000-0000-000000000000",
            "TemplateReleaseId": "00000000-0000-0000-0000-000000000000"
        }
    ],
    "Errors" : ["Failed to start cycle"],
    "UserId": "00000000-0000-0000-0000-000000000000"
}
```


</section>
<section class="card">
## Uninstalled Payload Example
```json
 {
    "Status": "uninstalled",
    "AccountId": "00000000-0000-0000-0000-000000000000",
    "AccountApiId": "ExampleAccount",
    "MarketplaceIntegrationPackageId": 1234
}
```



</section>
<section class="card">
## Started Payload Example
```json
 {
    "Status": "started",
    "AccountId": "00000000-0000-0000-0000-000000000000",
    "AccountApiId": "ExampleAccount",
    "MarketplaceIntegrationPackageId": 1234
}
```



</section>
<section class="card">
## Stopped Payload Example
```json
 {
    "Status": "stopped",
    "AccountId": "00000000-0000-0000-0000-000000000000",
    "AccountApiId": "ExampleAccount",
    "MarketplaceIntegrationPackageId": 1234
}
```

</section>
