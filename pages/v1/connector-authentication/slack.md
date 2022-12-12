---
title: Slack Authentication
sidebar: cyclr_sidebar
permalink: slack
tags: [connector]
---

## Partner Setup ##

Slack uses OAuth 2.0 for authentication so you must [register your Cyclr Partner with Slack](https://api.slack.com/apps) to obtain your **Client ID** and **Client Secret** values.

From [https://api.slack.com/apps](https://api.slack.com/apps) click the **Create an App** button then enter:
*  **App Name** - a name for your App.  This will be shown on-screen when users install the Slack Connector, and also appear as the username when you post to Slack.
*  **Development Slack Workspace** - which Slack Workspace your App belongs to.  This just gives it a "home" and doesn't prevent it from being installed in other people's workspaces.

![Slack - Create an App](./images/slack-create-an-app.png)


After you've created your App, set the **Redirect URLs** under the **Add features and functionality** section's **Permissions** button:

![Slack - Permissions](./images/slack-permissions.png)


**Redirect URL**: you must add a callback URL to allow Intercom to be used in your Cyclr Console and its accounts.

The URL is:

*   {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}

Your Cyclr Partner **Service Domain** can be found in your Cyclr Console under Settings > General Settings.

Once added, they should look similar to these:

![Slack - Redirect URLs](./images/slack-redirect-urls.png)

**Requesting Scopes**:

Scroll down to the Scopes section and click to **Add an OAuth Scope**. Scopes can be modified at a later stage by navigating to the **OAuth & Permissions** sidebar.

For example, try adding the chat:write scope to your Bot Token. It'll allow your app to post messages! While you're at it, add the channels:read scope so your app can gain knowledge about public Slack channels.

If you're confused about the difference between adding a Bot Token Scope or a User Token Scope, worry not:

*Add scopes to your Bot Token, not your User Token*.

One notable exception to that rule is if you need to act as a specific user (for example, posting messages on behalf of a user, or setting a user's status). In that situation, you'll need a User Token.


Now you can retrieve your **Client ID** and **Client Secret** values by going to **Basic Information** on the left then scrolling down to **App Credentials**:

![Slack - App Credentials](./images/slack-app-credentials.png)


Finally, in your **Cyclr Console** go to the **Connectors** menu, then **Connector Library** and set those values from the padlock button next to Slack.

## Webhook setup

The Slack Connector has webhooks for subscribing to **File Created** and **File Shared** Slack events. These are both able to use Cyclr's partner-level single URL webhook target. To implement either of these into your cycles, do the following:

#### Retrieve the partner level webhook URL

In your Cyclr console:

1. Open your Cyclr console and log into the correct partner account.
2. Click **Connectors** > **Application Connector Library** in the top menu bar.
3. Use the search bar to find the Slack Connector.
4. Click the **Setup Required** padlock icon.
5. Make a note of the **Webhook URL**. This is your partner-level webhook URL for the Slack Connector.

#### Setup events in Slack

On the [Slack API App page](https://api.slack.com/apps/) for your Slack App. You can find Slack's documentation on this [here](https://api.slack.com/apis/connections/events-api):

1. Click **Event Subscriptions** in the left-hand menu.
2. Set **Enable Events** to **On**.
3. Enter the **webhook URL** found in the previous section in the **Request URL** field. You will see a green **Verified** if the URL is valid.
4. Click **Subscribe to bot events** to expand out the section.
5. Click **Add Bot User Event**.
6. Enter the event name corresponding to the webhook you will use. You can add both at once if needed:
-   **file_created** for the **File Created** webhook.
-   **file_shared** for the **File Shared** webhook.

7. Click **Save Changes** at the bottom of the page. Any scopes missing from your Slack App will automatically be added based on the events you entered.

#### Setup the webhook in a cycle

In the cycle where you want to add the webhook:

1. Drag the **File Created** or **File Shared** Slack webhook onto the cycle builder and connect as normal.

You do not need to use the webhook URL from the webhook step as all requests will arrive there via the partner-level webhook URL you set up.
