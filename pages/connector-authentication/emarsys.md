---
title: Emarsys Authentication
sidebar: cyclr_sidebar
permalink: authenticate-emarsys
tags: [connector]



---



# **Account Setup** #

<a href=#emarsys-credentials>

To authenticate the connector you will need the following credentials. 

| Credentials | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| Username    | The user name of your Emarsys account. It is usually in the following format: *account_name00X*, where *X* is a digit. |
| Secret Key  | The secret key of your Emarsys application.                  |

To obtain these you will need to create an API user within Emarsys. You can find more information on creating an API User [here:](https://help.emarsys.com/hc/en-us/articles/115004740329#api-users) 

Once you have the username and secret, you can use them to authenticate the connector.



## Additional Information 

<a href=#custom-fields>

### Custom Fields

There are several methods which utilise custom fields in the Emarsys connector. For some of these you will need to map the fields manually. Please follow the instructions below on how to use these methods. 

#### **Contacts > Get Contact Data**



#### **Contact Lists > List Contact Data In A Contact List** 

When entering the **Fields** parameter, you will need to map any fields added manually: 

1. Edit your **Emarsys** Connector navigate to the **Contact Lists > List Contact Data In A Contact List** method. 
2. Add a Custom Field named `[].{{FieldId}}` The `{{FieldId}}` should match the requested fields in the **Fields** parameter.

#### **External Content > Request External Content For Personalisation**

This method allows you to use your own API to personalize content in your Emarsys messages. In order to use this method you will need to add custom request fields.

1. Edit your **Emarsys** Connector navigate to the **External Content > Request External Content For Personalisation** method.
2. Add a custom field named `[parameters].{{key}}` The `{{key}}` will be the key of the parameters, these are reference fields which can be requested from Emarsys. More information on the logic to structure this request can be found in Emarsys's [documentation for this method](https://dev.emarsys.com/docs/emarsys-api/ce8d99f0f480b-request-external-content-for-personalization)
