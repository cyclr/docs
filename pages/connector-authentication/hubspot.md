---
title: Hubspot Connector Guide
sidebar: cyclr_sidebar
permalink: hubspot-connector
tags: [connector]
---

Hubspot Setup
---------------

For Cyclr to connect with the Hubspot API you will need to create an "Application" in the Hubspot account, as detailed below:

  > NB. This part is completed once, by a Partner.  The client/customer does not need their own separate application within Hubspot.

1. Login to the Hubspot Developer Portal [here](https://app.hubspot.com/signup-v2/developers)
2. Follow the Hubspot [documentation](https://developers.hubspot.com/docs/faq/how-do-i-create-an-app-in-hubspot) to create an application
3. In the `Auth` tab you will see a `Client ID` and `Client Secret`.  Make a note of these to use in the connector setup.
4. The Redirect URL that creates the link between your Cyclr Console and Hubspot is shown page where the Client ID and Client Secret are entered.  It has the form
https://{{PartnerIdentifier}}/connector/callback.
5. Set the desired (minimum) Scopes you require to access. See [here](https://developers.hubspot.com/docs/api/working-with-oauth) for further information 

Permissions
---------------
In order to use the Products and Line Items methods, the user must be assigned a [paid Sales Hub seat](https://knowledge.hubspot.com/articles/kcs_article/account/manage-sales-hub-and-service-hub-paid-users) within Hubspot.

Connector Setup
---------------

The Connector now can be installed using the credentials obtained in the above steps:

**Client ID**: `Client ID`

**Secret**: `Client Secret`

**Scopes/Optional** You will need to match the Scopes you set when creating the oAuth App above

You will then be prompted to log in, select your Hubspot and authorize access to the connector.

Important note about Account selection
--------------------------------------

After entering your Client ID and Secret, and signing into hubspot, you will be presented with the **Choose an Account** screen.

It is important to select the main account, rather than the developer account.  You can identify the main account by looking for the one with Products attached.

In the example below, this would be the "Cyclr" account.

![](./images/hubspot-choose-acct.png)

## Connector Parameters 
#### (Useful if accessing this Connector via the API.  Property Names given here in the same format as they should be passed to the API.)

| Property Name   | Description    |
| ----------- | -----------    |
| Scopes      | The scopes of the connector. Default value is "contacts". |
| OptionalScopes   | The optional scopes of the connector. Default value is "content reports e-commerce forms" |
