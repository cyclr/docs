---
title: Cycle Data Storage
sidebar: cyclr_sidebar
permalink: cycle-data-storage
tags: [utility-connector]
menus:
    data-storage:
        title: Cycle Data Storage
        identifier: cycle-data-storage
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">
> **_PLEASE NOTE:_** Using Utility Connectors counts toward your overall task usage.


</section>
<section class="card">
## Purpose

To store some data in a Cycle and access it later in the same Cycle, you can use the **Cycle Data Storage** Connector.

Data can be written in one part of the Cycle and retrieved in another.

Any data that is stored in the Connector will only be accessible _within the same cycle_.

The **Cycle Data Storage** Connector works using simple Key and Value pairs.  The Key is unique and is used to set and get the Value.

If you wish to store more structured data or more than one value (perhaps the firstname, lastname, etc of a contact), you should use the **[Cycle *Object* Storage](./cycle-object-storage)** Connector as that allows multiple values to be stored as a single "object" against a Key value.


</section>
<section class="card">
## Usage

[How To Use Cycle Data Storage](./data-storage-usage) 


</section>
<section class="card">
## Related Topics

* [Cycle Object Storage](./cycle-object-storage)
* [Global Data Storage](./global-data-storage)
* [Global Object Storage](./global-object-storage)

</section>
