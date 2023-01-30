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

### Checking the required Authentication Type

To check the authentication type that the installed Account Connector requires, make the following call:

Request:

````http
    GET /v1.0/account/connectors/{id}
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
            "AuthType": "ApiKey",
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

### Account Connector Properties
Before beginning the authentication process, you should set the values of any Parameters on the Account Connector that aren't marked as Optional.

To identify what these Parameters are, look in the `Connector` section you receive when making the Cyclr API call above for Parameters with `IsAccountConnectorProperty`:`true` and `IsOptional`:`false`.

You could provide some interface of your own to obtain the values for these Parameters from the user.

Call the `POST /v1.0/account/connectors/{accountConnectorId}/properties` endpoint to set each of those values on your Account Connector.

The Account Connector should now be ready to authenticate.


[API Key Authentication](./api-key-authentication)  
[HTTP Basic Authentication](./basic-authentication)  
[OAuth Authentication](./oauth-authentication)
