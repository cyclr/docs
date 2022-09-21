---
title: HubSpot Connector Guide
sidebar: cyclr_sidebar
permalink: hubspot-connector
tags: [connector]
---

# HubSpot setup

For Cyclr to connect with the HubSpot API you will need to create an "App" within HubSpot, as detailed below:

> Note: This part can be completed once, by a Cyclr Partner. The client/customer does not need their own separate App within HubSpot.

1. Login to the HubSpot Developer Portal [here](https://app.hubspot.com/signup-v2/developers).
2. Follow the HubSpot [documentation](https://developers.hubspot.com/docs/faq/how-do-i-create-an-app-in-hubspot) to create an application.
3. In the `Auth` tab you will see a `Client ID` and `Client Secret`. Make a note of these to use in Cyclr's Connector setup.
4. The Redirect URL that creates the link between your Cyclr Console and HubSpot is shown on the page where the Client ID and Client Secret are entered. It has the form:
   `https://[Your Cyclr Service Domain]/connector/callback`
5. Set the scopes of your Hubspot App according to the method categories which you plan to use. A list of scopes and the permissions which they provide access to can be found [here](https://developers.hubspot.com/docs/api/working-with-oauth#scopes). By default, Hubspot installation in Cyclr will request the following scopes`crm.objects.contacts.read` , `crm.objects.contacts.write`,  `content` , `reports`,  `e-commerce` & `forms`. Scopes selected beyond these will need to be manually requested during connector installation. 



## Permissions

In order to use the Products and Line Items methods, the user must be assigned a [paid Sales Hub seat](https://knowledge.hubspot.com/articles/kcs_article/account/manage-sales-hub-and-service-hub-paid-users) within HubSpot.

# Cyclr setup

The Connector now can be installed using the credentials obtained in the above steps:

| Field           | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| Client ID       | The client ID of your Hubspot OAuth app.                     |
| Client Secret   | The secret of your Hubspot OAuth app.                        |
| Scopes          | A space separated list of permissions that your Hubspot OAuth app needs access to. These **must** be enabled on your Hubspot OAuth app or connector authentication will fail. By default, Cyclr will request the following scopes: `crm.objects.contacts.read` and `crm.objects.contacts.write`.  Any scopes entered here will override the default scopes. |
| Optional Scopes | A space separated list of optional permissions that your Hubspot OAuth app needs access to. If these are not enabled on your Hubspot OAuth app they will not be requested and functionality may be reduced. By default, Cyclr will request the following optional scopes: `content` `reports` `e-commerce` `forms`. Any scopes entered here will override the default scopes. |



You will then be prompted to log in, select your HubSpot and authorize access to the connector.

## Account selection

When authenticating the HubSpot Connector and signing into HubSpot, the user will be presented with the HubSpot **Choose an Account** screen.

During testing, you should select your main HubSpot account, rather than your developer account. You can identify the main account by looking for the one with items shown under the "PRODUCTS" heading as shown below.

In this example, that would be the "Cyclr" account:

![](./images/hubspot-choose-acct.png)

# Additional information

## Webhook setup

Hubspot webhooks utilise a single webhook URL, this requires some configuration of your Hubspot application.

Navigate to Cyclr Console > Connectors > Application Connector Library > Hubspot > Setup

Copy the Webhook URL to your clipboard. e.g. `https://<yourserivcedomain>/api/partnerwebhook/xxxxxx` (Note: Do not user the webhook URL from the builder, but this one under the partner console).

You will now need to setup the Hubspot application to send webhooks. This has three steps:

1.  Enter the URL
2.  Select events to subscribe to
3.  Activate the events

### Entering the URL

-   Navigate to the Hubspot Developers App [Dashboard](https://app.hubspot.com/developer), and select the application you use with Cyclr.
-   Within this application, navigate to Webhooks.
-   Paste the Webhook URL from your clipboard, into the "target URL"
-   Click Save (bottom of screen).

### Scopes

Setting up your subscriptions may require you to alter the scopes of the Hubspot application to allow the events to be sent. Please see Hubspot's documentation on webhook scopes [here](https://developers.hubspot.com/docs/api/webhooks#scopes). 

1. Click Create Subscription.
2. Select the objects and events that you wish to send to Cyclr.
3. Click Subscribe.

### Activating the events

1. Under event subscriptions.
2. Hover over the line with mouse and view subscriptions button will be shown, click this button.
3. Hover over the line with mouse and activate" button will be shown, click this button to activate the sending of the webhook.

Your application is now set up for Webhooks using Cyclr.

## Adding webhooks to your cycle or template

1. Drag the Webhook step from the sidebar into the Builder.
2. Connect the Webhook to another step.
3. Click Run to start the Cycle.

## Using custom objects

### Create a custom object schema

You first need a custom object schema to create custom object categories in the HubSpot connector. HubSpot allows you to create custom object schema on the Custom objects page of their documentation [here](https://developers.hubspot.com/docs/api/crm/crm-custom-objects). Custom object schema can be created on the **Object schema** tab under **Create a new schema**.

### Create a custom object method category

To create a custom object method category:

1. Go to the HubSpot connector Settings page:
    - For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **HubSpot** > **Edit Connector**.
    - For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **HubSpot** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Custom Objects** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Using the drop-down menu, select the custom object schema to use for the custom object method category.
5. Select **Copy**.

The new category will now use the custom object schema selected for all methods.

