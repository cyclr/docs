---
title: Insider Connector Guide
sidebar: cyclr_sidebar
permalink: insider-connector
tags: [connector]
---

## Connector Setup

To setup the connector you will need a **Partner Name** and **Request Token**, both of which should be provided by Insider.

1. Locate the Insider connector in the Cyclr console.

   > Cyclr Console > Connectors > Connector Library > Insider

2. Click the open padlock and on the next page enter the **Partner Name** and API Key (your Insider **Request Token**).

The connector is now authenticated and ready to use.

## User Guide

### Unifier Field (Required)

In order to send data to Insider, you must initialize a Unifier Field:

1. Go to https://{AccountName}.inone.useinsider.com/crm-attributes

2. Click **Create New CRM Attribute**

3. Set **Data Type** as **String** and **Attribute Name** as **email**

4. Make sure this has been selected as your **Unifier**

![unifier field](./images/insider_unifier.png)

This will pertain to the **Identifier Email** request field in the Cyclr methods which is a required field.

### Sending Custom Data (Optional)

In order for Insider to accept your custom attribute fields they must first be initialized in the Insider console.

1. Go to https://{AccountName}.inone.useinsider.com/crm-attributes

2. Click **Create New CRM Attribute**

3. Set the **Data Type** and **Attribute Name** for your custom attribute

Now from the **Edit Connector** page within the Cyclr console:

1. Select the method you want to add custom fields to

2. Click the **+** sign to bring up the **Add Method Field** form

   ![add custom field](./images/insider_add_cf.png)
   ![add custom field](./images/insider_cf_form.png)

3. For a custom **user attribute** the **Field Location** must be:

   - [users].attributes.custom.**AttributeName** (eg. [users].attributes.custom.hair_color)

   > Note: The **Attribute Name** must be exactly as defined in the Insider console. Eg. case sensitive etc.

4. For a custom **event parameter** the **Field Location** must be:

   - [users].[events].event_params.custom.**EventParameterName** (eg. [users].[events].event_params.custom.payment_type)

   > Note: The **Event Parameter Name** does not need to be defined in the Insider console.

5. Enter a **Display Name**, **Description** and **Data Type**

   > Note: To integrate properly with the Insider API, the **Data Type** as set in this drop-down can only be **Text**, **Integer**, **Boolean** or **DateTime**.

Your custom field is now initialized and ready to use.
