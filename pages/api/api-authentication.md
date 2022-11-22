---
title: API Authentication
sidebar: cyclr_sidebar
permalink: cyclr-api-authentication
tags: [embedding]
---

Cyclr API can be authenticated using the Client Credentials and Password flows. The [Password flow](./cyclr-api-authentication-password) will cease to be supported and stop functioning after May 2021. You should migrate to Client Credentials before then.

This document is for authenticating with the Cyclr API using the [OAuth 2.0](https://oauth.net/2/) Client Credentials flow.

### Get Client ID and Secret

You can generate a Client ID and Secret from the Cyclr Partner Console, Settings > OAuth Client Credentials

![Cyclr Console OAuth Client Credentials](./images/cyclr-api-client-credentials.png)

### Get Access Tokens

Once you have a Client ID and Secret you need to call the Cyclr API OAuth token endpoint to generate an access token.  This endpoint will be different depending on where your Cyclr Console is hosted:

Cyclr Console Location | API Domain
--- | ---
my.cyclr.com | https://api.cyclr.com/oauth/token
my.cyclr.uk | https://api.cyclr.uk/oauth/token
eu.cyclr.com | https://api.eu.cyclr.com/oauth/token

#### Required Request Body Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| grant_type | Identifies the OAuth flow being used. Must be client_credentials | client_credentials |
| client_id | Identifies the Cyclr Partner the token is for | abcdefg |
| client_secret | The matching secret for the client ID | abcdefghij123 |

#### Example Request

```http
POST https://{API Domain}/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id=abcdefg&client_secret=abcdefghij123
````
> NB. ``grant_type``, ``client_id`` and ``client_secret`` go in the body of the call - they are not added to the endpoint.

#### Example Response

```json
{
    "token_type": "bearer",
    "access_token": "************",
    "expires_in": 1209599,
    "clientId": "************"
}
```

| Parameter | Description |
| --- | --- |
| token_type | The type of token, this is always bearer |
| access_token | Token to use when making requests to the Cyclr API |
| expires_in | The amount of time in seconds until access_token will expire |
| clientId | Client ID provided when getting the token |

> Tokens will expire after 14 days, you will need to generate a new token when this occurs.

### Using the Access Token

All calls to the Cyclr must provide the access token in the Authorize HTTP request header.

````http
Authorization: Bearer {access_token}
````

#### Accessing Account Methods

For any calls to API methods that relate to an account the ID of the account must be provided as a HTTP header in the request.

````http
X-Cyclr-Account: {AccountID}
````

### Account Restricted Tokens

If required you can restrict access tokens to only work for a specific account by including the account ID in the scope when getting the access token.

#### Example Request

```http
POST https://{API Domain}/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id=abcdefg&client_secret=abcdefghij123&scope=account:{account_id}
````
