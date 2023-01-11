---
title: Optimail Connector Guide
sidebar: cyclr_sidebar
permalink: optimail-connector
tags: [connector]
---

Connector Setup
---------------

In order to setup the connector you will first need to retrieve your API key from Optimail.

To do this:
 * Log in to your Optimail account.
 * Select the `Integrations` option in the header of the page.
 * Select `API Key & Integration Guide`, and on this page you will see a field labeled `Account API ID`.
 
![](./images/optimail_api_key.png)

Clicking on this field will copy it to your clipboard, navigate back to the connector setup in Cyclr and paste this into the `API Key` field and press next.

![](./images/optimail_connector_api.png)

The connector is now authenticated and ready to use.

Retrieving Campaign IDs
-----------------------

The methods under `Subscriptions` require a Campaign ID, there is no way to retrieve these via the API. the Campaign ID is obtained via the Optimail portal. 

Within the Optimail portal:
  * Select `Campaigns` in the page header.
  * Select the campaign for which you wish to retrieve the ID.
  * On the campaign page you will see `CAMPAIGN API ID` field in the bottom left of the page.
  
![](./images/optimail_campaign_id.png)