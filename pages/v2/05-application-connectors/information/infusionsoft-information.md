---
title: Infusionsoft Connector Guide
sidebar: cyclr_sidebar
permalink: infusionsoft-information
tags: [Connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

The Create and Update Contacts functionality is handled with a single method 'Upsert Contacts'. This will perform a duplicate check within Infusionsoft for the entered email address. If a matching email address is found, the existing contact will be updated. If no match is found, a new contact will be created.

When entering a State or Country code it is advised that you use our Lookup feature, as the Infusionsoft API has strict requirements for valid Province and Country codes.

![keap portal](./images/infusionsoft_8.png)

![keap portal](./images/infusionsoft_9.png)

</section>
