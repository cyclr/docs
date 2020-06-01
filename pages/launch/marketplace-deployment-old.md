---
title: Marketplace Deployment-old
sidebar: cyclr_sidebar
permalink: marketplace-deployment-old
tags: [marketplaces-old]
---

To enable your users to view a Marketplace, simply present a "Connect" button or link within your application’s UI.

For example:

![Generic Host Application](./images/generic-host-app.png)

When a user clicks the **Connect** button, your application server should make a request towards the Cyclr REST API's _/v1.0/accounts/{AccountId}/marketplace_ endpoint:

### Request

```
curl -X POST
-H "Authorization: Bearer ${ACCESS_TOKEN}"
-H "Content-Type: application/json"
-H "Accept: application/json"

-d '{
    "MarketplaceId": 123,
    "partnerConnector": {
        "Name": "Connector Name",
        "Version": "1.0",
        "AuthValue": "00000000000000000000000000000000000000000",
        "Properties": [{"Name": "Url", "Value": "https://myapp.something.blah"}]
    }
}' "https://yourCyclrInstance/v1.0/accounts/0000000-0000-0000-0000-000000000000/marketplace"
```
In the examples above, replace *yourCyclrInstance* with *api.cyclr.com*, *api.cyclr.uk*, or your own domain if your Cyclr instance is self-hosted.

You should use a non-account restricted OAuth token as the Authorization for this request.

<table>
    <thead>
        <tr>
            <th>Request Parameter</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
        <tr>
            <th colspan="3">Marketplace &amp; Account<br/>
            <small>Parameters required to identify the Marketplace to show and account name</small></th>
        </tr>
    </thead>
    <tr>
        <td>MarketplaceId</td>
        <td>The numeric ID of the Marketplace to view.<br />
            You can find this through your Cyclr Console in your web browser's address bar after pressing **Edit** on your Marketplace, e.g.: https://my.cyclr.uk/console/2/marketplaces/category?categoryId=27</td>
        <td>123</td>
    </tr>
    <tr>
        <td>AccountName</td>
        <td>(Optional) If the account ID doesn't exist it will be created, you can include a name for the account otherwise the ID will be used as the name.</td>
        <td>New Cyclr Account Name</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">Partner Connector<br/>
            <small>Optional parameter to install a pre-authenticated partner connector into the account</small></th>
        </tr>
    </thead>
    <tr>
        <td>partnerConnector</td>
        <td>Providing your own platform's Cyclr Connector object here means your users will not be expected to authenticate against your platform during the Marketplace flow.</td>
        <td></td>
    </tr>
    <tr>
        <td>partnerConnector.Name</td>
        <td>A name you wish to give this instance of your Connector installed within the new or existing account.</td>
        <td>Connector Name</td>
    </tr>
    <tr>
        <td>partnerConnector.Version</td>
        <td>The version of the partner connector to be installed.</td>
        <td>1.0</td>
    </tr>
    <tr>
        <td>partnerConnector.AuthValue</td>
        <td>(Optional) Authentication value for your platform connector.
        If your platform requires a username and password, provide a base64 encoded version of "username:password".  
        Provide API keys as plain text.
        An OAuth token may also be provided here.</td>
        <td>dXNlcm5hbWU6cGFzc3dvcmQ=<br />
or<br />
NJ88GGgv79V79VvYFBBTHUIGu</td>
    </tr>
    <tr>
        <td style="white-space: nowrap">partnerConnector.[Properties]</td>
        <td>An array of properties required by the partner connector for successful installation. This is not relevant to all connectors.</td>
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
    "AccountId": "0000000-0000-0000-0000-000000000000",
    "ExpiresAtUtc": "2020-01-01T12:30:00.000Z",
    "MarketplaceUrl": "https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch/marketplace/1",
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
        <td>The ID of the newly created account, or the existing account you provided in your request.</td>
        <td>0000000-0000-0000-0000-000000000000</td>
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
        <td style="word-break: break-all">https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch/marketplace/1</td>
    </tr>
    <tr>
        <td>Token</td>
        <td>Marketplace URL token.</td>
        <td style="word-break: break-all">lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ=</td>
    </tr>
</table>

> After deploying Marketplace you will see an API User in your Cyclr console.
> The API User has access to the account however they cannot signin to the Cyclr interface.