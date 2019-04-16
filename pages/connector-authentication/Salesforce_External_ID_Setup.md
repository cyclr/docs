---
title: Salesforce Upsert Setup
sidebar: cyclr_sidebar
permalink: salesforce-upsert-setup
tags: [connector]
---

# Salesforce Upsert Methods Setup #

In order to use the Upsert Account or Upsert Contact methods you must first setup a custom external ID field within the object in salesforce.

**External ID Creation**

* To add a custom external ID field to an object in Salesforce first click the `Setup` button in the top right of the screen.
![](./images/external_id_setup_button.PNG)

* Scroll down to the `Build` label and click `Customize -> Account (Or Contact) -> Fields`.
![](./images/salesforce_external_id_customize.PNG)

* Once on the Fields screen scroll down to where it says 'Account Custom Fields & Relationships' and press `New`.
* Select the `Text` checkbox and press `Next`.
* Enter the Field Label and Length. Select `Do not allow duplicate values` and `Treat "ABC" and "abc" as different values`. And Select  `Set this field as the unique record identifier from an external system`, then press `Next`.
![](./images/salesforce_custom_fields_setup.PNG)
* Check `Visible` and press `Next` and then `Save`.
![](./images/salesforce_custom_fields_visible.PNG)

**Using the Upsert Methods**
 
Once you have setup your External ID field you are ready to use the corresponding Upsert method.

* Copy the API Name of your External ID field from Salesforce.
![](./images/salesforce_custom_fields_api_name.PNG)
* Go to setup the Upsert method in Cyclr, and insert the copied value into the 'External ID Field', and map your External ID value to the 'External ID' field.
![](./images/salesforce_custom_fields_cyclr.PNG)