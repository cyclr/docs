---
title: Microsoft Teams Authentication
sidebar: cyclr_sidebar
permalink: microsoft-teams-connector
tags: [connector]
---

## Partner Setup

**Many of the Microsoft Teams endpoints are protected, due to handling sensitive data. This means you need to apply for permission via [this request form](https://docs.microsoft.com/en-us/graph/teams-protected-apis). 
Do note that this can take up to a week to get approved, during which you cannot use the protected methods.**

The following methods in the connector are protected:
- List (Updated) Channel Messages
- Get Channel Message
- Get Team Chats (webhook)
- Get Channel Chats (webhook)

Microsoft Teams uses OAuth 2.0. Please sign up for an application on Microsoft first and get an OAuth client ID, client secret.

### Azure Active Directory OAuth Application

See here for the [official documentation for creating an Azure Active Directory application](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-integrating-applications).

To Summarize the above documentation:

1. Either log into your existing Azure account or [register for a free Azure account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
2. In your Microsoft Azure portal go to -> Azure Active Directory -> App Registrations -> New application registration.

   Below are the details you should provide:

   **Name**: Your Application Name

   **Reply URLs**: you must add a callback URL to allow Microsoft Teams to be used in your Cyclr Console and its Cyclr Accounts.

   The URL is:

    * `https://{{Your Cyclr Service Domain e.g. app-h.cyclr.com}}/connector/callback`

   **Multi-tenanted**: Yes

3. Set the appropriate permissions as described below.

### Permissions

You will need to set different permissions in Azure Active Directory depending on which methods you would like to utilize.

From the Application view (after the creation of the Application in step 3), navigate to "API Permissions" under "Manage" on the left side of the page. Add the following permissions:

| Method Category          | Type        | Permission Name               |
|--------------------------|-------------|-------------------------------|
| CallRecords              | Application | CallRecords.Read.All          |
| ChannelMessage           | Application | ChannelMessage.Read.All       |
|                          | Application | Calendars.ReadWrite           |
| ChannelSettings          | Application | ChannelSettings.Read.All      |
|                          | Application | ChannelSettings.ReadWrite.All |
| Group                    | Application | Group.Read.All                |
|                          | Application | Group.ReadWrite.All           |
| Team                     | Application | Team.ReadBasic.All            |
| TeamSettings             | Application | TeamSettings.Read.All         |
|                          | Application | TeamSettings.ReadWrite.All    |
| User                     | Application | User.Read.All                 |
|                          | Application | User.ReadWrite.All            |
| Directory                | Application | Directory.Read.All            |
|                          | Application | Directory.ReadWrite.All       |
| Channel                  | Application | Channel.ReadBasic.All         |

More information: https://docs.microsoft.com/en-us/graph/permissions-reference
### Cyclr Setup

Setup your Microsoft Teams App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Microsoft Teams**
*   Click the **Setup** button

Enter the following values:

**Client ID**: This is the Application ID displayed in the portal

**Client Secret**: Create a Password under Microsoft Azure portal > Azure Active Directory > App Registrations > Your Application > API Access > Keys. Copy and paste the password as the client secret.

**Tenant ID**: This is the Directory ID found below the Client ID in the portal

Your Microsoft Teams Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
