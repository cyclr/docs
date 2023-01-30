---
title: Zenoti Authentication
sidebar: cyclr_sidebar
permalink: zenoti-connector
tags: [connector]
---

<a href="client-id">

To authenticate your connector, you need to get the Client ID. You can find the Client ID in the login URL. For example, if the login URL is `https://mycompany.zenoti.com/SignIn.aspx` the Client ID is `mycompany`.

## Cyclr setup
  
### Console setup

To set up the Zenoti connector in Cyclr, go to your console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Zenoti connector.

3. Select the **Setup Required** icon.

4. Enter the Client ID in the setup window:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Client ID**      | The Zenoti [Client ID](#client-id).         |
   | **Client secret**  | Leave this value blank.                     |
   | **Callback URL**   | Cyclr fills this field by default.          |
  
5. Select **Save Changes**.

> **Note**: To use different settings for different accounts, leave the value blank. This means Cyclr asks you to enter the value when you install the connector into an account.

### Account setup

Cyclr asks for the below values when you install the Zenoti connector into an account:

| Value              | Description                                 |
| :----------------- | :------------------------------------------ |
| **Client ID**      | The Zenoti [Client ID](#client-id) if you didn't set it up in the console.         |
| **Client secret**  | Leave this value blank.                     |
| **Username**       | Your Zenoti account username.               |
| **Password**       | Your Zenoti account password.               |

> **Note**: You can use different details for different accounts.
