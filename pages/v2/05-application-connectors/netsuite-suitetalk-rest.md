---
title: Oracle NetSuite - SuiteTalk REST Web Services Connector Guide
sidebar: cyclr_sidebar
permalink: netsuite-suitetalk-rest-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## NetSuite Setup

Firstly [log in](https://system.netsuite.com/pages/customerlogin.jsp) to your NetSuite account.

### Create An Integration

1. From the top navigation bar go to **Setup** > **Integration** > **Manage Integrations** > **New**

2. Enter a name for the integration

3. **State** should be **Enabled**

4. From the **Authentication** section select **Token-Based Authentication**

5. Scroll down and click **Save**

Make a note of the **Consumer Key** and **Consumer Secret**.

### Finding Your Account ID

1. From the top navigation bar go to **Setup** > **Company** > **Company Information**

![Company information](./images/netsuite_suitetalk_1.png)

**Note: if your Account ID contains an underscore, replace it with a dash when populating the field during connector setup.**

### Enable Features

1. From the top navigation bar go to **Setup** > **Company** > **Enable Features**

2. Click the **SuiteCloud** subtab

3. In the **SuiteScript** section check **Client SuiteScript** and **Server SuiteScript**

4. In the **SuiteTalk (Web Services)** check **REST Web Services**

5. In the **Manage Authentication** section check **Token-Based Authentication**

6. Scroll to the bottom of the page and click **Save**

### Create A Role

If you haven't done so already you will need to create a custom role which includes the appropriate permissions to make the desired API calls.

1. From the top navigation bar go to **Setup** > **Users/Roles** > **Manage Roles** > **New**

2. Give the role a name

3. For **Authentication** check **Web Services Only Role**

4. From **Permissions** > **Transactions** add **Find Transaction**, **Invoice** and **Sales Order**. Each with Level: **Full**

5. From **Permissions** > **Reports** add **SuiteAnalytics Workbook**

6. From **Permissions** > **Lists** add any/all of the following: **Accounts**, **Contacts**, **Currency**, **Customers**, **Employees**, **Phonecalls**, **Projects**, **Subsidiaries**. Each with Level: **Full**

7. From **Permissions** > **Setup** add **Access Token Management**, **User Access Tokens** and **REST Web Services**. Each with Level: **Full**

8. Scroll to the bottom of the page and click **Save**

### Assign Role To User

1. From the top navigation bar go to **Setup** > **Users/Roles** > **Manage Users**

2. Select the user who should be assigned the role

3. From the user's profile page navigate to **Access** > **Roles**

4. Add the role created above

5. Scroll to the bottom of the page and click **Save**

### Create An Access Token

1. From the top navigation bar go to **Setup** > **Users/Roles** > **Access Tokens** > **New**

2. Enter the **Application Name (previously created integration)**, **User** and **Role**

3. Give the token a name and click **Save**

Make a note of the **Token ID** and **Token Secret**.


</section>
<section class="card">
## Connector Setup

1. Locate the Oracle NetSuite - SuiteTalk REST Web Services connector

   > Cyclr Console > Connectors > Connector Library > Oracle NetSuite - SuiteTalk REST Web Services

2. From the Edit Connector interface click 'Setup'

3. Enter the credentials retrieved in the above steps

4. Click **Next**

The connector is now authenticated and ready to use.


</section>
<section class="card">
## Troubleshooting Authentication Errors

The authentication error messages returned by NetSuite do not always give a full description of the error's details. To find more information you can view the "Login Audit Trail":

1. Go to Setup > Users/Roles > User Management > View Login Audit Trail

2. Check the Use Advanced Search box

3. Click the Results subtab

4. Add the following fields: Detail, Token-based Access Token Name, and Token-based Application Name

5. Click Submit

The Detail column displays error messages for any token-based authentication logins with a status of Failure.

</section>
