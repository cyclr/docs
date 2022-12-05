---
title: API Key Authentication
sidebar: cyclr_sidebar
permalink: api-key-authentication
tags: [installing]
menus:
  installing-templates:
    title: API Key Authentication
    url: /api-key-authentication
    weight: 8
---

_**For connectors that are authenticated using an API key provided by the 3rd party app.**_

Your user's API Key will need to be collected in your application and sent to Cyclr.

You can update an existing Account Connector with this Cyclr API Request where **AuthValue** is set to the API Key value:

Request:

````http
    PUT /v1.0/account/connectors/{Account Connector ID}
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000

    {
        "AuthValue": "0000000000000000000000000000000000000000"
    }
````

Response:

````json
    {
        "Id": 0,
        "Name": "Pipedrive",
        "Description": null,
        "AuthValue": "0000000000000000000000000000000000000000",
        "Authenticated": true,
        "Connector": {
            "Id": 0,
            "Name": "Pipedrive",
            "Description": "Sales CRM for small teams with big ambitions.",
            "Status": "Approved",
            "Version": "1.0",
            "Icon": null,
            "AuthDescription": null,
            "AuthType": "ApiKey",
            "OAuth2Type": "Unknown",
            "AuthScheme": null
        },
        "IsPartnerIntegrationConnector": false,
        "Properties": [],
        "CustomFields": []
    }
````

[HTTP Basic Authentication](./basic-authentication)  
[OAuth Authentication](./oauth-authentication)  
[Step Setup](./step-set-up)
