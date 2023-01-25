---
title: Vincere Connector Guide
sidebar: cyclr_sidebar
permalink: vincere-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">
## Using Custom Fields

When using custom fields, the mapping of the Field Location will vary based on the custom field's "type".

For example when using Candidate custom fields:

1. Run the method "Get Candidate Custom Fields" to list the available custom fields
2. Pay close attention to the "Key" and "Type" fields in the response

If we now want to add a custom field to "Get Candidate" the Field Location, depending on the custom field's type, would be as follows:

| Custom Field Type  | Field Location                                | Example                |
| :----------------- | :-------------------------------------------- | :--------------------- |
| TEXT_BOX           | The custom field's Key                        | 12345678901234567890   |
| TEXT_AREA          | The custom field's Key                        | 12345678901234567890   |
| CHECK_BOX          | The custom field's Key within square brackets | [09876543210987654321] |
| SELECT_BOX         | The custom field's Key within square brackets | [09876543210987654321] |
| RADIO              | The custom field's Key within square brackets | [09876543210987654321] |
| MULTIPLE_SELECTION | The custom field's Key within square brackets | [09876543210987654321] |

   ![custom fields for get methods](./images/vincere_custom_fields_1.png)

When using List methods such as "List New Candidate Records", make sure to include the correct parent array. For example **[items]**.

   ![custom fields for list methods](./images/vincere_custom_fields_2.png)
   
A guide for adding custom fields to a method can be found [here](https://docs.cyclr.com/adding-custom-fields).

</section>
