---
title: Microsoft Dynamics Custom Objects
sidebar: cyclr_sidebar
permalink: dynamics-custom-connector
tags: [connector]
---

# Dynamics CRM Custom Objects Connector Setup

This connector is designed to work with a single custom entity. When working with more than one, you must install a separate Dynamics CRM connector for each custom entity type.

### Installation

For details on how to authenticate this connector, review the [how to install the Microsoft Dynamics CRM Connector](dynamics-crm-online.md) guide as the Connectors use the same setup. See the image below for an example:

When setting up the connector you will also have to enter the names of the custom entity set and custom entity type you wish to interact with.

![](../images/dynamics_custom_objects_updated_1.png)

### Find the Entity Name

If you don't know the names of the custom entity set or custom entity type to work with, you can install the Connector then run some of the Methods to view the entities.  You can then install a new Connector with the entity's name as it _must be provided during installation_ for the Methods to work correctly.

Here's how you can do this:

- Install the Connector and enter any value for the custom entity set and/or custom entity type.
- Use the Lookup methods **List Entity Sets**, **List Entity Types** or **Get Entity Type** to find the names of the custom entity set or custom entity type you wish to use.
- Install a new copy of the Connector (this is necessary for the correct mapping of custom fields).
- Authenticate the connector, this time using the correct values for the custom entity set and custom entity type fields.
- Delete your original "investigating" copy of the Connector.

The Request and Response Fields for the specified custom entity will have been automatically created for the Methods.

Example:

![](../images/dynamics_custom_objects_updated_2.png)

You can edit the **Display Name** and **Description** as appropriate, but **do not** edit the **Field Location** or **Data Type** values; doing so could cause mapping issues.
