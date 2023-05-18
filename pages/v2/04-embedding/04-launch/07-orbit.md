---
title: ORBIT
sidebar: cyclr_sidebar
permalink: orbit
tags: [launch]
menus:
    launch:
        title: ORBIT
        identifier: orbit
        toggleonly: menutoggleonly
        weight: 7
---
{::options parse_block_html="true" /}
<section class="card">
ORBIT is LAUNCH’s companion, and gives your users a screen where they can view their installed integrations, as well as pause and delete them.

As a prepackaged integration management solution, you can deploy ORBIT in a similar way to LAUNCH and it’s accessible to your users via a pop-up, modal or iframe.

You can also customize the styling and layout of your ORBIT screen from your Cyclr console. To set your own custom HTML and CSS, go to **Settings** > **Appearance Settings**.

</section>
<section class="card">

## Deploy ORBIT

To obtain the ORBIT URL, you can make a call to the [`POST /v1.0/accounts/{id}/orbit`](https://api.cyclr.uk/docs/index#!/Accounts/Accounts_CreateUserOrbitToken_POST) endpoint. Make sure to use a non-account restricted OAuth token as the Authorization for this request.

### Request to Cyclr API

```h
curl -X POST
-H "Authorization: Bearer ${ACCESS_TOKEN}"
-H "Content-Type: application/json"
-H "Accept: application/json"
-d '{}' "https://yourCyclrInstance/v1.0/accounts/{AccountId}/orbit"
```
For more information on how to authenticate with the Cyclr API, see the page on [API authentication](cyclr-api-authentication).

</section>
<section class="card">

## ORBIT Response

The request receives a JSON response from the Cyclr API. If you use the `OrbitUrl`, this signs the user into the account and takes them to view the ORBIT screen.

> **Note**: The `OrbitUrl` is only valid for 5 minutes after you generate it.

```h
{
    "AccountId": "0000000-0000-0000-0000-000000000000",
    "ExpiresAtUtc": "2018-01-01T00:00:00+00:00",
    "OrbitUrl": "https://hostapp.cyclr.com/account/signinwithtoken?token=abc123&returnUrl=%2Forbit",
    "Token": "abc123"
}
```

### Response parameters

| **Response paramter** | **Description** | **Example** |
|---|---|---|
| `AccountId` | The ID of the newly created account or the existing account you provide in your request. | `0000000-0000-0000-0000-000000000000` |
| `ExpiresAtUtc` | The token's expiry timestamp. | `17/01/2018 12:11:22` |
| `OrbitUrl` | The URL that you can send your user to, typically opened in a popup browser window.  | `https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch` |
| `Token` | The Orbit URL token. | `lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ=` |

When you generate the ORBIT URL, it's valid for 5-minutes and for a single request only, so you need to pass your user to the URL immediately and one time only.

> **Note**: After you deploy ORBIT, your console displays an API User. The API User has access to the account, but they can’t sign in to the Cyclr interface.

</section>
