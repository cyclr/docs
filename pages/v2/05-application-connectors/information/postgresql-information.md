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

Cyclr uses Custom Object Categories to allow the PostgreSQL connector to access multiple database tables with a single connector. To access a table within a database, you need to create a Custom Object Category.

Custom Object Categories can be identified on the PostgreSQL connector settings page by the ![image](https://user-images.githubusercontent.com/78208292/225289872-083c23fe-19d1-45a7-9d39-09f1dc8afe6c.png)
 icon to the left of the method category.

### Add a Custom Object Category

From the PostgreSQL connector settings page:

1.  Under the **Methods & Fields** heading, select **Rows**.
2.  Select the ![image](https://user-images.githubusercontent.com/78208292/225290432-32ece385-25e9-40f6-b7f2-b5a55ec14b72.png)
 **Copy this Category to create a Custom Object Category** button.
3.  Select the **Select Object** dropdown.
4.  Select the schema and table name to access.
5.  Select **Copy**.

A new method category with the schema and table name selected in step 4 above will be added. The methods inside will target the schema and table selected in step 4 above.

### Remove a Custom Object Category

From the PostgreSQL connector settings page:

1.  Under the **Methods & Fields** heading, select the the Custom Object Category to remove.
2.  Select the ![image](https://user-images.githubusercontent.com/78208292/225290347-cfc53a7e-166c-40de-b0d6-fb905dfe539f.png)
 **Delete this Custom Object Category** button.
3.  Select **Confirm**.

> **Note**: Custom Object Categories cannot be deleted if methods within them are used in Cycles.

</section>

<section class="card">

## Select a Custom Object Category primary key

A primary key must be set when you use a Custom Object Category method that selects based on the primary key. Composite primary keys are supported.

The following methods require a primary key to be set before a request can be sent:

- Delete Table Row
- Get Table Row
- Update Table Row
- Upsert Table Row

Within the Cycle Builder, from the **Step setup** of a Custom Object Category method:

1. Select the **Ignore** dropdown.
2. Select **Lookup**.
3. Select **Select...**.
4. Select the primary key.

</section>
