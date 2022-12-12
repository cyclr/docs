
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

### Account Level Setup

#### Service Account with permissions

This requires a Google Workspace account with an admin user:

- Navigate to the [services account page](https://console.developers.google.com/iam-admin/serviceaccounts).
- Click **Create Service Account** and enter a name and description 
- On the **Grant users access to this service** screen, create a key and select format **JSON** 

**NB** Keep this file safe, it provides access to admin actions in your Google Workspace account. This will also be the only time that you can download the file, it is needed for further actions.
 
#### Enable domain-wide delegation

Enable Google Workspace domain-wide delegation in order to access your users\` Google Calendar data.
- Click on the newly create service account, and under **Actions** click **Edit**
- Under **Show domain-wide delegation**, enable **Enable Google Workspace Domain-wide Delegation** 
- Click **Save**
- A new column labeled **Domain-wide delegation** is shown: click **View Client ID** and note the value

#### Grant access to the service account

A super admin of the Google Workspace account completes this action:

- Go to the [admin console](http://admin.google.com/)
- Go to **Main Menu** > **Security** > **API Controls**
- Under **Domain wide delegation**, select **Manage Domain Wide Delegation**
- Click **Add new** and enter the `Client ID` noted during the domain-wide delegation  
- In the **OAuth Scopes** field, enter the following permissions:
  - **https://www.googleapis.com/auth/calendar** to allow API access to the Calendars service
  - **https://www.googleapis.com/auth/admin.directory.user.readonly** to allow API access to read users of the Workspace account
  - **https://www.googleapis.com/auth/admin.directory.group.readonly** to allow API access to read groups
- Click **Authorize**

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Google Calendar - Workspace App within Cyclr:

-   Go to your **Cyclr Console**
-   Click the **Connectors** menu along the top
-   Choose Connector Library
-   Scroll down to **Google Calendar - Workspace**
-   Click the **Setup** button

Enter the following values:

**Private Key**: This is the private key that is stored in the JSON file you downloaded earlier. Copy the value of the **private_key** field, it will start with **"-----BEGIN PRIVATE KEY-----"** and end with **"-----END PRIVATE KEY-----\n"**. Make sure to copy down **all** text between the quotation marks.

**client Email**: This can also be retrieved from the JSON file. Copy the value of the **client_email** value.

**User Email**: The email address of a user you would like to authorize as. It should be of an admin user to be able to run all the methods in the connector.


Your Google Calendar - Workspace Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>
