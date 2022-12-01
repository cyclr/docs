---
title: Magento 2 Connector
sidebar: cyclr_sidebar
permalink: magento-2-connector
tags: [connector]
---

Magento 2 Setup
---------------
**ApiKey Setup**

To authenticate the connector you will first have to create an API Key:

1. Log in to the admin portal, and click `System` > `Extensions` > `Integrations`.
2. Click `Add New Integration`.
3. Enter a unique name for the integration in the `Name` field, and enter your admin password in the `Your Password` field, leaving all other fields blank.
4. Click the API tab and set Resource Access to All.

    ![](./images/resource-access-all.png)

5. Click `Save`.
6. Click the `Activate` link next to your new integration.
7. Click `Allow` and copy the value in the `Access Token` field (Be sure to copy the **Access Token** and not the **Consumer Key**). 

![](./images/integration-tokens.png)

Now that you have your Access token go to the `Connector Setup` page in Cyclr.

1. On the first page you should enter the domain of your Magento site e.g. `https://my-magento-site.com` and click `Next`.
2. Paste your `Access Token` into the `API Key` field and click `Next`.
3. Your connector is now setup and ready to go.

### Bulk Endpoints

To use bulk methods such as Bulk Update Product you must enable/install asynchronous functionality and RabbitMQ on your Magento instance. More information can be found [here](https://devdocs.magento.com/guides/v2.4/rest/bulk-endpoints.html).

### Custom Methods

The Magento 2 connector allows for custom methods to be created for custom endpoints. This is done through custom objects on the **Custom Method** category.

### Set up a custom object

When you set up a custom object it creates a new method category with the endpoint you enter. To set up a custom object:

1. Go to the **Magento 2** connector **Settings** page.
2. Under the **Methods and Fields** heading, expand the **Custom Methods** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Enter the required custom method endpoint into **Specify object name**. 
5. Select **Copy**.

A new custom object category will have been created with the specified method endpoint. The **GET** or **POST** methods can be run from in here to call the specified endpoint. All request and response fields will need to be mapped manually.

### Webhooks

If you wish to use webhooks with **Magento 2** we have a dedicated **Magento 2 Webhooks** Connector, along with a plugin to install in your Magento instance.

More information can be found here: [https://docs.cyclr.com/magento-2-webhooks-connector](https://docs.cyclr.com/magento-2-webhooks-connector#magento-2-webhooks-setup)
