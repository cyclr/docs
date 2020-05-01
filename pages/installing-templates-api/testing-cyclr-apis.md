---
title: Testing Cyclr's APIs
sidebar: cyclr_sidebar
permalink: testing-cyclr-api
tags: [api]
---

Cyclr's interactive API references can be used to try things out, and to help you while testing and creating your own native deployment or working with data on demand.

### API Reference Location

Depending on where your Cyclr Console is hosted, you'll need to use the appropriate reference:

Cyclr Console Location | Documentation link
--- | ---
my.cyclr.com | [US API Reference](https://api.cyclr.com/docs/index)
my.cyclr.uk | [UK API Reference](https://api.cyclr.uk/docs/index)
eu.cyclr.com | [EU API Reference](https://api.eu.cyclr.com/docs/index)

### API Reference Authorization

Use your Cyclr account details to authenticate and work with all API endpoints directly within the API reference documentation.

To authenticate, expand any endpoint and click the "OFF" slider, then enter your details:

![](./images/testing-cyclrs-apis-auth.png)

<br/>

| Property | Description | Example |
| --- | --- | --- |
| **Username** | The username you use to signin to Cyclr | me@example.com |
| **Password** | The password for your user | Pa$$word |
| **Type** | Must be **Request body** | Request body |
| **ClientID** | The Client ID for your partner, can be found in the console | abc123defg |
| **Secret** | This should be left blank | |

The Cyclr API is divided into two parts, the Partner Level and the Account Level, you can use the same OAuth token for both but account level methods require that the **X-Cyclr-Account** header is included with the request.
