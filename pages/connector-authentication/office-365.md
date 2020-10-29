---
title: Microsoft Office 365
sidebar: cyclr_sidebar
permalink: office-365-connector
tags: [connector]
---

Microsoft Office 365 uses OAuth 2. Please sign up for an application on Microsoft first and get an OAuth client ID, client secret and tenant ID.

See here for the [official documentation for creating an Azure Active Directory application](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-integrating-applications).

We will summarise it in a few points:

1. Register a free Azure account or log into your Azure account if you already have one.
2. Go to Microsoft Azure portal -> Azure Active Directory -> App Registrations -> New application registration.

   Below are the details you should provide:

   **Name**: Your Application Name

   **Reply URLs**: you must add a callback URL to allow Microsoft Office 365 to be used in your Cyclr Console and its accounts.

   The URL is:

   * {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}

   **Multi-tenanted**: Yes
3. Set the correct permissions (more information below).
4. Go to Cyclr Console (https://yourCyclrInstance/console) > Connectors > Application Connector Library > Microsoft Office 365 > Setup

   **Client ID**: This is the Application ID displayed in the portal

   **Client Secret**: Create a Password under Microsoft Azure portal > Azure Active Directory > App Registrations > Your Application > API Access > Keys. Copy and paste the password as the client secret.
   

The Microsoft Office 365 connector is now set up! You can test it by installing it in one of your customer accounts.


When installing the Microsoft Office 365 Connector, the user will be asked to provide their **Directory/Tenant ID**. This appears as **Tenant ID** in the client's Azure Active Directory portal.

### Permissions

You will need to set different permissions in Azure Active Directory depending on which methods you would like to utilize.

From the Application view (after the creation of the Application in step 3), navigate to "API Permissions" under "Manage" on the left side of the page. Add the following permissions:

| Method Category                  | Type      | Permission Name            |
|----------------------------------|-----------|----------------------------|
| Users                            | Delegated | User.Read.All              |
|                                  | Delegated | User.ReadWrite.All         |
|                                  | Delegated | Directory.Read.All         |
|                                  | Delegated | Directory.ReadWrite.All    |
| Calendars/Calendar Groups/Events | Delegated | Calendars.Read             |
|                                  | Delegated | Calendars.Read.Shared      |
|                                  | Delegated | Calendars.ReadWrite        |
|                                  | Delegated | Calendars.ReadWrite.Shared |
| Emails                           | Delegated | Mail.Read                  |
|                                  | Delegated | Mail.Read.Shared           |
|                                  | Delegated | Mail.ReadWrite             |
|                                  | Delegated | Mail.ReadWrite.Shared      |
| OneDrive                         | Delegated | File.Read                  |
|                                  | Delegated | File.Read.All              |
|                                  | Delegated | File.ReadWrite             |
|                                  | Delegated | File.ReadWrite.All         |

More information: https://docs.microsoft.com/en-us/graph/permissions-reference
