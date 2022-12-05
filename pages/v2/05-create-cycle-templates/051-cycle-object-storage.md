---
title: Cycle Object Storage
sidebar: cyclr_sidebar
permalink: cycle-object-storage
tags: [utility-connector]
menus:
  utility-connectors:
    title: Cycle Object Storage
    url: /cycle-object-storage
---

## Purpose

To store some data in a Cycle in the form of one or more JSON objects and access that data later in the same Cycle, you can use the **Cycle Object Storage** Connector.

Any data that is stored in the Connector will only be accessible _within the same cycle_.

The **Cycle Object Storage** Connector works using a Key that sets and gets a Value that can contain several separate properties.  These could be several pieces of data about a contact such as their forename, surname etc.

If you only wish to store a single value, you could instead use the **[Cycle *Data* Storage](./cycle-data-storage)** Connector which works with simple Key and Value pairs.

## Installation

When installing this Connector, you're asked to provide a **Field List**.

This is a comma-separated list of the fields you intend to use.  Cyclr will automatically create them as Custom Fields on the **Add/Update Entry** and **Get All Entries** Methods.

You could enter ```firstname, lastname, dateofbirth``` for instance to create 3 separate Custom Fields to then map in a Cycle.

If you wish to add additional Fields after you've installed the Connector, you can simply return to the Setup and modify the Field List.

## Usage

**Add/Update Entry** Method: either creates a new entry or updates an existing one using a unique Key and any values you've provided for the other Fields.

**Get All Entries** Method: returns all of the stored values in the context of the Cycle you're working in.

This Connector builds upon the features of the **Cycle Data Storage** Connector and therefore supports most of the Methods documented here:

[Data Storage Usage](./data-storage-usage)

> **_PLEASE NOTE:_** Using Utility Connectors counts toward your overall task usage.

## Related Topics

* [Cycle Data Storage](./cycle-data-storage)
* [Global Data Storage](./global-data-storage)
* [Global Object Storage](./global-object-storage)
