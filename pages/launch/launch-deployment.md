---
title: LAUNCH Deployment
sidebar: cyclr_sidebar
permalink: launch-deployment
tags: [launch]
---

To enable your users to add an integration, simply present a “Connect” button or link within your application’s UI.

For example:

![Generic Host Application](./images/generic-host-app.png)

When a user clicks the **Connect** button, your application server should make a request towards the Cyclr REST API's _/v1.0/users/launch_ endpoint:

```
curl -X POST
-H "Authorization: Bearer ${ACCESS_TOKEN}"
-H "Content-Type: application/json"
-H "Accept: application/json"

-d '{
    "Username": "user@example.com", 
    "Password": "password",
    "AccountId": "0000000-0000-0000-0000-000000000000",
    "partnerConnector": {
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
            <th colspan="3">User &amp; Account Details<br/>
            <small>Parameters required to authorize the user &amp; identify the account templates will be launched into</small></th>
        </tr>
    </thead>
    <tr>
        <td>Username</td>
        <td>The name of the Cyclr account (and Cycrl user) to install this integration in, or to create if such an account (and user) does not already exist.</td>
        <td>user@example.com</td>
    </tr>    
    <tr>
        <td>Password</td>
        <td>The password to assign to the new Cyclr user account, if created. If you do not intend your end users to access the Cyclr application directly, this password can be an obscure value known only to your app.</td>
        <td>c0mpl3x_P455w0rd</td>
    </tr>
    <tr>
        <td>AccountName</td>
        <td>If your user doesn't already have an account within Cyclr, specify the name of the account to create here.</td>
        <td>New Cyclr Account Name</td>
    </tr>
    <tr>
        <td>AccountId</td>
        <td>If your user already has an account within Cyclr, specify the Id of that account to have the new integration installed there.  If this is not provided, a new Cyclr account will be created.</td>
        <td>0000000-0000-0000-0000-000000000000</td>
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
            <small>Optional parameter to install a pre-authenticated partner connector into the account</small></th>
        </tr>
    </thead>
    <tr>
        <td>partnerConnector</td>
        <td>Providing your own platform's Cyclr Connector object here means your users will not be expected to authenticate against your platform during the LAUNCH flow.
        </td>
        <td></td>
    </tr>
    <tr>
        <td>partnerConnector.Name</td>
        <td>A name you wish to give this instance of your connector installed within this new or existing account.</td>
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
        <td>partnerConnector.[Properties]</td>
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
</table>

***Response:***

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
