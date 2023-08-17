---
title: Add steps
sidebar: cyclr_sidebar
permalink: add-steps
tags: [templates]

menus:
    build-a-template:
        title: Add steps
        identifier: add-steps
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">

Steps are the building blocks of your integrations. Steps contain methods that allow you to send, retrieve, and process data from third party applications.

To view the different steps available for a connector, you can select the connector in the right sidebar of the template builder. This shows the different categories of steps, and you can select a category to see the available steps.

To add a step to the builder, select the step and drag it onto the builder canvas. The different types of step are color coded. For example, get steps are green, webhook steps are black, and action steps are blue. To connect different steps, select and drag the dot on the right side of the previous step and connect it to the dot on the left side of the next step.

> **Note**: If a step appears grayed out in the builder, it means you need to map the required fields of the step for it to work. For more information, see the documentation on how to [map fields](field-mapping).


</section>
<section class="card">

## Trigger steps

A trigger step is the first step in your integration. The trigger step starts the integration so you need to use a step that retrieves data. There are two types of trigger step that you can use:

*  **Get** steps, which you can use to get data from an application on a timer.
*  **Webhook** steps, which trigger the integration when they receive data.

</section>
<section class="card">

## Action steps

After you have a trigger step, you can add action steps to interact with the data. 

Action steps are color coded blue in the builder and include tasks such as the following:
*  Add contacts
*  Send a message
*  Create a task

</section>
<section class="card">

## Related page

*  [Tools](tools)
*  [Map step fields](field-mapping)

</section>