---
title: Magento 2 Connector
sidebar: cyclr_sidebar
permalink: magento-2-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Magento 2 Setup

<a name="api-key"></a>

To authenticate the connector, you need to create an API Key:

1. Log in to the Magento 2 admin portal, and select **System** > **Extensions** > **Integrations**.
2. Select **Add New Integration**.
3. Enter a unique name for the integration in the `Name` field, enter your admin password in the `Your Password` field, and leave all the other fields blank.
4. Select the API tab, set **Resource Access** to **All**, and then select **Save**.

    ![](./images/resource-access-all.png)

5. Select the **Activate** link next to your new integration.
6. Select **Allow** and copy the value in the **Access Token** field (not the **Consumer Key**). 

![](./images/integration-tokens.png)


</section>
<section class="card">
## Cyclr account setup

Cyclr asks you for the below values when you install the Magento 2 connector into an account:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Domain**         | The domain of your Magento 2 site, for example, `https://my-magento-site.com` |
   | **API Key**        | The [API Key](#api-key) from your Magento 2 account.                          |

> **Note**: You can use different details for different accounts.


</section>
<section class="card">

## Additional information

### Bulk endpoints

To use bulk methods such as Bulk Update Product, you need to enable/install asynchronous functionality and RabbitMQ on your Magento 2 instance. For more information, see the Magento documentation on [bulk endpoints](https://devdocs.magento.com/guides/v2.4/rest/bulk-endpoints.html).

### Custom Methods

The Magento 2 connector allows you to create custom methods for custom endpoints. You can create these methods with the custom objects in the **Custom Method** category.

### Set up a custom object

When you set up a custom object it creates a new method category with the endpoint you enter. To set up a custom object:

1. Go to the **Magento 2** connector's **Settings** page.
2. Under the **Methods and Fields** heading, expand the **Custom Methods** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Enter the required custom method endpoint into **Specify object name**. 
5. Select **Copy**.

This creates a new custom object category with the specified method endpoint. You can run the **GET** or **POST** methods from the new category to call the specified endpoint. You need to map all of the request and response fields manually.

### Webhooks

If you want to use webhooks with **Magento 2**, we have a dedicated **Magento 2 Webhooks** Connector and a plugin that you can install in your Magento 2 instance.

For more information, see our [Magento 2 Webhooks connector](https://docs.cyclr.com/magento-2-webhooks-connector#magento-2-webhooks-setup) documentation.

</section>
