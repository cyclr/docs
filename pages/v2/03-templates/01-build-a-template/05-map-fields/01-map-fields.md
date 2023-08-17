---
title: Map fields
sidebar: cyclr_sidebar
permalink: field-mapping
tags: [templates]

menus:
    fields:
        title: Map fields
        identifier: field-mapping
        toggleonly: menutoggleonly
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">
After you join two steps in the template builder, you can map the fields to determine how the steps interact with your data. To map a step’s fields, select the **Step Setup** cog icon on the step.

![An example of the Step Setup window where you can map fields.](./images/field-mapping-eg.png)

The column on the left displays the different fields for the step. You need to map all the fields that show a tick in the Required column in order for the step to work.

You can use the other columns to choose the sources that the step gets data from. These sources can be data from any preceding step, a combination of steps, or data that you enter.

</section>
<section class="card">

## Sources

There are several types of source that you can use to map data. The options available when you map a field depend on both the type of step and field you use.

| **Source** | **Usage** |
|---|---|
| **Ignore** | Leave the field blank and exclude it from the API call. |
| **Variable** | Use a parameter that you defined for the overall template. You can use these [variables](template-settings#variables) in multiple places in the template design. |
| **Type a Value** | Type in text or use [mergefields](#system-mergefields) to merge one or more values into the field. |
| **Previous Step** | Select data from a previous step to use. When possible, Cyclr suggests a mapping. |
| **Lookup** | Use Cyclr to connect to the third party application and retrieve a list of possible mapping values. For example, a mailing lists in an email marketing platform. |
| **Select a Value** | Select a value from a pre-configured list of values. |

</section>
<section class="card">

## System mergefields

You can use Cyclr system mergefields as the source value when you map fields.

| **Merge Field** | **Usage** |
|---|---|
| `{% raw %}{{LastSuccessfulRunDate}}{% endraw %}` | The last successful run date of the current step. For example, you can use this if you only want to get the latest data. |
| `{% raw %}{{Cyclr_Auth_ApiKey}}{% endraw %}` | The API key if the connector is using API key as the authentication type. |
| `{% raw %}{{Cyclr_Auth_Username}}{% endraw %}` | The username if the connector is using username/password as the authentication type. |
| `{% raw %}{{Cyclr_Auth_Password}}{% endraw %}` | The password if the connector is using username/password as the authentication type. |

You can use these mergefields to map fields directly, or as part of the content in a Type a Value source. For example, you can construct sentences:<br>
`{% raw %}The last run was {{LastSuccessfulRunDate}}{% endraw %}`.


</section>
<section class="card">

## User Configurable

To allow your customers to customize or finalize the field mapping when they install a template, you can set the field to **User Configurable**. You can still add values to these fields to test the steps, but the fields are blank when your customer installs the template.

</section>
