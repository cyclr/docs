---
title: Salesforce Upsert Setup
sidebar: cyclr_sidebar
permalink: salesforce-upsert-setup
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
# Salesforce Upsert Methods Setup

In order to use the Upsert Account or Upsert Contact methods you must first setup a custom external ID field within the object in salesforce.

Setting up the method will be a slightly different process depending upon whether you are using Salesforce Classic, or Lightning Experience.


</section>
<section class="card">
## External ID Creation - Salesforce Classic

1. To add a custom external ID field to an object in Salesforce first click the `Setup` button in the top right of the screen.
    ![](./images/external_id_setup_button.png)

2. Scroll down to the `Build` label and click `Customize -> Account (Or Contact) -> Fields`.
    ![](./images/salesforce_external_id_customize.png)

3. Once on the Fields screen scroll down to where it says 'Account Custom Fields & Relationships' and press `New`.
4. Select the `Text` checkbox and press `Next`.
5. Enter the Field Label and Length. Select `Do not allow duplicate values` and `Treat "ABC" and "abc" as different values`. And Select  `Set this field as the unique record identifier from an external system`, then press `Next`.
    ![](./images/salesforce_custom_fields_setup.png)
6. Check `Visible` and press `Next` and then `Save`.
    ![](./images/salesforce_custom_fields_visible.png)


</section>
<section class="card">
## External ID Creation - Lightning Experience

1. To add a custom external ID field to an object in Lightning Experience first click the `Setup` cog in the top right of the screen, and select `Setup`.
    ![](./images/external_id_setup_button-lightning.png)

2. Scroll down to the `Platform Tools` label and click `Objects and Fields -> Object Manager`.
    ![](./images/object_manager_menu_item-lightning.png)

3. Once on the Object Manager screen, select the object you wish to add an external field for.  For example, if you are setting up an `Upsert Account` method,  select `Account`.
    ![](./images/object_manager-lightning.png)

4. Select the `Fields & Relationships` from the menu and click the `New` button.
    ![](./images/new_field-lightning.png)
5. Select the `Text` checkbox and press `Next`.
6. Enter the Field Label and Length. Select `Do not allow duplicate values` and `Treat "ABC" and "abc" as different values`. And Select  `Set this field as the unique record identifier from an external system`, then press `Next`.
    ![](./images/salesforce_custom_fields_setup.png)
7. Check `Visible` and press `Next` and then `Save`.
    ![](./images/salesforce_custom_fields_visible.png)



</section>