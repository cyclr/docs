---
title: Collection splitting
sidebar: cyclr_sidebar
permalink: collection-splitting
tags: [templates]

menus:
    template-configuration:
        title: Collection splitting
        identifier: collection-splitting
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">

You can use collection splitting when you don't want a list of data to move through your cycle in a single transaction.  If you do want to use a single transaction, then you can disable collection splitting.

If you split a list into separate items, each item moves through the cycle in its own transaction.

Collection splitting can prevent your data from becoming too complex and difficult to process. For example, this can be beneficial in situations where you need to retrieve further lists of data for each item in an initial list. 

> **Note**: Collection splitting can slow down the speed Cyclr processes your data.

</section>
<section class="card">

## Set Collection Splitting

There are 2 locations where you can set collection splitting:

* To set collection splitting for an entire integration, select the **Settings** button in the template builder.
* To set collection splitting for an individual step, select the step's **Step setup** > **Advanced Settings**.

The individual step settings override the integration's settings.

### Cycle Collection Splitting

You have three collection splitting options for a cycle:

| **Setting** | **Behavior** |
| :--- | :--- |
| **First (Trigger) Step** | Splits a collection of data on the first Step in a Cycle. |
| **All Steps** | Splits collections of data on all Steps. |
| **None** | Doesn't perform any splitting. |

</section>
<section class="card">

## Collection Splitting requirements

In order for Cyclr to split a list of data, the **Response Fields** for the method need to define either a single list of objects (such as a list of contacts) or a single attribute list (such as a user with a list of their user attributes). 

If the response fields define multiple lists at the same level in the response data, Cyclr can't split the data.

</section>
<section class="card">

## Map from multiple lists

If you map from multiple lists of data on a step and need to specify how the two data sources relate to one another, Cyclr displays **Unique Field** dropdowns  beneath the mappings area on the **Step Setup** page:

![A screenshot of the unique field message in the Cyclr console.](./images/what-unique-field.png)

If there isn't a field that connects the list's sources, or if one or more of your lists contain items that match multiple items in another list, you might need to split your data earlier in the Cycle.

</section>
