---
title: Glossary
sidebar: cyclr_sidebar
permalink: cyclr-glossary
tags: [managing-cyclr]

menus:
    about-cyclr:
        title: Glossary
        identifier: cyclr-glossary
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">

### Account
You can give each of your customers an account in Cyclr. The account stores all of the cycles, connectors and authentication details for the customer. This allows you to keep information and data for each customer separate. For more information, see the [User accounts overview](overview-new-account).

### Account connector
An account connector is a connector that is installed into an account and authenticated against an application that the customer uses.

### Builder
The [Builder](template-builder) is an area of the Cyclr application that allows you to create cycle templates and custom integrations.

### Connector
A connector allows Cyclr to take and add data to an application. Most connectors use an external application's API, but some also work with databases and files. For more information, see the [Connector introduction](connector-introduction) page.

### Console
The console is your control panel and allows you to set up and manage your application and integrations. Your customers can't access the console. See the section on [Console configuration](cyclr-configuration) in the Cyclr documentation.

### Custom connector
A [custom connector](connector-introduction) is a connector that you can make within Cyclr to connect with an application of your choice.

### Cycle
Cycles are integrations that run in an account. You can build custom cycles for a specific customer in an account, or create a template that you can use for multiple customers. For more information, see the [Template introduction](template-basics) page.

### Cycle step
Cycles are composed of a number of **steps**. A step is usually a call to an application using the connector, but you can also use logic steps to help process data.

### Cycle transaction
When you trigger a cycle, it creates a cycle transation. This separates the request and response data that relatees to each step in the cycle from other data, allowing each cycle to have multiple transactions in progress simultaneously.

### Embedding
[Embedding](embed-cycles) is the term Cyclr uses to refer to the process of providing Cyclr integrations to your customer base.

### LAUNCH
[LAUNCH](launch) is one of Cyclr's tools that you can use to embed your Cyclr integrations into your application. You can use LAUNCH to offer a list of cycles to your customers for them to select and self-install into their account.

### Marketplace
A [Marketplace](marketplace) allows you to set up a store of integrations that you offer to your customers. The Marketplace is a flexible method of providing cycles to your customers as you can offer packages of cycles in a tree-like browsable structure.


### Sub account
You can add [sub accounts](sub-accounts) to accounts within your Cyclr application. Sub accounts allow you to organise multiple related accounts.

### Templates
Templates are definitions of cycles that you can create and add to any number of accounts. You can run templates for testing but they aren't usually live. For more information on templates, see the section on [Cycle templates](cycle-templates) in the Cyclr documentation. 

### Tools
Cyclr provides [tools](logic-tools) as steps that you can add to a cycle in order to process data.

</section>
