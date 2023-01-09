---
title: Embed Cyclr in an iframe
sidebar: cyclr_sidebar
permalink: iframe-embedding
tags: [embedding]
menus:
    embed-custom-ui:
        title: Embed with iframe
        identifier: iframe-embedding
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">
To embed Cyclr in an iframe within your own application, you will need to take the following steps:

1. Obtain an Access Token that enables you to make calls against the Cyclr API
2. Obtain a user-specific Sign-in Token
3. Build the URL for your iframe

### 1. Obtain a Cyclr API Access Token

#### Get Client ID and Secret

You can generate a Client ID and Secret from the Cyclr Partner Console by going to Settings > OAuth Client Credentials

![Cyclr Console OAuth Client Credentials](./images/cyclr-api-client-credentials.png)

Once you have a Client ID and Secret you need to call the Cyclr API OAuth Token endpoint to generate an Access Token.  The domain for that endpoint will be different depending on where your Cyclr Console is hosted:

Cyclr Console Location | API Domain
--- | ---
my.cyclr.com | https://api.cyclr.com
my.cyclr.uk | https://api.cyclr.uk
eu.cyclr.com | https://api.eu.cyclr.com

#### Required Request Body Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| grant_type | Identifies the OAuth flow being used. Must be `client_credentials` | client_credentials |
| client_id | Identifies the Cyclr Partner the token is for | abcdefg |
| client_secret | The matching secret for the client ID | abcdefghij123 |

#### Example Request

```html
POST https://{API Domain}/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id=abcdefg&client_secret=abcdefghij123
```
> NB. ``grant_type``, ``client_id`` and ``client_secret`` go in the Request Body - they are not added to the endpoint.

#### Example Response

```json
{
    "token_type": "bearer",
    "access_token": "************",
    "expires_in": 1209599,
    "clientId": "************"
}
```

### 2. Generate a User-Specific Sign-in Token

For this stage, you'll need the Access Token from the previous step, and the Cyclr Account's API ID.

To find this value in your Console, go to Accounts > Account Management and click the Settings button next to the Account - you'll see the API ID near the top:

![Cyclr Account API ID](./images/API_ID.png)

Make this call, specifying a user to sign in as.  If they don't already exist, they will be created:

```html
POST https://{API Domain}/v1.0/accounts/{API ID}/signintoken
Authorization: Bearer YOURACCESSTOKENHERE
Content-Type: application/json

{
	"Username" : "ApiUser"
}
```

This will return the following response:

```json
{
  "Token": "JWxm_cYOq0m6PYWcVPWpuSBP-ppqRwhBk",
  "ExpiresAtUtc": "2021-05-17T15:55:41.9993413Z"
}
```

**The Token returned will expire after 5 minutes and can only be used once**.  Each time you need to give a user access to a Cyclr Account through your iframe, you must generate a new Token.

### 3. Build the iframe's URL

Taking a Token returned above, build the URL to use as the value for a `src` attribute of an iframe in your application.

This is the structure of that URL:

`https://{Cyclr Service Domain}/account/signinwithtoken?token={Token}`

Your Service Domain can be found in your Cyclr Console under Settings > General Settings.

Here's how the full URL may look once set in the HTML code of a page in your application:

```html
<iframe src="https://myapp-h.cyclr.com/account/signinwithtoken?token=JWxm_cYOq0m6PYWcVPWpuSBP-ppqRwhBk"></iframe>
```

### Final Steps

You will need to check that iframe Embedding is turned ON in your Console under Settings > General Settings, and that you have added the domain hosting your application to the Host Source Whitelist.

For security reasons, the page hosting the iframe must be served over HTTPS.

</section>
