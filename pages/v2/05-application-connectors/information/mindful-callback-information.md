---
title: Mindful Callback information
sidebar: cyclr_sidebar
permalink: mindful-callback-information
tags: [connector]

linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Create Callback method

The **Create Callback** method allows you to send a `user_data` object with the request. This object can contain any number of key and value pairs. To send a key and value pair:

1. Go to the **Edit Connector** page for the Mindful Callback connector.
2. Under the **Methods & Fields** heading, find and select the **Create Callback** method.
3. Next to the **Request Fields** heading, select the red plus button.
4. In the **Field Location** box, enter `user_data.`, followed by the required key name. For example, `user_data.key1`.
5. Enter a suitable **Display Name** for this field.
6. Provide a **Description** for this field if you want to.
7. Set the **Date Type** to **Text** for the field.
8. Select **Create**.

This makes the field available in steps that use the **Create Callback** method. The value you assign to the field is stored and sent in the `user_data` object against the specified key name. You can repeat this process for any key and value pair you want to add to the `user_data` object.

> **Note**: Only keys that are allowlisted by the Widget’s User Data Set are submitted to Mindful Callback.

</section>
