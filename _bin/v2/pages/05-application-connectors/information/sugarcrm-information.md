---
title: SugarCRM Information
sidebar: cyclr_sidebar
permalink: sugarcrm-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

### Applying Filters To Calls

The following methods support the use of additional filters to refine your request:

- Get New And Updated Opportunities

- Search Opportunities

- Search Custom Objects

To apply an additional filter you should add a custom field to the request with a Field Location in the format of <em>field.operator</em> (example: campaign_name.$contains). You can then supply a value for that field when making your requests (example: 'Leads').

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

More information on adding custom fields can be found [here](https://docs.cyclr.com/adding-custom-fields).

</section>
