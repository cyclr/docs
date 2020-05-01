---
title: HTTP Basic Authentication
sidebar: cyclr_sidebar
permalink: basic-authentication
tags: [installing]
---

_**For connectors that are authenticated HTTP basic authentication.**_

Your user’s username and password will need to be collected in your application and sent to Cyclr like below

Concat the username and password like “username:password”

Base64 encode the concated username and password “dXNlcm5hbWU6cGFzc3dvcmQ=”, use this as the value to send to Cyclr

```http
    PUT /v1.0/account/connectors/{Account Connector ID}
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000

    {
        "AuthValue": "dXNlcm5hbWU6cGFzc3dvcmQ="
    }
````

Response:

````json
    {
        "Id": 0,
        "Name": "Pipedrive",
        "Description": null,
        "AuthValue": "dXNlbmFtZTpwYXNzd29yZA==",
        "Authenticated": true,
        "Connector": {
            "Id": 0,
            "Name": "Pipedrive",
            "Description": "Sales CRM for small teams with big ambitions.",
            "Status": "Approved",
            "Version": "1.0",
            "Icon": null,
            "AuthDescription": null,
            "AuthType": "Basic",
            "OAuth2Type": "Unknown",
            "AuthScheme": null
        },
        "IsPartnerIntegrationConnector": false,
        "Properties": [],
        "CustomFields": []
    }
````

[API Key Authentication](./api-key-authentication)<br/>[OAuth Authentication](./oauth-authentication)  
[Step Setup](./step-set-up)
