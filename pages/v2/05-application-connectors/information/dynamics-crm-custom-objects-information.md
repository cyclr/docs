---
title: Microsoft Dynamics information
sidebar: cyclr_sidebar
permalink: dynamics-custom-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Find the Entity Name

If you don't know the names of the custom entity set or custom entity type to work with, you can install the Connector then run some of the Methods to view the entities.  You can then install a new Connector with the entity's name.

> **Note**: You need to provide the entity name during installation for the methods to work correctly.

To find the entity name:

1. Install the Connector and enter any value for the custom entity set and/or custom entity type.
2. Use the Lookup methods **List Entity Sets**, **List Entity Types** or **Get Entity Type** to find the names of the custom entity set or custom entity type you wish to use.
3. Install a new copy of the Connector (this is necessary for the correct mapping of custom fields).
4. Authenticate the connector, this time using the correct values for the custom entity set and custom entity type fields.
5. Delete your original copy of the Connector.

Cyclr creates the Request and Response Fields for the specified custom entity automatically for the Methods. For example:

![](../images/dynamics_custom_objects_updated_2.png)

> **Note**: You can edit the **Display Name** and **Description** as appropriate but, to avoid mapping issues, don't edit the **Field Location** or **Data Type** values.
</section>
