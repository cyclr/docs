---
title: Calendly Authentication
sidebar: cyclr_sidebar
permalink: calendly-connector
tags: [connector]
---

## Calendly setup

Before you install the Calendly connector into a Cyclr account:

1. [Register a Calendly OAuth application](#register-a-calendly-oauth-application).
2. [Get a **client ID** and **client secret**](#get-a-client-id-and-client-secret) for your Calendly OAuth application.

<a href="register-a-calendly-oauth-application">

### Register a Calendly OAuth application

You can find Calendly's guide on how to register an OAuth application [here](https://help.klaviyo.com/hc/en-us/articles/7423954176283) under the **Register and authenticate your OAuth application** heading. On the **Register your public application** form, the **OAuth redirect URL** field is the callback URL of your Cyclr service domain. For example, `https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback`.

<a href="get-a-client-id-and-client-secret">

### Get a client ID and client secret

You will receive a client ID and client secret via email after [registering a Calendly OAuth application](#register-a-calendly-oauth-application). Contact Calendly support if you do not receive these.

## Cyclr console setup

To set up your Calendly connector, go to your Cyclr console:

1. Select **Connectors** > **Application Connector Library** at the top of the page.
2. Use the search box to find the **Calendly** connector.
3. Select the **Setup Required** icon.
4. Enter the below values, a value here will allow you to use a different value for each installation within an account:

    | Value             | Description                                 |
    | ----------------- | ------------------------------------------- |
    | **Client ID**     | The client ID of your Calendly account.     |
    | **Client Secret** | The client secret of your Calendly account. |

5. Select **Save Changes**.

> **Note**: To use different settings for different accounts, leave the value blank. This means Cyclr asks you to enter the value when you install the connector into an account.
