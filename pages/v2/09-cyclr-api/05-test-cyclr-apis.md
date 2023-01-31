---
title: Test Cyclr APIs
sidebar: cyclr_sidebar
permalink: testing-cyclr-api
tags: [api]
menus:
    cyclr-api:
        title: Test Cyclr APIs
        identifier: testing-cyclr-api
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">
Cyclr's interactive API references can be used to try things out, and to help you while testing and creating your own native deployment or working with data on demand.

</section>
<section class="card">

## API Location/Instance

Depending on where your Cyclr Console is hosted, you'll need to use the appropriate API Domain when making Requests:

Cyclr Console Location | API Domain | Interactive API Reference
--- | --- | ---
my.cyclr.com | https://api.cyclr.com | [US API Reference](https://api.cyclr.com/docs/index)
my.cyclr.uk | https://api.cyclr.uk | [UK API Reference](https://api.cyclr.uk/docs/index)
eu.cyclr.com | https://api.eu.cyclr.com | [EU API Reference](https://api.eu.cyclr.com/docs/index)
apac.cyclr.com | https://api.apac.cyclr.com | [APAC API Reference](https://api.apac.cyclr.com/docs/index)

</section>
<section class="card">

## API Reference Authorization

You can use your Cyclr account details to authenticate and work with all API endpoints directly within the API reference documentation.

1.  Expand the endpoint and select the **OFF** slider. 
2.  In the new window, select either **Basic auth** or **Request body** from the dropdown.
3.  Enter the **ClientID** and **Secret** that you want to use to authenticate.
4.  Select **Authorize**.

<br/>

Cyclr supports OAuth authentication. For more information, see the [API authentication](./cyclr-api-authentication) documentation.

> **Note**: The Cyclr API is divided into two parts, the Partner Level and the Account Level, you can use the same OAuth token for both but account level methods require that the account ID header is included with the request.

</section>
