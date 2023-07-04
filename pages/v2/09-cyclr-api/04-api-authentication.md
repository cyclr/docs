---
title: API authentication
sidebar: cyclr_sidebar
permalink: cyclr-api-authentication
tags: [api]
menus:
    cyclr-api:
        title: API authentication
        identifier: cyclr-api-authentication
        toggleonly: menutoggleonly
        weight: 4
---
{::options parse_block_html="true" /}
<section class="card">
You can use the [OAuth 2.0](https://oauth.net/2/) Client Credentials flow to authenticate with the Cyclr API.

There are certain values you need to use in order to make different calls to the Cyclr API:

*  [**API domain**](#api-domain) `{CyclrAPIDomain}`
*  [**Access token**](#access-token) `{access_token}`
*  [**Account ID**](#account-id) `{AccountId}`
*  [**Client ID** and **Client Secret**](#client-id-and-client-secret) `{client_id}`, `{client_secret}`
*  [**Service domain**](#service-domain) `{YourServiceDomain}`


</section>
<section class="card">
## API domain

The API domain you use to make API calls depends on where your Cyclr Console is hosted: 

| **Cyclr Console Location** | **API Domain**             |
|:---------------------------|:---------------------------|
| my.cyclr.com               | api.cyclr.com      |
| my.cyclr.uk                | api.cyclr.uk       |
| eu.cyclr.com               | api.eu.cyclr.com   |
| apac.cyclr.com             | api.apac.cyclr.com |


>  **Note**: Replace `{CyclrAPIDomain}` or `{CyclrAPIDomain}` in example calls with the correct domain for your console location.


</section>
<section class="card">
## Access token

All calls to the Cyclr must provide the access token in the Authorize HTTP request header:

```html
Authorization: Bearer {access_token}
```

Tokens expire after 14 days, so remember to generate a new one when necessary.

### Request
Once you have a **Client ID** and **Client Secret**, you can call the Cyclr API OAuth token endpoint to generate an access token.

```
POST https://{CyclrAPIDomain}/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id={client_idi}&client_secret={client_secret}
```

#### Query string parameters

These parameters are in the request body:

| Parameter | Description |
| --- | --- |
| grant_type | Use `client_credentials` to identify the OAuth flow. |
| client_id | Enter the **Client ID** to identify which Cyclr Partner the token is for. |
| client_secret | Enter the matching **Client Secret** for the Cyclr Partner. |

### Example Response

```js
{
    "token_type": "bearer",
    "access_token": "************",
    "expires_in": 1209599,
    "clientId": "************"
}
```

#### Response parameters

| Parameter | Description |
| --- | --- |
| `token_type` | The type of token is always `bearer`. |
| `access_token` | The token you use to make requests to the Cyclr API. |
| `expires_in` | The amount of time in seconds until the access token expires. |
| `clientId` | The **Client ID** you provide when you make the request. |


</section>
<section class="card">

## Account ID

For calls to API methods that relate to an account, you need to provide the **Account ID**  as a HTTP header in the request:

```html
X-Cyclr-Account: {AccountID}
```

To view an **Account ID** in your Cyclr console, go to **Accounts** > **Account Management** and select the **Settings** icon for the account you want to use.

The **Account ID** of an account is also displayed in the URL in this format: `accountId=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

### Account restricted access tokens

You can restrict access tokens to only work for a specific account if you include the **Account ID** in the scope when you make the [access token](#access-token) request:

```html
POST https://{API Domain}/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id=abcdefg&client_secret=abcdefghij123&scope=account:{account_id}
```


</section>
<section class="card">

## Client ID and Client Secret

To generate a **Client ID** and **Client Secret** from your Cyclr console:

1.  Go to **Settings** > **OAuth Client Credentials**.
2.  Select **Generate Credentials**.
3.  Write a description for the credential set, and select **Ok**.

The table displays the new **Client ID** next to the time you create it. To view the **Client Secret**, select the eye icon to the right side of the description.

![Cyclr Console OAuth Client Credentials](./images/cyclr-api-client-credentials.png)


</section>
<section class="card">

## Service domain

For some calls, you need to use your service domain, which is in the format: `{YourCompany}-h.cyclr.uk`.

To view your service domain in your Cyclr console, go to **Settings** > **General Settings**.

**Note**: Google doesn't verify third party domains, so you need to set up a custom domain to become a verified Google application.

For information on how to create a custom domain, see the [Custom Service Domains](custom-domains) documentation.
</section>
