---
title: Wait Until
sidebar: cyclr_sidebar
permalink: wait-until
tags: [templates]

menus:
    template-tools:
        title: Wait Until
        identifier: wait-until
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">

A **Wait Until** step allows you to hold processing until the cycle reaches a specific date or time. You can use a **Wait Until** step in two ways:

* Wait for a specific date.
* Wait for a dynamic date from your data.

> **Note**: The time that you select for the **Wait Until** period needs to be within the 1 day data retention period for the integration to run to completion.

</section>
<section class="card">

## Wait for a specific date

You can set up a step to wait until a static date and time, such as the date of an event or webinar that you run:

1. Select a **Wait Until** step from the **Tools** section and drag it into the main builder.
2. Connect the **Wait Until** step before the step that you want to schedule.
3. Select the **Step Setup** cog icon on the **Wait Until** step.
4. Select **Type a Value** and then select the calendar icon to choose a date and time.

</section>
<section class="card">

## Wait for a dynamic date in your data

You can also set up a step to wait for a dynamic date and time. For example, you can set a step to wait until a variable such as a contact’s subscription renewal date.

1. Select a **Wait Until** step from the **Tools** section and drag it into the main builder.
2. Connect the **Wait Until** step before the step that you want to schedule.
3. Select the **Step Setup** cog icon on the **Wait Until** step.
4. Select a step from the first dropdown, and then select a date/time field from the second dropdown.

</section>
