---
title: Shopify Authentication
sidebar: cyclr_sidebar
permalink: shopify
tags: [connector]
---

## Shopify ##

This document will explain what is needed to setup access to Shopify and install the connector.

### Setup Shopify Credentials ###
1. Create a Shopify private app and gain credentials. Instructions on how to do this can be seen [here](https://shopify.dev/tutorials/authenticate-a-private-app-with-shopify-admin#generate-public-app-credentials).
2. Make sure that the app has the right API permission. An error will show if Cyclr does not have the correct permission set in the app settings.

### Connector Setup ###
In the connector setup, enter the "Hostname". This is the first part of your Shopify domain, without the "https://". For example, if you login using "https://example.myshopify.com/admin" you should enter "example.myshopify.com".

The username should be the API Key and the password should be the API password that can be found on your app settings page.

![Shopify Details](./images/shopify-1.png)