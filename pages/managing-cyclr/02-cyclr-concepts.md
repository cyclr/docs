---
title: Cyclr Glossary
sidebar: cyclr_sidebar
permalink: cyclr-glossary
tags: [managing-cyclr concepts terms]

---

### Accounts

Each of a Cyclr Partner's Customers will have an account in Cyclr.

Into these accounts integrations can be developed, either based on templates or fully customized.  This provides segmentation between integrations running for different customers.  Connectors in an account are specifically authenticated for that customer.

#### Sub-accounts

Each account may have a number of sub-accounts.  You may for example want one account for a store, separated into sub-accounts for each location.  These accounts have access to the connectors of their "parent" account. <br>[Setting up Sub Accounts](/sub-accounts).

### Connectors

A Connector is a Cyclr implementation of an application's API. 

Connectors handle all aspects of the protocols and methods needed to pull or push data to the application via Cyclr.

### Account Connectors

Once a Connector is installed into an account it is referred to as an Account Connector - this holds authentication details specific to said account.

### Users

Users can be given access to Accounts, allowing them to install and modify the Account Connectors and Cycles.

### Templates

Templates are pre-made integrations that can be installed by Users into Accounts as Cycles.

### Cycles

Cycles are integrations in an Account that when activated, will perform all of the actions in the integration flow. Cycles can be triggered on a scheduled interval or by a webhook event in a third party application.

### Cycle Transaction

A Cycle Transaction is created each time a Cycle is triggered.  It segregates the request and response data relating to each Cycle Step from other data, allowing the Cycle to have multiple Transactions in progress simultaneously.

### Cycle Step

A Cycle is made up of a collection of Cycle Steps.  Each Cycle Step may:

* Connect with a third party API to send and/or receive data
* Perform a logic action such as delaying the Cycle Transaction for a period of time<br> 
or 
* Perform different actions depending on the data received from the third party API.
