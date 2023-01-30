---
title: Exact Connector
sidebar: cyclr_sidebar
permalink: exact-connector
tags: [connector]
---

Exact Setup
---------------
In order to authenticate the connector, you will need a **Client ID** and **Client Secret**.

First, you should register an app with Exact.

How to register your app
---------------

1. Go to the [Exact Online App Centre](https://apps.exactonline.com/gb/en-gb/V2).
2. From the country menu in the upper right corner of the website, select the preferred language.
3. Be aware that selecting a country defines the Exact Online website.
4. Click **Login**.
5. Enter your user name and password and click **Login**.
6. When you are authenticated you will be redirected to the App Centre.
7. Click **Manage my apps**
8. Click one of the options below:

    **Register for a testing app**: Your app will not be visible in the App Centre and cannot be used by external clients.
  
    **Register a production app**: Your app can be used by external clients. You have the option to publish your app in the App Centre, once it has been approved by your partner manager.

9. Enter a unique app name.  

   >A unique SEO name is automatically generated for the app name. The name of the app you create is unique per country, which means you can have an app with the same name across multiple countries.
  
10. For Redirect URI enter: <span>ht</span>tps://{{ServiceDomain}}/connector/callback (ServiceDomain should be substituted for your actual service domain)
    
    >Your Cyclr service domain, e.g. yourcompany.cyclr.com can be found in your Cyclr Console under Settings > General Settings > Service Domain.

11. Scroll down to find your Client ID and Client Secret. You can use these to authenticate your Exact connector.

  

    [For more information on getting your app set up, visit the official exact docs here](https://support.exactonline.com/community/s/knowledge-base#All-All-DNO-Content-oauth-eol-oauth-devstep1).

