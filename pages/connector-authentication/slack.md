---
title: Slack Authentication
sidebar: cyclr_sidebar
permalink: slack
tags: [connector]
---

## Partner Setup ##

Slack uses OAuth 2.0 for authentication so you must [register your Cyclr Partner with Slack](https://api.slack.com/apps) to obtain your **Client ID** and **Client Secret** values.

From [https://api.slack.com/apps](https://api.slack.com/apps) click the **Create an App** button then enter:
*  **App Name** - a name for your App.  This will be shown on-screen when users install the Slack Connector.
*  **Development Slack Workspace** - which Slack Workspace your App belongs to.  This just gives it a "home" and doesn't prevent it from being installed in other people's workspaces.

![Slack - Create an App](./images/slack-create-an-app.png)


After you've created your App, set the **Redirect URLs** under the **Add features and functionality** section's **Permissions** button:

![Slack - Permissions](./images/slack-permissions.png)


**Redirect URL**: you must add a callback URL to allow Intercom to be used in your Cyclr Console and it's accounts.

The URL is:

*   {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}

Your Cyclr Partner **Service Domain** can be found in your Cyclr Console under Settings > Integration Settings.

Once added, they should look similar to these:

![Slack - Redirect URLs](./images/slack-redirect-urls.png)


Now you can retrieve your **Client ID** and **Client Secret** values by going to **Basic Information** on the left then scrolling down to **App Credentials**:

![Slack - App Credentials](./images/slack-app-credentials.png)


Finally, in your **Cyclr Console** go to the **Connectors** menu, then **Connector Library** and set those values from the padlock button next to Slack.
