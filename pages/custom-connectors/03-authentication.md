---
title: Connector Authentication
sidebar: cyclr_sidebar
permalink: connector-authentication
tags: [connector-creation]
---

## Authentication Types

Cyclr supports various authentication types and, sometimes with the addition of scripting, it is possible to establish a connection with any API.

| Method | Description |
| --- | --- |
| ApiKey | The user should provide an API key as the HTTP header for the connector.|
| Basic  | The API uses HTTP basic authentication. |
| OAuth1 | The API uses OAuth 1.0a authentication. Requires: _ClientId _(also known as ConsumerKey), _ClientSecret _(also known as ConsumerSecret), _RequestTokenUrl_, _AuthorizeUrl_, _AccessTokenUrl_.|
| Auth2 | The API uses OAuth 2 authentication. Requires: _ClientId_, _ClientSecret_, _AuthoriseUrl_, _AccessTokenUrl_. |
| None | No authentication used.|
| AuthFields | the API needs to inject authentication fields into the POST message. Requires: _Name_, _Key_, _Type_. |

## OAuth2Type

These fields will only be used if the AuthType is OAuth2.

| Property | Description |
| ---- | ---- |
| AuthorisationCode | The client will redirect the user to the authorization server, the user will then be asked to login to the authorization server and approve the client.|
| ClientCredentials | Client will get the access token from the authorization server without user challenge.|
| PasswordCredentials | Client will get the access token from the authorization server using username and password.|


## Bearer Token

If an API requires a Bearer Token to be sent, for example when the API Key is used, then you can add Script at the Connector-level to prepend it with "Bearer " and set it as the **Authorization** HTTP Header in all Requests like this:

```javascript
function before_action() {
    method_request_headers.Authorization = 'Bearer ' + method_auth_value;
    return true;
}
```

Cyclr exposes the API Key entered during installation of the Connector through the **method_auth_value** variable in the **before_action** event.
