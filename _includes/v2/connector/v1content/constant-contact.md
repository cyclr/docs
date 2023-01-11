
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

To use the Constant Contact connector, create an application within Constant Contact to obtain a `Key` and `Secret`.

### Constant Contact application

1. Go to the Constant Contact API Portal (https://constantcontact.mashery.com/)
2. Click `Apps & API Keys`>`Applications`>`Create a New Application`
3. Give your application an appropriate name, and enter your company name.
4. For Website, enter https://cyclr.com
5. Set the Redirect URI to https://`ServiceDomain`/connector/callback 

    > `ServiceDomain` should be substituted for your actual service domain, e.g. yourcompany-h.cyclr.com which can be found in your Cyclr Console under `Settings > General Settings > Service Domain`.
6. Leave `Issue a new key for Constant Contact API` selected, and set to `Standard API Access`.
7. Agree to the terms of service and click `Register Application`.
8. You will now be presented with details of your app, along with its `Key` and `Secret`.  Take note of these.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

To authenticate the connector, use the `Key` and `Secret` from the applicaton setup as `Client ID` and `Client Secret` respectively.

</div>

</section>
