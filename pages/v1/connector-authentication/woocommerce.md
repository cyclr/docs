---
title: WooCommerce Authentication
sidebar: cyclr_sidebar
permalink: woocommerce-connector
tags: [connector]
---

## Partner Setup

### Before you start

If your WooCommerce site is on a CDN such as CloudFront, you may need to add a Page Rule (e.g. https://{domain}/wp-json/wc/*) or whitelist the IP address used by Cyclr (see https://docs.cyclr.com/cyclr-ip-whitelisting).

### Authenticating the Connector

To authenticate the WooCommerce connector you will need a Consumer Key and Consumer Secret.

To create or manage keys for a specific WordPress user:
1. Go to: **WooCommerce** > **Settings** > **Advanced** > **REST API**.
> Note: Keys/Apps was found at WooCommerce > Settings > API > Key/Apps prior to WooCommerce 3.4.
2. Select **Add Key**.  You are taken to the **Key Details** screen.
3. Add a **Description**.
4. Select the **User** you would like to generate a key for in the dropdown.
5. Select a level of access for this API key — **Read** access, **Write** access or **Read/Write** access.
6. Select **Generate API Key**, and WooCommerce creates API keys for that user.

You can now authenticate the connector, passing the **Consumer Key** you just obtained as the username, and the **Consumer Secret** as the password.