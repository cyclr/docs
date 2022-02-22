---
title: Sage CRM Authentication
sidebar: cyclr_sidebar
permalink: sagecrm-connector
tags: [connector]
---

### Cyclr Setup

Setup your Sage CRM App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Sage CRM**
*   Click the **Setup** button

Enter the following values:

**Base URL**: Externally accessible URL of your instance. e.g. "https://crm.mysageinstance.com".

**Username**:  The username you use to login to your Sage CRM instance.

**Password**: The password you use to login to your Sage CRM instance.


Your Sage CRM Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.


### Custom Entity category

You can create custom categories that allow you to access custom object data. This can be achieved by doing the following:
* Collapse the **Custom Entity** category in the connectors setup page.
* Type in the object that you would like to retrieve the data from. This should be the exact name of the object e.g. "Users".
* A newly created category will appear in your list. You are now able to list and retrieve individual objects from the entered name of the custom object.

More information can be found here: https://docs.cyclr.com/enhanced-objects
