---
title: Webhook
sidebar: cyclr_sidebar
permalink: webhook
menus:
    tools:
        title: Webhook
        identifier: webhook
        toggleonly: menutoggleonly
        weight: 7
---
{::options parse_block_html="true" /}
<section class="card">

The new **Webhook** step allows you to set up a webhook from inside the template builder. This means that you don’t have to set up the **Generic Webhook **utility connector. Instead, you can define the fields within the webhook step to create a webhook for a specific cycle.

The Webhook step uses the Generic webhook functionality, which means that you are billed for the Generic webhook. However, you are only billed for a single one, and can use the webhook step multiple times.

For a webhook step that supports XML or field autodiscovery, you can see the documentation on the [Generic Webhook step](generic-webhook).

</section>
<section class="card">

## Set up the Webhook step

Select the **Step Setup** icon on the webhook step to configure it for your cycle.

The first field is the **Webhook URL**, which is automatically filled with the default value. You can’t edit this value in the step, but you can select **Copy** to copy the value.

To generate the fields you want to use, you can enter data into the **Paste JSON** box. Once the data is there, select **Save** to create the fields. When successful, the application displays a message that says: **Fields created successfully.**

If the data isn’t in the correct format, the application alerts you with the following error message: **Error encountered trying to generate custom fields**.

Since the **Webhook** step doesn’t store the values that you enter but generates custom data from your field mapping, the application may change the format and example values in the **Paste JSON** box.

>** Note**: This Webhook doesn’t support XML.

</section>
<section class="card">

## Field Mapping

After you generate the fields for the Webhook step with JSON, you can map these fields for subsequent steps in the cycle, according to how you want the webhook step to function.

You map these fields in the same way as a standard method step. For more information, see the Cyclr documentation on how to [map fields](field-mapping).


### Example

 \
For example, you can enter data such as the following into the **Paste JSON** box in the **Webhook** step setup:

```

{

    "field1": 1,

    "field2": "example"

}

```

If you then connect another step, such as a **Decision** step, to the webhook step, you can select **Webhook** as the source, and the **Field** dropdown shows the fields you created:


![A screenshot of the webhook fields in a subsequent step's field mapping.](./images/webhook-fields.png)

</section>
<section class="card">

## Limitations

Since your user’s template builder isn’t upgraded to 2.0 yet, your users can’t edit cycles with this step. This means you can only use the Webhook step if you have access to the console. 

If they don’t have access, the application redirects them to the list of cycles. While cycles including these steps are visible, the **Edit** and **Copy** buttons are disabled.

</section>