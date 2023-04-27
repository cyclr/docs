---
title: Squareup Authentication
sidebar: cyclr_sidebar
permalink: squareup-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Squareup setup

You can install Squareup with either OAuth or Access Token authentication. When installed, select the authentication method to use.

### OAuth Authentication

You can use OAuth to authenticate both the sandbox and production versions of the Squareup environment. 

You need an application created with the Squareup [Developer Dashboard](https://developer.squareup.com/apps).To authenticate your connector, use the application ID and OAuth secret generated on Squareup.

In the [Developer Dashboard](https://developer.squareup.com/apps):

1.  Get your application credentials and set the redirect URL.

2.  Select **Open** for an application. If you don't have an application set up, create one.

3.  At the top of the page, set the dashboard mode to **Production**.

4.  In the left navigation pane, select **OAuth**.

5.  In the **Application ID** box, copy and save the application ID.

6.  In the **Application Secret box**, copy and save the application secret.

7.  In the **Redirect URL** box, enter the URL ```https://{Your Cyclr service domain}/connector/callback e.g. https://app-h.cyclr.com/connector/callback```. 

8.  Select **Save**.

To verify you installed your application, navigate to **Settings** > **App integrations** in the [Seller Dashboard](https://squareup.com/dashboard/).


### Access Token Authentication

You can use access tokens to authenticate both the sandbox and production versions of the Squareup environment.

To obtain the access tokens, go to the [applications page](https://developer.squareup.com/apps) in Squareup.

1.  Select the plus icon for a new application, or select **Open** on an existing application which you want to connect to Cyclr.
![The Squareup application page.](./images/squareup_application.png)

  *  To connect to the production environment, select **Production** at the top of the page and copy the **Production Access Token** seen on the page.
  ![The Squareup credentials page.](./images/squareup_credentials.png)

  *  To connect to the sandbox environment for staging, select **Sandbox** at the top of the page and copy the **Sandbox Access Token**.
  ![The Sandbox credentials page.](./images/squareup_sandbox_credentials.png)

2.  Paste your token into the **API Key** field on the Connector Setup page.
![The Squareup connector page.](./images/squareup_connector_setup.png)



</section>
<section class="card">
## Cyclr setup

To set up your Squareup (OAuth) connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the Squareup (OAuth) connector.
4. Select the **Setup Required** icon.
5. Enter the below values:   
  * **Client ID**: The client ID of your Squareup account.
  * **Client Secret**: The client secret of your Squareup account. 
6. Select **Save Changes**.

> **Note**: To use different settings for this connector on each account, leave these fields blank. This means Cyclr asks for these values when you install the connector into an account. 



</section>
<section class="card">
## Authentication errors

If you see a "Not Authorized" message when you authenticate a Squareup connector, make sure you're using the correct details:

* Sandbox or Production **Access tokens** found under "Credentials" in Squareup work with **API Key** authentication.
* Sandbox or Production **Application secrets** found under "OAuth" in Squareup work with **OAuth** authentication.

</section>
