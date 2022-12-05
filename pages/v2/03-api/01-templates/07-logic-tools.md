---
title: Logic Tools
sidebar: cyclr_sidebar
permalink: logic-tools
tags: [templates]
menus:
  templates:
    title: Logic Tools
    url: /logic-tools
    weight: 7
---

## Introduction

Cyclr provides 4 logic tools that can be used in Integration Cycles.  These are:

| Tool | Purpose |
| --- | --- |
| Decisions | Allows data to be split to follow different paths through the integration. |
| Delays | Allows a pause to be added to the flow. |
| Wait Until | Allows you to hold processing until a specific data/time has been reached. |
| Wait All | Allows you to add closing steps to a process when the integraton has been processing an array of transations in parallel. |

## Decisions

Decision steps can split the data in your cycle down a true or false branch.

![](./images/decision-example.png)

### Setting up a Decision step

Your cycle must contain at least one Get (green) or Webhook (grey) step so you have some data to work with.

Click and drag a Decision Step into your cycle and connect it where you wish to split the data, then click its cog Step Setup button.

![](./images/decision.png)

Decisions work by comparing a "Left Operand" to a "Right Operand"; in other words, it looks for a value in your data and compares it - using a condition you specify - to another value.

From within the Decision Step's Step Setup:

*   Choose a previous step and one of its fields; this is your Left Operand.
*   Choose a Condition, e.g. _Exists, Not Exists, Equals, Not Equals_.
*   Choose your Right Operand. This can the value of a previous step's field or you can type in a value.

The result of the screenshot example is that contacts with the last name of “Smith” are routed down the true branch; all other contacts will go down the false branch.

To create more advanced logic, you can chain multiple Decision steps together.

### IMPORTANT NOTE

**Decision steps only filter records from the steps to which they refer.  Take the example illustrated below:**

![](./images/example-decision.png)

* Step 3 has fields mapped from Step 1 and Step 2.
* Only Step 2's results are being filtered by a decision step.
* Any data from Step 1 will always be mapped, regardless of the results of Step 2.

## Delays

Delay steps added to a cycle, will execute without any scheduled delays. Connecting a Delay between two steps will allow you to set a fixed time that Cyclr should wait before it executes the next step.

![](./images/delay.png)

Click-drag a Delay from the logic section of the builder’s right sidebar.

Once the Delay s on the build canvas, connect it between two steps and click the setup cog in order to set the length of the delay.

You can also pause for a period based on a date field in your data. For example, when a contact’s subscription is due for renewal. To do this, you should use a Wait Until step.

## Wait Until

You can use a Wait Until step in two ways.

### Wait for a specific date

For example, the date of an event or webinar you are running.

![](./images/wait-until-fixed-date.png)

Select the Type a Value option and choose a date/time using the calendar and dropdown combos.

### Wait until dynamic date in your data

For example, a contact’s subscription renewal date.

![](./images/wait-until-dynamic-date.png)

Select a step from the first dropdown, then a field from the second. The field should be a date.

## Wait All

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
