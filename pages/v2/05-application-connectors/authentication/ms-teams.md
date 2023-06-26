---
title: Microsoft Teams Authentication
sidebar: cyclr_sidebar
permalink: microsoft-teams-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Partner setup

To install the Microsoft Teams connector in Cyclr you must [create an Azure Active Directory OAuth application](#create-an-application) and obtain a [client ID](#get-a-client-id), [client secret](#create-a-client-secret) and a [tenant ID](#get-a-tenant-id).

### Authentication method restrictions

#### OAuth 2.0 (application permissions)

When you use application permissions authentication, several of the endpoints are protected since they handle sensitive data. You need to apply for permission to use them with [this Microsoft request form](https://docs.microsoft.com/en-us/graph/teams-protected-apis). It can take up to a week to approve your permissions during which you cannot use the protected methods. The following methods are protected and only function once you have requested permission:

- **Messages** > **Get Channel Message**
- **Messages** > **List Channel Messages**
- **Messages** > **List Updated Channel Messages**
- **Webhooks** > **Get Team Chats**
- **Webhooks** > **Get Channel Chats**

#### OAuth 2.0 (delegated permissions)

You don't need to request any permissions for delegated permissions authentication as the user is required to consent permission during authentication.

Delegated permissions authentication has restrictions to several methods:

| **Method category**                                              | **Restriction**                                                  |
| ------------------------------------------------------------ | :----------------------------------------------------------- |
| Chats >  List New and Updated User Chats<br>Chats >  List New User Chats<br>Chats >  List User Chats | Chats can only be listed for the currently authenticated user. |
| Teams >  List Joined Teams                                   | Teams can only be listed for the currently authenticated user. |
| Webhooks >  Get Completed Call<br>Webhooks >  Get Team Chats<br>Webhooks >  Get Users Chats | These methods will not function.                             |

### Create an application

You need an Azure Active Directory OAuth application to authenticate the Microsoft Teams connector. For more information, see Microsoft's official documentation on how to [register an application](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app).

To create an application, from the Microsoft Azure portal:

1. Select the portal menu.
2. Select **Azure Active Directory** > **App registrations** > **New registration**.
3. Enter the following:
   | **Field**                   | **Value**                                                        |
   | ----------------------- | :----------------------------------------------------------- |
   | Name                    | Your application name.                                       |
   | Supported account types | `Accounts in any organizational directory (Any Azure AD directory - Multitenant)` |
   | Redirect URI            | **Select a platform > Web >** `https://{Your Cyclr service domain}/connector/callback `<br>Your Cyclr service Domain can be found in your Cyclr console under **Settings > General Settings > Service Domain**. |
4. Select **Register**.

### Get a client ID

To get a client ID for an application: From the application overview under the **Essentials** heading, note the value next to **Application (client) ID**.

### Get a tenant ID

To get a tenant ID for an application: From the application overview under the **Essentials** heading, note the value next to **Directory (tenant) ID**.

### Create a client secret

To create a client secret, from the application overview:

1. Select **Certificates & secrets > Client secrets > New client secret**.
2. Enter a **Description** and set the **Expires** duration.
3. Select **Add**.
4. Next to the newly created client secret, note the value under the **Value** heading

### Enable permissions

Each endpoint requires you to enable permissions in Azure Active Directory before you can use them. For more information, see the Microsoft documentation on [permissions](https://docs.microsoft.com/en-us/graph/permissions-reference).

To set permissions for your application, from the application overview:

1. Under the **Manage** heading, select **API permissions**.
2. Select **Add a permission**.
3. Under the **Microsoft APIs** tab, select **Microsoft Graph**.
4. Select **Delegated permissions** or **Application permissions**, depending on the authentication type you are using.
5. Select the required permissions.
6. Select **Add permissions**.

To set up permissions for all methods for application permissions, use the following permissions:

- CallRecords.Read.All
- ChannelMember.Read.All
- ChannelMessage.Read.All
- ChannelSettings.Read.All
- Chat.Read.All
- Directory.Read.All
- GroupMember.Read.All
- Presence.ReadWrite.All
- TeamSettings.Read.All
- Teamwork.Migrate.All
- User.Read.All

To set up permissions for all methods for delegated permissions, use the following permissions:

- ChannelMember.Read.All
- ChannelMessage.Read.All
- ChannelMessage.Send
- ChannelSettings.Read.All 
- Chat.Read
- GroupMember.Read.All
- Presence.ReadWrite
- TeamSettings.Read.All
- User.Read.All

The below table lists which permissions you require for each method category and authentication type:

| Method Category | Application permissions                                     | Delegated permissions                                 |
| :-------------- | :---------------------------------------------------------- | :---------------------------------------------------- |
| Calls           | CallRecords.Read.All                                        | Not supported                                         |
| Channels        | ChannelSettings.Read.All ChannelMember.Read.All             | ChannelSettings.Read.All ChannelMember.Read.All       |
| Chats           | Chat.Read.All                                               | Chat.Read                                             |
| Groups          | GroupMember.Read.All                                        | GroupMember.Read.All                                  |
| Members         | GroupMember.Read.All                                        | GroupMember.Read.All                                  |
| Messages        | ChannelMessage.Read.All Chat.Read.All Teamwork.Migrate.All  | ChannelMessage.Read.All Chat.Read ChannelMessage.Send |
| Presence        | Presence.ReadWrite.All                                      | Presence.ReadWrite                                    |
| Teams           | TeamSettings.Read.All                                       | TeamSettings.Read.All                                 |
| Users           | User.Read.All Directory.Read.All                            | User.Read.All                                         |
| Webhooks        | CallRecords.Read.All  ChannelMessage.Read.All Chat.Read.All | ChannelMessage.Read.All                               |

## Cyclr setup

To set up the Microsoft Teams connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.
2. Use the search box to find the Microsoft Teams connector.
3. Select the **Setup Required** icon.
4. Enter the below values:
   | **Value**     | **Description**                                      |
   | :------------ | :--------------------------------------------------- |
   | Client ID     | The **Application (client) ID** of your application. |
   | Client Secret | The client secret of your application.               |
5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

### Account setup

Cyclr asks you for the below values when you install the Microsoft Teams connector into an account:

| **Value**     | **Description**                                      |
| :------------ | :--------------------------------------------------- |
| Client ID     | The **Application (client) ID** of your application. |
| Client Secret | The client secret of your application.               |
| Tenant ID     | The **Directory (tenant) ID** of your application.   |

</section>
