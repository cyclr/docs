---
title: Deploy Marketplace
sidebar: cyclr_sidebar
permalink: marketplace-deployment
tags: [marketplaces,embedding]
menus:
    marketplace:
        title: Deploy Marketplace
        identifier: marketplace-deployment
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">
When integrating with a Cyclr Marketplace you can decide whether all users access it using the same built-in Account-level "API User" (**Account Marketplace** - this is the typical approach), or create separate users for each in the Cyclr Account (**User Marketplace**).

To enable your users to view a Marketplace and install templates, you will need to have an "Integrations" button or link within your own application's interface.

</section>
<section class="card">
## Account Marketplace

When a user clicks the **Integrations** button, your application server should make a Request towards the Cyclr REST API's `/v1.0/accounts/CYCLR_ACCOUNT_API_ID/marketplace` endpoint to obtain a **Marketplace URL**.  The user can then be directed to this URL in their web browser.

The **CYCLR_ACCOUNT_API_ID** used in the URL of the call tells Cyclr which Account to work against.  If an Account doesn't already exist with that API ID, then Cyclr will create a *new* Account using that value as the API ID and the **AccountName** value provided in your Request.

### Request

```
curl -X POST
-H "Authorization: Bearer ACCESS_TOKEN"
-H "Content-Type: application/json"
-H "Accept: application/json"

-d '{
    "MarketplaceId": MARKETPLACE_ID,
    "AccountName": "CYCLR_ACCOUNT_NAME",
    "PartnerConnector": {
        "Name": "Example Connector",
        "Version": "1.0",
        "AuthValue": "XXXXXXXXXX",
        "Properties": [{"Name": "Url", "Value": "http://customDomain.appName.com"}]
    }
}' "https://yourCyclrInstance/v1.0/accounts/CYCLR_ACCOUNT_API_ID/marketplace"
```

**All PartnerConnector Property Values must be passed as strings, even if they are numbers.**

In the example above, replace *yourCyclrInstance* with your [**API Domain** according to where your Cyclr Console is located](./testing-cyclr-api) (e.g. "api.cyclr.com"), or your own domain if your Cyclr instance is self-hosted.

When [obtaining a Cyclr API Access Token](./cyclr-api-authentication) for this call, you should *not* use an Account Restricted Token.

<table>
    <thead>
        <tr>
            <th>Request Parameter</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
        <tr>
            <th colspan="3">Marketplace &amp; Account<br/>
            <small>Parameters required to identify the Marketplace to show and Account to work in</small></th>
        </tr>
    </thead>
    <tr>
        <td>MarketplaceId</td>
        <td>The numeric ID of the Marketplace to view.<br />
            You can find this through your Cyclr Console in your web browser's address bar after pressing <strong>Edit</strong> on your Marketplace, e.g.: https://my.cyclr.uk/console/2/marketplaces/category?categoryId=10</td>
        <td>10</td>
    </tr>
    <tr>
        <td>AccountName</td>
        <td>(Optional) If the <strong>CYCLR_ACCOUNT_API_ID</strong> value provided in the Request's URL doesn't match an existing Cyclr Account, a new Account will be created using this name.  If no AccountName is provided, the CYCLR_ACCOUNT_API_ID value will be used as the new Account's name.</td>
        <td>New Cyclr Account Name</td>
    </tr>
    <tr>
        <td>AccountDescription</td>
        <td>(Optional) If the <strong>CYCLR_ACCOUNT_API_ID</strong> value you provide in the request's URL doesn't match an existing Cyclr account, it creates a new with this description.</td>
        <td>This is a Marketplace created account</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">Connector Authentications<br/>
            <small>Optional parameter to install pre-authenticated "partner connectors" into the Account.</small></th>
        </tr>
    </thead>
    <tr>
        <td>[ConnectorAuthentications]</td>
        <td>Providing your own platform's Cyclr Connector objects here means your users will not be expected to authenticate against your platform during the Marketplace flow.</td>
        <td></td>
    </tr>
    <tr>
        <td>[ConnectorAuthentications].Name</td>
        <td>The name to give this instance of your Connector in the Account.</td>
        <td>Connector Name</td>
    </tr>
    <tr>
        <td>[ConnectorAuthentications].Version</td>
        <td>The version of the partner connector to be installed.</td>
        <td>1.0</td>
    </tr>
    <tr>
        <td>[ConnectorAuthentications].AuthenticationId</td>
        <td>The ID of the authentication method you want this instance of your Connector to use. If the Connector only supports one form of authentication, this value becomes optional.</td>
        <td>0000000-0000-0000-0000-000000000000</td>
    </tr>
    <tr>
        <td>[ConnectorAuthentications].AuthValue</td>
        <td>(Optional) Authentication value for your platform connector.
        If your platform requires a username and password, provide a base64 encoded version of "username:password".  
        Provide API keys as plain text.
        An OAuth token may also be provided here.</td>
        <td>dXNlcm5hbWU6cGFzc3dvcmQ=<br />
or<br />
NJ88GGgv79V79VvYFBBTHUIGu</td>
    </tr>
    <tr>
        <td style="white-space: nowrap">[ConnectorAuthentications].[Properties]</td>
        <td>An array of properties required by the partner connector for successful installation. Required by some Connectors.</td>
        <td>[ {"Name": "Url", "Value": "http://customDomain.appName.com"} ]</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">Marketplace Display Options<br/>
            <small>Optional parameters to change the display behaviour of Marketplace</small></th>
        </tr>
    </thead>
    <tr>
        <td>InlineOAuth</td>
        <td>Defaults to true. Set it to false if you are running Marketplace in an HTML iframe and want OAuth redirect pages to be opened in a popup.</td>
        <td>false</td>
    </tr>
</table>

### Response

```json
{
    "AccountId": "CYCLR_ACCOUNT_API_ID",
    "ExpiresAtUtc": "2020-01-01T12:30:00.000Z",
    "MarketplaceUrl": "https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch/marketplace/10",
    "Token": "lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ="
}
```

<table>
    <thead>
        <tr>
            <th>Response Field</th>
            <th>Description</th>
            <th>Example Value</th>
        </tr>
    </thead>
    <tr>
        <td>AccountId</td>
        <td>The ID of the newly created account, or the existing account you provided in your Request.</td>
        <td>CustomerXYZ</td>
    </tr>
    <tr>
        <td>ExpiresAtUtc</td>
        <td>When the Token and MarketplaceUrl will expire.</td>
        <td>2020-01-01T12:30:00.000Z</td>
    </tr>
    <tr>
        <td>MarketplaceUrl</td>
        <td>The URL that your user should be sent to, typically opened in a popup browser window.  
            Once generated by Cyclr, this URL will only be valid for 5 minutes and will expire when first accessed.  You should therefore direct your user to it immediately after receiving it.</td>
        <td style="word-break: break-all">https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch/marketplace/10</td>
    </tr>
    <tr>
        <td>Token</td>
        <td>Marketplace URL token.</td>
        <td style="word-break: break-all">lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ=</td>
    </tr>
</table>

> After deploying a Marketplace you will see an "API User" in your Cyclr console.
> The "API User" has access to the Account, however they cannot signin to the Cyclr interface.


</section>
<section class="card">
## User Marketplace

When a user clicks the **Integrations** button, your application server should make a Request towards the Cyclr REST API's `/v1.0/users/marketplace` endpoint to obtain a **Marketplace URL**.  The user can then be directed to this URL in their web browser.

### Request

```
curl -X POST
-H "Authorization: Bearer ACCESS_TOKEN"
-H "Content-Type: application/json"
-H "Accept: application/json"

-d '{
    "MarketplaceId": MARKETPLACE_ID,
    "AccountName": "CYCLR_ACCOUNT_NAME",
    "AccountId": "CYCLR_ACCOUNT_API_ID",
    "Username": "USERNAME",
    "Password": "PASSWORD",
    "PartnerConnector": {
        "Name": "Example Connector",
        "Version": "1.0",
        "AuthValue": "XXXXXXXXXX",
        "Properties": [{"Name": "Url", "Value": "http://customDomain.appName.com"}]
    }
}' "https://yourCyclrInstance/v1.0/users/marketplace"
```

In the example above, replace *yourCyclrInstance* with your [**API Domain** according to where your Cyclr Console is located](./testing-cyclr-api), or your own domain if your Cyclr instance is self-hosted.

When [obtaining a Cyclr API Access Token](./cyclr-api-authentication) for this call, you should *not* use an Account Restricted Token.

<table>
    <thead>
        <tr>
            <th>Request Parameter</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
        <tr>
            <th colspan="3">Marketplace &amp; Account<br/>
            <small>Parameters required to identify the Marketplace to show and Account to work in</small></th>
        </tr>
    </thead>
    <tr>
        <td>MarketplaceId</td>
        <td>The numeric ID of the Marketplace to view.<br />
            You can find this through your Cyclr Console in your web browser's address bar after pressing <strong>Edit</strong> on your Marketplace, e.g.: https://my.cyclr.uk/console/2/marketplaces/category?categoryId=10</td>
        <td>10</td>
    </tr>
    <tr>
        <td>AccountId</td>
        <td>API ID of the Account to work in.</td>
        <td>CustomerXYZ</td>
    </tr>
    <tr>
        <td>AccountName</td>
        <td>(Optional) If the <strong>CYCLR_ACCOUNT_API_ID</strong> provided in the Request doesn't match an existing Cyclr Account, a new Account will be created using this name.  If no AccountName is provided, the CYCLR_ACCOUNT_API_ID value will be used as the new Account's name.</td>
        <td>New Cyclr Account Name</td>
    </tr>
    <tr>
        <td>AccountDescription</td>
        <td>(Optional) If the <strong>CYCLR_ACCOUNT_API_ID</strong> provided in the request doesn't match an existing Cyclr account, it creates a new account with this description.</td>
        <td>This is a Marketplace created account</td>
    </tr>
    <tr>
        <td>Username</td>
        <td>Username of the user accessing the Marketplace.</td>
        <td>USERNAME</td>
    </tr>
    <tr>
        <td>Password</td>
        <td>Password for the user.</td>
        <td>PASSWORD</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">Connector Authentications<br/>
            <small>Optional parameter to install pre-authenticated "partner connectors" into the Account.</small></th>
        </tr>
    </thead>
    <tr>
        <td>[ConnectorAuthentications]</td>
        <td>Providing your own platform's Cyclr Connector objects here means your users will not be expected to authenticate against your platform during the Marketplace flow.</td>
        <td></td>
    </tr>
    <tr>
        <td>[ConnectorAuthentications].Name</td>
        <td>The name to give this instance of your Connector in the Account.</td>
        <td>Connector Name</td>
    </tr>
    <tr>
        <td>[ConnectorAuthentications].Version</td>
        <td>The version of the partner connector to be installed.</td>
        <td>1.0</td>
    </tr>
    <tr>
        <td>[ConnectorAuthentications].AuthenticationId</td>
        <td>The ID of the authentication method you want this instance of your Connector to use. If the Connector only supports one form of authentication, this value becomes optional.</td>
        <td>0000000-0000-0000-0000-000000000000</td>
    </tr>
    <tr>
        <td>[ConnectorAuthentications].AuthValue</td>
        <td>(Optional) Authentication value for your platform connector.
        If your platform requires a username and password, provide a base64 encoded version of "username:password".  
        Provide API keys as plain text.
        An OAuth token may also be provided here.</td>
        <td>dXNlcm5hbWU6cGFzc3dvcmQ=<br />
or<br />
NJ88GGgv79V79VvYFBBTHUIGu</td>
    </tr>
    <tr>
        <td style="white-space: nowrap">[ConnectorAuthentications].[Properties]</td>
        <td>An array of properties required by the partner connector for successful installation. Required by some Connectors.</td>
        <td>[ {"Name": "Url", "Value": "http://customDomain.appName.com"} ]</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">Marketplace Display Options<br/>
            <small>Optional parameters to change the display behaviour of Marketplace</small></th>
        </tr>
    </thead>
    <tr>
        <td>InlineOAuth</td>
        <td>Defaults to true. Set it to false if you are running Marketplace in an HTML iframe and want OAuth redirect pages to be opened in a popup.</td>
        <td>false</td>
    </tr>
</table>

### Response

```json
{
    "AccountId": "CYCLR_ACCOUNT_API_ID",
    "ExpiresAtUtc": "2020-01-01T12:30:00.000Z",
    "MarketplaceUrl": "https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch/marketplace/10",
    "Token": "lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ="
}
```

<table>
    <thead>
        <tr>
            <th>Response Field</th>
            <th>Description</th>
            <th>Example Value</th>
        </tr>
    </thead>
    <tr>
        <td>AccountId</td>
        <td>The ID of the newly created account, or the existing account you provided in your Request.</td>
        <td>CustomerXYZ</td>
    </tr>
    <tr>
        <td>ExpiresAtUtc</td>
        <td>When the Token and MarketplaceUrl will expire.</td>
        <td>2020-01-01T12:30:00.000Z</td>
    </tr>
    <tr>
        <td>MarketplaceUrl</td>
        <td>The URL that your user should be sent to, typically opened in a popup browser window.  
            Once generated by Cyclr, this URL will only be valid for 5 minutes and will expire when first accessed.  You should therefore direct your user to it immediately after receiving it.</td>
        <td style="word-break: break-all">https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch/marketplace/10</td>
    </tr>
    <tr>
        <td>Token</td>
        <td>Marketplace URL token.</td>
        <td style="word-break: break-all">lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ=</td>
    </tr>
</table>

</section>
