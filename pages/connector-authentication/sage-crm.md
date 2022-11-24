---
title: Sage CRM Authentication
sidebar: cyclr_sidebar
permalink: sagecrm-connector
tags: [connector]
---

# Sage setup

### Enabling Allow Web Service Access for SOAP methods

Several legacy methods in the Sage CRM connector target SOAP endpoints. These methods include `(SOAP)` in the method name to indicate this. They require `Allow Web Service Access` from within a Sage CRM administrator account to be set to `true` to function. You can do this by following Sage's documentation [here](https://help.sagecrm.com/on_premise/en/2021R1/Dev/Content/Developer/WS_WebServicesUserSetup.htm). There's also a further setup guide detailing how to configure this web service once enabled [here](https://help.sagecrm.com/on_premise/en/2021R1/Dev/Content/Developer/WS_SpecifyingWebServiceConfigurationSettings.htm).

Some Sage CRM accounts may not have the ability to allow web service access. In this case, any methods marked `(SOAP)` will not function correctly.

# Cyclr setup

Setup your Sage CRM connector within Cyclr:

1. Go to your **Cyclr Console**
2. Click the **Connectors** menu along the top
3. Choose Connector Library
4. Scroll down to **Sage CRM**
5. Click the **Setup** button

Enter the following values:

-   **Base URL**: Externally accessible URL of your instance. e.g. "https://crm.mysageinstance.com".
-   **Username**: The username you use to login to your Sage CRM instance.
-   **Password**: The password you use to login to your Sage CRM instance.

Your Sage CRM Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

# Additional Information

### Custom Entity category

You can create custom object categories that allow you to access custom object data. To do this:

1. On the connector setup page, click on the **Custom Entity** category to expand it.
2. Click on the pink **Copy this Category to create a Custom Object Category** button.
3. In the **Specify object name** field, type in the object that you would like to retrieve the data from. This needs to be the exact name of the object, for example, "Users".
4. Click **Copy** to create the custom object. A dialogue appears to confirm it has been created.
5. The custom category created appears in your **Methods & Fields** list.

You can use this to list and retrieve individual objects based on the entered name of the custom object. More information can be found [here](https://docs.cyclr.com/enhanced-objects).
