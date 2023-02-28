---
title: MYOB AccountRight Live information
sidebar: cyclr_sidebar
permalink: myob-accountright-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Select an MYOB Company File

Once you install the connector, select **Step setup** in the template builder to select the Company File you want to use.

You can also select a company file when you create the template to integrate MYOB that you want to make available to your users. To define the company file, add it as a cycle level **Variable** in your template and reference the variable in each MYOB Step, with a single location to set or update it.

When you install the template through the Cyclr API, after you install and authenticate the MYOB AccountRight Live Connector, you can manually call the [**Get Files** Method](https://docs.cyclr.com/call-a-connector-method)) to show a list of Company Files to the user, allow them to select one, then set that in the Template.

</section>
