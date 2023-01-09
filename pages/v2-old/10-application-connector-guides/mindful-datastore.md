---
title: Mindful Datastore Authentication
sidebar: cyclr_sidebar
permalink: mindful-datastore-connector
tags: [connector]

---
{::options parse_block_html="true" /}
<section class="card">
## Mindful Datastore setup

To set up the Mindful Datastore connector to use in Cyclr, you need to get your API key. If you need more information, contact the Mindful support team.


</section>
<section class="card">
## Cyclr setup

To set up the Mindful Datastore connector in Cyclr:

1. Go to your **Cyclr Console**.

2. Select **Connectors** > **Application Connector Library** at the top of the page.

3. Use the search box to find the **Mindful Datastore** connector.

4. Select the **Setup Required** icon.

5. Enter the your **API Key**. 

6. Select **Save Changes**.


</section>
<section class="card">
## Additional information

### Custom Fields
The **Upsert Data Set** method allows you to send a `data_values` object with the request. This object can contain any number of key and value pairs. To send a key and value pair:

1. Go to the **Edit Connector** page for the Mindful Dataset connector.
2. Under the **Methods & Fields** heading, find and select the **Upsert Data Set** method.
3. Next to the **Request Fields** heading, select the red plus button.
4. In the **Field Location** box, enter `data_values.{required key name}`. For example, `data_values.key1`.
5. Enter a suitable **Display Name** for the field.
6. Provide a **Description** for the field if you want to.
7. Set the **Date Type** for the field to **Text**.
8. Select **Create**.

The makes the field available in steps that use the **Upsert Data Set** method. The value you assign to the field is stored and sent in the `data_values` object against the specified key name. You can repeat this process for any key and value pair you want to add to the `data_values` object.

### Custom objects

The **Get Data Set** method uses Cyclr custom objects to map possible dataset fields dynamically based on the specified customer contact number. 

### Set up a custom object

When you set up a custom object it creates a new method category with the parameters you enter. To set up a custom object:

1. Go to the **Mindful Datastore** connector **Settings** page.
2. Under the **Methods and Fields** heading, expand the **Data Sets** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Enter the required customer contact number into **Specify object name**. 
5. Select **Copy**.

A new custom object category will have been created with the specified contact number. **Get Data Set** can now be run from within this category with all dataset fields mapped automatically.

</section>
