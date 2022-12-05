---
title: Adding Custom Fields
sidebar: cyclr_sidebar
permalink: adding-custom-fields
tags: [templates]
menus:
  templates:
    title: Adding Custom Fields
    url: /adding-custom-fields
    weight: 5
---

## Manually Adding Custom Fields

By default, connectors will only include the standard fields used by an application. Where you need to work with additional fields in the application you are connecting to, it is possible to add these using custom fields.

![](./images/connector-custom-field.gif)

To add a custom field:

*   From the builder’s sidebar, click to expand the app connector and click Settings
*   In the section named Methods and Fields, click to expand the category and then the method you wish to add fields to
*   Under Request Fields or Response Fields (depending on whether you're sending or receiving the field), click the + button to add a field

The following needs to be specified

| Property | Description |
| --- | --- |
| Field Location | This is the field name as used by the API. Often this is just a case of copying the syntax of the existing fields. |
| Display Name | This is the “friendly” name as it will be shown in the user interface. |
| Description | You can optionally describe the field and provide documentation, for example how it is used. |
| Data Type | You can optionally define a data type for your field.  If it is datetime then add the subtype to allow for type conversions between different standards. Read more about [data types](./data-types)|

## Example Field Locations

If you only have a few fields, you may want to add them manually.

Taking the following example Response:

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

The Field Locations for those properties would be as follows:<br>
``[customfields].first_name``<br>
``[customfields].last_name``<br>
``[customfields].address.city``<br>
``total_records``

If you have a large number of fields to add, there is a more automated option as described below.

## Adding Fields Using JSON Example

If you have a JSON example of the request or response then this can be used to auto-add additional or custom fields.

Simply take the 'spy glass' icon by the Request or Response area - depending on where you wish to add the fields - and paste in the JSON example in the popup that opens.  Any fields that do not already exist will be added.  You may then need to tidy up the field names and data types that have been automatically generated.

*NOTE: Before pasting in a large JSON example, reduce it to only what you wish to work with as a field will be added for each property it contains. Any you don't wish to keep must be deleted one-by-one.*
