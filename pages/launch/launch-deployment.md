---
title: LAUNCH Deployment
sidebar: cyclr_sidebar
permalink: launch-deployment
tags: [launch]
---

## Overview

When integrating with LAUNCH you can decide whether all users access it using the same built-in Account-level "API User" (**Account LAUNCH** - this is the typical approach), or create separate users for each in the Cyclr Account (**User LAUNCH**).


To enable your users to add an integration, present a "Connect" button or link within your application's interface.

For example:

![Generic Host Application](./images/generic-host-app.png)



## Account LAUNCH

When a user clicks the **Connect** button, your application server should make a Request towards the Cyclr REST API's `/v1.0/accounts/CYCLR_ACCOUNT_API_ID/launch` endpoint to obtain a **LAUNCH URL**.  The user can then be directed to this URL in their web browser.

### Request
```
curl -X POST
-H "Authorization: Bearer ACCESS_TOKEN"
-H "Content-Type: application/json"
-H "Accept: application/json"

-d '{
    "AccountName": "CYCLR_ACCOUNT_NAME",
    "PartnerConnector": {
        "Name": "Example Connector",
        "Version": "1.0",
        "AuthValue": "XXXXXXXXXX",
        "Properties": [{"Name": "Url", "Value": "http://customDomain.appName.com"}]
    }
}' "https://yourCyclrInstance/v1.0/accounts/CYCLR_ACCOUNT_API_ID/launch"
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
            <th colspan="3">Account</th>
        </tr>
    </thead>
    <tr>
        <td>AccountName</td>
        <td>(Optional) If the <strong>CYCLR_ACCOUNT_API_ID</strong> value provided in the Request's URL doesn't match an existing Cyclr Account, a new Account will be created using this name.  If no AccountName is provided, the CYCLR_ACCOUNT_API_ID value will be used as the new Account's name.</td>
        <td>New Cyclr Account Name</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">Launched Cycle Options<br/>
            <small>Optional parameters to control the initial behaviour of the launched Cycle</small></th>
        </tr>
    </thead>
    <tr>
        <td>Start</td>
        <td>Defaults to true. Set to false if you don't want the launched Cycle to be started.</td>
        <td>false</td>
    </tr>
    <tr>
        <td>RunOnce</td>
        <td>Defaults to false. Set it to true if the Cycle being installed should only run once, then stop.</td>
        <td>true</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">Partner Connector<br/>
            <small>Optional parameter to install a pre-authenticated "partner connector" into the Account.  Only used if an Account is created by the call.</small></th>
        </tr>
    </thead>
    <tr>
        <td>PartnerConnector</td>
        <td>Providing your own platform's Cyclr Connector object here means your users will not be expected to authenticate against your platform during the LAUNCH flow.</td>
        <td></td>
    </tr>
    <tr>
        <td>PartnerConnector.Name</td>
        <td>The name to give this instance of your Connector in the Account.</td>
        <td>Connector Name</td>
    </tr>
    <tr>
        <td>PartnerConnector.Version</td>
        <td>The version of the partner connector to be installed.</td>
        <td>1.0</td>
    </tr>
    <tr>
        <td>PartnerConnector.AuthValue</td>
        <td>(Optional) Authentication value for your platform connector.
        If your platform requires a username and password, provide a base64 encoded version of "username:password".  
        Provide API keys as plain text.
        An OAuth token may also be provided here.</td>
        <td>dXNlcm5hbWU6cGFzc3dvcmQ=<br />
or<br />
NJ88GGgv79V79VvYFBBTHUIGu</td>
    </tr>
    <tr>
        <td>PartnerConnector.[Properties]</td>
        <td>An array of properties required by the partner connector for successful installation. Required by some Connectors.</td>
        <td>[ {"Name": "Url", "Value": "http://customDomain.appName.com"} ]</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">LAUNCH Options</th>
        </tr>
    </thead>
    <tr>
        <td>Tags</td>
        <td>An array of Tags that a Cycle must have at least one of to appear through LAUNCH.</td>
        <td>["CRM", "Email"]</td>
    </tr>
    <tr>
        <td>InlineOAuth</td>
        <td>Defaults to true. Set it to false if you are running LAUNCH in an HTML iframe and want OAuth redirect pages to be opened in a popup.</td>
        <td>false</td>
    </tr>
    <tr>
        <td>AutoInstall</td>
        <td>Defaults to true so that Cyclr will automatically start installation of a Template if only one is returned, avoiding the need for the user to select it. Set this to false to prevent that, requiring the user to select it instead.</td>
        <td>false</td>
    </tr>
    <tr>
        <td>SingleInstall</td>
        <td>Defaults to false so that Templates are shown whether they have been installed or not. Set to true to only show Templates that haven't already been installed in the Account.</td>
        <td>true</td>
    </tr>
    <tr>
        <td>CompleteParameter</td>
        <td>A value to pass through to the final page of the LAUNCH flow.</td>
        <td></td>
    </tr>
</table>

### Response

```json
{
    "AccountId": "CYCLR_ACCOUNT_API_ID",
    "ExpiresAtUtc": "2020-01-01T12:30:00.000Z",
    "LaunchUrl": "https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch",
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
        <td>When the Token and LAUNCH URL will expire.</td>
        <td>2020-01-01T12:30:00.000Z</td>
    </tr>
    <tr>
        <td>LaunchUrl</td>
        <td>The URL that your user should be sent to, typically opened in a popup browser window.  
            Once generated by Cyclr, this URL will only be valid for 5 minutes and will expire when first accessed.  You should therefore direct your user to it immediately after receiving it.</td>
        <td style="word-break: break-all">https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch</td>
    </tr>
    <tr>
        <td>Token</td>
        <td>LAUNCH URL token.</td>
        <td style="word-break: break-all">lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ=</td>
    </tr>
</table>

> After deploying LAUNCH you will see an "API User" in your Cyclr console.
> The "API User" has access to the Account, however they cannot signin to the Cyclr interface.

[How to Handle Callbacks](./handling-callback)

## User LAUNCH

When a user clicks the **Connect** button, your application server should make a request towards the Cyclr REST API's _/v1.0/users/launch_ endpoint:

> A new user will be created if the don't already exist.

### Request
```
curl -X POST
-H "Authorization: Bearer ${ACCESS_TOKEN}"
-H "Content-Type: application/json"
-H "Accept: application/json"

-d '{
    "AccountId": "0000000-0000-0000-0000-000000000000",
    "Username": "example",
    "Password": "P4$$w0rd",
    "PartnerConnector": {
        "Name": "Connector Name",
        "Version": "1.0",
        "AuthValue": "00000000000000000000000000000000000000000",
        "Properties": [{"Name": "Url", "Value": "https://myapp.something.blah"}]
    }
}' "https://yourCyclrInstance/v1.0/users/launch"
```

Replace *yourCyclrInstance* with *api.cyclr.com*, *api.cyclr.uk*, or your own domain if your Cyclr instance is self-hosted.

You should use a non-account restricted OAuth token as the Authorization for this request.

<table>
    <thead>
        <tr>
            <th>Request parameters</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
        <tr>
            <th colspan="3">Account</th>
        </tr>
    </thead>
    <tr>
        <td>AccountId</td>
        <td>ID of the account.</td>
        <td>0000000-0000-0000-0000-000000000000</td>
    </tr>
    <tr>
        <td>Username</td>
        <td>Username of the user the LAUNCH is for.</td>
        <td>example</td>
    </tr>
    <tr>
        <td>Password</td>
        <td>The users password.</td>
        <td>P4$$w0rd</td>
    </tr>
    <tr>
        <td>AccountName</td>
        <td>(Optional) If the account ID doesn't exist it will be created, you can include a name for the account otherwise the ID will be used as the name.</td>
        <td>New Cyclr Account Name</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">Launched Cycle Options<br/>
            <small>Optional parameters to control the initial behaviour of the launched cycle</small></th>
        </tr>
    </thead>
    <tr>
        <td>Start</td>
        <td>Defaults to true. Set to false if you don't want the launched cycle to be started.</td>
        <td>false</td>
    </tr>
    <tr>
        <td>RunOnce</td>
        <td>Defaults to false. Set it to true if the cycle being installed should only run once, then pause.</td>
        <td>true</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">Partner Connector<br/>
            <small>Optional parameter to install a pre-authenticated partner connector into the account.  Only used if an Account is created.</small></th>
        </tr>
    </thead>
    <tr>
        <td>PartnerConnector</td>
        <td>Providing your own platform's Cyclr Connector object here means your users will not be expected to authenticate against your platform during the LAUNCH flow.
        </td>
        <td></td>
    </tr>
    <tr>
        <td>PartnerConnector.Name</td>
        <td>The name to give this instance of your Connector in the Account.</td>
        <td>Connector Name</td>
    </tr>
    <tr>
        <td>PartnerConnector.Version</td>
        <td>The version of the partner connector to be installed.</td>
        <td>1.0</td>
    </tr>
    <tr>
        <td>PartnerConnector.AuthValue</td>
        <td>(Optional) Authentication value for your platform connector.
        If your platform requires a username and password, provide a base64 encoded version of "username:password".  
        Provide API keys as plain text.
        An OAuth token may also be provided here.</td>
        <td>dXNlcm5hbWU6cGFzc3dvcmQ=<br />
or<br />
NJ88GGgv79V79VvYFBBTHUIGu</td>
    </tr>
    <tr>
        <td>PartnerConnector.[Properties]</td>
        <td>An array of properties required by the partner connector for successful installation. This is not relevant to all connectors.</td>
        <td>[ {"Name": "Url", "Value": "http://customDomain.appName.com"} ]</td>
    </tr>
    <thead>
        <tr>
            <th colspan="3">LAUNCH Display Options<br/>
            <small>Optional parameters to filter the displayed templates shown in LAUNCH</small></th>
        </tr>
    </thead>
    <tr>
        <td>Tags</td>
        <td>An array of tags that a cycle must have at least one of to appear in LAUNCH.</td>
        <td>["CRM", "Email"]</td>
    </tr>
    <tr>
        <td>InlineOAuth</td>
        <td>Defaults to true. Set it to false if you are running LAUNCH in an iFrame and want OAuth redirect pages to be opened in a popup.</td>
        <td>false</td>
    </tr>
    <tr>
        <td>AutoInstall</td>
        <td>Defaults to true so that Cyclr will automatically start installation of a template if only one is returned, avoiding the need for the user to select it. Set this to false to prevent that, requiring the user to select it instead.</td>
        <td>false</td>
    </tr>
    <tr>
        <td>SingleInstall</td>
        <td>Defaults to false so that templates are shown whether they have been installed or not. Set to true to only show templates that aren't installed in the account.</td>
        <td>true</td>
    </tr>
    <tr>
        <td>CompleteParameter</td>
        <td>A value to pass through to the final page of the LAUNCH flow.</td>
        <td></td>
    </tr>
</table>

### Response

```json
{
    "AccountId": "0000000-0000-0000-0000-000000000000",
    "ExpiresAtUtc": "2020-01-01T12:30:00.000Z",
    "LaunchUrl": "https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch",
    "Token": "lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ="
}
```

<table>
    <thead>
        <tr>
            <th>Response fields</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
    </thead>
    <tr>
        <td>AccountId</td>
        <td>The ID of the newly created account or the existing account you provided in your request.</td>
        <td>0000000-0000-0000-0000-000000000000</td>
    </tr>
    <tr>
        <td>ExpiresAtUtc</td>
        <td>Token expiry timestamp.</td>
        <td>2020-01-01T12:30:00.000Z</td>
    </tr>
    <tr>
        <td>LaunchUrl</td>
        <td>The URL that your user should be sent to, typically opened in a popup browser window.  
  
Once generated by Cyclr, this URL will only be valid for 5 minutes and will expire when first accessed.  You should therefore direct your user to it immediately after receiving it.</td>
        <td style="word-break: break-all">https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch</td>
    </tr>
    <tr>
        <td>Token</td>
        <td>LAUNCH URL token.</td>
        <td style="word-break: break-all">lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ=</td>
    </tr>
</table>

[How to Handle Callbacks](./handling-callback)
