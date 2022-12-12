---
title: OneLogin Authentication
sidebar: cyclr_sidebar
permalink: onelogin-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
## OneLogin setup

To authenticate this connector, you need a OneLogin credential pair of **Client ID** and **Client Secret**. Find more information on how to obtain these credentials in OneLogin's [Working with API credentials](https://developers.onelogin.com/api-docs/1/getting-started/working-with-api-credentials) documentation.


</section>
<section class="card py-5 my-5">
## Cyclr setup

To set up the OneLogin connector in Cyclr, go to your **Cyclr Console**.

1. Select **Connectors** > **Application Connector Library** at the top of the page.

2. Use the search box to find the **OneLogin** connector.

3. Select the **Setup Required** icon.

4. Enter your `Client ID` and `Client Secret`. 

5. Enter your OneLogin **sub domain**. You can find the domain in your OneLogin frontend URL just before `.onelogin.com`. For example, if your frontend URL is `https://testing-dev.onelogin.com/portal`, your **sub domain** would be `testing-dev`.

6. Select **Save Changes**.


</section>
<section class="card py-5 my-5">
## Additional information

### Generate fields for the **Create App** method

The **Create App** method accepts a wide range of possible request parameters beyond what's mapped as standard in Cyclr. You can map these fields manually, or you can generate the fields based on an existing application. To generate fields:

1. Go to the **Edit Connector** page for the OneLogin connector.
2. Under the **Methods & Fields** heading, find and select the **Get App Template** method.
3. Specify the template app you want to use, and run this method.
4. Copy the returned JSON script under **Return Value**.
5. Under the **Methods & Fields** heading, find and select the **Create App** method.
6. In the **Request Fields** section, find and select the red magnifying glass icon.
7. Paste the copied JSON script into the **Sample Data** box.
8. Select **Generate**.

This process maps the possible request fields so they're ready to use when you create a new application.

### Map custom fields for the **List Users** and **Get User** methods

The **List Users** and **Get User** methods can return custom attributes if the're available. To map these in the response, map a custom field to the attribute's location:

1. Go to the **Edit Connector** page for the OneLogin connector.
2. Under the **Methods & Fields** heading, find and select the **List Users** or **Get User** method.
3. In the **Request Fields** section, find and select the red plus icon.
4. For **List Users**, set the field location to `[].custom_attributes.attributeName` where `attributeName` is the returned custom attribute.
5. For **Get User**, instead use the location `custom_attributes.attributeName`.
6. Give the field an appropriate **Display Name** and **Description**.
7. Set the **Data Type** to the expected returned data type.
8. Select **Create**.

This process means returned custom attributes map onto all steps that call these methods.

</section>
