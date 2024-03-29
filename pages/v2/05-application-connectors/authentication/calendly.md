---
title: Calendly Authentication
sidebar: cyclr_sidebar
permalink: calendly-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Calendly setup

Before you install the Calendly connector into a Cyclr account, you need to do the following:

1. [Register a Calendly OAuth application](#register-a-calendly-oauth-application).
2. [Get a **client ID** and **client secret**](#get-a-client-id-and-client-secret) for your Calendly OAuth application.

<a href="register-a-calendly-oauth-application">

### Register a Calendly OAuth application

To see how to register an OAuth application, see [Calendly's guide](https://help.klaviyo.com/hc/en-us/articles/7423954176283) under the **Register and authenticate your OAuth application** heading. 

On the **Register your public application** form, the **OAuth redirect URL** field is the callback URL of your Cyclr service domain. For example, `https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback`.

<a href="get-a-client-id-and-client-secret">

### Get a client ID and client secret

You receive a client ID and client secret via email when you [register a Calendly OAuth application](#register-a-calendly-oauth-application).  This might take up to 24 hours. Contact Calendly support if you don't receive these values.


</section>
<section class="card">
## Cyclr console setup

To set up your Calendly connector, go to your Cyclr console:

1. Select **Connectors** > **Application Connector Library** at the top of the page.
2. Use the search box to find the **Calendly** connector.
3. Select the **Setup Required** icon.
4. Enter the values below:

    | Value             | Description                                 |
    | ----------------- | ------------------------------------------- |
    | **Client ID**     | The client ID of your Calendly account.     |
    | **Client Secret** | The client secret of your Calendly account. |

5. Select **Save Changes**.

> **Note**: To use different settings for different accounts, leave the value blank. This means Cyclr asks you to enter the value when you install the connector into an account.

</section>
