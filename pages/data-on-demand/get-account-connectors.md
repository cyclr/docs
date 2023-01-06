---
title: Get account connectors
sidebar: cyclr_sidebar
permalink: get-account-connectors
tags: [data-on-demand]

---

Call the [/v1.0/account/connectors](https://api.cyclr.uk/docs/index#!/Account32Connectors/AccountConnectors_All_GET) request to retrieve a list of all of the installed connectors in an account. You can use the returned values to tell Cyclr which connector to interact with.

## Request

```
GET https://{yourCyclrDomain}/v1.0/account/connectors
Authorization: Bearer {access_token}
X-Cyclr-Account: {accountID}
```
## Request parameters

| **Parameter**         | **Description**                                       |
|:----------------------|:------------------------------------------------------|
| `{yourCyclrDomain}` | Replace with the API domain of your version of Cyclr. |
| `Authorization`       | Give your access token.                               |
| `X-Cyclr-Account`     | Give your Cyclr account ID.                           |


For more information on access tokens, see the page on [API Authentication](cyclr-api-authentication).

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

## Related pages
*  [Get connector methods](get-connector-methods)
*  [Call a connector method](call-a-connector-method)
