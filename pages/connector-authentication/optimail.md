---
title: Optimail Connector Guide
sidebar: cyclr_sidebar
permalink: optimail-connector
tags: [connector]
---

Connector Setup
---------------

In order to setup the connector you will first need to retrieve your API key from Optimail.

To do this log in to your Optimail account, and select the `Integrations` option in the header of the page. Once there, select `API Key & Integration Guide`, and on this page you should see a field labeled `Account API ID`.

![](./images/optimail_api_key.png)

Clicking on this field should copy it to your clipboard and you can navigate back to the connector setup in Cyclr and paste this into the `API Key` field and press next.

![](./images/optimail_connector_api.png)

The connector is now authenticated and ready to use.

Retrieving Campaign IDs
-----------------------

The methods under `Subscriptions` require the use of a Campaign ID. There is no way to retrieve these via the API, so you will have to get them from Optimail itself. To do so go to Optimail and select `Campaigns` in the page header, then select the campaign for which you wish to retrieve the ID. When on the campaign page you will see the `CAMPAIGN API ID` field in the bottom left of the page.

![](./images/optimail_campaign_id.png)