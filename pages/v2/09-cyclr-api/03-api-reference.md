---
title: API reference
sidebar: cyclr_sidebar
permalink: cyclr-api-reference
redirect_from: "/testing-cyclr-api/"
tags: [embedding]
menus:
    cyclr-api:
        title: API reference
        identifier: cyclr-api-reference
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">

Cyclr provides Swagger documentation for the API.  You can use the interactive API documentation to view available parameters, as well as to help you test endpoints as you work with the Cyclr API.

</section>
<section class="card">

## API domain and reference documentation

Your API domain depends on your Cyclr instance:

| Cyclr Console Location | API Domain | Interactive API Reference |
| --- | --- | --- |
| my.cyclr.com | https://api.cyclr.com | [US API Reference](https://api.cyclr.com/docs/index) |
| us2.cyclr.com | https://api.us2.cyclr.com | [US2 API Reference](https://api.us2.cyclr.com/docs/index)
| my.cyclr.uk | https://api.cyclr.uk | [UK API Reference](https://api.cyclr.uk/docs/index) |
| eu.cyclr.com | https://api.eu.cyclr.com | [EU API Reference](https://api.eu.cyclr.com/docs/index) |
| apac.cyclr.com | https://api.apac.cyclr.com | [APAC API Reference](https://api.apac.cyclr.com/docs/index) |
| Private | https://{your-api-instance} | https://\{your-api-instance\}/docs/index |



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
