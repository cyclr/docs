---
title: OAuth authentication link
sidebar: cyclr_sidebar
permalink: authenticate-link-api
tags: [accounts]

---

If the connector requires OAuth authentication to work with the third party API, you need to show the user a window to let them authenticate with their details.

If the user doesn’t have access to the Cyclr account, you can use an account one time sign in token:

1.  Call the `/v1.0/accounts/{id}/signintoken` endpoint to retrieve the one time sign in token.
2.  Build the URL.
3.  Send the URL to your user.

## Get a sign in token
You can use the sign in token to build a URL to send to the user. Call the [`/v1.0/accounts/{id}/signintoken`](https://api.cyclr.uk/docs/index#!/Accounts/Accounts_CreateOneTimeToken_POST_0) endpoint to retrieve the one time sign in token.

### Request
```
POST https://{yourCyclrInstance}/v1.0/accounts/{AccountId}/signintoken
Authorization: Bearer {access_token}
{
  "Username":"The username of user you want to sign in"
}
```
>  **Note**: If the user doesn’t already exist, this call creates one with this name.

### Response
```
{
  "Token":"***************************************",
  "ExpiresAtUtc":"2001-03-28T11:22:33.138Z"
}
```

## Build the URL
When you send the user the built URL, it redirects them to the third party OAuth flow. When they authenticate the account connector, the URL redirects the user to targetOrigin or a JavaScript message posts to the parent window.

```
https://{Partner Service Domain}/connectorauth/updateaccountconnectoroauth?id={AccountId}&token={SignInToken}&targetOrigin={RedirectURL}&callbackMessage={Message}
```
To view your Partner Service Domain, go to the console **Settings** > **General Settings**.

### URL query string

| **Parameter** | **Type** | **Description** |
|:---|:---|:---|
| `id` | integer | Enter the [`Id`](install-connector-api#example-response) of the installed connector you want the user to authenticate.  |
| `token` | string | Enter the account sign in [`Token`](#response). |
| `targetOrigin` | string | Specify what the origin of the other window must be to dispatch the javascript callback. If the callback message is null we will redirect to the targetOrigin |
| `callbackMessage` | string, optional | Write a callback message to send to the parent window. |

### Example built URL
```
https://PartnerServiceDomain]/connectorauth/updateaccountconnectoroauth?id=1&token=***************************************&targetOrigin=example.com&callbackMessage=done
```
## Related page

*  [User accounts overview](overview-new-account)
*  [API authentication](cyclr-api-authentication)