---
title: General settings
sidebar: cyclr_sidebar
permalink: console-general-settings
tags: [cyclr-config]

menus:
    cyclr-configuration:
        title: Appearance settings
        identifier: console-general-settings
        weight: 1
---

| Option | Documentation |
| --- | --- |
| Application Icon | Your application icon. Displayed in the navigation bar if Cyclr is used as a white-labelled service.  40x40 pixel PNG image with a transparent background. |
| Sign In Logo | Logo to use on the User Login Page.  PNG image, suggested dimensions of 300x100 pixels. |
| Fav Icon | Web browser "favicon" to use in Cyclr. |
| Application Display Name | Display name for your application. |
| Cycle Noun | Noun for calling cycles in the UI. Default to "Cycle". |
| Cycle Create Verb (Launch) | Verb for creating cycles in LAUNCH and Marketplace. Default to "Create". |
| Service Domain | To set up a custom domain please message our support team. |
| Enable Anonymous Accounts | Allows end users to open cycle and connector seeds links without having a Cyclr account. |
| Enable Beta/Planned Connectors | Allows beta and planned (coming soon) connectors to be displayed in the connector list.|
| Enable Custom Connectors | Allows end user accounts to create their own custom connectors. |
| Enable Cycle Sharing | Allows sharing of cycles across end user accounts. |
| Enable Notification Emails | To enable notification emails please message our support team.
| Enable Notification Webhook | Makes an HTTP call when there is an issue with an account’s cycles. https://docs.cyclr.com/notifications |
|	Notification Webhook URL | URL to use when Cyclr sends notifications for cycle issues. |
| Enable Transaction Error Webhook | Makes an HTTP call when an error occurs in a transaction. https://docs.cyclr.com/notifications |
| Enable User Login Page | Allows end users to log into to Cyclr by username and password. |
| Enable Cycle Form View | Sets the default cycle setup to be a linear form. The drag and drop builder can be toggled by going to the Advanced view. |
| Enable iframe Embedding | Allows Cyclr to be embedded in an iframe. This will remove the X-Frame-Options header and set "SameSite=None; Secure" to all cookies. Your hosting webpage must be served over HTTPS. **Note that this will reduce the visible options in the Settings menu presented within Accounts**. |
| Help Link Type | Determines how to show Cyclr help links; show Cyclr help links, hide Cyclr help Links or use custom help links. Default to "Show Cyclr help links". |
| Custom Help Link URL | URL to use for all help links when Help Link Type is set to "Use custom help links". |
| Custom Help Email Address | Email address to use for all helpdesk mailto links when Help Link Type is set to "Use custom help links". |
| Host Source Whitelist | A comma separated list of host sources that can embed your Cyclr application using iframe. This value will be present in the Content-Security-Policy (CSP) header. |
| Account Concurrent Transaction Limit | Maximum concurrent transactions allowed for an end user account. |
