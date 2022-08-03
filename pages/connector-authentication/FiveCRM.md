---
title: Five CRM
sidebar: cyclr_sidebar
permalink: FIVECRM-connector
tags: [connector]
---

# Five CRM Setup

You need the following details to setup the FiveCRM connector in Cyclr:

- A Five CRM Account
- A Five CRM Account Number
- A Five CRM 'Hash Code' that is associated with your username.

_Each Five CRM username has a unique hash code._

### Cyclr Setup

Setup your Five CRM App within Cyclr, enter the following values:

**Account Number**: Your Five CRM account number.

**Hash Code**: Your Five CRM Hash Code generated from your username.

### Connector Notes

This connector has some unique functionality:

- To edit contacts you are required to use the 'Accounts' methods and edit the contact within an account. It has been advised that you have a maximum of one contact per account.
- To add custom-fields, you have to add them manually to each method. The field needs to be attached to it's corresponding object. If your custom field is on an account, your Field Location would be 'account.{{FieldLocation}}'.
