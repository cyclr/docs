---
title: BNTouch Connector Guide
sidebar: cyclr_sidebar
permalink: bntouch-connector
tags: [connector]
---

## Setup

At setup you will be prompted to enter the ID and Name of your BNTouch account. These credentials should be issued by your BNTouch account manager.

You may have been given a URL that contains these credentials: (example)
https://www.bntouchmortgage.net/**account_name**/xmlpost/?schema=**schema_id**&id=**account_id**

If you require any further assistance obtaining these credentials please contact BNTouch:

- info@bntouchmortgage.com
- +1 888 971 1117

---

### Creating a Lead

When creating a Lead you are required to enter the ID of the schema you will be using. This again should be provided by your BNTouch account manager. The schema specifies how the data will be posted to the BNTouch API.

Although all request fields are marked as optional, at least one field must be populated for the request to succeed. Upon successful submition of a Lead you will receive a status of 'ACCEPTED'.
