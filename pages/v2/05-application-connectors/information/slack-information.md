---
title: Slack Information
sidebar: cyclr_sidebar
permalink: slack-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">
## Webhook setup

The Slack Connector has webhooks so you can subscribe to **File Created** and **File Shared** Slack events. Both of these events can use Cyclr's partner-level single URL webhook target. You can implement either of these into your cycles.

### Retrieve the partner level webhook URL

In your Cyclr console:

1. Open your Cyclr console and log into the correct partner account.
2. Go to **Connectors** > **Application Connector Library** in the top menu bar.
3. Use the search bar to find the Slack Connector.
4. Click the **Setup Required** padlock icon.
5. Make a note of the **Webhook URL**. This is your partner-level webhook URL for the Slack Connector.

### Setup events in Slack

On the [Slack API App page](https://api.slack.com/apps/) for your Slack App. You can find Slack's documentation on this [here](https://api.slack.com/apis/connections/events-api):

1. Select **Event Subscriptions** in the left-hand menu.
2. Set **Enable Events** to **On**.
3. Enter the **webhook URL** found in the previous section in the **Request URL** field. You will see a green **Verified** if the URL is valid.
4. Select **Subscribe to bot events** to expand out the section.
5. Select **Add Bot User Event**.
6. Enter the event name corresponding to the webhook you will use. You can add both at once if needed:
  -   **file_created** for the **File Created** webhook.
  -   **file_shared** for the **File Shared** webhook.

7. Select **Save Changes** at the bottom of the page. Any scopes missing from your Slack App are automatically added based on the events you entered.

### Setup the webhook in a cycle

In the cycle where you want to add the webhook, drag the **File Created** or **File Shared** Slack webhook onto the cycle builder and connect as normal.

You do not need to use the webhook URL from the webhook step as all requests will arrive there via the partner-level webhook URL you set up.

</section>
