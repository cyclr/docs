---
title: OpenCRM Connector Guide
sidebar: cyclr_sidebar
permalink: opencrm-information
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Additional information

### Adding Custom Fields

Your records may contain custom fields which by standard are not mapped each method's request or response fields. The API field names for custom fields can be found in your custom field settings within OpenCRM. An example of a custom field API field name would be "cf_123".

Once you have identified the custom field you want to add mappings for these can be added following the steps from this guide: https://docs.cyclr.com/adding-custom-fields

Most importantly, the API field name is what should be provided for the Field Location of the custom field.

The format varies slightly depending on whether the field is for a singular or plural method. ie. Get Contact or List Contacts.

| Method Name           | Response/Request Field | Field Location           | Example   |
| :-------------------- | :--------------------- | :----------------------- | :-------- |
| Upsert Contact        | Request                | <em>APIFieldName</em>    | cf_123    |
| Get Contact           | Response               | <em>APIFieldName</em>    | cf_123    |
| List Contacts         | Response               | [].<em>APIFieldName</em> | [].cf_123 |
| List New Contacts     | Response               | [].<em>APIFieldName</em> | [].cf_123 |
| List Updated Contacts | Response               | [].<em>APIFieldName</em> | [].cf_123 |

</section>
