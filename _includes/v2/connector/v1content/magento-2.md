
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

### Webhooks

If you wish to use webhooks with **Magento 2** we have a dedicated **Magento 2 Webhooks** Connector, along with a plugin to install in your Magento instance.

More information can be found here: [https://docs.cyclr.com/magento-2-webhooks-connector](https://docs.cyclr.com/magento-2-webhooks-connector#magento-2-webhooks-setup)
