---
title: Microsoft Education
sidebar: cyclr_sidebar
permalink: microsoft-education-connector
tags: [connector]
---

Microsoft Education uses OAuth 2.0. Please sign up for an application on Microsoft first and get an OAuth client ID, client secret.

### Azure Active Directory OAuth Application

See here for the [official documentation for creating an Azure Active Directory application](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-integrating-applications).

To Summarize the above documentation:

1. Either log into your existing Azure account or [register for a free Azure account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
2. In your Microsoft Azure portal go to -> Azure Active Directory -> App Registrations -> New application registration.

   Below are the details you should provide:

   **Name**: Your Application Name

   **Reply URLs**: you must add a callback URL to allow Microsoft Office 365 to be used in your Cyclr Console and its Cyclr Accounts.

   The URL is:

   * {% raw %}https://{{Your Cyclr Service Domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}

   **Multi-tenanted**: Yes
   
3. Set the appropriate permissions as described below.

### Permissions

You will need to set different permissions in Azure Active Directory depending on which auth flow you would like to utilize.

From the Application view (after the creation of the Application in step 3), navigate to "API Permissions" under "Manage" on the left side of the page. Add the following permissions:

| Method Category                  | Type        | Permission Name                  |
|----------------------------------|-------------|----------------------------------|
| Edu                              | Delegated   | EduAssignments.ReadWriteBasic    |
|                                  | Delegated   | EduAssignments.ReadWrite         |
|                                  | Delegated   | EduAssignments.ReadBasic         |
|                                  | Delegated   | EduAssignments.Read              |
|                                  | Delegated   | EduAssignments.ReadBasic         |
|                                  | Application | EduAssignments.ReadWrite         |
|                                  | Application | EduAssignments.ReadBasic         |
|                                  | Application | EduAssignments.Read              |
|                                  | Application | EduAssignments.ReadBasic         |


More information: https://docs.microsoft.com/en-us/graph/permissions-reference


### Connector Setup
Go to Cyclr Console (https://yourCyclrInstance/console) > Connectors > Application Connector Library > Microsoft Office 365 > Setup

   **Client ID**: This is the Application ID displayed in the portal

   **Client Secret**: Create a Password under Microsoft Azure portal > Azure Active Directory > App Registrations > Your Application > API Access > Keys. Copy and paste the password as the client secret. 

The Microsoft Office 365 Connector is now set up! You can test it by installing the Conneector and calling some Methods.
