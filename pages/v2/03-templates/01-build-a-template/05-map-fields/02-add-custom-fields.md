---
title: Add custom fields
sidebar: cyclr_sidebar
permalink: adding-custom-fields
tags: [templates]

menus:
    fields:
        title: Add custom fields
        identifier: adding-custom-fields
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">


By default, connectors only include the standard fields that an application uses. If you need to work with additional fields in the application, you can add custom fields to the connector.

### Access connector settings

There are multiple ways you can access a connector's settings:

* From the template builder, select the application connector to expand it, and then select **Settings**.
* From the Cyclr console, select **Templates** > **Template Connectors** from the menu, and then select the **Edit Connector** icon next to the connector you want to edit.

</section>
<section class="card">

## Manually add custom fields

1. In the section named **Methods and Fields**, select the category you want to use to expand it, and then select the method you want to add fields to.
2. Select the  **Add field** plus icon by either **Request Fields** or **Response Fields** (depending on whether you’re sending or receiving the field) to add a field.

![A screenshot with a red box to highlight the button you select to add a custom field.](./images/connector-custom-field.png)

3. Specify the following values:

| **Property** | **Description** |
|---|---|
| **Field Location** | The field name that the API uses. You can usually copy the syntax of the existing fields. |
| **Display Name** | The name that displays to your customers in the interface. |
| **Description** | **Optional**. You can describe the field and provide documentation. |
| **Data Type** | **Optional**. You can define a data type for your field. If it’s a datetime, then you can add the subtype to allow for type conversions between different standards. For more information, see the page on [data types](data-types). |


### Example field locations

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

If you have a large number of fields to add, you can use [JSON](#use-json-to-add-fields) to automate the process .


</section>
<section class="card">

## Use JSON to add fields

If you have a JSON example of the request or response, you can use the JSON to auto-add custom fields:

1. In the section named **Methods and Fields**, select the category you want to use to expand it, and then select the method you want to add fields to.
2. Select the **Generate Fields** pencil icon from either the **Request** or **Response** fields area, dependent on where you want to add the fields.
3. Paste the JSON example into the popup window that opens and select **Generate**.

This adds any fields that don’t already exist, but you might still need to check over the field names and data types that are automatically generated.

> **Note**: Before you paste in a large JSON example, ensure that it only contains properties that you want to add as fields.

</section>
