---
title: HubSpot Connector Guide
sidebar: cyclr_sidebar
permalink: hubspot-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
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
<section class="card">
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
