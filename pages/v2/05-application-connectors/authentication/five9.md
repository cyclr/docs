---
title: Five9 authentication
sidebar: cyclr_sidebar
permalink: five9-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Five9 setup

### Requirements

To connect with Cyclr, you need a valid set of Five9 credentials.

Five9 recommend using the credentials of a user with the Virtual Call Center supervisor role. This user needs to have the relevant permissions enabled to allow them to send requests to the Five9 API. You can find more information about permissions in the **Users** chapter of the Five9 Virtual Contact Center Basic Administrator’s Guide.

</section>

<section class="card">

## Cyclr setup

### Account setup

Cyclr asks you for the below values when you install the Five9 connector into an account:

| Value           | Description                                     |
| :-------------- | :---------------------------------------------- |
| **Data Center** | The data center of the Five9 instance.          |
| **Username**    | The username to access the Five9 instance with. |
| **Password**    | The password to access the Five9 instance with. |

> **Note**: You can use different details for different accounts.

### Enhanced Object Category setup

To use the statistics category of methods, you need to make a copy of this category for each set of statistics that you want to use. For more information, see the [copy a category](https://docs.cyclr.com/enhanced-objects#copy-a-category) section of the Enhanced Objects page.

</section>
