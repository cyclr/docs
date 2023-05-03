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

The QuickBooks connector uses single partner URL webhooks, that can be triggered by certain events. Follow the next steps in the developer console to set up webhooks.

1. In the Production section, select Webhooks.
2. Enter the **Partner Endpoint URL**, which can be found in the **Cyclr console** under Connectors > Application Connector Library > QuickBooks > Customise installation user experience/Setup Required icon. This is where the server will send notifications.
3. In the **Event Frequency** dropdown, select how long we should aggregate events for.
4. Select the **Show webhooks** link.
5. Review the required events and operations.
6. Select the events you would like to receive notifications for.
7. Select **Save**.

</section>
