---
title: Chargebee information
sidebar: cyclr_sidebar
permalink: chargebee-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Use custom fields with Chargebee

You can set up custom fields within Chargebee, or you can add them manually through Cyclr. For more information about custom fields, see the  official [Chargebee documentation](https://www.chargebee.com/docs/2.0/custom_fields.html).

</section>
<section class="card">

## Set up custom fields in Chargebee

To set up a custom field in Chargebee:

1. Go to your **Chargebee Site**.
2. Select **Settings** in the left side menu.
3. Select **Configure Chargebee**.
4. Find and select **Custom fields**.
5.Select where you want to create the custom fields from the drop down. For example, **Customer** or **Subscriptions**.
6. Select the **field type** and fill in the details in the field creation screen that appears.
   * **Field Label**: Text that will appear on the UI for hosted pages and invoices.
   * **API Name**: Field reference for API calls and merges.

### Publish custom fields to a live site

The custom fields are considered active and are only available on the test site. To use the custom fields, you need to publish the fields to your live site. This means you can include custom field information in the invoices that you send to your customers, or in the hosted pages viewed by them. 

>**Note**: Ensure that you check how the fields work for all your use cases before you push it to your live site.

To publish your custom fields, go to the **Custom Fields main page**:

1. Select **Publish to Live** and confirm changes.
2. The custom fields will now be available on your **LIVE** site.

If you use **In-app Checkout**, navigate to **Settings** > **Configure Chargebee** > **Custom Fields** to make further changes in the LIVE site.

</section>
<section class="card">

## Manually add custom fields in Cyclr

You can set up custom fields in Cyclr. For more information, see the [Cyclr documentation](https://docs.cyclr.com/adding-custom-fields#example-field-locations).

> **Note**: Make sure to add these fields to all required methods. For example, `GET` and `UPDATE`.

1. From the builder’s sidebar, expand the Chargebee connector and select **Settings**.
2. In the section named **Methods and Fields**, expand the category and then the method you want to add fields to.
3. Under **Request Fields** or **Response Fields** (depending on whether you’re sending or receiving the field), select the **+** button to add a field.
4. The following needs to be specified:

   - **Field Location** - Make sure the location is exactly the same as in ChargeBee, with the format `API_Name`. For example, c`f_plan_id`.
   - **Display Name** - Enter a name to identify the field in the user interface.
   - **Description** - Optional: Write a description of the field, or instructions on how to use the field.
   - **Data Type** - Optional: Define a data type for your field. If the data type is datetime,  add the subtype to allow for type conversions between different standards.

### Field and data types

Each type of field has a corresponding data type:

- Single line text: 'Text' (maximum character limit is 99).
- Multiline text: 'Text' (maximum character limit is 250).
- Dropdown: 'Text'
- Checkbox: 'Boolean'
- URL: 'Text'
- Email: 'Text'
- Date picker: 'DateTime' subtype: 'yyyy-MM-dd'
- Timestamp: 'DateTime' subtype: 'unix'
- Numbers: 'Integer'


</section>
<section class="card">

## Configure meta data

For more information on meta data, see the  [Chargebee documentation](https://www.chargebee.com/docs/2.0/metadata.html).

### Manually add meta data custom fields in Cyclr

You can set up meta data custom fields in Cyclr. For more information, see the [Cyclr documentation](https://docs.cyclr.com/adding-custom-fields#example-field-locations).

> **Note**: Make sure to add these fields to all required methods. For example, `GET` and `UPDATE`.

1. From the builder’s sidebar, expand the Chargebee connector and select **Settings**.
2. In the section named **Methods and Fields**, expand the category and then the method you want to add fields to.
3. Under **Request Fields** or **Response Fields** (depending on whether you’re sending or receiving the field), select the **+** button to add a field.
4. The following needs to be specified:

   - **Field Location** - Enter the location in the format: "meta_data.`key`". This supports nested objects.
   - **Display Name** - Enter a name to identify the field in the user interface.
   - **Description** - Optional: Write a description of the field, or instructions on how to use the field.
   - **Data Type** - Optional: Define a data type for your field. If the data type is datetime,  add the subtype to allow for type conversions between different standards.

</section>
