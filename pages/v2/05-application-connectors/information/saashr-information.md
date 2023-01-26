---
title: SaaShr information
sidebar: cyclr_sidebar
permalink: saashr-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Map custom fields

For methods that accept key and value pairs in an array, you might need to map custom fields. Some methods that require custom fields are **Update Cost Center** and **Update Employee Pay Information**. You can map these fields through the Cyclr console:

1. Go to the **Edit Connector** page for the SaaShr connector.
2. Under the **Methods & Fields** heading, find the method you want to map custom fields on.
3. Next to the **Request Fields** heading, select the red plus button.
4. In the **Field Location** box, enter the required custom field name and the field's index (as an integer) that you want to create in the format `{FieldName}.{FieldIndex}`. For example: `gl_codes.123`.
5. Enter a suitable **Display Name** for this field.
6. **Optional**: Provide a **Description** for this field.
7. Set the **Date Type** to **Text** for the field.
8. Select **Create**.
 
When you map a custom field for a method, the field is available in any steps that use the method. The value assigned to the field is stored in the custom field's array with the specified index. You can repeat the process for any key and value pair you want to add to the custom field's array.

### Available fields

* The **Update Cost Center** method allows this mapping for the following fields: `gl_codes`, `custom_fields` and `contacts`.
* The **Update Employee Pay Information** only allows this mapping for `gl_codes`.

</section>
