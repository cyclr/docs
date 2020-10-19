---
title: SuiteCRM Authentication
sidebar: cyclr_sidebar
permalink: suitecrm-connector
tags: [connector]

---

## Authentication ##

Please Note - Each installation of the connector needs its own dedicated user, or you may see "Invalid Session" errors.  If you need to add further users, you can consult [SuiteCRM's official documentation](https://docs.suitecrm.com/admin/administration-panel/users/#_user_management).

The SuiteCRM Connector requires the following information to install.

1. Domain (Your account's domain - for example **xyz.staging.coursecrm-hosting.com**)
2. Username and Password (The same Username and Password you use to access SuiteCRM)
3. Application Name (An identifier for the application accessing the API) - An identifier for the application being used. For example, "My SuiteCRM REST Client".

## Note about Contact methods ##

It should be noted that the SuiteCRM API will only return the first two email addresses of a record.  To see any additional email addresses, you will need to access your SuiteCRM portal.
