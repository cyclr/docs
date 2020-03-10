---
title: Shopify Authentication
sidebar: cyclr_sidebar
permalink: shopify
tags: [connector]
---

## Shopify ##

This document will explain what is needed to setup access to Shopify and install the connector.

### Setup Shopify Credentials ###
1. Create a Shopify private application and get the credentials. Instructions on how to do this can be seen [here](https://shopify.dev/tutorials/authenticate-a-private-app-with-shopify-admin#generate-public-app-credentials).
2. Make sure that the correct "Admin API Permisssions" have been set for the webhooks in use. The permissions can be set in the application settings of your Cyclr private appilcation in Shopfiy. 
   * "Checkout" webhooks require "read_orders, write_orders" permissions.
   * "Orders" webhooks require "read_orders, write_orders" permissions.
   * "Products" webhooks require "read_orders, write_orders" permissions.
   * "Refund" webhooks require "read_orders, write_orders" permissions.
   * "Customers" webhooks require "read_customers, write_customers" permissions.

### Connector Setup ###
In the connector setup, enter the "Hostname". This is the first part of your Shopify domain, without the "https://". For example, if you login using "https://example.myshopify.com/admin" you should enter "example.myshopify.com".

The username should be the API Key that can be found on your application settings page.

The password should be the API password that can be found on your application settings page.

![Shopify Details](./images/shopify-1.png)
