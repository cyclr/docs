---
title: App Direct
sidebar: cyclr_sidebar
permalink: appdirect-connector
tags: [connector]
---

# App Direct

## Setup

In order to install a **App Direct (OAuth2.0)** Connector, you must first create a App Direct OAuth 2.0 **App** in App Directs's Developer portal.

### Preparation 

When creating your oAuth App, you will need to provide your Cyclr Partner **Service Domain** so it's best to have that information to hand before you begin.

This is specific to your instance of Cyclr and can be found in your Cyclr Partner Console under **Settings > General Settings > Service Domain**.

Your Cyclr Partner may have been setup with a default Service Domain, but this can be changed if you would prefer to remove mentions of 'cyclr' from it.  Contact Support for more.

### Creating a oAuth App

Follow the instructions provided by App Direct [here](https://help.appdirect.com/develop/Content/MarketplaceManager/Create-Web-ServerApp-API-Client.htm) to create a OAuth 2.0 App in App Direct.


Select:
* **Client Type:** Web server appliction 

* **Grant type:** Authorization Code and Refresh Token

* **Redirect URL(s)**, enter your Cyclr Service Domain in this format: `https://[Your Cyclr Service Domain]/connector/callback`

* **User-level scopes:** It is best practice to use the minimum required for the methods you require.

* **Allowed IP addresses:** Either leave blank, or if you wish to Cyclrs IP addresses to whitelist can be found [here](https://docs.cyclr.com/cyclr-ip-whitelisting)

After saving the form note down the Consumer Key (Client ID) and Secret (This will not be shown again) that are displayed

You should now take your Client ID and Client Secret values and store them in your Cyclr Console against the AppDirect entry.

### Cyclr Setup

From your Cyclr Console, click the **Connectors** option along the top then **Application Connector Library**, find **AppDirect** - you may need to use the Search box to locate it - then click the Padlock button and paste and save your values there.

You should now be able to successfully install a **AppDirect** Connector.

At this point it would be a good idea to install a Connector and run a test against one of the Methods, just to make sure the authentication process has been completed successfully.


