---
title: Add custom fields
sidebar: cyclr_sidebar
permalink: adding-custom-fields
tags: [templates]

menus:
    create-cycle-templates:
        title: Add custom fields
        identifier: adding-custom-fields
        toggleonly: menutoggleonly
        weight: 4
---
{::options parse_block_html="true" /}
<section class="card">

## Manually add custom fields

By default, connectors only include the standard fields that an application uses. If you need to work with additional fields in the application, you can add custom fields to the connector.

### Access connector settings

There are multiple ways to access a connector's settings:

* From the template builder, select the application connector to expand it and then select **Settings**.

* From the Cyclr console, select **Templates** > **Template Connectors** from the menu, and then select the **Edit** button next to the Connector you want to edit.

### Add/update fields

1.   In the section named **Methods and Fields**, select the category you want to use to expand it, and then select the method you want to add fields to.
2.   Under **Request Fields** or **Response Fields** (depending on whether you're sending or receiving the field), select the **+** button to add a field.

![A screenshot with a red box to highlight the button you select to add a custom field.](./images/connector-custom-field.png)

3. Specify the following values:

| Property | Description |
| --- | --- |
| Field Location | This is the field name as used by the API. Often this is just a case of copying the syntax of the existing fields. |
| Display Name | This is the “friendly” name as it will be shown in the user interface. |
| Description | You can optionally describe the field and provide documentation, for example how it is used. |
| Data Type | You can optionally define a data type for your field.  If it is datetime then add the subtype to allow for type conversions between different standards. Read more about [data types](./data-types)|


</section>
<section class="card">

## Example field locations

If you only have a few fields, such as in the example response below, you can add the fields manually. 

```JSON
{
    "customfields":[
        {
            "first_name":"John",
            "last_name":"Smith"
            "address":{
                "city": "London"
            }
        }
    ],
    "total_records": 23
}
```

For this example, the field locations for those properties are as follows:<br>
``[customfields].first_name``<br>
``[customfields].last_name``<br>
``[customfields].address.city``<br>
``total_records``

If you have a large number of fields to add, you can automate the process using [JSON](#use-json-to-add-fields).


</section>
<section class="card">

## Use JSON to add fields

If you have a JSON example of the request or response, you can use the JSON to auto-add additional or custom fields:

1. Select the magnifying glass icon from either the request or response area, dependent on where you want to add the fields.
2. Paste the JSON example into the popup window that opens.

This adds any fields that don't already exist, but you might still need to check over the field names and data types that are automatically generated.

> **Note**: Before you paste in a large JSON example, ensure that it only contains properties that you want to add as fields.

</section>
