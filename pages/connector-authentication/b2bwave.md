---
title: B2B Wave Connector
sidebar: cyclr_sidebar
permalink: b2bwave-connector
tags: [connector]
---

B2B Wave Setup
---------------
In order to authenticate the connector, you will need your App Code and API Token.

**How to find your App Code and API Token**

* Log in to your B2B Wave admin account.
* Click Profile on the top right.
 ![](./images/b2bwave-clickprofile.png)
* Select API configuration
 ![](./images/b2bwave-clickapiconfig.png)
* Your App Code and API Token should be listed.  Make a note of these.
  ![](./images/b2bwave-unpw.png)

Connector Setup
---------------
The Connector can be installed using the credentials obtained in the above steps:

**Username**: `Your App Code`

**Password**: `Your API Token`

Methods
---------------
A list of the methods available within the B2B Wave Connector.

* **Customers**
  * **Create Customer** - Create a Customer Record
  * **Get Customer** - Get Customer by ID
  * **Get Customer by Email** - Get Customer details from an email address
  * **List Customers** - List all Customers
  * **List Customers by Query** - List all Customers returned by a search
  * **List New Customers** - List Customers added since last run
  * **List Updated Customers** - Get Customers updated since last run
  * **Update Customer** - Update a Customer Record
* **Orders**
  * **Create Order** - Create an Order
  * **Get Order** - Get Order by ID
  * **List New Orders** - List Orders created since the last run
  * **List Orders** - List Orders with Details
  * **List Orders by Query** - List Orders by Search Query
  * **List Updated Orders** - List Orders Updated since the last run
  * **Update Order Status** - Update the status of an Order 
*  **Products**
   * **Get Product** - Get Product by ID
   * **List New Products** - List Products created since the last run
   * **List Products** - List all Products
   * **List Products by Query** - List Products by Search Query
   * **List Updated Products** - List Products Updated since the last run


