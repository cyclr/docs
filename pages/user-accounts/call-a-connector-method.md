---
title: Call a Connector Method
sidebar: cyclr_sidebar
permalink: call-a-connector-method
tags: [embedding]
---

### Introduction

In this guide, you will use the Cyclr API to call a connector method. Cyclr will act as a proxy and pass your request to the external application.

Before you start, you'll need to have created a Cyclr Account and have installed and authenticated an Account Connector within it.

### Get Account Connectors

Let's get a list of installed account connectors from your account so Cyclr knows which account connector you want to make the request with.

#### Request:

```http
GET https://yourCyclrInstance/v1.0/account/connectors
Authorization: Bearer ****************************************************************
X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
```

#### Response:

```json
[
    {
        "Id": 123,
        "Name": "Salesforce Account 1",
        "Description": "",
        "Connector": {
            "Id": 1,
            "Name": "Salesforce"
        }
    },
    {
        "Id": 456,
        "Name": "Salesforce Account 2",
        "Description": "",
        "Connector": {
            "Id": 1,
            "Name": "Salesforce"
        }
    }
]
```

In the response, **123** is an Account Connector ID. **1** is the ID for the underlying Cyclr Connector.

### Identify the Connector Method to Call

Each Connector Method in Cyclr has a *MethodUniqueIdentifier* value. You can get a list of Methods with their unique identifiers using the 2 endpoints below.

(use the first endpoint for Connectors that don't have a "Version" property)

```GET https://yourCyclrInstance/v1.0/connectors/{name}/methods```

```GET https://yourCyclrInstance/v1.0/connectors/{name}/{version}/methods```

#### Response:

```json
[
	{
		"Id": 116,
		"Name": "Update Ticket",
		"Description": "Updates a ticket.",
		"EndPoint": "https://api.example/updateTicket",
		"MethodUniqueIdentifier": "8f8df8ef-3007-11e7-a033-06abe76375dd"
	},
	{
		"Id": 117,
		"Name": "Delete Ticket",
		"Description": "Deletes a ticket.",
		"EndPoint": "https://api.example/deleteTicket",
		"MethodUniqueIdentifier": "56d8a7ef-3457-af37-a3fd-0645386a75bd"
	}
]
```


### Call a Connector Method

You can now call a Connector Method and get the response from the third-party application.

Some Connector Methods may alter the response returned by the third-party API, such as changing the structure to improve how Cyclr can work with it.  If you're familiar with an application's API, you may notice some Responses look a little different.

#### Request

```http
POST https://yourCyclrInstance/v1.0/account/connectors/{account connector ID}/methods/{method ID or Method Unique Identifier}
Authorization: Bearer ****************************************************************
Content-Type: application/json
X-Cyclr-Account: 00000000-0000-0000-0000-000000000000

{}
```

#### Response

```json
{
    "records": [{
            "Id": "1001",
            "FirstName": "John",
            "LastName": "Smith",
            "Name": "John Smith",
            "Email": "johnsmith@example.com"
        },
        {
            "Id": "1002",
            "FirstName": "Jane",
            "LastName": "Doe",
            "Name": "Jane Doe",
            "Email": "janedoe@example.com"
        }
    ]
}
```

### Call a Connector Method with Parameters

If the method you are calling requires any values to be passed, they can be included in your Request Body as follows:

#### Request

```http
POST https://yourCyclrInstance/v1.0/account/connectors/{account connector ID}/methods/{method ID or Method Unique Identifier}
Authorization: Bearer ****************************************************************
Content-Type: application/json
X-Cyclr-Account: 00000000-0000-0000-0000-000000000000

{
    "Parameters": {
        "400123": "true"
    },
    "Fields": {
        "500123": "test@example.com"
    }
}
```

> <h3>The Method ID changes between releases of the Connector and may be deprecated over time, so we recommend using the Method Unique Identifier in these calls.</h3>

### IP Restriction

Access to Cyclr APIs used for passing requests to external applications is restricted by IP. The IP restricted APIs are as follows:
1. GET /v1.0/account/connectors/{id}/methods/{methodId} Calls a connector method
2. POST /v1.0/account/connectors/{id}/methods/{methodId} Calls a connector method
3. GET /v1.0/account/connectors/{id}/test/{methodId} Tests a connector method
4. POST /v1.0/account/connectors/{id}/test/{methodId} Tests a connector method

If you are using Cyclr APIs to call standard connectors, i.e. third-party connectors that are not native to your application, the Cyclr API request can only be made from a list of IP addresses approved by us.

Native connectors with the **IsPartnerIntegrationConnector** flag set to true can be called from any IP addresses.

If you would like to use Cyclr APIs to call standard connectors, please contact our support team to whitelist your IP.
