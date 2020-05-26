---
title: API Authentication
sidebar: cyclr_sidebar
permalink: cyclr-api-authentication
tags: [embedding]
---

Authentication with the Cyclr API is provided using the [OAuth 2.0](https://oauth.net/2/) Client Credentials flow.

To see the old Password flow documentation [Click Here](./cyclr-api-authentication-password)

### Get Client ID and Secret

You can generate a Client ID and Secret from the Cyclr Partner Console, Settings > OAuth Client Credentials

![Cyclr Console OAuth Client Credentials](./images/cyclr-api-client-credentials.png)

### Get Access Tokens

Once you have a Client ID and Secret you need to call the Cyclr API OAuth token endpoint to generate an access token

https://\{you-instance-url\}/oauth/token

#### Required parameters

| Parameter | Description | Example |
| --- | --- | --- |
| grant_type | Identifies the OAuth flow being used. Must be client_credentials | client_credentials |
| client_id | Identifies the Cyclr Partner the token is for | abcdefg |
| client_secret | The matching secret for the client ID | abcdefghij123 |

#### Example Request

```http
POST https://yourCyclrInstance/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id=abcdefg&client_secret=abcdefghij123
````

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
POST https://yourCyclrInstance/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id=abcdefg&client_secret=abcdefghij123&scope=account:{account_id}
````