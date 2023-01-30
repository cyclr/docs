---
title: Facebook Messenger information
sidebar: cyclr_sidebar
permalink: facebook-messenger-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Webhook setup

Facebook Messenger webhooks utilize a single webhook URL, so you need to configure your Facebook application:

1. In your Cyclr console, go to **Connectors** > **Application Connector Library** > **Facebook Messenger** > **Setup**
2. Set the **Verify Token** to an alphanumeric string of your choice. Make a note of the string.
3. Copy the **Webhook URL** to your clipboard.
4. Navigate to the [Facebook Developers App Dashboard](https://developers.facebook.com/apps), and select the application you use with Cyclr.
5. Within the application, navigate to **Products** > **Messenger** > **Settings**.
6. Scroll down to the Webhook section.
7. Select the **Edit Callback URL** button to open a dialog.
8. Paste the **Webhook URL** from your clipboard, and enter the **Verify Token** you noted down in step 2.
9. Select **Verify and Save**, so Facebook verifies the endpoint.

</section>
<section class="card">

## Use webhooks

1. Drag the **Webhook** step from the sidebar into the Builder.
2. Open the Webhook **settings**, and enter the Page ID.
3. Connect the Webhook to another step.
4. Select **Run** to start the Cycle. The step contacts Facebook and subscribes the page to message Webhooks.

If you want to remove the Webhook and cancel the Page subscription, stop the Cycle, and **Delete** the Webhook step. The deletion of the Webhook step triggers Cyclr to contact Facebook and unsubscribe the Page from message Webhooks.

</section>
<section class="card">

## Webhook field configuration

The body of the incoming message varies depending on the message type received, so only a set of core fields are mapped by default.
Use the **Edit Connector** page to add the fields you want to use. For more information, see the Facebook documentation on [message events](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages).

</section>
<section class="card">

## Add new Facebook pages

To use a new Facebook page with an authenticated connector, you need to reauthenticate with Facebook. During the OAuth flow, use the **Edit Settings** button to select the new page, and grant the permissions.

</section>
<section class="card">

## Roles and test users

If your application isn't approved by Facebook, you need to set the users that can interact with the application from the developer console. To create a test user, select the menu on the left side of the screen, and select **Roles** > **Test Users**.

</section>
<section class="card">

## Official Facebook Documentation

[https://developers.facebook.com/docs/apps/register](https://developers.facebook.com/docs/apps/register)

</section>
