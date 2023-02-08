---
title: QuickBooks Connector
sidebar: cyclr_sidebar
permalink: quickbooks-connector
tags: [connector]
keywords: [intuit]
---
{::options parse_block_html="true" /}
<section class="card">

## QuickBooks setup

To authenticate the Quickbooks connector, you need a **Client ID** and **Client Secret**.

To obtain these values, you need a QuickBooks Online application. Tou can create an app through the Quickbooks [developer portal]((https://developer.intuit.com/app/developer/myapps):

> **Note**: There are sections for **Development** and **Production** apps, and these steps are for a **Development** app.

1. Select the **Create an app** button and select **QuickBooks Online and Payments**.
2. Name your app and select **Accounting** from the scopes.  If you're based in the US, you can add the **Payments** scope later.
3. Select **Create App**.
4. Go to **Development** > **Keys & OAuth**, and note down the `Client ID` and `Client Secret`.
5. Under **Redirect URIs**, change the existing value to: `https://{ServiceDomain}/connector/callback`.

    > **Note**: To find your Service domain in your Cyclr Console, go to **Settings** > **General Settings** > **Service Domain**.

6. Scroll down and select **Save**.

</section>
<section class="card">

## Cyclr setup

To set up the Quickbooks connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Quickbooks connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Client ID**   | The **Client ID** from your Quickbook application. |
   | **Client Secret**   | The **Client Secret** from your Quickbook application.                               |
   | **Callback URL**| Cyclr fills this field by default.           |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

### Account setup

Cyclr also asks you for the **Base Domain** when you install the Quickbooks connector into an account

* For a development app, use `sandbox-quickbooks.api.intuit.com`.
* For a production app, use `quickbooks.api.intuit.com`.

</section>
<section class="card">

## Additional information

To map custom fields on the **Update Purchase Order** method, complete the following steps:

1. In the connector settings page, locate the **Update Purchase Order** method.
2. Under the **Request Fields** heading, select the red **+** button.
3. Enter the required field location in the format 'CustomField.FieldName', where 'FieldName' is the `DefinitionId` of the custom field to update.
4. Enter any additional information for the method field and then select **Create**.
</section>
