---
title: Install a Connector
sidebar: cyclr_sidebar
permalink: install-a-connector
tags: [embedding]
---

This article will guide you through installing a connector into an account. You must already have an [OAuth Access Token](obtain-account-authorization-token).

### Getting the connector ID

You need the ID of a connector before you can install it. You can find a connector by calling the /v1.0/connectors endpoint, this will show the connectors that are available to the account.

#### Request

```http
    GET https://yourCyclrInstance/v1.0/connectors HTTP/1.1
    Authorization: Bearer ****************************************************************
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

#### Response

````json
    [
       {  
          "Id":1,
          "Name":"Example Connector",
          "Description":"This is an example connector.",
          "Status":"Approved",
          "Version":"1.0",
          "Icon":"",
          "AuthDescription":"",
          "AuthType":"ApiKey",
          "OAuth2Type":"Unknown",
          "AuthScheme":null
       },
       {...}
    ]
````

### Installing the connector

Now that you have a connector ID, the connector can be installed by calling the /v1.0/connectors/{id}/install endpoint.

#### Body parameters

| Parameter | Description |
| --- | --- |
| **Name** | The name for the installed connector |
| **Description** | _(Optional)_ Any description for the installed connector |
| **AuthValue** | _(Optional)_ Authentication value for the third party API that will be used by the connector. Provide username and password as base64 (username:password), provide API keys as plain text. OAuth can only be provided if you have your own OAuth flow implementation. To use Cyclr’s implementation see the next step. |

#### Request

````http
    POST https://yourCyclrInstance/v1.0/connectors/1/install
    Authorization: Bearer ****************************************************************
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000

    {"Name":"Example", "AuthValue":"example-api-key"}
````

#### Response

````json
    {  
       "Id": 1,
       "Name":"Example",
       "AuthValue":"example-api-key",
       "Authenticated":true,
       "Connector":{ ... },
       ...
    }
````

The connector is now installed into the account, if the connector doesn’t use OAuth you’re all done; otherwise, read on to authenticate with OAuth.

### Authenticating OAuth connectors

If the connector requires an OAuth authentication to work with the third party API, you will be required to show the user a popup that will take them through the OAuth flow. First you need to get an account one time sign in token, this will be used to allow a web browser to sign in using the credentials of the Oauth token.

#### Request

````http
    POST https://yourCyclrInstance/v1.0/accounts/tokens
    Authorization: Bearer ****************************************************************
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

#### Response

````json
    {
      "Token":"***************************************",
      "ExpiresAtUtc":"2017-11-29T16:22:36.7257196Z"
    }
````

Now you have a sign in token, you can "build" the URL to send the user to where they will begin the OAuth flow.

#### URL & Querystring

| **URL** | https://[Partner Service Domain]/connectorauth/updateaccountconnectoroauth |
| **id** | This is the ID of the installed connector from the response when [installing the connector](#installing-the-connector) |
| **token** | The account sign in token |
| **targetOrigin** | Specifies what the origin of the other window must be for the javascript callback event to be dispatched. If the callback message is null we will redirect to the targetOrigin |
| **callbackMessage** | (Optional) Callback message to be sent to the parent window |

#### Example built URL

    https://[Partner Service Domain]/connectorauth/updateaccountconnectoroauth?id=1&token=***************************************&targetOrigin=example.com&callbackMessage=done

When the user is sent to the built URL they will be redirected to the third party OAuth flow. On completion they will be either redirected to targetOrigin or a JavaScript message will be posted to the parent window.
