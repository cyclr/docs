---
title: Install the connector
sidebar: cyclr_sidebar
permalink: install-connector-api
tags: [accounts]

menus:
    install-connectors:
        title: Install the connector
        identifier: install-connector-api
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">

If you have the [connector ID](get-connectors), you can install the connector into an account. To install the connector, call the `/v1.0/connectors/{id}/install` endpoint. For more information about the endpoint, see the [Interactive API reference](cyclr-api-reference) page.

</section>
<section class="card">
## Request

```
POST https://{CyclrAPIDomain}/v1.0/connectors/{ConnectorId}/install HTTP/1.1
Authorization: Bearer {access_token}
X-Cyclr-Account: {AccountID}
{
  "Name": "{ConnectorName}",
  "Description": "{ConnectorDescription}",
  "AuthenticationId": "{AuthenticationId}",
  "AuthValue": "{AuthValue}",
  "Properties": [
    {
      "Name": "{PropertyName}",
      "Value": "{PropertyValue}",
      "Id": {PropertyId},
    }
  ]
}

```

</section>
<section class="card">
## Request parameters

| **Path parameter** | **Type** | **Description**                                    |
|:-------------------|:---------|:---------------------------------------------------|
| `{ConnectorId}`    | integer  | Enter the [ID](get-connectors#connector-id) of the connector you want to install. |

| **Body parameters** |  | **Type** | **Description** |
|---|---|---|---|
| `Name` |  | string | Name the account connector |
| `Description` |  | string, optional | Describe the account connector. |
| `AuthenticationId` |  | string | Enter the ID of the authentication method you want to use. See Get connectors for more information. |
| `AuthValue` |  | string, optional | **Basic Authentication**: enter the base64 encoded value of the username and password.<br>**Oauth**: enter the `{access_token}`.<br>**API Key**: enter the `{ApiKey}`. |
| **`Properties`** |  | Array, optional | If `Parameters.IsAccountConnectorProperty` is `true` in the [GET connectors](get-connectors#response-items) response, include this array of values from the response. |
|  | `Name` | string | Enter the `Parameters.TargetName` value. |
|  | `Value` | array[string] | Enter a value from the options in `Parameters.Values`. |
|  | `Id` | integer | Enter the `Pararameters.Id` value. |


</section>
<section class="card">
## Example response

```
{
  "Id": 54321,
  "Name": "Installed Example",
  "Description": "Alex's Example account connector",
  "AuthValue": "access_token",
  "Authenticated": true,
  "Connector": {
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
    "Parameters": [...],
    ...
    ,
  }
}
```


</section>
<section class="card">
## Authentication
Authentication is optional in this call because, if your customer has access to the account, they can authenticate the connector themselves. 

For more information on how to authenticate a specific application connector, see the **Application connector guides** documentation.

If the connector uses OAuth authentication, see the page on how to [Authenticate OAuth connectors (API)](authenticate-link-api) to send the customer an authentication link.

</section>
