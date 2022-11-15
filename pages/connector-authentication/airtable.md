---
title: Airtable Authentication
sidebar: cyclr_sidebar
permalink: airtable-connector
tags: [connector]
---

# Partner Setup

## Retrieving API Key
*   Visit your [account page](https://airtable.com/account) and copy the API key in the **API** area.

## Retrieving Base ID and Table Name
*   Base ID can be accessed by visiting the [API area](https://airtable.com/api) and clicking on the table base you want to use. In the introduction area of the page you are redirected to, your base ID is shown e.g. "The ID of this base is app123ABC.".
*   The table name is the name of the table in the base you want to operate on. Note: This is NOT the name of the base.

# Cyclr Setup

Setup your Airtable App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Airtable**
*   Click the **Setup** button

Enter the following values:

**API Key**: Retrieved from the previous steps.


Your Airtable Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

# Airtable custom objects

The Airtable connector uses Cyclr custom objects to make methods dynamic based on module names. Each custom object name requires:

-   [The Base ID](#find-the-base-id) of the Table that you want to work with.
-   [The Table Name](#find-the-table-name) of the Table you want to interact with.
    Note: Base IDs and Table Names can be different for each client account.

## Set up a custom object

When you set up a custom object it creates a new method category with the parameters you enter. To set up a custom object:

1. Go to the Airtable connector **Settings** page:
    - For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **Airtable** > **Edit Connector**.
    - For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **Airtable** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Records (Custom Object)** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Enter the BaseID, followed by a dot, and then the Table Name into **Specify object name**. For example, `appTCumMdMOC1Zcqz.TestTable`.
5. Select **Copy**.

