---
title: Mindful Callback Authentication
sidebar: cyclr_sidebar
permalink: mindful-callback-connector
tags: [connector]

---

## Mindful Callback setup

## Cyclr setup

To set up the Mindful Callback connector in Cyclr:

1. Go to your **Cyclr Console**.

2. Select **Connectors** > **Application Connector Library** at the top of the page.

3. Use the search box to find the **Mindful Callback** connector.

4. Select the **Setup Required** icon.

5. Enter the your **Organization ID**.             |

6. Select **Save Changes**.

## Additional Information
The **Create Callback** method allows for a `user_data` object to be sent with the request. This object can contain any number of key and value pairs. To send a key and value pair:

1. Go to the **Edit Connector** page for the Mindful Callback connector.
2. Under the **Methods & Fields** heading, find the **Create Callback** method.
3. Next to the **Request Fields** heading, select the red plus button.
4. In the **Field Location** box, enter `user_data.` followed by the required key name. For example: `user_data.key1`.
5. Enter a suitable **Display Name** for this field.
6. Provide a **Description** for this field if you wish.
7. Set the **Date Type** to **Text** for the field.
8. Click **Create**.
9. The field will now be available in steps using this method. The value assigned to the field will be stored and sent in the `user_data` object against the specified key name.
10. This process can be repeated for any key and value pair you wish to add to the `user_data` object.

> **Note**: Only keys that are whitelisted by the Widget’s User Data Set are submitted to Mindful Callback.
