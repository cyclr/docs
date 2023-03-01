---
title: Emarsys information
sidebar: cyclr_sidebar
permalink: authenticate-emarsys-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

<a href=#custom-fields></a>

</section>
<section class="card">

## Custom fields

In the Emarsys connector, some methods use custom fields that you need to map manually:

* Contacts > Get Contact Data
* Contact Lists > List Contact Data In A Contact List

When you enter the **Fields** request parameter, the method responds with equivalent response fields. You need to map these fields manually. 

From the **Edit Connector** page of the Emarsys connector:

1. Under the **Methods & Fields** heading, expand the corresponding method. 
2. Under the **Response Fields** heading, select the **+** button.
3. Complete the fields:

   | Field              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | The `FieldId` of the custom field. This should match the field ID entered into the **Fields** request parameter and have the format `[].{{FieldId}}`. You can find the `FieldId` of the field with the the **Utilities > List Contact Fields** method. |
   | **Display Name**   | The display name of the custom field in the Cyclr UI (optional). |
   | **Description**    | The description of the custom field in the Cyclr UI (optional). |
   | **Data Type**      | The Data type of the custom field. This should match the `Type` of the custom field in Emarsys. |

4. Select **Create**.

### External Content > Request External Content For Personalisation

This method allows you to use an external API to personalize content in messages. You need to map custom parameters and response fields.

To map the parameters, go to the **Edit Connector** page of the Emarsys connector:

1. Under the **Methods & Fields** heading, expand the corresponding method. 
2. Under the **Request Fields** heading, select the **+** button.
3. Complete the fields below:

   | Field              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | The Emarsys parameter to add external content to. The field location should match the Emarsys `StringId` of the field and have the format `[parameters].{{StringId}}`. You can find the `StringId` of the field, referred to as `key` in the Emarsys documentation, with the **Utilities > List Contact Fields** method. |
   | **Display Name**   | The display name of the custom field in the Cyclr UI (optional). |
   | **Description**    | The description of the custom field in the Cyclr UI (optional). |
   | **Data Type**      | The Data type of the custom field. This should match the `Type` of the custom field in Emarsys. |

4. Select **Create**.

To map response fields, go to the **Edit Connector** page of the Emarsys connector:

1. Under the **Methods & Fields** heading, expand the corresponding method. 
2. Under the **Response Fields** heading, select the **+** button.
3. Complete the fields:

   | Field              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | Response fields for the method include the **fields** entered and **parameters** mapped in the method request. For each, the field location should match the field `key` or parameter `StringId` of the field and have the format `[content].{{key}}` or `[content].{{StringId}}` respectively. |
   | **Display Name**   | The display name of the custom field in the Cyclr UI (optional). |
   | **Description**    | The description of the custom field in the Cyclr UI (optional). |
   | **Data Type**      | The Data type of the custom field. This should match the `Type` of the custom field in Emarsys. |

4. Select **Create**.

For more information, see the Emarsys [API documentation for this method](https://dev.emarsys.com/docs/emarsys-api/ce8d99f0f480b-request-external-content-for-personalization).

</section>
