---
title: RFMS Authentication
sidebar: cyclr_sidebar
permalink: rfms-connector
tags: [connector]


---

<a name="rfms-set-up"></a>

# RFMS set up

You need the following information to set up the RFMS connector in Cyclr:

- The [Store ID and API Key](#getting-the-store-id-and-api-key)

<a name="getting-the-store-id-and-api-key"></a>

### Getting the Store Id and Api Key

You need a Store ID and Api Key to authenticate the RFMS connector in
Cyclr. Before you can get these you need to
[generate an API Token](https://rfmsapps.zendesk.com/hc/en-us/articles/360015957574-RFMS-Standard-API). You can
find RFMS' guide on getting the Store ID and Api Key in the RFMS
console [here](https://rfmsapps.zendesk.com/hc/en-us/articles/360015957574-RFMS-Standard-API).

# Cyclr set up

<a name="console-setup"></a>

### Console setup

To set up your RFMS connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the RFMS connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different
   settings for each account on installation:
   - **StoreId**: The [Store ID](#getting-the-store-id-and-api-key) of your
     RFMS account.
   - **Api Key**: The [API Key](#getting-the-store-id-and-api-key) of
     your RFMS account.
6. Select **Save Changes**.

Your RFMS connector is now set up! You can test it by installing it to a
Cyclr account and then executing one of the methods to confirm it returns data.
