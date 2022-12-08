---
title: HubSpot Connector Guide
sidebar: cyclr_sidebar
permalink: hubspot-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
## HubSpot setup

To connect Cyclr with the HubSpot API, you need to create an app within HubSpot, as detailed below:

> **Note**: A Cyclr Partner can complete this once. Your client/customer doesn't need their own separate app within HubSpot.

1. Login to the HubSpot Developer Portal [here](https://app.hubspot.com/signup-v2/developers).
2. Follow the HubSpot [documentation](https://developers.hubspot.com/docs/faq/how-do-i-create-an-app-in-hubspot) to create an application.
3. The `Auth` tab shows a `Client ID` and `Client Secret`. Make a note of these to use in Cyclr's connector setup.
4. Get the redirect URL that creates the link between your Cyclr Console and HubSpot. The URL is shown on the page where you enter the Client ID and Client Secret, and has the form:
   `https://[Your Cyclr Service Domain]/connector/callback`
5. Set the scopes of your Hubspot App according to the method categories that you plan to use. You can find a list of scopes, and the permissions which they provide access to, [here](https://developers.hubspot.com/docs/api/working-with-oauth#scopes). By default, Hubspot installation in Cyclr requests the following scopes: `crm.objects.contacts.read`, `crm.objects.contacts.write`, `content`, `reports`, `e-commerce` & `forms`. You need to manually request any scopes beyond these during connector installation.

### Permissions

In order to use the Products and Line Items methods, you need to assign the user a [paid Sales Hub seat](https://knowledge.hubspot.com/articles/kcs_article/account/manage-sales-hub-and-service-hub-paid-users) within HubSpot.


</section>
<section class="card py-5 my-5">
## Cyclr setup

You can install the connector with the credentials obtained in the above steps:

| Field           | Description                                                                                                                                                                                                                                                                                                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client ID       | The client ID of your Hubspot OAuth app.                                                                                                                                                                                                                                                                                                                                      |
| Client Secret   | The secret of your Hubspot OAuth app.                                                                                                                                                                                                                                                                                                                                         |
| Scopes          | A space separated list of permissions that your Hubspot OAuth app needs access to. You need to enable these on your Hubspot OAuth app or connector authentication fails. By default, Cyclr will request the following scopes: `crm.objects.contacts.read` and `crm.objects.contacts.write`. Any scopes you enter here override the default scopes.                    |
| Optional Scopes | A space separated list of optional permissions that your Hubspot OAuth app needs access to. If you don't enable these on your Hubspot OAuth app, Cyclr doesn't request them and it can reduce functionality. By default, Cyclr requests the following optional scopes: `content`, `reports`, `e-commerce`, and `forms`. Any scopes you enter here override the default scopes. |

You are then prompted to log in, select your HubSpot, and authorize access to the connector.

### Account selection

When you authenticate the HubSpot connector and sign into HubSpot, it presents the user with the HubSpot **Choose an Account** screen.

To test, select your main HubSpot account instead of your developer account. To identify the main account, look for the account with items shown under the **PRODUCTS** heading.

In this example, that would be the "Cyclr" account:

![](./images/hubspot-choose-acct.png)


</section>
<section class="card py-5 my-5">
## Additional information

### Webhook setup

Hubspot webhooks utilise a single webhook URL, which requires some configuration of your Hubspot application.

1.  Navigate to your Cyclr Console > **Connectors** > **Application Connector Library** > **Hubspot** > **Setup**.

2.  Copy the Webhook URL to your clipboard. For example, `https://<yourservicedomain>/api/partnerwebhook/xxxxxx`.
    > **Note**: Don't use the webhook URL from the builder. Make sure to get the URL from under the partner console.

You need to setup the Hubspot application to send webhooks. This has three steps:

1.  Enter the URL.
2.  Alter scopes to select the events to subscribe to.
3.  Activate the events.

#### Enter the URL

1.  Navigate to the Hubspot Developers App [Dashboard](https://app.hubspot.com/developer), and select the application you use with Cyclr.
2.  Within this application, navigate to Webhooks.
3.  Paste the Webhook URL from your clipboard, into the **target URL**.
4.  Select **Save** (at the bottom of the screen).

#### Scopes

To set up your subscriptions, you might need to alter the scopes of the Hubspot application to allow the events to send. For more information, see Hubspot's [documentation on webhook scopes](https://developers.hubspot.com/docs/api/webhooks#scopes).

1. Select **Create Subscription**.
2. Choose the objects and events that you wish to send to Cyclr.
3. Select **Subscribe**.

#### Activate the events

1.  Under event subscriptions, hover over the line with your mouse to show the **view subscriptions** button and select the button.
2.  Hover over the line with your mouse to show the **activate** button and select this button to activate the sending of the webhook.

### Add webhooks to your cycle or template

1.  Drag the Webhook step from the sidebar into the builder.
2.  Connect the Webhook to another step.
3.  Select **Run** to start the cycle.

### Use custom objects

#### Create a custom object schema

To create custom object categories in the HubSpot connector, you need a custom object schema. HubSpot allows you to create custom object schema on the [Custom objects page](https://developers.hubspot.com/docs/api/crm/crm-custom-objects) of their documentation.  You can create custom object schema on the **Object schema** tab under **Create a new schema**.

#### Create a custom object method category

You can also create a custom object method category.

1. Go to the HubSpot connector Settings page:
   *  For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **HubSpot** > **Edit Connector**.
   *  For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **HubSpot** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Custom Objects** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Use the drop-down menu and select the custom object schema to use for the custom object method category.
5. Select **Copy**.

The new category then uses the custom object schema selected for all methods.

</section>
