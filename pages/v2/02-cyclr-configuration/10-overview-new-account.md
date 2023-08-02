---
title: Customer accounts
sidebar: cyclr_sidebar
permalink: overview-new-account
tags: 
menus:
    user-accounts:
        title: Customer accounts
        identifier: overview-new-account
        toggleonly: menutoggleonly
        weight: 10
---
{::options parse_block_html="true" /}
<section class="card">

Typically, each of your customers have their own Cyclr account where you can keep their data and integrations separate from your other customers’ data.

For information on how to create and configure accounts via the Cyclr API, go to the [API section](#manage-accounts-via-apiI) of this page.

</section>
<section class="card">

## Create an account

To create a new Cyclr account from the console, go to **Accounts** > **Account Management**, and select **Add New Account**.

</section>
<section class="card">

## Install connectors and cycles

You can install connectors and integration cycles into accounts to provide them to your customers. 

### Install connectors

To install a connector into an account:

1.  Find the account you want to use and select **Open Account**.
2.  Select **Connectors** in the left sidebar to switch to the Connectors tab.
3.  Select the **Install New Utility** or the **Install New Application** button depending on what you want to install.

For more information on how to install and authenticate a specific connector, see the [Connector guides](connector-guides) section.

### Install cycles

To install a cycle into an account:

1.  Find the account you want to use and select **Open Account**.
2.  Select the **Templates** button to open the list of available template.
3.  Select the Use Template button on the template you want to use.

This opens the template builder so you can configure the cycle for the account, and adds the template as a cycle inside the account. When you add a cycle to an account, Cyclr automatically installs the included connectors.


</section>
<section class="card">

## Sub accounts

You can set up sub accounts within a customer account. This allows you to organize multiple related accounts, and each sub account has access to the connectors in its parent account.

For example, you could have a customer account for a bookstore chain, with a sub account for each location.

### Create a sub account in the console

You can set up sub accounts from your Cyclr console:

1. Go to **Accounts** > **Account Management**.
2. In the **Sub Accounts** column of the account, select the number displayed.
3. Select the **Add New Sub Account** button.

Since sub accounts function the same as main customer accounts, you can set them up in the same way.

### Task usage in sub accounts

Your Cyclr console displays the task usage for each sub account in the same way as standard accounts. 

> **Note**: Sub accounts’ task usage isn’t included in their parent account’s task usage.

</section>
<section class="card">

## Manage accounts via API

### Access Cyclr’s API

To make calls to the Cyclr API, you need to get an access token:

1. Identify your Cyclr instance and find the [API Domain](http://cyclr-api-authentication#api-domain) to use in your API calls.
2. Make an API call to [get an access token](http://cyclr-api-authentication#access-token).

### Create an account

You can create accounts via the Cyclr API with the[ `POST /v1.0/accounts`](https://api.cyclr.com/docs/index#!/Accounts/Accounts_Create_POST) endpoint. For more information, see the page on how to [create accounts](create-account).

### Create a sub account

To create a sub account, follow the same steps as on the [create account](http://create-account) page, but provide the additional `ParentAccountId` parameter in the request body to define which account you want to add it to:

```json
POST /v1.0/accounts
Authorization: Bearer ****************************************************************
Content-Type: application/json

{
  "ParentAccountId": "ParentID",
  "Id": "Sub1ID",
  "Name": "Sub Account #1"
}
```

### Install connectors and cycles

You can also use the Cyclr API to install connectors and templates into accounts as you create them so that the connectors are always available. 

> **Note**: When you install a template into an account, Cyclr automatically installs any missing connectors, so you don’t need to use API calls to add all of them.

* [Install a connector into an account](install-connectors).
* [Install a cycle into an account](install-cycle).

</section>
