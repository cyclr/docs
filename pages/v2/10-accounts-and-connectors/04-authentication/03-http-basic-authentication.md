---
title: HTTP basic authentication
sidebar: cyclr_sidebar
permalink: basic-authentication
tags: [installing]
menus:
    account-connector-authentication:
        title: HTTP basic authentication
        identifier: basic-authentication
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">
_**For connectors that use HTTP Basic authentication.**_

Your user’s username and password will need to be collected by your application then passed to Cyclr as follows:

*  Concatenate the username and password as “username:password”.
*  Base64 encode the concatenated username and password value, giving something this: “dXNlcm5hbWU6cGFzc3dvcmQ=”

That string should then be set as the **AuthValue** property of the Account Connector:

```html
    PUT /v1.0/account/connectors/{Account Connector ID}
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000

    {
        "AuthValue": "dXNlcm5hbWU6cGFzc3dvcmQ="
    }
```

Response:

```json
    {
        "Id": 0,
        "Name": "Pipedrive",
        "Description": null,
        "AuthValue": "dXNlcm5hbWU6cGFzc3dvcmQ=",
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
```

[API Key Authentication](./api-key-authentication)<br/>[OAuth Authentication](./oauth-authentication)  
[Step Setup](./step-set-up)

</section>
