---
title: Microsoft Azure Active Directory Connector Guide
sidebar: cyclr_sidebar
permalink: azure-ad-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Authentication

The Microsoft Azure Active Directory connector is authenticated with the OAuth2.0 protocol. You will need to register an application and provide the connector with that application's Client ID (Application ID) and Client Secret.

Please follow Microsoft's official guide to registering an application in Azure Active Directory. That documentation can be found [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app).

- For "Supported account types" you should select "Accounts in any organizational directory (Any Azure AD directory - Multitenant)"
- Redirect URI should be {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}
- Client ID (Application ID) is displayed in the overview of your created app
- Generate a Client Secret by following [these steps](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-client-secret)

Permissions must be set for the application. The following table details the permissions required for each method category in the connector.

| Category     | Permissions                          |
| :----------- | :----------------------------------- |
| Groups       | Group.Read.All, GroupMember.Read.All |
| Organization | Organization.Read.All                |
| People       | People.Read.All                      |
| Places       | Place.Read.All                       |
| Users        | User.Read.All                        |

In addition to the category specific permissions, you should add permissions for **offline_access** and **Directory.Read.All**.

To add these permissions in Azure Active Directory:

1. From **App registrations** in the Azure portal select your application
2. Select **API permissions** from the menu on the left
3. Click **+ Add a permission**. This will open the permissions menu
   ![add permission button](./images/permissions_4.png)
4. From **Microsoft APIs** select **Microsoft Graph** and then **Delegated permissions**
   ![permissions menu](./images/permissions_1.png)
   ![permissions menu 2](./images/permissions_2.png)
5. You will be presented with a series of permissions categories
6. Select the checkboxes for the appropriate permissions and click **Add permissions**
   ![checked permission](./images/permissions_5.png)
7. You must then **Grant admin consent for _organization_**
   ![grant admin consent](./images/permissions_3.png)

### Connector Setup

To allow your clients to access their own data through your Active Directory App, you must save the Client ID and Client Secret values in your Cyclr Console.

1. Locate the Microsoft Azure Active Directory connector

   > Cyclr Console > Connectors > Application Connector Library > Microsoft Azure Active Directory

2. From the Edit Connector interface click 'Setup'

3. Enter your Client ID and Client Secret then click 'Save Changes'


The Microsoft Azure Active Directory Connector can now be installed and the user will only be asked to authenticate your App.

</section>
