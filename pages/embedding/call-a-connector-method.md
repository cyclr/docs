---
title: Call a Connector Method
sidebar: cyclr_sidebar
permalink: call-a-connector-method
tags: [embedding]
---

### Introduction

In this guide, you will use the Cyclr API to call a connector method. Cyclr will act as a proxy and pass your request to the external application.

Before you start, make sure you have created an end user account and authenticated a connector.

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

In the response, **123** is an account connector ID. **1** is the ID for the underlying connector.

### Call a Connector Method

You can now call a connector method and get the raw response from the third-party application.

Each method in Cyclr has a *unique external ID*. You can get a list of methods with their unique identifiers using ```https://yourCyclrInstance/v1.0/connectors/{Connector ID}/methods```. *Connector ID* here is not the ID for your account connector instance (*123* in the sample response above), but the ID for the underlying connector (*1* in the sample response above).

#### Request

```http
GET https://yourCyclrInstance/v1.0/account/connectors/{account connector ID}/methods/{method ID}
Authorization: Bearer ****************************************************************
X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
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

If the method you are calling requires any field or parameter to be passed to the third-party application, they should be included in your request body.

#### Request

```http
POST https://yourCyclrInstance/v1.0/account/connectors/{account connector ID}/methods/{method ID}
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

### IP Restriction

Access to Cyclr APIs used for passing requests to external applications is restricted by IP. The IP restricted APIs are as follows:
1. GET /v1.0/account/connectors/{id}/methods/{methodId} Calls a connector method
2. POST /v1.0/account/connectors/{id}/methods/{methodId} Calls a connector method
3. GET /v1.0/account/connectors/{id}/test/{methodId} Tests a connector method
4. POST /v1.0/account/connectors/{id}/test/{methodId} Tests a connector method

If you are using Cyclr APIs to call standard connectors, i.e. third-party connectors that are not native to your application, the Cyclr API request can only be made from a list of IP addresses approved by us.

Native connectors with the **IsPartnerIntegrationConnector** flag set to true can be called from any IP addresses.

If you would like to use Cyclr APIs to call standard connectors, please contact our support team to whitelist your IP.
