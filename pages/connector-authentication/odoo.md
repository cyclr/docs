---
title: Odoo Authentication
sidebar: cyclr_sidebar
permalink: odoo-connector
tags: [connector]
---

## Odoo setup

You can find Odoo's documentation on how to configure your Odoo instance for API access [here](https://www.odoo.com/documentation/16.0/developer/api/external_api.html?highlight=pagination#configuration). Please contact your server administrator if you need help to obtain credentials.

<a name="get-database-names"></a>

### Get database names

To get database names on your Odoo instance, visit `{Server URL}/web/database/selector` in a web browser. When you set up the connector in Cyclr, use the full database name as it appears in the list.

## Cyclr setup

### Account setup

You will be asked for the below values when you install the Odoo connector within an account:

| Value             | Description                                                  |
| :---------------- | :----------------------------------------------------------- |
| **Server URL**    | The URL of the server where the Odoo instance is hosted including port if required. For example, `https://hosted-odoo-instance.net:8443`. |
| **Database Name** | The [database name](#get-database-names) to access.          |
| **Username**      | The username to login to the instance with.                  |
| **Password**      | The password to login to the instance with.                  |
