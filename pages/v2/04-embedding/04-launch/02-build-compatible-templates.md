---
title: Build compatible templates
sidebar: cyclr_sidebar
permalink: building-integration-templates-launch
tags: [launch]

menus:
    launch:
        title: Build compatible templates
        identifier: building-integration-templates-launch
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">
Any integration templates built using the Cyclr template builder are available in the LAUNCH flow.

</section>
<section class="card">

## Display your integrations

To make an integration available for your users in the LAUNCH flow, you need to select the **Integration Published **toggle within the template settings.
  
![Integration Published](./images/integration_published.png)
  
To ensure that LAUNCH displays your integration to your users with the right context, you can add a relevant [tag](#tag-templates) to the integration before you publish it.

### Integration name

The name that you give to an integration template is the name that you present to your user through the LAUNCH flow. To help your user make the most appropriate selection, keep your integration template names concise, descriptive, and unique.

</section>
<section class="card">


### Integration description

The description that you give to an integration template is the description that you present to your user through the LAUNCH flow.

To help your users understand their integration options, you can add a clear description.

### User configurable fields

You can use the **User Configurable** toggle to control whether or not you present the field to your end user during the field mapping screen for a step.

![LAUNCH Step Setup](./images/step_setup.png)

If you select a value, that value is presented to your end user as the default value or mapping. Your user can change the value if they need to. If you don’t select a value at all, your user is responsible for specifying a value or mapping before they can proceed. If you don’t enable the **User Configurable** toggle, the mapping specified in the template is used and your user can’t change it.



</section>
<section class="card">

## Cycle-level parameters

If you need the same request parameters in multiple steps for one template, you can use cycle level parameters to ensure that your user only needs to specify the value once during the LAUNCH flow.

> **Note**: Make sure to enable the **User Configurable** toggle for any cycle level parameters you want to use before you publish your template.

</section>
<section class="card">

## Tag templates

You can use tags on templates to filter integration templates so that your users are only provided integrations that are relevant to them. For example, you can tag integrations according to the type of application they connect with, such as email marketing or accounting, or a specific application such as Salesforce or Facebook.

</section>
