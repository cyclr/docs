---
title: Stopping a Cycle
sidebar: cyclr_sidebar
permalink: stopping-a-cycle
keywords: [cycle,stop,stopping]
---

When you stop a Cycle you have two choices:
**Stop**, or **Finish and Stop**.
![Deactivate Cycle Popup](./images/deactivate-cycle.png)


### Stop / Finish and Stop

What happens to your transactions depends on which option you choose:

#### 1. Stop

Any transactions that are currently being processed will be dropped.  Any that are already *queued* however, will wait for the Cyclr to be resumed.

#### 2. Finish and Stop

The cycle will stop once all currently processing/queued transactions have completed.

### In Progress Transactions

To check for transactions currently in progress, go to the Transactions page for the Cycle and filter by In Progress Transactions:

![In Progress Transactions Filter](./images/in-progress-txns.png)

### Manually dropping transactions

If you have transactions in progress/queued that you want to drop so you can start fresh, you should:

1. Stop your cycle.
2. Make a copy of the cycle.
3. Delete the *original* cycle.

Your new cycle will start with no transactions queued/waiting.
