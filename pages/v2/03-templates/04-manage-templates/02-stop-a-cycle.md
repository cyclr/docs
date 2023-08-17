---
title: Stop a cycle
sidebar: cyclr_sidebar
permalink: stopping-a-cycle
tags: [templates]
menus:
    manage-templates:
        title: Stop a cycle
        identifier: stopping-a-cycle
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">

To stop a cycle from in an account, open the cycle and select the **Stop** icon.

There are two ways that you can stop an in progress integration: **Stop** or **Finish and Stop**.

<img src="./images/deactivate-cycle.png" alt="Deactivate Cycle Popup" width="80%">

</section>
<section class="card">

## Stop

If you select **Stop**, any [in progress transactions](#in-progress-transactions) stop immediately and the integration stops running. 

Any in-progress transactions don’t continue if you resume the cycle. Transactions that haven’t started yet do continue if you resume the cycle, unless 24 hours pass, when the integration cancels all waiting transactions.

</section>
<section class="card">

## Finish and Stop

If you select **Finish and Stop**, the integration waits until all of the in progress and queued transactions complete and then stops.

</section>
<section class="card">

## In progress transactions

To view your in progress and queued transactions for a cycle in an account, select **View Reports**.

> **Note**: You can delete transactions from this page, but you may want to [manually drop transactions](#manually-drop-transactions) to avoid potential errors with in progress transactions.

</section>
<section class="card">

## Manually drop transactions

You can stop processing in progress or queued transactions for an integration:

1. Select **Stop** to stop the integration immediately.
2. Select **Copy Workflow** to make a copy of the integration cycle.
3. Delete the original integration cycle, which also deletes all existing transactions.

The new copy of the integration cycle doesn’t have any existing transactions.

</section>
