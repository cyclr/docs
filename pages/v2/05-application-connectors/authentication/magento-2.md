---
title: Magento 2 Connector
sidebar: cyclr_sidebar
permalink: magento-2-connector
tags: [connector]
linkedpage: true
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
