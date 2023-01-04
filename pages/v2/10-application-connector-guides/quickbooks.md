---
title: QuickBooks Connector
sidebar: cyclr_sidebar
permalink: quickbooks-connector
tags: [connector]
keywords: [intuit]
---
{::options parse_block_html="true" /}
<section class="card">
QuickBooks Setup
---------------

To authenticate the connector you need a Client ID and Secret.

To obtain these, you will need to create a QuickBooks Online application.

### Creating an App
1. Visit [https://developer.intuit.com/app/developer/myapps](https://developer.intuit.com/app/developer/myapps).
2. Click the ![](./images/QuickBooksCreateAnApp.png) button.
3. Select `QuickBooks Online and Payments`.
4. Give your app a name, and select `Accounting` from the scopes.  If you are based in the US, and wish to add the `Payments` scope, you can add this later.
5. Click ![](./images/QuickBooksCreateApp.png).
    > Note that there are sections here for `Development` and `Production` apps.  We will be focussing on the `Development` app in this guide.
6. `Under Development > Keys & OAuth`, you will find two important sections: the keys (`Client ID` and `Client Secret`) **which you should now note down**, and `Redirect URIs`.
7. Under `Redirect URIs`, change the existing value to:
 ht<span></span>tps://`ServiceDomain`/connector/callback

    > Your Cyclr service domain, e.g. yourcompany-h.cyclr.com can be found in your Cyclr Console under ``Settings > General Settings > Service Domain``.

8. Scroll down and click ![](./images/QuickBooksSave.png).

### Setting up the connector

1. During installation of the connector, you will be asked for `Client ID` and `Client Secret`.  Give those you noted down in stage 6 of the instructions above.

2. You will also be asked for the `Base Domain`.  In this example, as we are working with a development app, you would give sandbox-quickbooks.api.intuit.com <span>.</span>

    > Later, when you have your production app set up, you will enter quickbooks.api.intuit.com here.

3. You can now ![](./images/QuickBooksSignIn.png) to Quickbooks and your connector will be installed.

</section>
