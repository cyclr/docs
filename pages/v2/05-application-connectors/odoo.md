---
title: Odoo Authentication
sidebar: cyclr_sidebar
permalink: odoo-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Odoo setup

You can find Odoo's documentation on how to configure your Odoo instance for API access [here](https://www.odoo.com/documentation/16.0/developer/api/external_api.html?highlight=pagination#configuration). Please contact your server administrator if you need help to obtain credentials.

<a name="get-database-names"></a>

### Get database names

To get database names on your Odoo instance, visit `{Server URL}/web/database/selector` in a web browser. When you set up the connector in Cyclr, use the full database name as it appears in the list.


</section>
<section class="card">
## Cyclr setup

### Account setup

Cyclr asks you for the below values when you install the Odoo connector within an account:

| Value             | Description                                                  |
| :---------------- | :----------------------------------------------------------- |
| **Server URL**    | The URL of the server that hosts the Odoo instance. Include the port if it's required. For example, `https://hosted-odoo-instance.net:8443`. |
| **Database Name** | The [database name](#get-database-names) for Cyclr to access.          |
| **Username**      | The username for Cyclr to log in to the instance with.                  |
| **Password**      | The password for Cyclr to log in to the instance with.                  |

</section>
