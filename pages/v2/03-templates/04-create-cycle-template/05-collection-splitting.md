---
title: Collection splitting
sidebar: cyclr_sidebar
permalink: collection-splitting
tags: [templates]

menus:
    create-cycle-templates:
        title: Collection splitting
        identifier: collection-splitting
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">
Collection Splitting can be used when you don't want a list of data to move through your Cycle in a single Transaction.  If you do, then you can disable Collection Splitting.

Splitting a list into separate items results in each item moving through a Cycle in its own Transaction.

This can be beneficial in situations where you're retrieving further lists of data for each item in an initial list, to avoid the data becoming too complex and difficult to process.

</section>
<section class="card">

## Configuring Collection Splitting

There are 2 locations Collection Splitting can be set:

* from the Cycle __Settings__ button along the top of the Builder
* using the Step-level overrides found in each Step's __Step Setup__ > Advanced Settings area

The option on a Step will always override the Cycle __Settings__ option.

</section>
<section class="card">

## Cycle Collection Splitting

Clicking the __Settings__ button along the top of the Cycle Builder shows the current Cycle-level splitting:

| Setting | Behaviour |
| --- | --- |
| First&nbsp;(Trigger)&nbsp;Step | Splits a collection of data on the first Step in a Cycle. |
| All Steps | Splits collections of data on all Steps. |
| None | Doesn't perform any splitting. |

</section>
<section class="card">

## Collection Splitting Requirements

Cyclr isn't always able to split a list of data, even when it's been configured to do this.

Splitting is dependent on the Response Fields defined on a Method, not the actual data coming back from an API call.

For Collection Splitting to be possible, the Response Fields on a Method must define either a single "main list" of objects - such as a list of contacts being returned - or a single "attribute list" - such as returning a user with a list of their user groups.

If multiple lists are defined by Response Fields at the same "depth" in the Response data, splitting will not be possible.

</section>
<section class="card">

## Mapping from Multiple Lists

If mapping from more than one list of data on a Step, Cyclr may display **Unique Field** dropdowns beneath the standard Mappings area in **Step Setup** if you need to specify how the two data sources relate to one another.

![A screenshot of the unique field message in the Cyclr console.](./images/what-unique-field.png)

If there isn't a field (e.g. an email address or customerId) that connects the lists sources, or one or more of your lists contain items that match multiple items in another list, you may need to split your data when retrieving it earlier in the Cycle.

</section>
