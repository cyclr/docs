---
title: BigChange JobWatch information
sidebar: cyclr_sidebar
permalink: bigchange-jobwatch-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">


</section>
<section class="card">

## Map custom fields

The BigChange JobWatch connector has custom field support for several methods. For more information, see the  find a [list of compatible methods](#custom-field-compatiable-methods). To add a custom field to a method:

1. Go to the **Edit Connector** page for the BigChange JobWatch connector.
2. Under the **Methods & Fields** heading, locate the required method by expanding out the categories and method name.
3. Select the pink **+** button to add a method field.
4. Enter the following:
5. 
   | Value              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | The custom field location, which must have the format `cust_<custom field name>`. The `<custom field name>` value has the exact same format as on the contact details page. |
   | **Display Name**   | The display name of the custom field within the Cyclr UI.    |
   | **Description**    | The description of the custom field within the Cyclr UI.     |
   | **Data Type**      | The data type of the custom field. This should be set to `Text`. |
   
5. Select **Create**.

<a name="custom-field-compatiable-methods"></a>


</section>
<section class="card">

## Custom field compatible methods

You can add custom fields for contacts, contact notes, and jobs in the following methods:

-   `Create Contact`
-   `Update Contact`
-   `Update Contact Note`
-   `Create Job`
-   `Update Job`

You can view custom fields for contacts, contact notes, and jobs in the following methods:

-   `Get Contact`
-   `Get Contact Note`
-   `Get Job`
-   `List Contact Notes`
-   `List Contacts`
-   `List Group Jobs`
-   `List Jobs`
-   `List Jobs by Contact`
-   `Search Contacts`
-   `Search Contacts By Email`
-   `Search Contacts By Email, ID, Or Reference`
-   `Search Contacts By Phone Number`
-   `Search Contacts By Postcode`

</section>
