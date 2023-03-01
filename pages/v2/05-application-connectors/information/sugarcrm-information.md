---
title: SugarCRM information
sidebar: cyclr_sidebar
permalink: sugarcrm-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">
## Apply filters to calls

The following methods support the use of additional filters to refine your request:

- **Get New And Updated Opportunities**
- **Search Opportunities**
- **Search Custom Objects**

To apply an additional filte, you can add a custom field to the request with a** Field Location** in the format: `field.operator`, for example, `campaign_name.$contains`. You can then supply a value for that field when you make your requests, such as `Leads`.

The supported filter operators are as follows:

| Operator    | Description                                                                             |
| :---------- | :-------------------------------------------------------------------------------------- |
| $equals     | Performs an exact match on that field.                                                  |
| $not_equals | Matches on non-matching values.                                                         |
| $starts     | Matches on anything that starts with the value.                                         |
| $ends       | Matches anything that ends with the value.                                              |
| $contains   | Matches anything that contains the value.                                               |
| $in         | Finds anything where field matches one of the values as specified as an array.          |
| $not_in     | Finds anything where field does not match any of the values as specified as an array.   |
| $is_null    | Checks if the field is null. This operation does not need a value specified.            |
| $not_null   | Checks if the field is not null. This operation does not need a value specified.        |
| $lt         | Matches when the field is less than the value.                                          |
| $lte        | Matches when the field is less than or equal to the value.                              |
| $gt         | Matches when the field is greater than the value.                                       |
| $gte        | Matches when the field is greater than or equal to the value.                           |

For more information, see the Cyclr documentation on how to [add custom fields]](https://docs.cyclr.com/adding-custom-fields).

</section>
