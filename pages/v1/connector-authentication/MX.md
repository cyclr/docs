---
title: MX Authentication
sidebar: cyclr_sidebar
permalink: mx-connector
tags: [connector]

---

## MX setup

To authenticate the MX connector, you will need a valid `Client ID` and `API Key`.

To obtain an `API Key` and authenticate the connector, please follow the steps below:

### 1. Log into the MX dashboard

Log into the MX dashboard found [here](https://dashboard.mx.com).

### 2. Locate a valid `Client ID` and `API Key`

On the home page of the dashboard, find the available `Client ID` and `API Key` seen under **Your Account** in either the **Development** or **Production** sections, depending on which environment you wish to authenticate.

### 3. Allow the Cyclr IP address to access MX 

Add the Cyclr servers IP to MX Whitelist. https://docs.cyclr.com/cyclr-ip-allowlist (note they only allow US server IP's)


## Authenticate the connector

You can now use the `Client ID` and `API Key` to authenticate your MX connector. First select either the **Development URL** or **Production URL** depending on which environment you wish to authenticate. Click next. Then enter the corresponding `Client ID` and `API Key` and click next.

Your MX connector is now set up! You can test it by installing it to one of your Cyclr accounts and using one of the methods to confirm it returns data. Please read the information below concerning how to run `Institution` methods.


# Additional information


## Creating custom Institution objects

Once the connector is authenticated, you can create custom `Institution` objects. This will automatically populate request and response fields for methods within the custom object. To create a custom object:

1. Go to the **Edit Connector** page for the MX connector.
2. Under the **Methods & Fields** heading, locate the **Institutions** category and select it to expand.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Use the dropdown menu to select the required `Institution`.
5. Select **Copy**.
6. This process can be repeated for any number of available `Institutions`.

Methods in the newly created custom category will now run against the specified `Institution`.
