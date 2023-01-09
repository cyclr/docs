---
title: Cross Updating Preventer
sidebar: cyclr_sidebar
permalink: cross-updating-preventer
tags: [utility-connector]
menus:
    utility-connectors:
        title: Cross Updating Preventer
        identifier: cross-updating-preventer
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">
> **_PLEASE NOTE:_** Using Utility Connectors counts toward your overall task usage.


</section>
<section class="card">
## Purpose

Many integrations are triggered when details of an updated record in one application are sent to a second application to keep the data in sync.

There are occasions when this process needs to be bi-directional and this can result in an infinite cross-updating loop where System A updates System B, which causes System B to update System A, and so on.  This continual triggering of updates isn't useful and will eat into your monthly Task Allowance, as well as cause unnecessary updates in both systems.

The Cyclr **Cross Updating Preventer** (or "XUP" for short) is designed to avoid this situation.  It can be used to make sure that an inbound update to an application does not result in a returning outbound update.



</section>
<section class="card">
## Overview

### Inbound or Outbound?
First off, you must decide which of the two systems is the "main" one as you need to be consistent when using the Cross Updating Preventer's Methods.

Once you've decided, data moving *from* that system is considered *Outbound*, and data coming *back* from a another system into it is "Inbound".

### Separate Connectors for each Type of Object
If there are multiple "types" of data that you wish work with - such as Contacts and Leads in Salesforce - then you should install a separate Cross Updating Preventer Connector for each type to keep their data separate.

### Common Key
You must identify some data you can use as a "Common Key".  This will be used as a unique value to both store and lookup data in the Cross Updating Preventer for each data object.

The value must be something that's unique to each object and that exists in the data being moved in both the Inbound and Outbound directions.  If you were synchronizing Contacts between 2 systems, you might use Email Address.

For systems where there isn't a shared and unique value, you could use a "concatenated Common Key" by combining the unique ID values from each system with a dividing character such as `[SystemA ID]_[SystemA ID]`, e.g. `5325_AVb38nj`.  When using a concatenated Common Key, you must ensure you combine the values in the same way wherever they're used.  Each system would also need to store a reference to the other system's ID value on its objects, like a Foreign Key on a database record.


</section>
<section class="card">
## Methods

There are 4 main Methods on the Connector.  Their purpose is to check if data being sent from one system to the other is the result of a previous update so has been sent before, and if so to prevent it from continuing.

These "Outbound" Methods are used in a Cycle sending data *from* the "main" system:
* Update OK (Outbound)
* Store Data (Outbound)
<br />

These "Inbound" Methods are used in a Cycle receiving data *into* the "main" system:
* Update OK (Inbound)
* Store Data (Inbound)



### **Update OK** Methods
These simply compare the data you map to them with data previously stored by the opposite direction's **Store Data** Method.

### **Store Data** Methods
These store the data you map to them in the Cross Updating Preventer's internal storage, ready to be used by the opposite direction's **Update OK** Method.



</section>
<section class="card">
## How it Works

**Update OK (*Outbound*)** compares the values you map on it with values that have been stored by **Store Data (*Inbound*)** for a specific Common Key value.  If there is any difference between those values, the Transaction leaves the Step through the True Exit, meaning the update should continue.  If the values are all the same, then it leaves through the False Exit indicating this isn't a real update as the data hasn't changed since the last time it was seen.

**Update OK (*Inbound*)** does the same against values stored by **Store Data (*Outbound*)**.


While the Methods are named `... (Inbound)` and `... (Outbound)`, they don't actually interact with each other within a Cycle.  Instead they work with the other Method in the Cycle moving data in the opposite direction.


### Mappings
You must map the same fields across the 2 corresponding Steps, but also ensure they are formatted the same way to enable them to be compared correctly. Depending on the data, you may need to use Script to accomplish this.

So **Update OK (*Inbound*)** and **Store Data (*Outbound*)** must have the same fields mapped (and values formatted the same way).

And **Update OK (*Outbound*)** and **Store Data (*Inbound*)** must have the same fields mapped (and values formatted the same way).



</section>
<section class="card">
## Cycle Setup

The screenshot below shows how you might build 2 Cycles that synchronize Contacts between Salesforce and HubSpot.

![](./images/cross-updating-preventer-2-cycles.png)

Here we've arbitrarily decided that Salesforce is the "main" system so changes passing from there to HubSpot are considered "Outbound" with changes coming back from HubSpot to Salesforce as "Inbound".

The colored boxes and joining lines indicate how the Update OK and Store Data Steps work together: the **Update OK (Outbound)** Step checks the data stored by **Store Date (Inbound)**, and the **Update OK (Inbound)** Step checks the data stored by **Store Data (Outbound)**.


</section>
