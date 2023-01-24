---
title: Eventbrite Authentication
sidebar: cyclr_sidebar
permalink: eventbrite-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
# Eventbrite setup

You need the following information to set up the Eventbrite connector:

1. An Eventbrite API key associated with your account.
2. An Eventbrite client secret associated with your account.

### Creating an API key and client secret in Eventbrite

Create an API key and client secret on the [API keys page](https://www.eventbrite.com/account-settings/apps) of your Eventbrite account. From the API keys page, do the following:

1. Select **Create API Key**.
2. Enter a **First Name** and **Last Name** to associate with the keys.
3. Enter an **Application URL**, this can be any URL but is required.
4. Enter the **OAuth Redirect URI** of your Cyclr account. This has the following format:
    `{% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}`
5. Enter an **Application Name** and **Description**, these can be anything but are required.
6. Confirm the **I have read the terms of use and agree to their terms** checkbox.
7. Select **Create Key**.
8. Select the new entry in the API keys list, this will have the same name as the application name entered in step 5.
9. Make note of the **API key** and **Client secret** below the expanded entry.


</section>
<section class="card">
## Cyclr setup

To set up your Eventbrite connector within your Cyclr console:

1. Go to the **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the Eventbrite connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:
    - **Client ID**: The API key of your Eventbrite account.
    - **Client Secret**: The client secret of your Eventbrite account.
6. Select **Save Changes**.

Your Eventbrite connector is now set up! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.


</section>
