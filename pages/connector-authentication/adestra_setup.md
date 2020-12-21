---
title: Upland Adestra Authentication
sidebar: cyclr_sidebar
permalink: authenticate-adestra
tags: [connector]

---

## API user ##
To authenticate the Adestra you will need to setup an API user with the required access rights. Please see the Adestra documentation on setting up a user (here)[https://app.adestra.com/doc/page/current/index/admin/users/users]

The account, username and password will be required to authenticate the connector.
## Authenticating the connector
*Username:* this should be perpended with the lower-case account name and a dot (e.g. my_account.username).

*Password:* password of the API user
## Notes
The Adestra system has the concept of tables some method calls require a table ID. You can call the List Core, and List Data table methods to find the ID.

The contact methods have the default ID and Email specified; you can add custom fields as specified on the method for the required table. The table definition can be downloaded from the Adestra portal or via the connector table methods.
