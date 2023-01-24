---
title: OneLogin Authentication
sidebar: cyclr_sidebar
permalink: onelogin-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## OneLogin setup

To authenticate this connector, you need a OneLogin credential pair of **Client ID** and **Client Secret**. Find more information on how to obtain these credentials in OneLogin's [Working with API credentials](https://developers.onelogin.com/api-docs/1/getting-started/working-with-api-credentials) documentation.


</section>
<section class="card">
## Cyclr setup

To set up the OneLogin connector in Cyclr, go to your **Cyclr Console**.

1. Select **Connectors** > **Application Connector Library** at the top of the page.

2. Use the search box to find the **OneLogin** connector.

3. Select the **Setup Required** icon.

4. Enter your `Client ID` and `Client Secret`. 

5. Enter your OneLogin **sub domain**. You can find the domain in your OneLogin frontend URL just before `.onelogin.com`. For example, if your frontend URL is `https://testing-dev.onelogin.com/portal`, your **sub domain** would be `testing-dev`.

6. Select **Save Changes**.


</section>
