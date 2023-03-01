---
title: Infusionsoft information
sidebar: cyclr_sidebar
permalink: infusionsoft-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Create and Update Contacts

The Create and Update Contacts functionality is handled with a single method 'Upsert Contacts'. This will perform a duplicate check within Infusionsoft for the entered email address. If a matching email address is found, the existing contact will be updated. If no match is found, a new contact will be created.

## State and Country codes

The Infusionsoft API has strict requirements for valid Province and Country codes. To make sure you use a valid State or Country code, you can use our **Lookup** feature:

![keap portal](./images/infusionsoft_8.png)

![keap portal](./images/infusionsoft_9.png)

</section>
