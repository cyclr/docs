
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Microsoft Office 365 uses OAuth 2.0. 

Sign up for an application on Microsoft to get your OAuth `Client ID` and `Client Secret`.

### Azure Active Directory OAuth Application

See  the [official documentation for creating an Azure Active Directory application](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-integrating-applications) for full information.

To Summarise the above documentation:

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

You will need to set different permissions in Azure Active Directory depending on which methods you would like to utilize.

You must also set the Type of each Permission differently depending on which Connector you're using:
* **Microsoft Office 365** Connector: set Permissions as "Delegated"
* **Microsoft Office 365 (Application Permissions)**: set Permissions as "Application"

From the Application view (after the creation of the Application in step 3), navigate to "API Permissions" under "Manage" on the left side of the page. Add the following permissions:

| Method Category                  | Type      | Permission Name            |
|----------------------------------|-----------|----------------------------|
| Users                            | Delegated/Application according to the Connector | User.Read.All              |
|                                  |  | User.ReadWrite.All         |
|                                  |  | Directory.Read.All         |
|                                  |  | Directory.ReadWrite.All    |
| Calendars/Calendar Groups/Events |  | Calendars.Read             |
|                                  |  | Calendars.Read.Shared      |
|                                  |  | Calendars.ReadWrite        |
|                                  |  | Calendars.ReadWrite.Shared |
| Emails                           |  | Mail.Read                  |
|                                  |  | Mail.Read.Shared           |
|                                  |  | Mail.ReadWrite             |
|                                  |  | Mail.ReadWrite.Shared      |
| OneDrive                         |  | File.Read                  |
|                                  |  | File.Read.All              |
|                                  |  | File.ReadWrite             |
|                                  |  | File.ReadWrite.All         |

More information: https://docs.microsoft.com/en-us/graph/permissions-reference


</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

- Go to your Cyclr Console (https://yourCyclrInstance/console) 
- Go to **Connectors** > **Application Connector Library**
- Find the Microsoft Office 365 connector
- Click **Setup**
- Enter your `Client ID`: the Application ID displayed in the portal
- Enter your `Client Secret`: 
   - Create a Password at **Microsoft Azure portal** > **Azure Active Directory** > **App Registrations** > **Your Application** > **API Access** > **Keys** 
   - Copy and paste the password as the Client Cecret 

You are now ready to install the Connector.  When you do so you will need the **Tenant ID**.  This is the Directory ID found below the **Client ID** in the portal.

</div>

</section>
