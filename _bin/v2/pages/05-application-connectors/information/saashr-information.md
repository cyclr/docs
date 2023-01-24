---
title: SaaShr Information
sidebar: cyclr_sidebar
permalink: saashr-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

### Custom field mapping
In some cases, further field mapping is required on methods which accept key and value pairs in an array. This can be seen in the methods **Update Cost Center** and **Update Employee Pay Information**. To map fields, please follow these steps:

1. Go to the **Edit Connector** page for the SaaShr connector.
2. Under the **Methods & Fields** heading, find the method you wish to map custom fields on.
3. Next to the **Request Fields** heading, select the red plus button.
4. In the **Field Location** box, enter the required custom field name, followed by a dot, followed by the field's index you wish to create. The index must be an integer. For example: `gl_codes.123`.
5. Enter a suitable **Display Name** for this field.
6. Provide a **Description** for this field if you wish.
7. Set the **Date Type** to **Text** for the field.
8. Click **Create**.
9. The field will now be available in steps using this method. The value assigned to the field will be stored in the custom field's array with the specified index.
10. This process can be repeated for any key and value pair you wish to add to the custom field's array.

The **Update Cost Center** method allows this mapping for the following fields: `gl_codes`, `custom_fields` and `contacts`.

The **Update Employee Pay Information** only allows this mapping for `gl_codes`.

</section>
