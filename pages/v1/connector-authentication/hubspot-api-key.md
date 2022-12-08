---
title: Hubspot Api Key Connector Guide
sidebar: cyclr_sidebar
permalink: hubspot-api-key-connector
tags: [connector]
---

Hubspot Setup
---------------

For Cyclr to connect with the Hubspot API you will need to create an "Application" in the Hubspot account, as detailed below:

  > NB. This part is completed once, by a Partner.  The client/customer does not need their own separate application within Hubspot.

1. Login to the Hubspot Developer Portal [here](https://app.hubspot.com/signup-v2/developers)
2. Follow the Hubspot [documentation](https://developers.hubspot.com/docs/faq/how-do-i-create-an-app-in-hubspot) to create an application.
3. On the 'Auth' tab, enable either the `Contacts` or `Tickets` scope, depending on which you want to make CRM cards for.
4. In the same tab, note down the `App ID`.
5. Under the `Apps` tab at the top of the page, click on `Get HubSpot API key`. Click `Show key` and note down the presented API key.

Connector Setup
---------------

The Connector now can be installed using the credentials obtained in the above steps:

**API Key**: `API Key`

**Application ID**: `App ID`

Your HubSpot Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

