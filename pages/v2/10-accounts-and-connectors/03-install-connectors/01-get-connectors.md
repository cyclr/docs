---
title: Get the connector ID
sidebar: cyclr_sidebar
permalink: get-connectors
tags: [accounts]

menus:
    install-connectors:
        title: Get connectors
        identifier: get-connectors
        toggleonly: menutoggleonly
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">
You need the ID of a connector before you can install it. To show a list of connectors available to the account, call the [`/v1.0/connectors`](https://api.cyclr.uk/docs/index#!/Connectors/Connectors_All_GET) endpoint.


</section>
<section class="card">
## Request

```
GET https://{yourCyclrInstance}/v1.0/connectors HTTP/1.1
Authorization: Bearer {access_token}
X-Cyclr-Account: {AccountID}
```


</section>
<section class="card">
## Response items

These are the values you need to include in the request when you install the connector into an account:

<a name="connector-id"></a>

| **Parameter**     | **Type** | **Description**                                                                                                       |
|:------------------|:---------|:----------------------------------------------------------------------------------------------------------------------|
| `Id`                | integer  | The ID of the connector. Use this value as the `ConnectorId` when you install the connector.                            |
| `Authentication.Id` | string   | The ID of the connector’s authentication type. Use the value of the authentication method you want to use as the `AuthenticationId` when you install the connector. |

If `Parameters.IsAccountConnectorProperty` is `true`, you also need the following values:

| **Parameter**         | **Type**      | **Description**                                        |
|:----------------------|:--------------|:-------------------------------------------------------|
| `Parameters.TargetName` | String        | The name of the account connector property.            |
| `Parameters.Values`     | array[string] | The possible values of the account connector property. |
| `Parameters.Id`         | integer       | The ID of the account connector property.              |


</section>
<section class="card">
## Example response

```
[
  {
    "Id": 12345,
    "Name": "Example",
    "Description": "Connect securely with your Example application",
    "Status": "Approved",
    "Version": "null",
    "Icon": "Base64 image data for the connector icon",
    "AuthDescription": "null",
    "AuthType": "ApiKey", <this says deprecated in swagger, should it be null?>
    "OAuth2Type": "AuthorisationCode",<can we correct the spelling here?>
    "AuthScheme": "Authorization", 
    "Parameters": [
      {
        "IsAccountConnectorProperty": true,
        "TargetType": "Script",
        "TargetName": "isSandbox",
        "IsSensitive": false,
        "Id": 7654321,
        "Name": "Is Sandbox?",
        "Description": "Sandbox oAuth servers will not authenticate production credentials (and vice versa).",
        "IsOptional": false,
        "DataType": "Text",
        "TriggerName": "null",
        "Values": [
          "true",
          "false"
        ],
       ...
       ,
    "Authentication": [
      {
        "Id": "12abc345-1a2b-123a-1ab2-1234ab5c6d7e",
        "AuthName": "OAuth 2.0",
        "AuthDescription": "In sandbox mode, sign in to see the authorization page.",
        "AuthType": "OAuth2",
        "OAuth2Type": "AuthorisationCode",
        "AuthScheme": "null"
      }
      {
        "Id": "12abc345-1a2b-12ab-1abc-a12b3c4e567e",
        "AuthName": "API Key",
        "AuthDescription": null,
        "AuthType": "ApiKey",
        "OAuth2Type": "AuthorisationCode",
        "AuthScheme": "Authorization"
      }
    ]
  }
]
```

</section>
<section class="card">
## Related pages

* The `GET /v1.0/connectors` [API reference](https://api.cyclr.uk/docs/index#!/Connectors/Connectors_All_GET) documentation.
* [Install a connector](install-connector-api)
* [API authentication](cyclr-api-authentication)


</section>
