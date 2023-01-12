---
title: Shopify (oAuth) Authentication
sidebar: cyclr_sidebar
permalink: shopify-oauth
tags: [connector]
---

## Shopify (oAuth) ##

If you are using API key authentication please see the documentation [here](https://docs.cyclr.com/shopify)

This document will explain what is needed to setup access to Shopify and install the connector.

### Setup Shopify oAuth Application ###
1. Create a Shopify custom or public oAuth application and bind it to your store. The instructions on how to do this can be seen [here](https://help.shopify.com/en/partners/making-apps).
2. The Redirect URL that is needed is: The URLs is: {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %} 
3. You will need the client ID and Secret provided by the application to authorise the connector.
4. This application will need to be associated with your shop, as instructed in shopify documentation.

### Connector Setup ###
- In the connector setup, enter the "Hostname". This is the first part of your Shopify domain, without the "https://". For example, if you login using "https://example.myshopify.com/admin" you should enter "example.myshopify.com".
- The Client ID is the Client ID found on your application settings page.
- The Secret is the Secret found on your application settings page.

![Shopify Details](./images/shopify-2.png)
