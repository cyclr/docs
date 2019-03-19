---
title: Call a Connector Method
sidebar: cyclr_sidebar
permalink: call-a-connector-method
tags: [embedding]
---

### Introduction

In this guide, you will use the Cyclr API to call a connector method. Cyclr will act as a proxy and pass your request to the external application.

Before you start, make sure you have created an end user account and authenticated a connector.

### Account Access Token

You need to have a valid **Account** access token to make API calls on your user's behalf.

For more information on getting access tokens, please see [API Authentication](./cyclr-api-authentication).

### Get Account Connectors

Let's get a list of installed account connectors from your account so Cyclr knows which account connector you want to make the request with.

#### Request:

```http
GET https://api.cyclr.com/v1.0/account/connectors
Authorization: Bearer ****************************************************************
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

Each method in Cyclr has a *unique external ID*. You can get a list of methods with their unique identifiers using ```https://api.cyclr.com/v1.0/connectors/{Connector ID}/methods```. *Connector ID* here is not the ID for your account connector instance (*123* in the sample response above), but the ID for the underlying connector (*1* in the sample response above).

#### Request

```http
GET https://api.cyclr.com/v1.0/account/connectors/{account connector ID}/methods/{method ID}
Authorization: Bearer ****************************************************************
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
