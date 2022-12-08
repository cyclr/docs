---
title: Neo4j Connector Guide
sidebar: cyclr_sidebar
permalink: neo4j-connector
tags: [connector]
---

# Neo4j Connector

You need the following details to setup the **Neo4j** connector in Cyclr:

- An AuraDB or self-hosted Neo4j Database.
- A Username and Password of a user assigned to that Database.
- The corresponding "neo4j+s" address. Example: **"neo4j+s://db123456.databases.neo4j.io"**
- We officially support Neo4j version 4.0 or greater.

### Cyclr Setup

A **Neo4j** Connector within Cyclr required the following values during the setup phase:

**Username**: The username attached to your Neo4j instance.

**Password**: The password attached to your Neo4j instance.

**Base URL**: The connection URL for your Neo4j Instance, it must use the 'neo4j+s' protocol, not HTTP.

**Database**: The name of the Database within your Neo4j instance you wish to connect to.

_You can connect 1 Database to a neo4j connector. If you wish to use multiple databases, you will need to install multiple connectors._

### Using Custom Object Categories

Your connector can now utilise all methods within the 'Custom Object (Node)' category on all Node types in your database.

To do this, on the connector setup page, open the 'Custom Object (Node)' category and click the 'copy' button.

On the modal popup, use the dropdown to select the Node type you wish to use.

Once you click 'Copy', a new category will be created. The category will have a title which matches the Node type selected.

Any of the methods within this category will apply to that node type, and generate custom request and response fields from that Node type. For instance, under the 'Create Node' method, Cyclr will automatically generate the available Node properties you can submit, with the correct Data Types.

### Adding Additional Properties

If you wish to add additional properties to your objects, you can do this directly within the connector setup page.

Open either the 'Create Node' or 'Update Node' in the correct category.

Under the fields tab, should be all the available fields on the Node type.

Click the '+' icon next to 'Request Fields' to add a new field.

- Enter the name of the property under 'Field Location'. This is will also act as the 'Display Name' when added to the other methods.
- Skip the 'Display Name' input.
- Skip the 'Description'.
- Choose the DataType you would like the API to store the data as.

Once the field has been added, create or update 1 node, by calling the method, with the new field.

Now, in all your other methods, the response & request fields should automatically map this new property.
_You may need to refresh the page for this to load._

### Creating Brand New Node Types

You can create a brand new Node type in Cyclr.

When creating a new 'Custom Object (Node)' category, instead of selecting one of the existing values, you can select 'Type a value'. This value will be your new Node name.

Once created, you can add custom properties to this new Node type using the previous section of this guide.
  