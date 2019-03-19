---
title: API Authentication
sidebar: cyclr_sidebar
permalink: cyclr-api-authentication
tags: [embedding]
---

The Cyclr API authentication is provided using [OAuth2](https://oauth.net/2/). OAuth tokens are granted to either manage the partner or access and modify a partner account.

### Get access token

You need to get an access token from Cyclr by calling the token endpoint with either your email address &  
password that you use to login to Cyclr for access the partner API endpoints, or the username & password  
of an account user to access an account.

#### Request

**Partner access token**

```http
POST https://api.cyclr.com/oauth/token
Content-Type: application/x-www-form-urlencoded
client_id={ClientID}&grant_type=password&username={username}&password={password}
```

**Account access token**

```http
POST https://api.cyclr.com/oauth/token
Content-Type: application/x-www-form-urlencoded
client_id={ClientID}&client_secret={AccountID}&grant_type=password&username={username}&password={password}
```

*   **client_id** – the client ID of the Partner. This can be found in the Cyclr Console.
*   **client_secret** –  
    _(Optional)_ the ID of the account this token is for
*   **grant_type** – the Cyclr Partner API only supports the password grant\_type
*   **username** – the username of the authenticating user
*   **password **– the password for the user

#### Response

```json
{
    "access_token": "************",
    "token_type": "bearer",
    "expires_in": 1209599,
    "refresh_token": "************",
    "userName": "************",
    "clientId": "************",
    ".issued": "Thu, 24 Nov 2016 16:32:59 GMT",
    ".expires": "Thu, 08 Dec 2016 16:32:59 GMT"
}
```

*   **access_token** – the token used when making requests to the API
*   **expires_in** – the amount of time in seconds until access_token will expire
*   **refresh_token** – the token that can be used to generate a new access token without the username and  
    password

### Refresh access token

To refresh an access token, before or after expiry, you need to call the oauth token endpoint with a **grant_type** of **refresh_token** and pass the refresh token that was included with the current access token. Once refreshed the old token will be no longer work.

```http
POST https://api.cyclr.com/oauth/token
Content-Type: application/x-www-form-urlencoded
client_id={ClientID}&grant_type=refresh_token&refresh_token={RefreshToken}
```

### Calling an API method

To authenticate your requests you need to include the access token in the Authorization HTTP header.

```http
Authorization: Bearer {AccessToken}
```

[View Cyclr’s API Endpoints](./api-endpoints)
