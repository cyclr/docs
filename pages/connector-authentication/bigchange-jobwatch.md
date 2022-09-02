---
title: BigChange JobWatch
sidebar: cyclr_sidebar
permalink: bigchange-jobwatch-connector
tags: [connector]
---

# BigChange JobWatch setup

You need the following information to set up the BigChange JobWatch connector in Cyclr:

- The [API key](#getting-the-api-key) of your BigChange JobWatch account.
- The username and password of your BigChange JobWatch account.

<a name="getting-the-api-key"></a>

## Getting the API key

Please contact your BigChange JobWatch customer service representative if you need help getting your API key.

# Cyclr setup

## Account setup

You will be asked for the following values when installing the BigChange JobWatch connector within an account:

| Value        | Description                                      |
| :----------- | :----------------------------------------------- |
| **API Key**  | The API key of your BigChange JobWatch account.  |
| **Username** | The username of your BigChange JobWatch account. |
| **Password** | The password of your BigChange JobWatch account. |

# Additional information

## Mapping custom fields

The BigChange JobWatch connector has custom field support for several methods. You can find a list of compatiable methods [here](#custom-field-compatiable-methods). To add a custom field to a method:

1. Go to the **Edit Connector** page for the BigChange JobWatch connector.
2. Under the **Methods & Fields** heading, locate the required method by expanding out the categories and method name.
3. Select the pink **+** button to add a method field.
4. Enter the following:
   | Value              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | The custom field location, which must have the format `cust_<custom field name>`. The `<custom field name>` value has the exact same format as on the contact details page. |
   | **Display Name**   | The display name of the custom field within the Cyclr UI.    |
   | **Description**    | The description of the custom field within the Cyclr UI.     |
   | **Data Type**      | The data type of the custom field. This should be set to `Text`. |
5. Select **Create**.

<a name="custom-field-compatiable-methods"></a>

## Custom field compatiable methods

You can add custom fields for contacts, contact notes, and jobs in the following methods:

-   `Create Contact`
-   `Update Contact`
-   `Update Contact Note`
-   `Create Job`
-   `Update Job`

You can view custom fields for contacts, contact notes, and jobs in the following methods:

-   `Get Contact`
-   `Get Contact Note`
-   `Get Job`
-   `List Contact Notes`
-   `List Contacts`
-   `List Group Jobs`
-   `List Jobs`
-   `List Jobs by Contact`
-   `Search Contacts`
-   `Search Contacts By Email`
-   `Search Contacts By Email, ID, Or Reference`
-   `Search Contacts By Phone Number`
-   `Search Contacts By Postcode`
