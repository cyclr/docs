---
title: Call a connector method
sidebar: cyclr_sidebar
permalink: call-a-connector-method
tags: [data-on-demand]
menus:
    data-on-demand:
        title: Call a connector method
        identifier: call-a-connector-method
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">
You can use the [`MethodUniqueIdentifier`](get-connector-methods) and the [account ID](cyclr-api-authentication) to call a connector method and get the response from a third-party application.


>  **Note**: Some Connector Methods alter the format of the response returned by the third-party API to improve how it works with Cyclr.


</section>
<section class="card">
## Request

```
POST https://{CyclrAPIDomain}/v1.0/account/connectors/{account connector ID}/methods/{MethodUniqueIdentifier}
Authorization: Bearer {access_token}
Content-Type: application/json
X-Cyclr-Account: {accountID}

{}
```

### Request parameters

| **Parameter**                           | **Description**                                                       |
|:----------------------------------------|-----------------------------------------------------------------------|
| `{CyclrAPIDomain}`                   | Replace with the API domain of your version of Cyclr.                 |
| `{Account connector ID}`                | Replace with the account connector ID. See Get account connectors.    |
| `{method ID or MethodUniqueIdentifier}` | Replace with the unique method identifier. See Get connector methods. |
| `access_token`                          | Give your access token.                                               |

>  **Note:** It’s more reliable to use the Method Unique Identifier as the method ID can change between releases.

### Pass parameters with a request

If the method you are calling requires any values to be passed, you can include them in your request body:

```
POST https://{CyclrAPIDomain}/v1.0/account/connectors/{account connector ID}/methods/{method ID or Method Unique Identifier}
Authorization: Bearer {access_token}
Content-Type: application/json
X-Cyclr-Account: {accountID}

{
    "Parameters": {
        "400123": "true"
    },
    "Fields": {
        "500123": "test@example.com"
    }
}
```


</section>
<section class="card">
## Example response

```
{
    "records": [{
            "Id": "1001",
            "FirstName": "John",
            "LastName": "Doe",
            "Name": "John Doe",
            "Email": "johndoe@example.com"
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


</section>
<section class="card">
## Related pages

*  [Get account connectors](get-account-connectors)
*  [Get connector methods](get-connector-methods)


</section>
