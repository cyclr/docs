
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

To authenticate the connector you need a `Client ID` and `Client Secret`.

To obtain these, you will need to create a QuickBooks Online application.

### Creating an App
1. Go to [https://developer.intuit.com/app/developer/myapps](https://developer.intuit.com/app/developer/myapps)
2. Click the ![](./images/QuickBooksCreateAnApp.png) button
3. Select **QuickBooks Online and Payments**
4. Give your app a name, and select `Accounting` from the scopes -  if you are based in the US, and wish to add the `Payments` scope, you can add this later.
5. Click ![](./images/QuickBooksCreateApp.png).
    > Note that there are sections here for **Development** and **Production** apps - in this guide we focus on the **Development** app 
6. Under **Development** > **Keys & OAuth**, see the two sections: the keys `Client ID` and `Client Secret` **which you should now note**, and `Redirect URIs`
7. Under `Redirect URIs`, change the existing value to:
    `https://[ServiceDomain]/connector/callback`

    > Your Cyclr service domain, e.g. yourcompany-h.cyclr.com can be found in your Cyclr Console under **Settings** > **General Settings** > Service Domain**

8. Scroll down and click ![](./images/QuickBooksSave.png).

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. During installation of the connector, you will be asked for `Client ID` and `Client Secret`.  Give those you noted down in stage 6 of the instructions above.

2. You will also be asked for the `Base Domain`.  In this example, as we are working with a development app, you would give `sandbox-quickbooks.api.intuit.com`.

    > Later, when you have your production app set up, you will enter quickbooks.api.intuit.com here.

3. You can now ![](./images/QuickBooksSignIn.png) to Quickbooks and your connector will be installed.

</div>

</section>
