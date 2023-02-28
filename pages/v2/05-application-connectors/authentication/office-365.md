---
title: Microsoft Office 365
sidebar: cyclr_sidebar
permalink: office-365-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Office 365 setup

Microsoft Office 365 uses OAuth 2.0. To use the Office 365 connector, sign up for an application on Microsoft first and get the following authentication values:
* OAuth client ID.
* Client secret.

### Create an Azure Active Directory OAuth application

For more information, see the [official documentation for creating an Azure Active Directory application](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-integrating-applications).

To summarize the above documentation:

1. Either log into your existing Azure account or [register for a free Azure account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
2. In your Microsoft Azure portal, go to **Azure Active Directory** > **App Registrations** > **New application registration**.
3. Provide the following details:

  * **Name**: Your Application Name
  * **Reply URLs**: you must add a callback URL to allow Microsoft Office 365 to be used in your Cyclr Console and its Cyclr Accounts. The URL is `{% raw %}https://{{Your Cyclr Service Domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}`.
  * **Multi-tenanted**: Yes
   
4. Set the appropriate permissions.

### Set permissions

You need to set different permissions in **Azure Active Directory** depending on which methods you want to use. You also need to set the **Type** of each Permission differently depending on which Connector you use:

* **Microsoft Office 365** Connector: set permissions as **Delegated**.
* **Microsoft Office 365 (Application Permissions)**: set permissions as **Application**.

From the Application view, under **Manage** on the left side of the page, navigate to **API Permissions**. Add the following permissions:

| **Method Category**              | **Permission Name**        |
|----------------------------------|----------------------------|
| Users                            | User.Read.All              |
|                                  | User.ReadWrite.All         |
|                                  | Directory.Read.All         |
|                                  | Directory.ReadWrite.All    |
| Calendars/Calendar Groups/Events | Calendars.Read             |
|                                  | Calendars.Read.Shared      |
|                                  | Calendars.ReadWrite        |
|                                  | Calendars.ReadWrite.Shared |
| Emails                           | Mail.Read                  |
|                                  | Mail.Read.Shared           |
|                                  | Mail.ReadWrite             |
|                                  | Mail.ReadWrite.Shared      |
| OneDrive                         | File.Read                  |
|                                  | File.Read.All              |
|                                  | File.ReadWrite             |
|                                  | File.ReadWrite.All         |

> **Note**: For each permission, the type is either **Delegated** or **Application** dependent on the connector you use.
For more information, see the Microsoft documentation on [permissions](https://docs.microsoft.com/en-us/graph/permissions-reference).

</section>
<section class="card">

## Cyclr setup

To set up the Office 365 connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Office 365 connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | *Client ID**   | The **Application ID** from your Microsoft Azure portal.                       |
   | **Client Secret**   | The [password](#secret) from your Microsoft Azure portal.                             |
   | **<default value>**| Cyclr fills this field by default.          |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

### Account setup

Cyclr asks you for the **Tenant ID** when you install the connector into an account. The **Tenant ID**  is the **Directory ID** from your Microsoft Azure portal, which you can find below the **Client ID**.

When you install the connector, it shows two authorization options: **Common** and **Organization**.
* If you select **Common**, the connector allows you to use work or organization accounts, and personal Microsoft accounts, during authentication.
* If you select **Organization**, the connector only allows you to use work or organization during authentication.
   
</section>

</section>
