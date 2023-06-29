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

## Webhooks

The QuickBooks connector uses single partner URL webhooks, that certain events can trigger. To set up webhooks, follow the next steps in the developer console:

1. In the **Production** section, select **Webhooks**.
2. Enter the **Partner Endpoint URL** to specify where the server sends notifications. To find the URL in the **Cyclr console**, go to **Connectors** > **Application Connector Library** > **QuickBooks** and select the **Customise installation user experience/Setup Required** icon.
3. In the **Event Frequency** dropdown, select how long you want to aggregate events for.
4. Select the **Show webhooks** link.
5. Review the required events and operations and select the events you want to receive notifications for.
6. Select **Save**.

> **Note**: Please wait a minimum of 10 minutes after setting the webhook URL in the console, before trying to test. Quickbooks can experience issues with a delay when setting a new URL, so this will prevent any false errors.
</section>
