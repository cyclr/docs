---
title: Decision steps
sidebar: cyclr_sidebar
permalink: decision-steps
tags: [templates]

menus:
    tools:
        title: Decision steps
        identifier: decision-steps
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">

## Decision steps

You can use a decision step to split the data in your integration between a **true** branch and a **false** branch. 

Decision steps only filter the data from the step that you connect them to. Any data from steps before that step processes as normal.

![An example of a decision step that determines where to record data.](./images/decision-example.png)

</section>
<section class="card">

## Set up a Decision step

Decision steps compare a **Left Operand** to a **Right Operand** to filter your data. To control how the step filters your data, you need to specify the **Condition** it uses to compare values.

To specify the condition, select the **Step Setup** cog icon:

1. Select a previous step and one of its fieldsr by as your **Left Operand**.
2. Select a **Condition** from the dropdown.
3. Select either another field from a previous step or enter a value as the **Right Operand**.

### Example

For example, you can set the following fields:

* Left Operand: `Name`.
* Condition: `Equals`.
* Right Operand `Smith`. 

This setup causes the decision step to route data that includes the last name “Smith” down the true branch, and all other data goes down the false branch.

> **Note**: To create more advanced logic, you can chain multiple decision steps together.

</section>