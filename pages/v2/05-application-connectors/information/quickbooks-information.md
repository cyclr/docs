---
title: QuickBooks Connector
sidebar: cyclr_sidebar
permalink: quickbooks-information
tags: [connector-information]
keywords: [intuit]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Custom fields

You can map custom fields for the **Update Purchase Order** method:

1. In the connector settings page, locate the **Update Purchase Order** method.
2. Under the **Request Fields** heading, select the red **+** button.
3. Enter the required field location in the format 'CustomField.FieldName', where 'FieldName' is the `DefinitionId` of the custom field to update.
4. Enter any additional information for the method field and then select **Create**.

</section>
<section class="card">
  
## Webhooks

The QuickBooks connector uses single partner URL webhooks, that certain events can trigger. To set up webhooks, follow the next steps in the developer console:

1. In the **Production** section, select **Webhooks**.
2. Enter the **Partner Endpoint URL** to specify where the server sends notifications. To find the URL in the **Cyclr console**, go to **Connectors** > **Application Connector Library** > **QuickBooks** and select the **Customise installation user experience/Setup Required** icon.
3. In the **Event Frequency** dropdown, select how long you want to aggregate events for.
4. Select the **Show webhooks** link.
5. Review the required events and operations and select the events you want to receive notifications for.
6. Select **Save**.

> **Note**: After you set the webhook URL in the console,  please wait a minimum of 10 minutes before you try to test a webhook. There are sometimes delays with Quickbooks when you set a new URL, so prevent anif you wait you can prevent any false errors.

</section>
<section class="card">

## Realm ID

If your customer sets a **Realm ID** (Company ID) when they install the connector, then all of their cycles that use this connector use the **Realm ID**.  If your customer doesn't set a **Realm ID**, then each step in a cycle asks for the value.

Your customer can find their **Realm ID** in Quickbooks:

1. Go to **Settings** and select **Your Account** > **Settings**.
2. Select the **Billing and Subscription** tab.
3. On the **Your Account** page, make a note of the Realm ID/Company ID at the top of the page.

</section>
