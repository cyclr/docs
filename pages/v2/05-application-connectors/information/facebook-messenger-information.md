---
title: Facebook Messenger Information
sidebar: cyclr_sidebar
permalink: facebook-messenger-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
## Webhook Setup

Facebook Messenger webhooks utilise a single webhook URL, this requires some configuration inside your Facebook application.

1. Navigate to Cyclr Console > Connectors > Application Connector Library > Facebook Messenger > Setup
2. Set the **Verify Token** to an alphanumeric string of your choice. Make a note of this.
3. Copy the **Webhook URL** to your clipboard.
4. Navigate to the [Facebook Developers App Dashboard](https://developers.facebook.com/apps), and select the application you use with Cyclr.
5. Within this application, navigate to Products > Messenger > Settings.
6. Scroll down to the Webhook section.
7. Click the **Edit Callback URL** button, a dialog will open.
8. Paste the **Webhook URL** from your clipboard, and enter the **Verify Token** you took note of earlier.
9. Click **Verify and Save**, Facebook will then verify the endpoint.

Your application is now set up for Webhooks using Cyclr.

</section>
<section class="card">
## Webhook Usage

1. Drag the Webhook step from the sidebar into the Builder.
2. Open the Webhook settings, and enter the Page ID.
3. Connect the Webhook to another step.
4. Click **Run** to start the Cycle. This will contact Facebook and subscribe this page to message Webhooks.

If you wish to remove the Webhook and cancel the Page subscription, you must stop the Cycle, and **Delete** the Webhook step. 
The deletion of the Webhook step will trigger Cyclr to contact Facebook and unsubscribe the Page from message Webhooks.

</section>
<section class="card">
## Webhook Field Configuration

The body of the incoming message will vary depending on the message type received; for this reason, only a set of core fields are mapped by default.
Please use the Edit Connector page to add the fields you wish to use. Documentation for Facebook message events is available [here](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages).

</section>
<section class="card">
## Adding New Facebook Pages

To use a new Facebook page with an already authenticated connector, you will need to reauthenticate with Facebook.
During the OAuth flow, use the **Edit Settings** button to select the new page, and grant permission.

</section>
<section class="card">
## Roles & Test Users

If your application has not been approved by Facebook, the only users that will be able to interact with it must be set within the developer console. To create a test user, click the menu on the left, and select ``Roles`` > ``Test Users``.

</section>
<section class="card">
## Official Facebook Documentation

[https://developers.facebook.com/docs/apps/register](https://developers.facebook.com/docs/apps/register)

</section>
