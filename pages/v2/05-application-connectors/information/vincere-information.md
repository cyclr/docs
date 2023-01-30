---
title: Vincere information
sidebar: cyclr_sidebar
permalink: vincere-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Use Custom Fields

When you use custom fields, the Field Location mapping varies based on the custom field type.

For example, to use Candidate custom fields:

1. Run the **Get Candidate Custom Fields** method to list the available custom fields.
2. Make note of the `Key` and `Type` fields in the response

If you want to add a custom field to **Get Candidate**, the table below shows the **Field Location** you need to use depending on the field type.

| Custom Field Type  | Field Location                                | Example                |
| :----------------- | :-------------------------------------------- | :--------------------- |
| TEXT_BOX           | The custom field's Key                        | 12345678901234567890   |
| TEXT_AREA          | The custom field's Key                        | 12345678901234567890   |
| CHECK_BOX          | The custom field's Key within square brackets | [09876543210987654321] |
| SELECT_BOX         | The custom field's Key within square brackets | [09876543210987654321] |
| RADIO              | The custom field's Key within square brackets | [09876543210987654321] |
| MULTIPLE_SELECTION | The custom field's Key within square brackets | [09876543210987654321] |

   ![custom fields for get methods](./images/vincere_custom_fields_1.png)

When you use List methods, such as **List New Candidate Records**, make sure to include the correct parent array. For example `[items]`.

   ![custom fields for list methods](./images/vincere_custom_fields_2.png)
   
For more information, see the Cyckr documentation on how to [add custom fields to a method](https://docs.cyclr.com/adding-custom-fields).

</section>
