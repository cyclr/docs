---
title: Exerp Information
sidebar: cyclr_sidebar
permalink: exerp-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

### Mapping extended attribute fields

The methods `Centers > Get Center` and `People > Get Person` dynamically return extended attribute fields. To map these fields within Cyclr:

1. Go to the **Settings** page of the Exerp connector:
    - For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **Exerp** > **Edit Connector**.
    - For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **Exerp** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Centers** or **People** categories.
3. Expand the method you want to map custom fields for - either **Get Center** or **Get Person**.
4. Select the pink **+** icon.
5. Enter the following:

   | Value | Description |
   | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Field Location | The extended attribute field ID. This should be entered as `extendedAttributes.{ExtendedAttributeId}`. For example, if the `ExtendedAttributeId` is `EXAMPLE_ATTRIBUTE_ID` then enter `extendedAttributes.EXAMPLE_ATTRIBUTE_ID` as the field location. You can find the `ExtendedAttributeId` of an extended attribute field by running the corresponding method on the **Edit Connector** page. The response on the **Method Response** tab will contain an `extendedAttributes` object and each key this contains is an `ExtendedAttributeId`. |
   | Display Name | The display name to use within Cyclr. |
   | Description | The description to use within Cyclr. |
   | Data Type | The data type of the extended attribute. |

6. Select **Create**.
7. Steps in a cycle can now have the extended attribute mapped.

</section>
