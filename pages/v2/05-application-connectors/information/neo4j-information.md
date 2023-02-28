---
title: Neo4j information
sidebar: cyclr_sidebar
permalink: neo4j-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Use Custom Object Categories

If you authenticated your connector, you can use all of the methods within the **Custom Object (Node)** category on all Node types in your database.

To use the custom object categories, go to the Neo4j setup page in Cyclr:

1. Open the **Custom Object (Node)** category, and select the **copy** button.
2. On the modal popup, use the dropdown to select the **Node type** you wish to use.

When you select **copy**, Cyclr creates a new custom object category. The category has a title that matches the **Node type** you select.

Any of the methods in the category apply to the node type you select, and generate custom request and response fields from that **Node type**. For example, under the **Create Node** method, Cyclr automatically generates the available Node properties you can submit with the correct data types.

</section>
<section class="card">

## Add additional properties

You can add additional properties to your objects from the connector setup page:

1. Open either **Create Node** or **Update Node** in the correct category to display all the available fields on the Node type under the field tab.
2. Select the **+** icon next to **Request Fields** to add a new field.
3. Enter the name of the property under **Field Location**. This value acts as the **Display Name** when you add it to other methods.
4. Skip the **Display Name** input.
5. Skip the **Description**.
6. Choose the **DataType** you would like the API to store the data as.

Once you add the field, you can call the method with the new field to create or update 1 node.

In all your of other methods, the response & request fields automatically map the new property.

> **Note**: If the new property doesn't load, you can refresh the page.

</section>
<section class="card">

## Create new Node types

To create Node type in Cyclr, create a new **Custom Object (Node)** category, and select **Type a value** instead of one of the existing values. Set the value as your new Node's name. The new Node type functions the same as other Node types.
  
</section>
