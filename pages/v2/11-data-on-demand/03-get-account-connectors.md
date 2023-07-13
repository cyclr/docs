---
title: Get account connectors
sidebar: cyclr_sidebar
permalink: get-account-connectors
tags: [data-on-demand]

menus:
    data-on-demand:
        title: Get account connectors
        identifier: get-account-connectors
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">

Call the `/v1.0/account/connectors` request to retrieve a list of all of the installed connectors in an account. You can use the returned values to tell Cyclr which connector to interact with. For more information about the endpoint, see the [Interactive API reference](cyclr-api-reference) page.

</section>
<section class="card">
## Request

```
GET https://{CyclrAPIDomain}/v1.0/account/connectors
Authorization: Bearer {access_token}
X-Cyclr-Account: {accountID}
```

</section>
<section class="card">
## Request parameters

| **Parameter**         | **Description**                                       |
|:----------------------|:------------------------------------------------------|
| `{CyclrAPIDomain}` | Replace with the API domain of your version of Cyclr. |
| `Authorization`       | Give your access token.                               |
| `X-Cyclr-Account`     | Give your Cyclr account ID.                           |


For more information on access tokens, see the page on [API Authentication](cyclr-api-authentication).


</section>
<section class="card">
## Example response

```
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
### Response parameters

| **Parameter**    | **Description**                             |
|:-----------------|:--------------------------------------------|
| `Id`             | The ID of your account connector.           |
| `Name`           | The account connector name.                 |
| `Description`    | The account connector description.          |
| `Connector.Id`   | The ID of the underlying Cyclr connector.   |
| `Connector.Name` | The name of the underlying Cyclr connector. |


</section>
<section class="card">
## Related pages
*  [Get connector methods](get-connector-methods)
*  [Call a connector method](call-a-connector-method)

</section>
