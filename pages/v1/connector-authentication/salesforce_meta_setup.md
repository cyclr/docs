---
title: Salesforce Metadata Connector Guide
sidebar: cyclr_sidebar
permalink: salesforce-metadata-connector
tags: [connector]
---

## Authentication

When installing the **Salesforce Metadata** Connector you'll need to provide a Username and Password for the Salesforce account you wish to work with.

You can optionally enter an Account Type.  Possible values are "enterprise" or "partner".

## Creating Custom Fields

To create custom fields within Salesforce, there are three fundamental steps that must be carried out:

* Create the custom field
* Set the field level security for the field
* Add the field to a layout

> In this example we will add a Picklist field to the Event Object and Layout using several Methods from the Salesforce Metadata Connector in a Cycle.

### Create the custom field

Many of the request fields for the method "Create Custom Field" are optional by default. It is the case, however, that depending on the Data Type selected some of the optional fields will be required. The following table details these requirements.

| Data Type | "Optional" Fields Required |
| :-------- | :------------------------- |
| Text      | Length                     |
| Number    | Precision, Scale           |
| Checkbox  | Default Value              |
| Picklist  | Picklist Values            |
| Currency  | Precision, Scale           |
| Percent   | Precision, Scale           |
| Location  | Scale                      |

> The Field Name for a custom field should end with "\_\_c". For example "myCustomField\_\_c".

![create field](./images/create_custom_field_2.png)

### Set the field level security for the field

Setting the field level security for a custom field in Salesforce defines the permissions each profile has in relation to the field. Examples of profiles include "Admin", "Standard", "Customer Community User" etc.

If you would like to make the field available to all profiles you should place a "List Profiles" step before the "Set Field Level Security" step in your cycle. You can then map the Profile Name from "List Profiles" and bulk update the permissions.

Alternatively to set the field level security for one profile only, the lookup feature is available to retrieve a list of profile names to choose from.

![field level security](./images/field_level_security.png)

### Add the field to a layout

Finally the field needs to be added to a specific layout within Salesforce. Both the Layout Name and Layout Section Label must be specified, both can be retrieved using the lookup feature for those fields.

![add to layout](./images/add_to_layout.png)

![full cycle](./images/full_cycle.png)

---

You will now be able to see the field from the Page Layouts interface in Salesforce: **Setup** > **Objects and Fields** > **Object Manager** > select the object > **Page Layouts**.

![event layout](./images/event_layout.png)

---

An example of a cycle where we are setting the field level security for all profiles might look as follows. Notably, we are adding "List Profiles" before "Set Field Level Security" to set the field level security for all profiles.

![example cycle](./images/salesforce_meta_1.png)
