---
title: Marketplace webhook callback
sidebar: cyclr_sidebar
permalink: marketplace-webhook
tags: [marketplaces]
menus:
    marketplace:
        title: Marketplace webhook callback
        identifier: marketplace-webhook
        toggleonly: menutoggleonly
        weight: 6
---
{::options parse_block_html="true" /}
<section class="card">

When you integrate with a Cyclr Marketplace, you can specify a Webhook URL for Cyclr to send notifications to.

1. In the Cyclr Console, select **Embedding** > **Marketplace** and select the **Settings** cog icon. 
2. Enter the **Marketplace Notification URL**.

</section>
<section class="card">

## Examples

### Installed payload 

```
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

### Uninstalled payload

```
{
    "Status": "uninstalled",
    "AccountId": "00000000-0000-0000-0000-000000000000",
    "AccountApiId": "ExampleAccount",
    "MarketplaceIntegrationPackageId": 1234
}
```

### Started payload

```
{
    "Status": "started",
    "AccountId": "00000000-0000-0000-0000-000000000000",
    "AccountApiId": "ExampleAccount",
    "MarketplaceIntegrationPackageId": 1234
}
```

### Stopped payload

``
{
    "Status": "stopped",
    "AccountId": "00000000-0000-0000-0000-000000000000",
    "AccountApiId": "ExampleAccount",
    "MarketplaceIntegrationPackageId": 1234
}
```