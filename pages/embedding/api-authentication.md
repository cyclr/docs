---
title: API Authentication
sidebar: cyclr_sidebar
permalink: cyclr-api-authentication
tags: [embedding]
---

Authentication with the Cyclr API is provided using the [OAuth 2.0](https://oauth.net/2/) Password Grant flow.

### Get Access & Refresh Tokens

To get an access token you need to call the Cyclr API OAuth token endpoint

https://\{you-instance-url\}/oauth/token

#### Required parameters

| Parameter | Description | Example |
| --- | --- | --- |
| client_id | Identifies the Cyclr Partner the token is for | abcdefg |
| grant_type | Identifies the OAuth flow being used. Must be password | password |
| username | Username of the user generating the token | you%40example.com |
| password | Password for the user generating the token | abc123 |

#### Example Request

```http
POST https://yourCyclrInstance/oauth/token
Content-Type: application/x-www-form-urlencoded

client_id=abcdefg&grant_type=password&username=you%40example.com&password=abc123
````

#### Example Response

```json
{
    "token_type": "bearer",
    "access_token": "************",
    "refresh_token": "************",
    "expires_in": 1209599,
    "userName": "************",
    "clientId": "************"
}
```

| Parameter | Description |
| --- | --- |
| token_type | The type of token, this is always bearer |
| access_token | Token to use when making requests to the Cyclr API |
| refresh_token | Token that can be used to generate a new access token without needing to provide username and password |
| expires_in | The amount of time in seconds until access_token will expire |
| userName | Username provided when getting the token |
| clientId | Client ID provided when getting the token |

### Using the Access Token

All calls to the Cyclr must provide the access token in the Authorize HTTP request header.

```http
Authorization: Bearer {access_token}
````

#### Accessing Account Methods

For any calls to API methods that relate to an account the ID of the account must be provided as a HTTP header in the request.

```http
X-Cyclr-Account: {AccountID}
````

### Refreshing the Access Token

The access_token will expire and stop authenticating, to continue using the token a refresh must be made. This can happen before or after the access_token has expired.
To refresh the access_token we will call the /oauth/token endpoint again, but with different parameters. Once used the refresh_token and access_token are no longer valid, you should from then on use the new tokens returned from the refresh call.

| Parameter | Description | Example |
| --- | --- | --- |
| client_id | Identifies the Cyclr Partner the token is for | abcdefg |
| grant_type | Identifies the OAuth flow being used. Must be refresh_token | refresh_token |
| refresh_token | The refresh_token that was provided with the access token | abcdegfhigjk123xyz |

#### Example Request

```http
POST https://yourCyclrInstance/oauth/token
Content-Type: application/x-www-form-urlencoded

client_id=abcdefg&grant_type=refresh_token&refresh_token=abcdegfhigjk123xyz
```

#### Example Response

```json
{
    "token_type": "bearer",
    "access_token": "************",
    "refresh_token": "************",
    "expires_in": 1209599,
    "userName": "************",
    "clientId": "************"
}
```

| Parameter | Description |
| --- | --- |
| token_type | The type of token, this is always bearer |
| access_token | Token to use when making requests to the Cyclr API |
| refresh_token | Token that can be used to generate a new access token without needing to provide username and password |
| expires_in | The amount of time in seconds until access_token will expire |
| userName | Username provided when getting the token |
| clientId | Client ID provided when getting the token |


### Account Restricted Tokens

If required you can restrict access_tokens to only work for a specific account by including the account ID as client_secret parameter when getting and refreshing tokens.
