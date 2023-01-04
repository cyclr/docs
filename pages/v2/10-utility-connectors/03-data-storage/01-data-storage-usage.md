---
title: Data storage usage
sidebar: cyclr_sidebar
permalink: data-storage-usage
tags: [utility-connector]
menus:
    data-storage:
        title: Data storage usage
        identifier: data-storage-usage
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">
## Usage

This Global Data Storage and Cycle Data Storage connectors can be installed multiple times, and each instance will have its own associated data set.  When the connector is installed it is advisable to give it a name that reflects how it will be used.

For the Global Data Storage Connector, a maximum of 1,000,000 items can be stored.<br />
For a Cycle Storage Connector (e.g. Cycle Data Storage and Cycle Object Storage), a maximum of 1,000,000 items can be stored by each Cycle.

Data is stored as Key/Value pairs.

**Keys** cannot exceed 128 characters.  \
**Values** cannot exceed 1,024 characters.

### Single Record Operations

#### Set a Value
This will create a Key/Value pair if the Key does not already exist.  If it does exist, the current Value will be updated to the new Value you provide.  This behaves as an Upsert

#### Append Value
If the supplied Key value already exists, then the new Value you provided will be appended to the current value.  If the Key does not exist, a new entry is created.

#### Get a Value
The Value field is returned for the specified Key.

#### Delete Key
Deletes a Key/Value Pair

### Data Set Operations

#### Get All Vales
This will return all the records in the data set.  A subsequent step in an Integration Cycle might then iterate through each Key/Value pair.

#### Delete All Keys
This will remove all the entries in the data set.


</section>
<section class="card">
## Related Topics

[Global Data Storage](./global-data-storage) | [Cycle Data Storage](./cycle-data-storage) 

</section>
