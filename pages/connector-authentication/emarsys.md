---
title: Emarsys Authentication
sidebar: cyclr_sidebar
permalink: authenticate-emarsys
tags: [connector]
---

# Account Setup

<a href=#emarsys-credentials>

To authenticate the connector you will need the following credentials:

| Credentials    | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| **Username**   | The user name of your Emarsys account. It is usually in the following format: `account_name00X`, where `X` is a digit. |
| **Secret Key** | The secret key of your Emarsys application.                  |

To obtain these you will need to create an API user within Emarsys. You can find more information on creating an API User [here](https://help.emarsys.com/hc/en-us/articles/115004740329#api-users).

Once you have the username and secret, you can use them to authenticate the connector.

## Additional Information 

<a href=#custom-fields>

### Custom Fields

In the Emarsys connector there are some methods which utilise custom fields which will need to be manually mapped:

#### Contacts > Get Contact Data

#### Contact Lists > List Contact Data In A Contact List

When entering the **Fields** request parameter, the method will respond with equivalent response fields. These fields need to be mapped manually. From the **Edit Connector** page of the Emarsys connector:

1. Under the **Methods & Fields** heading, expand the corresponding method. 

2. Under the **Response Fields** heading, select the **+** button.

3. Complete the fields:

   | Field              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | The `FieldId` of the custom field. This should match the field ID entered into the **Fields** request parameter and have the format `[].{{FieldId}}`. The `FieldId` of the field can be found by using the **Utilities > List Contact Fields** method. |
   | **Display Name**   | The display name of the custom field in the Cyclr UI (optional). |
   | **Description**    | The description of the custom field in the Cyclr UI (optional). |
   | **Data Type**      | The Data type of the custom field. This should match the `Type` of the custom field in Emarsys. |

4. Select **Create**.

#### External Content > Request External Content For Personalisation

This method allows you to use an external API to personalize content in messages. Custom `parameters` and response fields will need to be mapped as required. From the **Edit Connector** page of the Emarsys connector, to map parameters:

1. Under the **Methods & Fields** heading, expand the corresponding method. 

2. Under the **Request Fields** heading, select the **+** button.

3. Complete the fields:

   | Field              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | The Emarsys parameter to add external content to. The field location should match the Emarsys `StringId` of the field and have the format `[parameters].{{StringId}}`. The `StringId` of the field, referred to as `key` in the Emarsys documentation, can be found by using the **Utilities > List Contact Fields** method. |
   | **Display Name**   | The display name of the custom field in the Cyclr UI (optional). |
   | **Description**    | The description of the custom field in the Cyclr UI (optional). |
   | **Data Type**      | The Data type of the custom field. This should match the `Type` of the custom field in Emarsys. |

4. Select **Create**.

From the **Edit Connector** page of the Emarsys connector, to map response fields:

1. Under the **Methods & Fields** heading, expand the corresponding method. 

2. Under the **Response Fields** heading, select the **+** button.

3. Complete the fields:

   | Field              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | Response fields for the method will include the **fields** entered and **parameters** mapped in the method request. For each, the field location should match the field `key` or parameter `StringId` of the field and have the format `[content].{{key}}` or `[content].{{StringId}}` respectively. |
   | **Display Name**   | The display name of the custom field in the Cyclr UI (optional). |
   | **Description**    | The description of the custom field in the Cyclr UI (optional). |
   | **Data Type**      | The Data type of the custom field. This should match the `Type` of the custom field in Emarsys. |

4. Select **Create**.

For more information, see the Emarsys API documentation for this method [here](https://dev.emarsys.com/docs/emarsys-api/ce8d99f0f480b-request-external-content-for-personalization).



