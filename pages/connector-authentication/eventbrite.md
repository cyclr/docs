---
title: Eventbrite Authentication
sidebar: cyclr_sidebar
permalink: eventbrite-connector
tags: [connector]
---

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
    ```html
    https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback
    ```
5. Enter an **Application Name** and **Description**, these can be anything but are required.
6. Confirm the **I have read the terms of use and agree to their terms** checkbox.
7. Select **Create Key**.
8. Select the new entry in the API keys list, this will have the same name as the application name entered in step 5.
9. Make note of the **API key** and **Client secret** below the expanded entry.

# Cyclr setup

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

# Event custom objects

The Eventbrite connector uses Cyclr custom objects to make methods dynamic based on an event ID. Each event custom object requires its corresponding event ID to function. This enables custom fields to be automatically mapped for each event custom object created.

### Find the event ID

You need an event ID to set up a custom object. To find a specific event ID:

1. Log into your Eventbrite account.
2. In the top navigation bar, mouse over the account name and select **Manage my events**.
3. Select the event you want to create a custom object for.
4. The URL to the page of this event contains the event ID required to set up a custom object in the form `?eid=<event ID>`. For example, if the URL of an event is `https://www.eventbrite.co.uk/myevent?eid=328737431507` then the module name is `328737431507`.

### Set up a custom object

When you set up a custom object it creates a new method category with the parameters you enter. To set up a custom object:

1. Go to the Eventbrite connector **Settings** page:
    - For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **Eventbrite** > **Edit Connector**.
    - For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **Eventbrite** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Events (custom object)** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Enter the event ID into **Specify object name**.
5. Select **Copy**.

### Change custom object display name

To change the display name of a custom object method category:

1. Expand the method category by selecting the method category name.
2. Select the **Edit this Custom Object Category** icon.
3. Move the **Object Name** field to the **Object Value** field.
4. Change the **Object Name** field as required. This does not require a specific format.
5. Select **Save**.
