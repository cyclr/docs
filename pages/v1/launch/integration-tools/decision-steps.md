---
title: Decision Steps
sidebar: cyclr_sidebar
permalink: decision-steps
tags: [builder-tools]
---

Decision steps can split the data in your cycle down a true or false branch.

![](./images/decision-example.png)

Setting up a Decision step
--------------------------

Your cycle must contain at least one Get (green) or Webhook (grey) step so you have some data to work with.

Click and drag a Decision Step into your cycle and connect it where you wish to split the data, then click its cog Step Setup button.

![](./images/decision.png)

Decisions work by comparing a "Left Operand" to a "Right Operand"; in other words, it looks for a value in your data and compares it - using a condition you specify - to another value.

From within the Decision Step's **Step Setup**:

*   Choose a previous step and one of its fields; this is your Left Operand.
*   Choose a Condition, e.g. _Exists, Not Exists, Equals, Not Equals_.
*   Choose your Right Operand. This can the value of a previous step's field or you can type in a value.

The result of the screenshot example is that contacts with the last name of “Smith” are routed down the true branch; all other contacts will go down the false branch.


To create more advanced logic, you can chain multiple Decision steps together.
