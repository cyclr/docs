---
title: OpenCRM information
sidebar: cyclr_sidebar
permalink: opencrm-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Add custom fields

Your records may contain custom fields which aren't mapped for each method's request or response fields. You can find the API field names for custom fields in your custom field settings within OpenCRM. An example of a custom field API field name is `cf_123`.

To add mappings  for a custom field, you can follow the steps in the Cyclr documentation on how to [Add custom fields](adding-custom-fields/

To add a custom field, you need to provide the API field name for the **Field Location** of the custom field.

The format varies slightly depending on whether the field is for a singular or plural method, such as **Get Contact** or **List Contacts**.

| Method Name           | Response/Request Field | Field Location           | Example   |
| :-------------------- | :--------------------- | :----------------------- | :-------- |
| Upsert Contact        | Request                | <em>APIFieldName</em>    | cf_123    |
| Get Contact           | Response               | <em>APIFieldName</em>    | cf_123    |
| List Contacts         | Response               | [].<em>APIFieldName</em> | [].cf_123 |
| List New Contacts     | Response               | [].<em>APIFieldName</em> | [].cf_123 |
| List Updated Contacts | Response               | [].<em>APIFieldName</em> | [].cf_123 |

</section>
