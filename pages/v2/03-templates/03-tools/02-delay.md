---
title: Delay
sidebar: cyclr_sidebar
permalink: delay
tags: [templates]

menus:
    template-tools:
        title: Delay
        identifier: delay
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">

You can add **Delay** steps to a cycle, to pause your integration cycle. If you connect a **Delay** step between two steps in a cycle template, you can set a fixed time that Cyclr waits before it executes the next step.

You can set up a Delay step in the integration template builder:

1. Select a **Delay** step from the **Tools** section and drag it into the main builder.
2. Connect the **Delay** step between two steps..
3. Select the **Step Setup** icon on the **Delay** step.
4. Enter an integer and select a unit of time from the drop down to set the delay time.The options available are:
    * Seconds
    * Minutes
    * Hours
    * Days
    * Weeks

> **Note**: You can also pause for a period based on a date field in your data. For example, when a contact’s subscription is due for renewal. To do this, you should use a [Wait Until](wait-until) step.

</section>
