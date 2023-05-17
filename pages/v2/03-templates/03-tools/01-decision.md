---
title: Decision
sidebar: cyclr_sidebar
permalink: decision
tags: [templates]

menus:
    template-tools:
        title: Decision
        identifier: decision
        toggleonly: menutoggleonly
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">

You can use **Decision** steps to split the data in your cycle template down a true or false branch. **Decision** steps work by comparing a **Left Operand** to a **Right Operand**, which means that you can specify a condition in order to look for a value in your data and compare it to another value.

**Decision** steps only filter records from the steps that you connect them to. For example, in the screenshot below, only **Step 2**’s results are filtered by the decision step, so the cycle maps all data from **Step 1** regardless of the filter.

![A screenshot example of a decision step in a cycle template.](./images/example-decision.png)

</section>
<section class="card">

## Set up a Decision step

To set up a decision step, you need at least one Get (green) or Webhook (grey) step in the cycle template so you have data to work with.

1. Select and drag a **Decision **step into the main template builder and connect it to another step where you want to split the data.
2. Select the **Step Setup** cog icon on the **Decision** step.
3. Select a previous step and select a field to work as the **Left Operand**.
4. Select a **Condition** from the dropdown.
5. If you use a condition other than `Exists` or `Not Exists`, you need to enter a **Right Operand**. This can be a value from a previous step’s field, or a value that you enter.

> **Note**: To create more advanced logic, you can chain multiple Decision steps together.


### Example

In the screenshot example, the fields would be Left Operand: ``Name``, Condition: ``Equals``, Right Operand ``Smith``. The result is that contacts with the last name of “Smith” are routed down the true branch, and all other contacts will go down the false branch:

![An example of a decision step that determines where to record data.](./images/decision-example.png)

</section>
