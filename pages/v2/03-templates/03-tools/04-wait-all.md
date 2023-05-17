---
title: Wait All
sidebar: cyclr_sidebar
permalink: wait-all
tags: [templates]

menus:
    template-tools:
        title: Wait All
        identifier: wait-all
        toggleonly: menutoggleonly
        weight: 4
---
{::options parse_block_html="true" /}
<section class="card">

You can use a **Wait All** step to make your cycle wait for all current transactions in the cycle to complete before the cycle executes the remaining steps.

If you use **Decision** steps, you might have multiple transactions moving independently in a cycle. You can then use a **Wait All** step to ensure these complete before a subsequent steps run so that they have the correct data.

After all of the **In Progress** transactions complete in a cycle, the **Wait All** step creates a new transaction to execute any subsequent steps.

### Example

For example, you can split contacts from Salesforce into individual transactions. Each transaction contains one contact and will be created in either List A or B in MailChimp depending on the Decision step result. The **Wait All** step means that the cycle waits for every contact to be processed before it posts the Slack message to say that the data import has finished.

![An example of a **Wait All** step that posts a slack message when all transactions are complete.](./images/wait-all-example.png)

</section>
<section class="card">

## Usage

### Transactions

The **Wait All** step only continues once there are no **In Progress** transactions in the cycle, regardless of when they start. To avoid issues, don’t set a cycle with a **Wait All** step to run too frequently.

You don’t need to connect all steps to a **Wait All** step for it to function correctly. For example, even if you don’t connect it to both exits of a **Decision** step, the** Wait All** still executes once all **In Progress** transactions complete.

> **Note**: Since the first step in a cycle typically retrieves the data that will be processed, if the first step in a cycle fails to execute successfully, the cycle doesn’t continue from the **Wait All** step.


### Mapping

A **Wait All** step effectively splits a Cycle into 2 parts: steps that come before the **Wait All** and steps that come after it. Because of this, you can’t map steps that come after a **Wait All** from Steps that come before it.
</section>
<section class="card">


</section>
