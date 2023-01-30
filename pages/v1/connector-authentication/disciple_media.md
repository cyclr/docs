---
title: Disciple Media Authentication
sidebar: cyclr_sidebar
permalink: disciple-media-connector
tags: [connector]
---

## Partner Setup

First, login to your existing Disciple Media account or [sign up for one.](https://www.disciplemedia.com/pricing/)


#### Retrieving OAuth2 Details

*   [Login](https://console.disciplemedia.com/users/log_in) to your Disciple Media Account.
*   Click Integrations in the side menu.
*   You will be able to reveal the API Key used for your app.
*   Note the **API Key**.

### Cyclr Setup

Setup Disciple Media within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Disciple Media**
*   Click the **Setup** button

Enter the following values:

**API Key**:  The API Key that we retrieved from the webservice.

**Domain**:  The domain for your Disciple Media app.


Your Disciple Media Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

### Using Webhooks

Webhook requests undergo a validation check before being accepted. Make sure you have provided a secret for the webhook in Disciple Media (https://<span>{AccountSubdomain}.</span>disciplemedia.com/admin/webhooks/) and entered that secret at connector setup. If no secret is provided or the secret does not match the webhook will be rejected.

![disciple webhook setup](./images/disciple_webhook_1.png)

![connector setup](./images/disciple_webhook_2.png)
