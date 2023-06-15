---
title: General settings
sidebar: cyclr_sidebar
permalink: console-general-settings
tags: [cyclr-config]

menus:
    cyclr-configuration:
        title: General settings
        identifier: console-general-settings
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">

| **Option** | **Description** |
| --- | --- |
| Application Icon | Upload your application icon as a 40x40 pixel PNG image with a transparent background. The navigation displays this icon if you use Cyclr as a white-labelled service.  |
| Sign In Logo | Upload a logo as a PNG image to use on your user login page. A size of 300x100 pixels is ideal. |
| Fav Icon | Upload a web browser "favicon" to use for your Cyclr application. |
| Application Display Name | Enter a display name for your application. |
| Application User Agent | ??? |
| Cycle Noun | Enter a custom name for cycles within the application. The default noun is **Cycle**. |
| Cycle Create Verb (Launch) | Enter a custom verb for creating cycles in LAUNCH and Marketplaces. The default verb is **Create**. |
| Service Domain | View your Cyclr service domain. To set up a custom domain, contact the [support team](community-site#support-team). |
| Enable Beta/Planned Connectors| Select this toggle to allow the connector list to display beta and planned (coming soon) connectors.|
| Enable Custom Connectors | Select this toggle to allow your customer accounts to create their own custom connectors. |
| Enable Cycle Sharing | Select this toggle to allow you to [copy a cycle](copy-account-cycle) from an account as a template that you can use for multiple customer accounts. |
| Enable Notification Webhook | Select this toggle to allow the application to make a HTTP call when there's an issue with an account’s cycles. |
| Enable Transaction Error Webhook | Select this toggle to allow the application to make a HTTP call when an error occurs in a transaction. |
|	Transaction Error Webhook URL | Enter the URL you want to use when Cyclr sends notifications for cycle issues. |
| Transaction Error Webhook Include Warnings | ??? |
| Enable User Login Page | Select this toggle to allow your customers to log into to Cyclr by username and password. |
| Enable Cycle Form View | Select this toggle to set the default cycle setup to be a linear form. To toggle the drag and drop format in the builder, go to the **Advanced view**. |
| Enable iframe Embedding | Select this toggle so you can embed Cyclr in an iframe. This removes the X-Frame-Options header and sets `SameSite=None; Secure` to all cookies. To embed in an iframe, your hosting webpage must be served over HTTPS. **Note**: This reduces the visible options in the accounts settings menu. |
| Enable inline OAuth connector authentication | ??? |
| Help Link Type | Select an option from the dropdown to determine how to show Cyclr help links: **Show Cyclr help links**, **Hide Cyclr help links**, or **Use custom help links**. The default setting is **Show Cyclr help links**. |
| Host Source Whitelist | Enter a comma separated list of host sources that can embed your Cyclr application using iframe. This value is then present in the Content-Security-Policy (CSP) header. |
| Account Concurrent Transaction Limit | Enter a maximum concurrent transactions that you want to allow for your customer accounts. |

</section>
