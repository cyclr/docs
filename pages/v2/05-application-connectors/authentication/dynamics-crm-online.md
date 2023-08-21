---
title: Microsoft Dynamics CRM
sidebar: cyclr_sidebar
permalink: dynamics-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Microsoft Dynamics CRM setup

### Prerequisites

To use the Microsoft Dynamics CRM connector, you need Microsoft account and an Azure Active Directory application with Microsoft. For more information on how to create an application, see the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-integrating-applications).

To summarize how to create an application:

1. If you don't already have an account, register a free Azure account or Dynamics Online trial account.

2. Go to the Microsoft Azure portal, and select **Azure Active Directory** > **App Registrations** > **New application**.

3. Enter the details below:
   * **Name**: your application name.
   * **Supported Account Types**: select one of the Multitenant options.
   * **Redirect URI**: select **Web** and enter your cyclr callback URL (`https://{YourServiceDomain}/connector/callback`)

4. From the **Manage** menu, select **API Permissions** > **Add a permisssion**. Select **Dynamics CRM** and check the box for **user_impersonation**.

5. From your Cyclr console, select **Connectors** > **Connector Library** > **Dynamics CRM Online** > **Setup**.

### Get authentication details.

The Microsoft Dynamics CRM connector uses OAuth2.0, so to connect with Cyclr, you need the **Client ID** and the **Client Secret** from the Microsoft Azure application.

The **Client ID** is the Application ID displayed in the Microsoft Azure portal. 

You can create a **Client Secret** in the Microsoft Azure portal:
1. Go to **Azure Active Directory** > **App Registrations** > **Your Application** > **Certificates & secrets**.
2. Select **Client Secrets** > **New Client Secret**.
3. Copy the **Value** property.

</section>
<section class="card">

## Cyclr setup

To set up the Microsoft Dynamics CRM connector connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Microsoft Dynamics CRM connector connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**          | **Description**                             |
   | :----------------- | :------------------------------------------ |
   | **Resource**   | The domain of your Microsoft Dynamics CRM account url. For example, `https://example.crm.dynamics.com`. |
   | **Client ID**   | The application ID from of the Microsoft application. |
   | **Client Secret**| The corresponding Client Secret from the Microsoft application. |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.


</section>
<section class="card">

## Install the connector using the Cyclr API

To install the Microsoft Dynamics CRM Connector with the Cyclr API as part of an automated process, you need to set the domain of the Dynamics CRM Online instance as follows before you get an authentication token.

Create an Account Connector Property named **Resource** and provide its value:

```HTTP
curl -X POST 
     -H 'Content-Type: application/json' 
     -H 'Accept: application/json' 
     -d '{
            "Name": "Resource",
            "Value": "https://example.crm.dynamics.com"
         }'
'https://{CyclrAPIDomain}/v1.0/account/connectors/DYNAMICS_ACCOUNT_CONNECTOR_ID/properties'
```

After you successfully create the **Account Connector Property**, you can get a one-time sign-in token and call `/UpdateAccountConnectorOAuth` to complete the user challenge.

</section>
<section class="card">

## Errors

### Error: AADSTS500011

If you encounter the error: 
   `AADSTS500011: The resource principal named [Resource URL] was not found in the tenant named [Tenant ID]. This can happen if the application has not been installed by the administrator of the tenant or consented to by any user in the tenant. You might have sent your authentication request to the wrong tenant.`

Ensure you're using the correct **Resource URL** in the Connector's Setup.  This is the URL of your _customer's_ Microsoft Dynamics account and should be similar to "https://mycompany.crmXX.dynamics.com".

If unsure, go to your _customer's_ Microsoft Dynamics account through a web browser and copy it from the address bar.

### Error: AADSTS65001

Follow the below step if you are getting the error:
   `AADSTS65001: The user or administrator has not consented to use the application with ID ” named ”. Send an interactive authorization request for this user and resource.`

1. In your _customer's_ Microsoft Azure portal, go to Azure Active Directory -> App registrations -> Your App name -> API permissions
2. Click the "Grant admin consent for ..." button to allow the app to be installed into their directory.  If the button is greyed out, the user you are logged in as doesn't have the appropriate permission - you may require an administrator to do this.

</section>
