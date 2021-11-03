---
title: Microsoft Azure DevOps Connector Guide
sidebar: cyclr_sidebar
permalink: azure-devops-connector
tags: [connector]
---

For reference, Microsoft's full Azure DevOps Authentication documentation can be found [here](https://docs.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops).

The **Microsoft Azure DevOps** Connector is authenticated using OAuth2.0.

## Preparation

Either your or your end-users will need to [register an application with Microsoft](https://app.vsaex.visualstudio.com/app/register) and provide its details to Cyclr.

If you intend to have all your users accept the same Authorized Scopes when they authenticate a **Microsoft Azure DevOps** Connector, you can register a single application and set its details and Scopes in your Cyclr Console's *Connectors > Application Connector Library* entry.

If your users will require different Authorized scopes, either they or you can register separate applications with the appropriate scopes set.  Details of the application and scopes being used must then be provided when authenticating the Connector.

When authenticating the Connector, the Scopes parameter used **must** match the Authorized scopes specified on the application being used.  If they are different, you will see an `InvalidScope` error from Microsoft's API.

## Registering an Application

Registering an application is done [here](https://app.vsaex.visualstudio.com/app/register)

Set the **Authorization callback URL** to:

`https://<Your Cyclr Service Domain e.g. app-h.cyclr.com>/connector/callback`

<br />

Select appropriate **Authorized scopes** for your use-case.

We suggest at least adding "Work items (full)" as it is required for most methods apart from Audit Logs and Accounts.
 
[A list of available scopes can be found here](https://docs.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?toc=%2Fazure%2Fdevops%2Forganizations%2Ftoc.json&bc=%2Fazure%2Fdevops%2Forganizations%2Fbreadcrumb%2Ftoc.json&view=azure-devops#scopes)

<br />

After registering your application your **App ID**, **App Secret** and **Client Secret** are displayed.

Keep a note of these details to refer to.


## Partner Setup

**If you plan to use the same Scopes for all your users:**

In your Cyclr Console, go to Connectors > Application Connector Library and locate the entry for **Microsoft Azure DevOps**.

Enter your **App ID** into the *Client ID* box, your **Client Secret** into the *Client Secret* box and specify the same list of *Scopes* that you set on your application, then click Save.

**If you plan to use different Scopes for your users:**

You should leave the Application Connector Library entry blank.  Doing this requires the user to provide all the details when installing the Connector.  This also allows different application details and related Scopes to be used that meet each user's requirements.


## Connector Setup

When installing the Connector the **Organization ID** and **Project Name** to work with are needed.

These details can be found by logging in to the [DevOps portal](https://aex.dev.azure.com/):

<img src="./images/AzureDevOps1.png" style="zoom:75%;" />

<br />

1. Begin installation of the **Microsoft Azure DevOps** Connector and enter the **Organization ID** and **Project Name** values.

2. Click 'Sign In' and a new window will open prompting you to log in.

3. Select your Azure account and authorize access.

The Connector is now authenticated and ready for use.


## Setting Scopes/InvalidScope Error

The list of permissions you set for the **Scopes** Connector parameter must *exactly* match the **Authorized scopes** you set when registering your App at [https://app.vsaex.visualstudio.com/app/register](https://app.vsaex.visualstudio.com/app/register).

If they are different you will see an `InvalidScope` error when authenticating the Connector.
