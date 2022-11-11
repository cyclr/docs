---
title: Squareup Authentication
sidebar: cyclr_sidebar
permalink: squareup-connector
tags: [connector]
---

Squareup can be installed with either OAuth or Access Token authentication. When installed you select the authentication method to use.

# OAuth Authentication

OAuth can be used to authenticate both the sandbox and production versions of the Squareup environment. 

You must have an application created using the Squareup [Developer Dashboard](https://developer.squareup.com/apps). You use the application ID and OAuth secret generated on Squareup to authorize your connector.

In the [Developer Dashboard](https://developer.squareup.com/apps)

* Get your application credentials and set the redirect URL.

* Choose Open for an application. If you do not have an application set up create one.

* At the top of the page, set the dashboard mode to Production.

* In the left navigation pane, choose OAuth.

* In the Application ID box, copy and save the application ID.

* In the Application Secret box, choose Show, and then copy and save the application secret.

* In the Redirect URL box, enter the URL ```https://{Your Cyclr service domain}/connector/callback e.g. https://app-h.cyclr.com/connector/callback```. 

* Choose Save.

* [Seller Dashboard](https://squareup.com/dashboard/) navigate to Settings > App integrations to verify your application is installed.


# Access Token Authentication

Access tokens can be used to authenticate both the sandbox and production versions of the Squareup environment.

In order to obtain the access tokens go to the applications page in Squareup [here](https://developer.squareup.com/apps).

- Create a `New Application`, or select `View Details` of an existing application which you'd like to connect to Cyclr.
![](./images/squareup_application.png)

- If you wish to connect to the production environment. Copy the `Personal Access Token` seen on the page.
![](./images/squareup_credentials.png)

- If you wish to connect to the sandbox environment for staging. Scroll down to the sandbox section and copy the `Sandbox Access Token` from there.
![](./images/squareup_sandbox_credentials.png)

- Paste your token into the `API Key` field on the Connector Setup page.
![](./images/squareup_connector_setup.png)


# Cyclr setup

## Console setup

To set up your Squareup (OAuth) connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the Squareup (OAuth) connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:   
  * **Client ID**  The client ID of your Squareup account.
  * **Client Secret**  The client secret of your Squareup account. 
6. Select **Save Changes**.



# Authentication errors

If you see a "Not Authorized" message when you authenticate a Squareup connector, be sure you're using the correct details.

* Sandbox or Production **Access tokens** found under "Credentials" in Squareup are used with **API Key** authentication.
* Sandbox or Production **Application secrets** found under "OAuth" in Squareup are used with **OAuth** authentication.



