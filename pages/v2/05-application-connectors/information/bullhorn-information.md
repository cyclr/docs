---
title: Bullhorn information
sidebar: cyclr_sidebar
permalink: bullhorn-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Retrieve custom objects

> Note: This currently only applies to the **Job Order** methods

To retrieve custom object fields with your Job Order requests, follow these steps:

1. Find the fields of the custom object using the method **Job Orders** > **Get Custom Object Fields**

   ![Custom Object Fields](./images/bullhorn_cf_1.png)

2. Add the fields of the custom object to the desired method with the Field Location `[data].**CustomObjectName**.[data].**FieldName**` for **List New Job Orders** or **List Updated Job Orders**, or `data.**CustomObjectName**.[data].**FieldName**` for **Get Job Order**. For example, with List New Job Orders:

   ![Add Custom Fields](./images/bullhorn_cf_2.png)
   
3. Add the custom object name and field names to the **Custom Objects** parameter when you make the request. The correct format is `ObjectName(FieldName,FieldName,FieldName)`. For example:

   ![Add Query](./images/bullhorn_cf_3.png)

</section>
