---
title: Deploy LAUNCH
sidebar: cyclr_sidebar
permalink: launch-deployment
tags: [launch]
menus:
    launch:
        title: Deploy LAUNCH
        identifier: launch-deployment
        toggleonly: menutoggleonly
        weight: 4
---
{::options parse_block_html="true" /}
<section class="card">

## Overview

When you provide your integrations with LAUNCH, there are two ways you can give access to your users:

* An **Account LAUNCH** has a built-in API account that all users use to access the Marketplace. 
* A **User LAUNCH** needs you to create separate user profiles for each user in your Cyclr account.

To allow your users to access LAUNCH, you need to provide your users with a link or button within your application that directs your user to the [LAUNCH URL](#deploy-launch-request).

</section>
<section class="card">

## Deploy LAUNCH request

You need to set up the link that you provide so that your application makes a request to the Cyclr REST API [`/v1.0/accounts/CYCLR_ACCOUNT_API_ID/launch`](https://api.cyclr.uk/docs/index#!/Accounts/Accounts_Launch_POST) endpoint in order to obtain a LAUNCH URL. This directs your user to that URL when they select the link to your integrations.

When you obtain a [Cyclr API Access Token](https://docs.cyclr.com/cyclr-api-authentication) for this call, don't use an Account Restricted Token.

### Example request

Replace `{yourCyclrInstance}` with your [API Domain](https://docs.cyclr.com/testing-cyclr-api) according to the location of your Cyclr console, or your own domain if your Cyclr instance is self-hosted.

```
curl -X POST
-H "Authorization: Bearer ACCESS_TOKEN"
-H "Content-Type: application/json"
-H "Accept: application/json"

-d '{
    "AccountName": "CYCLR_ACCOUNT_NAME",
    "ConnectorAuthentications": {
        "Name": "Example Connector",
        "Version": "1.0",
        "AuthValue": "XXXXXXXXXX",
        "Properties": [{"Name": "Url", "Value": "http://customDomain.appName.com"}]
    }
}' "https://{yourCyclrInstance}/v1.0/accounts/CYCLR_ACCOUNT_API_ID/launch"
```
### Request parameters

<div class="tg-wrap"><table>
<colgroup>
       <col span="1" style="width: 35%;">
       <col span="1" style="width: 15%;">
       <col span="1" style="width: 50%;">
    </colgroup>
<thead>
  <tr>
    <th><strong>Request Parameter</strong></th>
    <th><strong>Type</strong></th>
    <th><strong>Description</strong></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="4"><strong>Account</strong></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td>string, optional.</td>
    <td>If the <code>CYCLR_ACCOUNT_API_ID</code> value in the request's URL doesn't match an existing Cyclr Account, Cyclr creates a new Account with this name. If you don’t provide an account name, Cyclr uses the <code>CYCLR_ACCOUNT_API_ID</code> value as the new Account's name.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>AccountDescription</code></td>
    <td>string, optional.</td>
    <td>If the <code>CYCLR_ACCOUNT_API_ID</code> value from the request URL doesn't match an existing Cyclr account, Cyclr creates a new account with this description.</td>
    <td></td>
  </tr>
  <tr>
    <td colspan="4"><strong>Launched Cycle Options</strong><br>Optional parameters to control the initial behavior of the launched Cycle.</td>
  </tr>
  <tr>
    <td><code>Start</code></td>
    <td>boolean</td>
    <td>Defaults to <code>true</code>. Set the parameter to <code>false</code> if you don't want to start the installed integration.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>RunOnce</code></td>
    <td>boolean</td>
    <td>Defaults to <code>false</code>. Set the parameter to <code>true</code> if you want the installed integration to only run once.</td>
    <td></td>
  </tr>
  <tr>
    <td colspan="4"><strong>Connector Authentications</strong><br>Optional parameter to install pre-authenticated "partner connectors" into the Account.</td>
  </tr>
  <tr>
    <td><code>[ConnectorAuthentications]</code></td>
    <td></td>
    <td>Provide your own platform's Cyclr Connector objects so that your users don’t need to authenticate against your platform during the LAUNCH flow.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>[ConnectorAuthentications].Name</code></td>
    <td>string</td>
    <td>Name this instance of your connector in the account to help identify it.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>[ConnectorAuthentications].Version</code></td>
    <td>string</td>
    <td>Specify the version of the connector you want the user to install.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>[ConnectorAuthentications].AuthenticationId</code></td>
    <td>string</td>
    <td>Provide the ID of the authentication method you want this instance of your Connector to use. If the Connector only supports one form of authentication, this value is optional.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>[ConnectorAuthentications].AuthValue</code></td>
    <td>string, optional.</td>
    <td>(Optional) Provide the authentication value for your platform connector. If your platform requires a username and password, provide a base64 encoded version of <code>username:password</code>. You can also provide OAuth tokens and API keys as plain text.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>[ConnectorAuthentications].[Properties]</code></td>
    <td>array</td>
    <td>Provide an array of any properties that the partner connector requires for successful installation. Note: Not all connectors require this array.</td>
    <td></td>
  </tr>
  <tr>
    <td colspan="4"><strong>LAUNCH Options</strong></td>
  </tr>
  <tr>
    <td><code>Tags</code></td>
    <td>array</td>
    <td>Provide an array of tags to identify the integration. Am integration needs at least one tag to appear through LAUNCH.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>InlineOAuth</code></td>
    <td>boolean</td>
    <td>This parameter defaults to <code>false</code> except for partners that existed before Aug 2022, where the default is <code>true</code>. Set the parameter to <code>false</code> if you run LAUNCH in an HTML iframe and want to open OAuth redirect pages in a popup.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>AutoInstall</code></td>
    <td>boolean</td>
    <td>This parameter defaults to <code>true</code>, so Cyclr automatically starts installing a template if only one is returned. This means that your user doesn’t need to select it if it’s the only option.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>SingleInstall</code></td>
    <td>boolean</td>
    <td>This parameter defaults to <code>false</code> so that LAUNCH shows the user all templates, even if they are already installed. Set the parameter to <code>true</code> to only show templates that the user hasn’t installed before.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>CompleteParameter</code></td>
    <td>string</td>
    <td>Provide a value to pass through to the final page of the LAUNCH flow.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>Wizard</code></td>
    <td>boolean</td>
    <td>This parameter defaults to <code>false</code>. Set to <code>true</code> to display mappings to the user as a step-by-step wizard, or <code>false</code> to show them all at once as a single form.</td>
    <td></td>
  </tr>
  <tr>
    <td><code>DisplayDescriptions</code></td>
    <td>boolean</td>
    <td>This parameter defaults to <code>false</code>. Set the parameter to <code>true</code> to display template descriptions to the user on the cycle selection screen.</td>
    <td></td>
  </tr>
</tbody>
</table></div>

</section>
<section class="card">

## Deploy LAUNCH response

```json
{
    "AccountId": "CYCLR_ACCOUNT_API_ID",
    "ExpiresAtUtc": "2020-01-01T12:30:00.000Z",
    "LaunchUrl": "https://hostapp.cyclr.com/account/signinwithtoken?token=lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ%3D&returnUrl=%2Flaunch",
    "Token": "lld3UjpZKkuh0I7ObHR0EtxRsPo0No1GqNSyAi8pqXQ="
}
```
### Response parameters

<table class="col2-75">
<thead>
  <tr>
    <th><strong>Response Field</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>AccountId</code></td>
    <td>The ID of account you provided in your request, or the ID of the new account if you didn’t provide one.</td>
  </tr>
  <tr>
    <td><code>ExpiresAtUtc</code></td>
    <td>The date and time that the token and LAUNCH URL expires.</td>
  </tr>
  <tr>
    <td><code>LaunchUrl</code></td>
    <td>The URL that you can send your user to, typically in a popup browser window. When Cyclr generates the URL, it’s only valid for 5 minutes and expires after it’s first accessed. You can therefore direct your user to the URL immediately after you recieve it.</td>
  </tr>
</tbody>
</table>


When you deploy LAUNCH, your console displays an API User. The user has access to the account, but can’t sign in to the console themselves.

</section>
<section class="card">

## Deploy user LAUNCH

To deploy a user LAUNCH, you can make the same request to the Cyclr REST API’s [`/v1.0/users/launch`](https://api.cyclr.uk/docs/index#!/Users/Users_CreateUserLaunchToken_POST) endpoint. To create the account, you need to pass two extra parameters in the request:

<div class="tg-wrap"><table>
<colgroup>
       <col span="1" style="width: 35%;">
       <col span="1" style="width: 15%;">
       <col span="1" style="width: 50%;">
    </colgroup>
<thead>
  <tr>
    <th><strong>Request Parameter</strong></th>
    <th><strong>Type</strong></th>
    <th><strong>Description</strong></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>AccountId</code></td>
    <td>string</td>
    <td>Identify the Account to use.</td>
  </tr>
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
</table></div>

### Example request
```h
curl -X POST
-H "Authorization: Bearer ${ACCESS_TOKEN}"
-H "Content-Type: application/json"
-H "Accept: application/json"

-d '{
    "AccountId": "0000000-0000-0000-0000-000000000000",
    "Username": "example",
    "Password": "P4$$w0rd",
    "ConnectorAuthentications": {
        "Name": "Connector Name",
        "Version": "1.0",
        "AuthValue": "00000000000000000000000000000000000000000",
        "Properties": [{"Name": "Url", "Value": "https://myapp.something.blah"}]
    }
}' "https://yourCyclrInstance/v1.0/users/launch"
```

</section>
