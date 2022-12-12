---
title: FIVE CRM
sidebar: cyclr_sidebar
permalink: FIVECRM-connector
tags: [connector]
---

# FiveCRM Setup

You need the following details to setup the **FIVE CRM** connector in Cyclr:

- A FiveCRM Account
- A FiveCRM Account Number
- A FiveCRM 'Hash Code' that is associated with your username.

_Each FiveCRM username has a unique hash code._

### Cyclr Setup

When installing a **FIVE CRM** Connector within Cyclr, enter the following values:

**Account Number**: Your FiveCRM account number.

**Hash Code**: Your FiveCRM Hash Code generated from your username.

### Connector Notes

This connector has some unique functionality:

- To edit contacts you are required to use the 'Accounts' methods and edit the contact within an account. It has been advised that you have a maximum of one contact per account.
- To add custom-fields, you have to add them manually to each method. The field needs to be attached to it's corresponding object. If your custom field is on an account, your Field Location would be 'account.{{FieldLocation}}'.
