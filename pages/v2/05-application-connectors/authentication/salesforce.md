---
title: Salesforce Authentication
sidebar: cyclr_sidebar
permalink: salesforce-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

This guide applies to Salesforce, Salesforce Service Cloud, and other services that use Salesforce authentication.

</section>
<section class="card">
## Partner Setup

Salesforce uses OAuth 2 for remote API access. To receive the OAuth **Client ID** and **Client Secret** values you need to authenticate with Salesforce, you need to register Cyclr within Salesforce as your own Connected App.

For more information on how to create a **Connected App**. see the [Salesforce documentation](https://help.salesforce.com/articleView?id=connected_app_create.htm).


</section>
<section class="card">

## Salesforce setup

Log into your Salesforce account. If you don't have an existing account, you can register for a free Salesforce Developer Edition account through the [Salesforce website](https://developer.salesforce.com/).

> **Note**: You can use any Salesforce account to create a Connected App, but note that Sandbox accounts destroy Connected Apps when you refresh.

### Create your App within Salesforce

The process of creating an app in Salesforce varies slightly depending on if you use **Salesforce Classic**, or **Lightning Experience**.

#### Salesforce Classic 
 1.   Log into your Salesforce account.
 2.   Select **Setup** in the top right of the page.
 3.   From the menu on the left, go to **Build** > **Create** > **Apps**.
 4.   From the **Connected Apps** table, select **New**.

#### Lightning Experience
1.   Log into your Salesforce account.
2.   Select **Setup** in the top right of the page.
3.   From the menu on the left, go to **Platform Tools** > **Apps** > **App Manager**.
4.   Select **New Connected App**.

### Enter basic information

Whether you are using **Salesforce Classic** or **Lightning Experience**, when the **New Connected App** screen is shown, complete the form as follows:

* **Connected App Name:** enter a name for your application

* **API Name:** this will default to the same value as your Connected App Name

* **Contact Email:** your email address

### API (Enable OAuth Settings)

Select the **Enable OAuth Settings** box to display further options.

* **Callback URL**: you need to add a callback URL so you can use Salesforce in your Cyclr Console and its accounts.
    The URLs is `https://{YourCyclrServiceDomain}/connector/callback`.

* **Selected OAuth Scopes**: you need to add the following 2 Scopes to enable Cyclr to use your App:
    * **Full access (full)**, or if you know which data you wish to restrict, you can select from this [list](https://help.salesforce.com/articleView?id=sf.remoteaccess_oauth_tokens_scopes.htm&type=5).
    * **Perform requests on your behalf at any time** (`refresh\_token, offline\_access`).

* **Require Secret for Refresh Token Flow**: make sure to clear this checkbox.

Your OAuth settings should look like the following image:

![Salesforce OAuth Partner Setup](./images/salesforce-partner-setup-oauth.png)

### Obtain authentication values

When you save the settings, you need to request access to view the consumer key and secret immediately. To request access, go to the **API (Enable OAuth Settings)** section and select the **Manage Consumer Details** button. Salesforce then emails you with a verification code that you can use to reveal the authentication values.

Make a note of the **Consumer Key** and **Consumer Secret** values as you’ll need them in order to authenticate the connector with Cyclr.

> **Note**: It can take up to 10 minutes for any changes to your Connected App to take effect in Salesforce. If you attempt to use your app before it has had time to update, you might encounter an error.

![Salesforce Update Error](./images/salesforce_update_error.png)

### Expired access/refresh token errors

Salesforce only allows up to five unique access/refresh token pairs to be issued for each user in a Connected App. Older tokens will be automatically revoked by Salesforce.  [More information](https://help.salesforce.com/articleView?id=remoteaccess_request_manage.htm).

</section>
<section class="card">

## Cyclr Setup

To set up the Salesforce connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Salesforce connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Client ID**   | The **Consumer Key** from your Salesforce Connected app.                          |
   | **Client Secret**   | The **Consumer Secret** from your Salesforce Connected app.    |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.


</section>
