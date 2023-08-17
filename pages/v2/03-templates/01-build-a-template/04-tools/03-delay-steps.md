---
title: Delay steps
sidebar: cyclr_sidebar
permalink: delay-steps
tags: [templates]

menus:
    tools:
        title: Delay steps
        identifier: delay-steps
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">

## Delay steps

You can use a delay step to make an integration wait for a fixed amount of time before it continues to the next step.

### Set up a delay step

1. Connect the delay step between two steps.
2. Select the **Step Setup** cog icon.
3. Enter an integer, and select a unit of time from the dropdown. The options available are:

    * Seconds
    * Minutes
    * Hours
    * Days
    * Weeks

> **Note**: To pause an integration for a period based on a date field in your data, such as when a subscription is due for renewal, you can use a [Wait Until](wait-until-steps) step.

</section>