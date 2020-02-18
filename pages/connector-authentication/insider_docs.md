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

In order to send data to Insider, you must first define a Unifier Field:

1. Go to https://{AccountName}.inone.useinsider.com/crm-attributes

2. Click **Create New CRM Attribute**

3. Set the **Data Type**

4. When setting the **Attribute Name** for the Unifier Field you have the choice of one of the default Unifier Field names (**email**, **phone_number**), or you can use a custom name of your choice

5. Make sure this has been selected as the **Unifier**

![unifier field](./images/insider_unifier.png)

This is what will be referenced by **Identifier Type** in the Cyclr methods which is a required field.

### Sending Custom Data (Optional)

In order for Insider to accept your custom attribute fields they must first be defined in the InOne console.

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

   > Note: The **Attribute Name** must be exactly as defined in the InOne console. Eg. case sensitive etc.

4. For a custom **event parameter** the **Field Location** must be:

   - [users].[events].event_params.custom.**EventParameterName** (eg. [users].[events].event_params.custom.payment_type)

   > Note: The **Event Parameter Name** does not need to be defined in the InOne console.

5. Enter a **Display Name**, **Description** and **Data Type**

   > Note: To integrate properly with the Insider API, the **Data Type** as set in this drop-down can only be **Text**, **Integer**, **Boolean** or **DateTime**.

Your custom field is now initialized and ready to use.
