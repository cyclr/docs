
<section class="setup webhooks" markdown="1">

## Webhooks setup

<div class="section-content" markdown="1">

It is assumed that you have already installed our [Magento 2 Webhooks plugin](https://github.com/cyclr/cyclr-magento-2).

To authenticate the connector use your existing Magento 2 `API Key`.

See the [Magento 2 integration instructions]( https://docs.cyclr.com/magento-2-connector#magento-2-setup) to set up an integration within Magento.

To get API Key:

1. Log in to the admin portal, and click `System` > `Extensions` > `Integrations`.
2. Click the `Edit` pencil next to your integration.

    ![](./images/edit_integration.png)

3. Scroll down and copy your access token

    ![](./images/integration-tokens.png)

Now that you have your Access token go to the `Connector Setup` page in Cyclr.

1. On the first page enter your Magento site URL e.g. `https://my-magento-site.com` and click `Next`
2. Enter your `Access Token` into the `API Key` field and click `Next` : be sure to enter your **Access Token** and not your **Consumer Key**

Your connector is now setup and ready to go!

> Depending on your firewall settings you may need to manually enable DELETE commands.

### Available Webhooks

- Customer
    - New Customer
    - Customer Updated
    - Customer Deleted
- Product
    - New Product
    - Product Updated
    - Product Deleted
- Order
    - New Order
    - Order Updated
- Subscriber
    - Subscriber Saved



