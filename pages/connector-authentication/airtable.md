---
title: Airtable Authentication
sidebar: cyclr_sidebar
permalink: airtable-connector
tags: [connector]
---

## Airtable setup

You need an API key, Base ID and table name from Airtable to use the Airtable connector in Cyclr:

*  To get the API key, go to the Airtable [account page](https://airtable.com/account) and copy of the API key from the **API** section.
*  To get the Base ID, go to the [API](https://airtable.com/api) section in Airtable and select the table base you want to use. Copy the BaseID from the **Introduction** section.
*  The table name is the name of the table in the base (**not** the name of the base).

## Cyclr account setup

Cyclr asks you for the below values when you install the <connector name> connector into an account:

| Value              | Description                                   |
| :----------------- | :------------------------------------------   |
| **API key**        | Your Airtable API key.                        |
| **BaseID**         | The BaseID of the base you want Cyclr to use. |
| **Table name**     | The name of the table you want Cyclr to use.  |

You can test the connector in one of your Cyclr accounts if you call a method to confirm it can return some data.

## Additional information

### Airtable custom objects

The Airtable connector uses Cyclr custom objects to make methods dynamic based on module names. Each custom object name requires:

*   The BaseID of the table that you want to work with.
*   The table name of the table you want to interact with.

> **Note**: The BaseID and table name can be different for each client account.

#### Set up a custom object

If you set up a custom object, you create a new method category with the parameters you enter. To set up a custom object:

1. Go to the Airtable connector **Settings** page:
    - For template connectors, go to **Templates** > **Template Connectors** > **Airtable** > **Edit Connector**.
    - For connectors within a cycle, go to **Design New Template** > **Application Connectors** > **Airtable** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Records (Custom Object)** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Enter `{BaseID}.{table name}` into the **Specify object name** field. For example, `appTCumMdMOC1Zcqz.TestTable`.
5. Select **Copy**.

