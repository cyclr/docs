---
title: Salesforce Metadata Connector Guide
sidebar: cyclr_sidebar
permalink: salesforce-metadata-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Create Custom Fields

To create custom fields in Salesforce, you need to do three steps:

* Create the custom field
* Set the field level security for the field
* Add the field to a layout

The example on this page adds a **Picklist** field to the **Event Object** and **Layout** using several methods from the Salesforce Metadata Connector in a cycle.

### Create the custom field

Many of the request fields for the **Create Custom Field** method are optional by default, but some of these fields are required for different data types. The following table details these requirements:

| Data Type | "Optional" Fields Required |
| :-------- | :------------------------- |
| Text      | Length                     |
| Number    | Precision, Scale           |
| Checkbox  | Default Value              |
| Picklist  | Picklist Values            |
| Currency  | Precision, Scale           |
| Percent   | Precision, Scale           |
| Location  | Scale                      |

> **Note**: End the **Field Name** for a custom field with `\_\_c`. For example `myCustomField\_\_c`.

![create field](./images/create_custom_field_2.png)

### Set the field level security for the field

To define the permissions each profile has in relation to the field, set the field level security for a custom field in Salesforce. For example, some profiles you can use are **Admin**, **Standard**, and **Customer Community User**.

To make the field available to all profiles, you can place a **List Profiles** step before the **Set Field Level Security** step in your cycle. You can then map the Profile Name from **List Profiles** and bulk update the permissions.

To set the field level security for one profile only, you can use the lookup feature to retrieve a list of profile names to choose from.

![field level security](./images/field_level_security.png)
</section>
<section class="card">

## Add custom field to a layout

To add the field to a specific layout within Salesforce, you need to specify both the **Layout Name** and **Layout Section Label**. You can use the Lookup feature to find the values for both of those fields.

![add to layout](./images/add_to_layout.png)

![full cycle](./images/full_cycle.png)

When you add the custom field, you can view the field from the Page Layouts interface in Salesforce. Go to **Setup** > **Objects and Fields** > **Object Manager**, select the object, and select **Page Layouts**.

![event layout](./images/event_layout.png)

### Example

An example of a cycle where you set the field level security for all profiles might look similar to the image below. To set the field level security for all profiles,the example adds the **List Profiles** step before the **Set Field Level Security** step.

![example cycle](./images/salesforce_meta_1.png)

</section>
