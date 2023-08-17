---
title: Wait All steps
sidebar: cyclr_sidebar
permalink: wait-all-steps
tags: [templates]

menus:
    tools:
        title: Wait All steps
        identifier: wait-all-steps
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">

You can use a **Wait All** step to ensure that all transactions that run in your integration complete so you can add closing steps to your integration. After all in progress transactions complete in a cycle, the wait all step creates a single new transaction to execute any subsequent steps. 

For example, you can want to use a **Wait All** step if you use [collection splitting](collection-splitting) where multiple transactions move independently through a cycle.

> **Note**: Since a **Wait All** step splits your cycle into two parts, you can’t map steps that you place after a **Wait All** step to steps that come before the **Wait All** step.

### Example

In the example below, the integration splits data from Google Analytics into individual transactions that contain data to add to either sheet A or B in Google Sheets. The **Wait All** step ensures that the integration only posts the Slack message once the integration completes all of the transactions.

![An example of a **Wait All** step that posts a slack message when all transactions are complete.](./images/wait-all-example.png)

</section>
<section class="card">

## Notes on use

* If the first step in your cycle fails to execute successfully, the **Wait All** step doesn’t consider all of the transactions to be complete and the cycle doesn’t continue. 
* If you run your cycle frequently, a **Wait All** step might cause unintended delays as it waits for all in progress transactions to complete, regardless of whether they’re from the same run.
* You don’t need to connect all Steps to a **Wait All** for it to execute. For example, you don’t have to connect both exits of a Decision step to a **Wait All** step for it to function. 

</section>