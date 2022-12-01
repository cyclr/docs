---
title: Stopping a Cycle
sidebar: cyclr_sidebar
permalink: stopping-a-cycle
keywords: [cycle,stop,stopping]
singlecard: false
menus:
  managing-cyclr:
    title: Stopping a Cycle
    url: /stopping-a-cycle
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
_**This article refers to Cycles, but the same applies to Templates.**_

When you stop a running Cycle you have two choices: **Stop**, or **Finish and Stop**
![Deactivate Cycle Popup](./images/deactivate-cycle.png)


### Stop / Finish and Stop

What happens to your transactions depends on which option you choose:

#### Stop

Any transactions that are currently being processed will be stopped where they are and won't continue if the Cycle is resumed.

Any transactions that are waiting to be processed however, will wait for the Cycle to be resumed.

If a Cycle is stopped for 24 hours or more, all of its waiting transactions will automatically be dropped.

</section>
<section class="card py-5  my-5">
#### Finish and Stop

The Cycle will stop once all currently processing/queued transactions have completed.


### In Progress Transactions

To check for transactions that are either queued or currently being executed, go to the **Transactions** page for the Cycle and use the filtering options on the cog button in the top right to display only "In Progress Transactions":

![In Progress Transactions Filter](./images/in-progress-txns.png)
<br />

While it is possible to delete In Progress Transactions here, that can cause issues as they are currently being processed so the recommended way is instead to follow the steps below in the **Manually Dropping Transactions** section.

Completed Transactions can be deleted without issue.

</section>
<section class="card py-5 my-5">
### Manually Dropping Transactions

If you have transactions in progress/queued that you want to stop and not continue processing for any reason, you should:

1. Stop your Cycle by using the "Stop" option so it stops immediately.
2. Make a copy of the Cycle.
3. Delete the *original* Cycle which will also delete all of its existing transactions.

Your new Cycle won't have any existing transactions.
</section>
