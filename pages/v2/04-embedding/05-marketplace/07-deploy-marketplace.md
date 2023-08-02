---
title: Deploy a Marketplace
sidebar: cyclr_sidebar
permalink: marketplace-deployment
tags: [marketplaces,embedding]
menus:
    marketplace:
        title: Deploy a Marketplace
        identifier: marketplace-deployment
        toggleonly: menutoggleonly
        weight: 7
---
{::options parse_block_html="true" /}
<section class="card">

There are two types of Marketplace. An **Account Marketplace** has a built-in API account that all users use to access the Marketplace. A **User Marketplace** needs you to create separate user profiles for each user in your Cyclr account.

You need an **Integrations** button in your application’s interface to allow your users to view a marketplace and install templates.

1. Make the following request from your application server to the Cyclr REST API’s [/v1.0/accounts/{id}/marketplace](https://api.cyclr.uk/docs/index#!/Accounts/Accounts_Marketplace_POST) endpoint to get a Marketplace URL.
2. Direct the user to the URL in their web browser.

> **Note**: If you deploy a Marketplace, you can see an API User in your Cyclr console. The API User has access to the account, but can’t sign in to the Cyclr interface.

</section>
<section class="card">

## Deploy Marketplace request

```
curl -X POST
-H "Authorization: Bearer {access_token}"
-H "Content-Type: application/json"
-H "Accept: application/json"

-d '{
    "MarketplaceId": {MarketplaceId},
    "AccountName": "{CyclrAccountName}",
    "ConnectorAuthentications": {
        "Name": "{ExampleConnector}",
        "Version": "{VersionNumber}",
	    "AuthenticationId": "{AuthenticationId}",
        "AuthValue": "{AuthenticationValue}",
        "Properties": [{"Name": "{Url}", "Value": "{http://customDomain.appName.com}"}]
    }
}' "https://{yourCyclrDomain}/v1.0/accounts/{AccountId}/marketplace
```

> **Note**: Pass all `ConnectorAuthentications` property values as strings, even if they’re numbers.

### Parameters

<table>
<thead>
  <tr>
    <th colspan="2"><strong>Request parameter</strong></th>
    <th><strong>Type</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="2"><code>{access_token}</code></td>
    <td>string</td>
    <td>Enter your <a href="https://docs.cyclr.com/cyclr-api-authentication#access-token" target="_blank" rel="noopener noreferrer">Access Token</a> to authenticate the Cyclr API.</td>
  </tr>
  <tr>
    <td colspan="2"><code>yourCyclrDomain</code></td>
    <td>string</td>
    <td>Specify your <a href="https://docs.cyclr.com/cyclr-api-authentication#api-domain" target="_blank" rel="noopener noreferrer">API domain</a> according to the location of your Cyclr console. If your Cyclr instance is self-hosted, this value is your own domain.</td>
  </tr>
  <tr>
    <td colspan="2"><code>MarketplaceID</code></td>
    <td>integer</td>
    <td>Identify the marketplace to show.</td>
  </tr>
  <tr>
    <td colspan="2"><code>InlineOAuth</code></td>
    <td>Boolean, <strong>optional</strong></td>
    <td>Set to <code>true</code> to open all redirect pages inline with the webpage. If you run Marketplace in a HTML iframe, set this parameter to false to open OAuth redirect pages as a popup.</td>
  </tr>
  <tr>
    <td colspan="2"><code>AccountName</code></td>
    <td>string, <strong>optional</strong></td>
    <td>Name the account if you create a new account.</td>
  </tr>
  <tr>
    <td colspan="2"><code>AccountDescription</code></td>
    <td>string, <strong>optional</strong></td>
    <td>Provide a description of the account.</td>
  </tr>
  <tr>
    <td colspan="2"><code>ConnectorAuthentications</code></td>
    <td>array, <strong>optional</strong></td>
    <td>Use connector authentication to avoid the need for your users to authenticate against your platform.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>Name</code></td>
    <td>string</td>
    <td>Name the instance of your connector in the account.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>Version</code></td>
    <td>string</td>
    <td>Specify the version of the partner connector that you install. For example, <code>1.0</code>.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>AuthenticationId</code></td>
    <td>string</td>
    <td>Identify the connector authentication method you want to use.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>AuthValue</code></td>
    <td>string</td>
    <td>If your platform needs a username and password, provide a base64 encoded version of "username:password". You can also use an OAuth token, or provided API keys as plain text.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>Properties</code></td>
    <td>Array, <strong>optional</strong></td>
    <td>Provide properties that some partner connectors need to successfully install.</td>
  </tr>
  <tr>
    <td colspan="2"><code>AccountId</code></td>
    <td>string</td>
    <td>Specify to Cyclr which account to use. If an account with this ID doesn’t exist, Cyclr creates a new account using this value.</td>
  </tr>
  <tr>
    <td><code>CompleteParameter</code></td>
    <td></td>
    <td>A custom value be included in the Marketplace webhook callback.</td>
  </tr>
</tbody>
</table>

</section>
<section class="card">

## Deploy Marketplace response

```
{
    "MarketplaceUrl": "{MarketplaceUrl}",
    "AccountId": "{AccountId}",
    "Token": "{UrlToken}",
    "ExpiresAtUtc": "{DateTimeValue}"
    
}
```

### Parameters

| **Response Field** | **Description** |
|:---|:---|
| `AccountId` | Provides the ID of either the new account, or the account that you specified in the request. |
| `ExpiresAtUtc` | Displays when the Token and MarketplaceUrl expires. |
| `MarketplaceUrl` | Provides the URL you can send your user to. This URL expires five minutes Cyclr generates it or when the user accesses it. |
| `Token` | Provides the Marketplace URL token. |

</section>
<section class="card">

## Deploy a user Marketplace

To deploy a user Marketplace, you can make the same request to the the Cyclr REST API’s [/v1.0/users/marketplace](https://api.cyclr.uk/docs/index#!/Users/Users_CreateUserMarketplaceToken_POST) endpoint.

To create the account, you need to pass two extra parameters in the request:

<table>
<thead>
  <tr>
    <th><strong>Request parameter</strong></th>
    <th><strong>Type</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>Username</code></td>
    <td>string</td>
    <td>Identify the user’s account.</td>
  </tr>
  <tr>
    <td><code>Password</code></td>
    <td>string</td>
    <td>Authenticate the user’s account.</td>
  </tr>
</tbody>
</table>

</section>
