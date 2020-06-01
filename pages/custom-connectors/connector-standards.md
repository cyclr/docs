---
title: Connector Standards
sidebar: cyclr_sidebar
permalink: connector-standards
---

Cyclr Connector Standards Guide
---------------------------

## Connector Details
* Name should not include any version information
* Version should be same as API version
* Description should be from the product, google search result will likely give appropriate text
* Logo should be 400x400 and scale down nicely
* Connectors should only use 1 API version

## Authentication
- Use OAuth where available

## Methods
#### Naming Convention:
- **Get**: Used when the method retrieves a single item
- **List**: Used when the method retrieves multiple items
- **Create**: Used when the method creates an item (Do not use add)
- **Delete**: Used when the method deletes an item
- **Update**: Used when the method updates an item<br><br> 
  *Note:* When an endpoint carries out multiple functions, such as Creating or Updating, name the method logically e.g. "**Create Or Update** Contact"
  
#### Descriptions:
* Descriptions should be provided and end with a "."

#### Functionality
* All entities should inlcude methods for **Get**, **Get New**, **Get Updated**, **List**, **Create**, **Update**, **Delete** unless not supported by the API

## Fields & Parameters
- Descriptions should end in "."
- Should provide lookup/triggers for IDs where possible
- IDs should be descriptive of the method rather than generic. e.g. "Contact **ID**" rather than "**ID**"


#### System Fields
- Should be in [PascalCase](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-1.1/x2dbyw72(v=vs.71)) e.g. "AddressLine1"
- IDs should follow PascalCase e.g. "**Id**"
- Should be consistent to our naming convention rather than to the API

#### Display Names
- Each word should be seperated with a space and capitalised e.g. "Address Line 1"
- IDs should be uppercase e.g. "**ID**"
