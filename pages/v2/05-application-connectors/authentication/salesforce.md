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

Salesforce uses OAuth 2 for remote API access. You must register Cyclr within Salesforce as your own Connected App to receive OAuth Client ID and Client Secret values to enable Cyclr to authenticate with Salesforce.

You can find the official Salesforce documentation for creating a **Connected App** [here](https://help.salesforce.com/articleView?id=connected_app_create.htm).


</section>
<section class="card">
## Salesforce Setup – Register Your Application

You can register for a free [Salesforce Developer Edition account here (click "Sign Up" at the top of that page)](https://developer.salesforce.com/) or log into your existing Salesforce account if you have one.  You can use any Salesforce account to create a Connected App, it doesn’t have to be a Developer Edition account, but we would advise against using a Sandbox account as Connected Apps are destroyed when they are refreshed.

### Create your App within Salesforce

The process of creating an app in Salesforce varies slightly depending upon whether you are using **Salesforce Classic**, or **Lightning Experience**.

> #### Salesforce Classic 
> 1.   Log into your Salesforce account
> 2.   Click **Setup** in the top right
> 3.   From the menu on the left, select **Build** > **Create** > **Apps**
> 4.   From the **Connected Apps** table click **New**

> #### Lightning Experience
> 1.   Log into your Salesforce account
> 2.   click **Setup** in the top right
> 3.   From the menu on the left, select **Platform Tools** > **Apps** > **App Manager**
> 4.   Click **New Connected App**

### Basic Information

Whether you are using **Salesforce Classic** or **Lightning Experience**, when the **New Connected App** screen is shown, complete the form as follows:

* **Connected App Name:** enter a name for your application

* **API Name:** this will default to the same value as your Connected App Name

* **Contact Email:** your email address

### API (Enable OAuth Settings)

Tick the **Enable OAuth Settings** box to display further options.

* **Callback URL**: you must add a callback URL to allow Salesforce to be used in your Cyclr Console and its accounts.
    The URLs is `https://{YourCyclrServiceDomain}/connector/callback`.

* **Selected OAuth Scopes**: you must add the following 2 Scopes to enable Cyclr to use your App:
    * **Full access (full)** or if you know which data you wish to restrict to you can select from this [list](https://help.salesforce.com/articleView?id=sf.remoteaccess_oauth_tokens_scopes.htm&type=5).
    * **Perform requests on your behalf at any time** (`refresh\_token, offline\_access`).

* **Require Secret for Refresh Token Flow**: make sure to **clear** this checkbox.

The OAuth settings should look like this:

![Salesforce OAuth Partner Setup](./images/salesforce-partner-setup-oauth.png)

After saving your App, make a note of your **Consumer Key** and **Consumer Secret** values as you’ll need to enter these into Cyclr.

> **Note**: It can take up to 10 minutes for any changes to your Connected App to take effect in Salesforce. If you attempt to use your app before it has had time to update, you might encounter an error.

![Salesforce Update Error](./images/salesforce_update_error.png)

</section>
<section class="card">

## Cyclr Setup

Setup your Salesforce App within Cyclr:

*   go to your **Cyclr Console**
*   click the **Connectors** menu along the top
*   choose Connector Library
*   scroll down to **Salesforce**
*   click the **Setup** button

Enter the following values:

**Client ID**:  the _Consumer Key_ of your Salesforce Connected App

**Client Secret**: the _Consumer Secret_ of your Salesforce Connected App

Your Salesforce Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

### Expired access/refresh token errors

Salesforce only allows up to five unique access/refresh token pairs to be issued for each user in a Connected App. Older tokens will be automatically revoked by Salesforce.  [More information](https://help.salesforce.com/articleView?id=remoteaccess_request_manage.htm).


</section>
