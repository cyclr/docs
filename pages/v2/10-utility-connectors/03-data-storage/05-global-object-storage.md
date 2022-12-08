---
title: Global Object Storage
sidebar: cyclr_sidebar
permalink: global-object-storage
tags: [utility-connector]
menus:
    utility-connectors:
        title: Global Object Storage
        identifier: global-object-storage
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
> **_PLEASE NOTE:_** Using Utility Connectors counts toward your overall task usage.

## Purpose


To store some data in the form of one or more JSON objects and then access that data (in any Cycle in the same Cyclr Account) you can use the **Global Object Storage** Connector.

The **Global *Object* Storage** Connector works by using a Key that sets and gets a Value that can contain several separate properties.  These could be several pieces of data about a contact such as their forename, surname etc.

If you only wish to store a single value, you could instead use the **[Global *Data* Storage](./global-data-storage)** Connector which works with simple Key and Value pairs.

## Installation

When installing this Connector, you're asked to provide a **Field List**.

This is a comma-separated list of the fields you intend to use.  Cyclr will automatically create them as Custom Fields on the **Add/Update Entry** and **Get All Entries** Methods.

You could enter ```firstname, lastname, dateofbirth``` for instance to create 3 separate Custom Fields to then map to in a Cycle.

If you wish to add additional Fields after you've installed the Connector, you can simply return to the Setup and modify the Field List.

## Usage

**Add/Update Entry** Method: either creates a new entry or updates an existing one using a unique Key and any values you've provided for the other Fields.

**Get All Entries** Method: returns all of the stored values in the connector.

This Connector builds upon the features of the **Global Data Storage** Connector and therefore supports most of the Methods documented here:

[Data Storage Usage](./data-storage-usage)

## Related Topics

* [Cycle Data Storage](./cycle-data-storage)
* [Cycle Object Storage](./cycle-object-storage)
* [Global Data Storage](./global-data-storage)

</section>
