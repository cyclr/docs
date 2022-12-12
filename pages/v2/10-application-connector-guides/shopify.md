---
title: Shopify Authentication
sidebar: cyclr_sidebar
permalink: shopify
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
# Shopify

This document explains how to set up Shopify and install the Shopify connector in Cyclr.

<a name="shopify-set-up"></a>


</section>
<section class="card py-5 my-5">
## Shopify set up

To authenticate the Shopify connector in Cyclr you need:

- The [hostname](#getting-the-hostname) of the Shopify store you want to manage.
- The [admin API access token](#getting-an-admin-api-access-token) of a custom app within the store you want to manage.

<a name="getting-the-hostname"></a>

### Getting the hostname

Your Shopify domain contains your hostname. For example, if the Shopify domain is `https://example.myshopify.com/admin` then the hostname is `example.myshopify.com`. Shopify's documentation on domains can be found [here](https://help.shopify.com/en/manual/domains).

<a name="getting-an-admin-api-access-token"></a>

### Getting an admin API access token

You first need to create a custom app within the store to get an admin API access token. Shopify's documentation on creating a custom app can be found [here](https://help.shopify.com/en/manual/apps/custom-apps). When creating a custom app, ensure that the correct **Admin API Permissions** have been set for the webhooks your connector will use. The table below contains a list of webhooks and scopes:

| Cyclr webhook | Shopify scopes                  |
| ------------- | ------------------------------- |
| Checkout      | read_orders, write_orders       |
| Customers     | read_customers, write_customers |
| Orders        | read_orders, write_orders       |
| Products      | read_orders, write_orders       |
| Refunds       | read_orders, write_orders       |

You can find the admin API access token in the newly created custom app under **API credentials** > **Admin API access token**. The token can be viewed once before being permanently hidden. To get a new token you need to uninstall and reinstall the app to your store. Shopify's documentation on doing this can be found [here](https://shopify.dev/apps/auth/admin-app-access-tokens#rotating-api-credentials-for-admin-created-apps).

<a name="cyclr-set-up"></a>


</section>
<section class="card py-5 my-5">
## Cyclr set up

<a name="connector-set-up"></a>

### Account setup 

You will be asked for the following values when installing the Shopify connector within an account:

- **Hostname**: The [hostname](#getting-the-hostname) of the Shopify store you want to manage.
- **API Key**: The [admin API access token](#getting-an-admin-api-access-token) of a custom app within the store you want to manage.

Your Shopify connector is now set up! You can test it by executing one of the methods to confirm it can return some data.

</section>
