---
title: Delay Steps
sidebar: cyclr_sidebar
permalink: delay-steps
tags: [builder-tools]
---

Steps added to a cycle, will execute without any scheduled delays.

Connecting a Delay between two steps will allow you to set a fixed time that Cyclr should wait before it executes the next step.

#### Setting up a Delay

Click-drag a Delay from the logic section of the builder’s right sidebar.

![](./images/delay.png)

Once the Delay s on the build canvas, connect it between two steps and click the setup cog in order to set the length of the delay.

You can also pause for a period based on a date field in your data. For example, when a contact’s subscription is due for renewal. To do this, you should use a Wait Until step.