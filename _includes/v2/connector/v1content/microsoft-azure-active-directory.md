
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

The Microsoft Azure Active Directory connector is authenticated with the OAuth2.0 protocol. 

Register an application and provide the connector with that application's `Client ID` (Application ID) and `Client Secret`.

See [Microsoft's official guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) to registering an application in Azure Active Directory. 

- **Supported account types** : select `Accounts in any organizational directory (Any Azure AD directory - Multitenant)`
- **Redirect URI** : `https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback`
- **Client ID** (Application ID) is displayed in the overview of your created app
- **Client Secret**:  Follow [these steps](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-client-secret) to get this

Set the application permissions : the table details the permissions required for each method category in the connector.

| Category     | Permissions                          |
| :----------- | :----------------------------------- |
| Groups       | Group.Read.All, GroupMember.Read.All |
| Organization | Organization.Read.All                |
| People       | People.Read.All                      |
| Places       | Place.Read.All                       |
| Users        | User.Read.All                        |

In addition to the category specific permissions, add permissions for **offline_access** and **Directory.Read.All**.

To add these permissions in Azure Active Directory:

1. From **App registrations** in the Azure portal select your application
2. Select **API permissions** from the menu on the left
3. Click **+ Add a permission** to open the permissions menu
   ![add permission button](./images/permissions_4.png)
4. From **Microsoft APIs** select **Microsoft Graph** and then **Delegated permissions**
   ![permissions menu](./images/permissions_1.png)
   ![permissions menu 2](./images/permissions_2.png)
5. A series of permissions categories are shown
6. Select the checkboxes for the appropriate permissions and click **Add permissions**
   ![checked permission](./images/permissions_5.png)
7. Click **Grant admin consent for _organization_**
   ![grant admin consent](./images/permissions_3.png)

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Save the `Client ID` and `Client Secret` values in your Cyclr Console to allow your clients to access their own data through your Active Directory App.

1. Find the Microsoft Azure Active Directory connector

   >  **Cyclr Console** > **Connectors** > **Application Connector Library** > **Microsoft Azure Active Directory**

2. Click **Setup** in the Edit Connector interface 

3. Enter your `Client ID` and `Client Secret` 
4. Click **Save Changes**


The Microsoft Azure Active Directory Connector can now be installed and the user will only be asked to authenticate your App.

</div>
</section>
