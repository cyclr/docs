---
title: Service Fusion Authentication
sidebar: cyclr_sidebar
permalink: servicefusion-connector
tags: [connector]
---


# Partner Setup

Before you can install your connector, you need to register an oAuth application with Service Fusion:

* In [OAuth Apps](https://admin.servicefusion.com/developerSettings/oauthApps), create new app (if you don't already have one) by clicking to Add New OAuth App.
* Enter the Name and Redirect URL.
{% raw %}`https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback`{% endraw %}
* Click Add OAuth App, you will be redirected to the page with the generated Client ID and Client Secret for your app.
* Save the generated Client ID and Client Secret of your app, you will need them in the next steps.


### Cyclr Setup

Setup your Service Fusion App within Cyclr:

*   go to your **Cyclr Console**
*   click the **Connectors** menu along the top
*   choose Connector Library
*   Search for **Service Fusion**
*   click the **Setup** button

Enter the following values:

**Client ID**:  the _Consumer Key_ of your Salesforce Connected App

**Client Secret**: the _Consumer Secret_ of your Salesforce Connected App
