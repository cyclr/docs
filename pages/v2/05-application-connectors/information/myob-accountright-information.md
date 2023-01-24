---
title: MYOB AccountRight Live
sidebar: cyclr_sidebar
permalink: myob-accountright-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

### Selecting an MYOB Company File

Once the Connector has been installed, the Company File is selected through a Step's Setup popup in the Cycle Builder.

Alternatively, when creating a Template for integrating with MYOB that you wish to make available to your users, you can use a Cycle-level **Variable** in your Template and reference that in each MYOB Step, giving yourself a single location to set or update it.

When installing the Template through the Cyclr API, after the MYOB AccountRight Live Connector has been installed and authenticated, you can then manually call the **Get Files** Method ([see here](https://docs.cyclr.com/call-a-connector-method)) to show a list of Company Files to the user, allow them to select one, then set that in the Template.

</section>
