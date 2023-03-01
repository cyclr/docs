---
title: Orderbot information
sidebar: cyclr_sidebar
permalink: orderbot-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Map custom fields

Methods in the **Products** > **Custom Fields** category dynamically return custom field data dependant on how custom fields are set up in the Orderbot UI. You can map these fields in Cyclr:

1. Go to the **Edit Connector** page for the Orderbot connector:
2. Under the **Methods and Fields** heading, expand the **Products** category and then **Custom Fields** category.
3. Expand the method you want to map custom fields for: either **Get Product (Custom Fields)** or **List Products (Custom Fields)**.
4. Select the pink **+** icon.
5. Enter the following: 
    | Value              | Description                                                  |
    | ------------------ | ------------------------------------------------------------ |
    | **Field Location** | The custom field name set within Orderbot. For get methods, this should just be entered as the field name. For list methods, this should be entered as the field name prepended with `[].`. For example, if the custom field in Orderbot is named `expLicCode`, then the field location for get methods should be set to `expLicCode` and for list methods should be set to `[].expLicCode`. |
    | **Display Name**   | The display name of the custom field within the Cyclr UI.    |
    | **Description**    | The description of the custom field within the Cyclr UI.     |
    | **Data Type**      | The data type of the custom field. This should match the data type of the custom field in Orderbot. |
    
6. Select **Create**.

</section>
