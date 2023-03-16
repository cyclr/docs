---
title: PostgreSQL information
sidebar: cyclr_sidebar
permalink: postgresql-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Access a table

Cyclr uses custom object categories to allow the PostgreSQL connector to access multiple database tables with a single connector. To access a table within a database, you need to create a Custom object category.

You can identify custom object categories on the PostgreSQL connector settings page with the ![The custom object category icon.](./images/postgresql-custom-object.png)
 icon to the left of the method category.

### Add a custom object category

From the PostgreSQL connector settings page:

1.  Under the **Methods & Fields** heading, select **Rows**.
2.  Select the ![The copy icon.](./images/postgresql-custom-object-copy.png)
 **Copy this Category to create a Custom object category** button.
3.  Select the **Select Object** dropdown.
4.  Select the schema and table name to access.
5.  Select **Copy**.

This adds a new method category with the schema and table name you select in step 4. The methods inside the method category target the same schema and table name.

### Remove a custom object category

From the PostgreSQL connector settings page:

1.  Under the **Methods & Fields** heading, select the custom object category you want to remove.
2.  Select the ![The bin icon.](./images/postgresql-custom-object-remove.png)
 **Delete this Custom object category** button.
3.  Select **Confirm**.

> **Note**: You cannot delete custom object categories if you are using methods from within them in cycles.

</section>

<section class="card">

## Select a custom object category primary key

You need to set a primary key when you use a custom object category method that selects a record based on the primary key. Cyclr supports composite primary keys.

The following methods requires you to set a primary key before a request can be sent:

- Delete Table Row
- Get Table Row
- Update Table Row
- Upsert Table Row

In the cycle builder, from the **Step setup** of a Custom object category method:

1. Select the **Ignore** dropdown.
2. Select **Lookup**.
3. Select **Select...**.
4. Select the primary key.

</section>


