---
title: Test Cyclr APIs
sidebar: cyclr_sidebar
permalink: testing-cyclr-api
tags: [api]
menus:
    api:
        title: Test Cyclr APIs
        identifier: testing-cyclr-api
        weight: 4
---

Cyclr's interactive API references can be used to try things out, and to help you while testing and creating your own native deployment or working with data on demand.

### API Location/Instance

Depending on where your Cyclr Console is hosted, you'll need to use the appropriate API Domain when making Requests:

Cyclr Console Location | API Domain | Interactive API Reference
--- | --- | ---
my.cyclr.com | https://api.cyclr.com | [US API Reference](https://api.cyclr.com/docs/index)
my.cyclr.uk | https://api.cyclr.uk | [UK API Reference](https://api.cyclr.uk/docs/index)
eu.cyclr.com | https://api.eu.cyclr.com | [EU API Reference](https://api.eu.cyclr.com/docs/index)
apac.cyclr.com | https://api.apac.cyclr.com | [APAC API Reference](https://api.apac.cyclr.com/docs/index)

### API Reference Authorization

Use your Cyclr account details to authenticate and work with all API endpoints directly within the API reference documentation.

To authenticate, expand any endpoint and click the "OFF" slider, then enter your details:

![](./images/testing-cyclrs-apis-auth_2020-11.png)

<br/>

Cyclr supports 2 of the OAuth 2.0 authentication flows:

* [Client Credentials](./cyclr-api-authentication)
* [Password flow](./cyclr-api-authentication-password) [support ends May 2021]



The Cyclr API is divided into two parts, the Partner Level and the Account Level, you can use the same OAuth token for both but account level methods require that the **X-Cyclr-Account** header is included with the request.
