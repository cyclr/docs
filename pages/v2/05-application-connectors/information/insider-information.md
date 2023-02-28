---
title: Insider information
sidebar: cyclr_sidebar
permalink: insider-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Unifier field (required)

In order to send data to Insider, you need to define a Unifier Field:

1. Go to `https://{AccountName}.inone.useinsider.com/crm-attributes`.
2. Select **Create New CRM Attribute**.
3. Set the **Data Type**.
4. When you set the **Attribute Name** for the Unifier Field, choose one of the default Unifier Field names (**email**, **phone_number**), or use a custom name of your choice.
5. Make sure this has been selected as the **Unifier**

![unifier field](./images/insider_unifier.png)

The Unifier field is references as **Identifier Type** in the Cyclr methods, as a required field.

</section>
<section class="card">

## Send Custom Data (Optional)

In order for Insider to accept your custom attribute fields they must first be defined in the InOne console.

1. Go to `https://{AccountName}.inone.useinsider.com/crm-attributes`.
2. Select **Create New CRM Attribute**.
3. Set the **Data Type** and **Attribute Name** for your custom attribute.

From the **Edit Connector** page within the Cyclr console:

1. Select the method you want to add custom fields to.
2. Select the **+** sign to bring up the **Add Method Field** form:

   ![add custom field](./images/insider_add_cf.png)
   ![add custom field](./images/insider_cf_form.png)

3. For a custom **user attribute**, set the **Field Location** to `[users].attributes.custom.**AttributeName**`. For example, `[users].attributes.custom.hair_color)`.

   > **Note**: The **Attribute Name** must be exactly as defined in the InOne console. Eg. case sensitive etc.

4. For a custom **event parameter**, set the **Field Location** to `[users].[events].event_params.custom.**EventParameterName**` For example, `[users].[events].event_params.custom.payment_type`.

   > **Note**: The **Event Parameter Name** does not need to be defined in the InOne console.

5. Enter a **Display Name**, **Description** and **Data Type**

   > **Note**: To integrate properly with the Insider API, the **Data Type** as set in this drop-down can only be **Text**, **Integer**, **Boolean** or **DateTime**.

</section>
