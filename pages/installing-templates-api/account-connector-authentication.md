---
title: Authenticate Account Connector
sidebar: cyclr_sidebar
permalink: authenticate-account-connector
tags: [installing]
---

_**Your users will be required to provide authentication information before Cycles can be run.**_

Cyclr supports three types of connector authentication:

| **API Key** | Your user will provide an API Key from the third party application that gives access to the third party API |
| **HTTP Basic** | Your user will provide a username and password to access the third Party API |
| **OAuth** | Your user will be taken through an OAuth flow which will generate a token that can be used to access the third party API |

For each connector requiring authentication, take your user through the appropriate flow.

Check the authentication type that the installed Account Connector requires.

Request:

````http
    GET /v1.0/account/connectors/0
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

Response:

````json
    {
        "Id": 0,
        "Name": "Pipedrive",
        "Description": null,
        "AuthValue": null,
        "Authenticated": false,
        "Connector": {
            "Id": 0,
            "Name": "Pipedrive",
            "Description": "Sales CRM for small teams with big ambitions.",
            "Status": "Approved",
            "Version": "1.0",
            "Icon": null,
            "AuthDescription": null,
            "AuthType": "**ApiKey**",
            "OAuth2Type": "Unknown",
            "AuthScheme": null
        },
        "IsPartnerIntegrationConnector": false,
        "Properties": [],
        "CustomFields": []
    }
````

In this example, the AuthType for this Account Connector is ApiKey.

The response also confirms that the Account Connector is not yet authenticated (“Authenticated”: false).

[API Key Authentication](./api-key-authentication)  
[HTTP Basic Authentication](./basic-authentication)  
[OAuth Authentication](./oauth-authentication)
