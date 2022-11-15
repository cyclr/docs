---
title: Mindful Datastore Authentication
sidebar: cyclr_sidebar
permalink: mindful-datastore-connector
tags: [connector]

---

## Cyclr setup

To set up the Mindful Datastore connector in Cyclr:

1. Go to your **Cyclr Console**.

2. Select **Connectors** > **Application Connector Library** at the top of the page.

3. Use the search box to find the **Mindful Datastore** connector.

4. Select the **Setup Required** icon.

5. Enter the your **API Key**. 

6. Select **Save Changes**.

## Additional Information
The **Upsert Data Set** method allows you to send a `data_values` object with the request. This object can contain any number of key and value pairs. To send a key and value pair:

1. Go to the **Edit Connector** page for the Mindful Dataset connector.
2. Under the **Methods & Fields** heading, find and select the **Upsert Data Set** method.
3. Next to the **Request Fields** heading, select the red plus button.
4. In the **Field Location** box, enter `data_values.` followed by the required key name. For example: `data_values.key1`.
5. Enter a suitable **Display Name** for this field.
6. Provide a **Description** for this field if you wish.
7. Set the **Date Type** to **Text** for the field.
8. Select **Create**.

The makes the field available in steps that use the **Upsert Data Set** method. The value you assign to the field will be stored and sent in the `data_values` object against the specified key name. You can repeat this process for any key and value pair you wish to add to the `data_values` object.
