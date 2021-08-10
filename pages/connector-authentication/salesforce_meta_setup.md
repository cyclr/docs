---
title: Salesforce Metadata Connector Guide
sidebar: cyclr_sidebar
permalink: salesforce-metadata-connector
tags: [connector]
---

# Authentication

1. Locate the Salesforce Metadata connector

   > Cyclr Console > Connectors > Connector Library > Salesforce Metadata

2. From the Edit Connector interface click 'Setup'

3. Enter your Salesforce Username and Password

4. Optionally enter an Account Type, the possible values are "enterprise" or "partner"

5. Click **Next**

The connector is now authenticated and ready to use.

# Creating Custom Fields

To create custom fields there are three fundamental steps that must be carried out.

> In this example we will add a Picklist field to the Event Layout, via the Activity object.

## 1 - Create the custom field

Many of the request fields for the method "Create Custom Field" are optional by default. It is however the case that depending on the Data Type selected some of the optional fields will be required. The following table details these requirements.

| Data Type | "Optional" Fields Required |
| :-------- | :------------------------- |
| Text      | Length                     |
| Number    | Precision, Scale           |
| Checkbox  | Default Value              |
| Picklist  | Picklist Values            |
| Currency  | Precision, Scale           |
| Percent   | Precision, Scale           |
| Location  | Scale                      |

Please note: not all objects allow the addition of custom fields directly. For example to add a field to the Event object you should select Activity as the target object. Custom fields cannot be added directly to the Event object, instead they should be added to the Activity object, from which the Event object inherit's it's custom fields.

You can however add custom fields to the Event layout as we will see in step 3.

> The Field Name for a custom field should end with "\_\_c". For example "myCustomField\_\_c".

![Company information](./images/create_field.png)

## 2 - Set the field level security for the field

Setting the field level security for a custom field defines the permissions each profile has in relation to the field. Examples of profiles include "Admin", "Standard", "Customer Community User" etc.

If you would like to make the field available to all profiles you should place a "List Profiles" step before the "Set Field Level Security" step in your cycle. You can then map the Profile Name from "List Profiles" and bulk update the permissions.

Alternatively to set the field level security for one Profile only, the lookup feature is available to retrieve a list of profile names to choose from.

![Company information](./images/field_level_security.png)

## 3 - Add the field to a layout

Finally the field needs to be added to a specific layout. Both the Layout Name and Layout Section Label must be specified, however these can both be retrieved using the lookup feature for those fields.

![Company information](./images/add_to_layout.png)

---

You will now be able to see the field from the Page Layouts interface in Salesforce: **Setup** > **Objects and Fields** > **Object Manager** > select the object > **Page Layouts**.

![Company information](./images/event_layout.png)

---

An example of a cycle where we're setting the field level security for all profiles might look as follows.

![Company information](./images/salesforce_meta_1.png)