---
title: Wait All Steps
sidebar: cyclr_sidebar
permalink: wait-all
tags: [builder-tools]
---

A **Wait All** Step waits for all Transactions running in a Cycle to complete before moving on and executing the Steps that appear after it.

This can be useful when working with Collection Splitting where multiple Transactions are moving independently through a Cycle and there are Steps you wish to run after they've been completed.

Shortly after all "In Progress" Transactions have completed in a Cycle, a single new Transaction is created on the Wait All Step to execute any remaining Steps placed after it.

![](./images/wait-all-example.png)

In the example above, contacts from Salesforce will be split into individual Transactions. Each Transaction contains one contact and will be created in either List A or B in MailChimp depending on the Decision step result.

After all contacts have been processed, the Step following the Wait All will be executed. This will post a message on Slack to notify users that the data import has finished.

### Notes on use

* Wait All Steps consider the first Step in a Cycle to be important as they typically retrieve the data that will be processed.  If the first Step in a Cycle fails to execute successfully, Cyclr won't continue from the Wait All Step as a result.
* Avoid setting your Cycle to run too frequently as the Wait All Step only continues once there are no "In Progress" Transactions running on the Cycle, regardless of when and how they were started.
* A Wait All Step effectively splits a Cycle into 2 parts: Steps that come before the Wait All and Steps that come after it.  Because of this, Steps placed after a Wait All are not able to map from Steps that come before it.
* You don't need to connect all Steps to a Wait All to have it fire.  Decision Steps and Methods that have True and False Exits can't prevent a Wait All functioning by not linking their Exits to it.  The Wait All will still fire once all "In Progress" Transactions have been completed.
