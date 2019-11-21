---
title: Microsoft Dynamics Custom Objects
sidebar: cyclr_sidebar
permalink: dynamics-custom-connector
tags: [connector]
---

# Dynamics CRM Custom Objects Connector Setup #

This connector is designed to work with a single custom entity. When working with more than one, you must install a separate Dynamics CRM connector for each custom entity type.

### Installation

For details on how to authenticate this connector click [here](dynamics-crm-online.md). See the image below for an example:

When setting up the connector you will also have to enter the name of the custom entity you wish to interact with. 

![](../images/dynamics_custom_setup.png)

*Note: You will have to add an 's' to the end of the name in order for it to function correctly e.g. `custom_item` would become `custom_items`.*

### Adding Request and Response Fields

All methods come without request or response fields. Before using the connector you will have to add them where necessary. To add response fields to `GET` methods, go into the connector settings and expand the method you wish to add fields to.

Test the method:

![](../images/dynamics_custom_test_run.png)

If data is returned, copy the body of the response and open the `Generate Fields` box:

![](../images/dynamics_custom_test_generate.png)

Paste the response data into the text box and click generate:

![](../images/dynamics_custom_data_sample.png)

Your fields should now exist, like the example below:

![](../images/dynamics_custom_data_format.png)

Now you can format the display names to make them more descriptive of what they represent. The display name is what you will see in the Cycle itself.

To create request fields for `POST` and `PUT` methods, the method is the same as the above, except that you must know the structure of the entity you are going to create.

Once that is all setup, you should be able to use the connector as you would any other.