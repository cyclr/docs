---
title: Shopify Authentication
sidebar: cyclr_sidebar
permalink: shopify
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
# Shopify

This document explains how to set up Shopify and install the Shopify connector in Cyclr.

<a name="shopify-set-up"></a>


</section>
<section class="card">
## Shopify set up

To authenticate the Shopify connector in Cyclr you need:

* The [hostname](#getting-the-hostname) of the Shopify store you want to manage.
* The [admin API access token](#getting-an-admin-api-access-token) of a custom app within the store you want to manage.

<a name="getting-the-hostname"></a>

### Get the hostname

Your Shopify domain contains your hostname. For example, if the Shopify domain is `https://example.myshopify.com/admin` then the hostname is `example.myshopify.com`. Shopify's documentation on domains can be found [here](https://help.shopify.com/en/manual/domains).

<a name="getting-an-admin-api-access-token"></a>

### Get an admin API access token

To get an admin API access token, you need to create a custom app within the store. For information on how to create a custom app, see [Shopify's documentation](https://help.shopify.com/en/manual/apps/custom-apps). When you create a custom app, ensure that you set the correct **Admin API Permissions** for the webhooks your connector will use. The table below contains a list of webhooks and the required scopes:

| **Cyclr webhook** | **Shopify scopes**                  |
| ----------------- | ----------------------------------- |
| Checkout          | `read_checkouts`, `write_checkouts` |
| Customers         | `read_customers`, `write_customers` |
| Orders            | `read_orders`, `write_orders`       |
| Products          | `read_products`, `write_products`   |
| Refunds           | `write_payment_sessions`            |

> **Note**: This is not an exhaustive list of scopes that you can use. To see all available scopes, see the [Shopify documentation](https://shopify.dev/docs/api/usage/access-scopes#authenticated-access-scopes) on authenticated access scopes.


You can find the admin API access token in the newly created custom app under **API credentials** > **Admin API access token**. You can only view the token once before it's permanently hidden. To get a new token, you need to uninstall and reinstall the app to your store. For more information, see Shopify's documentation on [rotating API credentials](https://shopify.dev/apps/auth/admin-app-access-tokens#rotating-api-credentials-for-admin-created-apps).

<a name="cyclr-set-up"></a>


</section>
<section class="card">
## Cyclr set up

<a name="connector-set-up"></a>

### Account setup 

Cyclr asks for the following values when installing the Shopify connector within an account:

- **Hostname**: The [hostname](#getting-the-hostname) of the Shopify store you want to manage.
- **API Key**: The [admin API access token](#getting-an-admin-api-access-token) of a custom app within the store you want to manage.

</section>
