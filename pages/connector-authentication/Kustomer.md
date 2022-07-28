---
title: Kustomer Authentication
sidebar: cyclr_sidebar
permalink: Kustomer-connector
tags: [connector]
---

### Partner Setup

Before setting up the **Kustomer** Connector, you will need to get an **API key**.

This can be obtained in your Kustomer account webpage, from the **API Keys** settings page. You can access this page by going to **Settings** and selecting **Security > API Keys**.

When creating a new key, you can select an API role and apply a descriptive label to the key. Roles are useful to limit the operations requests using that key can perform.

### Cyclr Setup

Setup your Kustomer App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Kustomer**
*   Click the **Setup** button

Enter the following values:

* **API key**

Sign in to Kustomer and allow Cyclr Connector to connect to it.

Your Kustomer Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

### Outbound Webhook Setup

** You can have up to 5 outbound user-created webhooks set up at any time in your Kustomer organization.

** To create an outbound webhook:

Select **Settings** and go to **Platform > Outbound Webhooks**.

Select **Add Outbound Webhook**.

Enter a name for the webhook, which is how you'll identify this hook throughout the Kustomer platform.

Then, fill in the **Destination URL**. This is the inbound webhook URL for the application that will be receiving data from Kustomer.

Next, choose which Kustomer events trigger the webhook to send data. Use the **Webhook Trigger Events** to set any number of the following Kustomer events:

** Conversation Create
** Conversation Update
** Customer Create
** Customer Update
** Message Create
** Message Update
** Team Create
** Team Update
** User Create
** User Update

Select **Save Changes** in the bottom toolbar.

For more information go to https://help.kustomer.com/outbound-webhooks-rkUQvela8
