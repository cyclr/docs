---
title: SaaShr Authentication
sidebar: cyclr_sidebar
permalink: saashr-connector
tags: [connector]
---

<a name="saashr-setup"></a>

# SaaShr setup

You will need the following to authenticate the SaaShr connector in an account:

1. The `username` for your SaaShr account.
2. The `password` for your SaaShr account. For the first time setup, this will be set as your account password.
3. The short `company name` for your SaaShr account.
4. The URL of your SaaShr installation. For example, if you access SaaShr using `https://secure.saashr.com` then enter `https://secure.saashr.com`.
5. The `API key` of your SaaShr account.

If you do not have any of this information, please contact your SaaShr account manager.

<a name="first-time-setup"></a>

### First time setup

When installing the SaaShr connector for the first time you need to enter an additional `setup password`. This will be provided by SaaShr as an auto-generated password that will be changed to the `password` value on first installation. Further authentications of the same SaaShr account will then only require the `password` that was entered on the first installation to be provided.

<a name="cyclr-setup"></a>

# Cyclr setup

<a name="account-setup"></a>

### Account setup

You will be asked for the following values when installing the SaaShr connector within an account:

| Value              | Description                                                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Base URL**       | The URL of your SaaShr installation. For example, if you access SaaShr using `https://secure.saashr.com` then enter `https://secure.saashr.com`. |
| **Company Name**   | The short company name for your SaaShr account. All methods will make calls using this company name.                                             |
| **Username**       | The username for your SaaShr account.                                                                                                            |
| **Password**       | The password for your SaaShr account. For the first time setup, this will be set as your account password for subsequent installations.          |
| **Setup Password** | Only required if this is your first time integrating with the API. This is an auto-generated password provided by SaaShr.                        |
| **API Key**        | The API key of your SaaShr account.                                                                                                              |

# Further information

## Custom field mapping
In some cases, further field mapping is required on methods which accept key and value pairs in an array. This can be seen in the methods **Update Cost Center** and **Update Employee Pay Information**. To map fields, please follow these steps:

1. Go to the **Edit Connector** page for the SaaShr connector.
2. Under the **Methods & Fields** heading, find the method you wish to map custom fields on.
3. Next to the **Request Fields** heading, select the red plus button.
4. In the **Field Location** box, enter the required custom field name, followed by a dot, followed by the field's index you wish to create. The index must be an integer. For example: `gl_codes.123`.
5. Enter a suitable **Display Name** for this field.
6. Provide a **Description** for this field if you wish.
7. Set the **Date Type** to **Text** for the field.
8. Click **Create**.
9. The field will now be available in steps using this method. The value assigned to the field will be stored in the custom field's array with the specified index.
10. This process can be repeated for any key and value pair you wish to add to the custom field's array.

The **Update Cost Center** method allows this mapping for the following fields: `gl_codes`, `custom_fields` and `contacts`.

The **Update Employee Pay Information** only allows this mapping for `gl_codes`.
