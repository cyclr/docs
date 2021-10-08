---
title: Google Calendar - Workspace Authentication
sidebar: cyclr_sidebar
permalink: google-calendar-workspace-connector
tags: [connector]
---

## Account Level Setup

#### Create Service Account with appropriate permissions
The actions in this guide require a Google Workspace account with an admin user.
* Navigate to the [services account page](https://console.developers.google.com/iam-admin/serviceaccounts).
* Click **Create Service Account** and enter an appropriate name and description. 
* On the **Grant users access to this service** screen, create a key and select the **JSON** format.
* Keep this file safe, if foreign users gain access to this file they are able to perform admin actions in your Google Workspace account. We will need it later. This will also be the only time that you can download the file.
 
#### Enable domain-wide delegation
Now we need to enable Google Workspace domain-wide delegation so that you are able to access your users Google Calendar data.
* Click on the newly create service account, and under **Actions** click **Edit**.
* Under **Show domain-wide delegation**, make sure **Enable Google Workspace Domain-wide Delegation** is ticked.
* Click save.
* A new column labeled **Domain-wide delegation** will be present, click **View Client ID** and note down the value.

#### Grant access to the service account
This action must be completed by a super admin of the Google Workspace account.
* Navigate to the [admin console](http://admin.google.com/).
* Go to **Main Menu** > **Security** > **API Controls**.
* Under **Domain wide delegation**, select **Manage Domain Wide Delegation**.
* Click **Add new**. Enter the **Client ID** we retrieved earlier in the appropriate area. 
* In the **OAuth Scopes** field, enter the following permissions:
  * **https://www.googleapis.com/auth/calendar** - allows API access to the Calendars service.
  * **https://www.googleapis.com/auth/admin.directory.user.readonly** - allows API access to read users of the Workspace account.
  * **https://www.googleapis.com/auth/admin.directory.group.readonly** - allows API access to read groups.
* Click Authorize.

### Cyclr Setup

Setup your Google Calendar - Workspace App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Google Calendar - Workspace**
*   Click the **Setup** button

Enter the following values:

**Private Key**: This is the private key that is stored in the JSON file you downloaded earlier. Copy the value of the **private_key** field, it will start with **"-----BEGIN PRIVATE KEY-----"** and end with **"-----END PRIVATE KEY-----\n"**. Make sure to copy down **all** text between the quotation marks.

**client Email**: This can also be retrieved from the JSON file. Copy the value of the **client_email** value.

**User Email**: The email address of a user you would like to authorize as. It should be of an admin user to be able to run all the methods in the connector.


Your Google Calendar - Workspace Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
