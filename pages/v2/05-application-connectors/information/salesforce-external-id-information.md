---
title: Salesforce Upsert information
sidebar: cyclr_sidebar
permalink: salesforce-upsert-setup-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Salesforce Upsert Methods Setup

In order to use the Upsert Account or Upsert Contact methods, you need to set up a custom external ID field within the object in salesforce.

The process to set up the method is slightly different depending on whether you use Salesforce Classic or Lightning Experience.

</section>
<section class="card">

### External ID Creation - Salesforce Classic

1. To add a custom external ID field to an object in Salesforce, select the **Setup** button in the top right of the window.
    ![](./images/external_id_setup_button.png)

2. Scroll down to the **Build** label and select **Customize** > either **Account** or **Contact** > **Fields**.
    ![](./images/salesforce_external_id_customize.png)

3. On the Fields screen, scroll down to **Account Custom Fields & Relationships** and select **New**.
4. Select the **Text** checkbox and press **Next**.
5. Enter the Field Label and Length. 
6. Select **Do not allow duplicate values** and **Treat "ABC" and "abc" as different values**, select  **Set this field as the unique record identifier from an external system**, then select **Next**.
    ![](./images/salesforce_custom_fields_setup.png)
6. Select **Visible** and press **Next** and then **Save**.
    ![](./images/salesforce_custom_fields_visible.png)


</section>
<section class="card">

### External ID Creation - Lightning Experience

1. To add a custom external ID field to an object in Lightning Experience, select the **Setup** cog in the top right of the screen, and select **Setup**.
    ![](./images/external_id_setup_button-lightning.png)

2. Scroll down to the **Platform Tools** label and select **Objects and Fields** > **Object Manager**.
    ![](./images/object_manager_menu_item-lightning.png)

3. On the Object Manager screen, select the object you want to add an external field for.  For example, if you want to set up an **Upsert Account** method, select **Account**.
    ![](./images/object_manager-lightning.png)

4. Select the **Fields & Relationships** from the menu and select the **New** button.
    ![](./images/new_field-lightning.png)
5. Select the **Text** checkbox and select **Next**.
6. Enter the Field Label and Length. Select **Do not allow duplicate values**, **Treat "ABC" and "abc" as different values**., and  **Set this field as the unique record identifier from an external system**, then select **Next**.
    ![](./images/salesforce_custom_fields_setup.png)
7. Select **Visible**, select **Next**, and then select **Save**.
    ![](./images/salesforce_custom_fields_visible.png)

## Use the Upsert methods
 
You can use the **External ID** field you set up to use the corresponding Upsert method.

1. Copy the API Name of your External ID field from Salesforce:

    **Salesforce Classic**
    ![](./images/salesforce_custom_fields_api_name.png)

    **Lightning Experience**
    ![](./images/salesforce_custom_fields_api_name-lightning.png)

2. Go to set up the Upsert method in Cyclr, insert the copied value into the **External ID Field**, and map your External ID value to the **External ID** field.
    ![](./images/salesforce_custom_fields_cyclr.png)

</section>
