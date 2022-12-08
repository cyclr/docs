---
title: Sub accounts
sidebar: cyclr_sidebar
permalink: sub-accounts
tags: [accounts]

menus:
    user-accounts:
        title: Sub accounts
        identifier: sub-accounts
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
Within a Cyclr Account, it's possible to set up **Sub Accounts**.

Sub Accounts are a way of organising multiple related accounts.

You may for example want an account for a bookstore chain, and a Sub Account for each location.

Each Sub Account has access to use the installed connectors in its *parent* account.

## Creating a Sub Account in the Console

To set up a Sub Account you would:

1. Go to **Console** > **Accounts** > **Account Management**

2. Identify the **Account** in which you wish to make a **Sub Account**.  In the **Sub Accounts** column for this Account, click the number of **Sub Accounts** (this will likely be 0).

3. Click **Add New Sub Account**.

4. You can now set up a **Sub Account** just as you would an ordinary **Account**.

## Creating a Sub Account using the Cyclr API

You use the standard `POST /v1.0/accounts` endpoint to create an Account, you just provide an additional **ParentAccountId** property in the Request Body to tell Cyclr which Account to add it under:

```http
POST /v1.0/accounts
Authorization: Bearer ****************************************************************
Content-Type: application/json

{
  "ParentAccountId": "ParentID",
  "Id": "Sub1ID",
  "Name": "Sub Account #1"
}
```

## Task Usage in Sub Accounts

Your Cyclr Console displays Task Usage for each Sub Account in the same wasy as standard Accounts.

Sub Accounts Task Usage is not included within their parent Account's Task Usage.

</section>
