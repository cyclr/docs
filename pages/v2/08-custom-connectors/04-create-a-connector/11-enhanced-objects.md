---
title: Enhanced objects
sidebar: cyclr_sidebar
permalink: enhanced-objects
tags: [connector-creation]
menus:
    create-a-connector:
        title: Enhanced objects
        identifier: enhanced-objects
        toggleonly: menutoggleonly
        weight: 11
---
{::options parse_block_html="true" /}
<section class="card">

You can add custom objects to a connector in Cyclr. 

## Enable category customization

To create custom objects, you need to copy a category to use for the custom objects. 

1. Go to **Connectors** > **Custom Connectors** in the console, and select the **Releases** button for the connector you want to use.
2. Select the **Edit** button on release you want to use, and go to the **Methods** tab. 
3. Expand the category that you want to use, and select **Edit Category**.
4. Turn on the **Category Customisation Enabled** toggle and select an appropriate trigger from the **Object Lookup Trigger** dropdown.

    ![Object Lookup Trigger](./images/enhanced_objects_1.png)

</section>
<section class="card">

## Set up the connector method category

To use a custom object in connector method calls, such as in the method endpoint URL or the request body, you can use the system mergefield `CyclrObjectName`. Cyclr populates the `CyclrObjectName` mergefield with the name or value of the category.

1. Select the **Edit** button for the method you want to use, and make sure the **Method Type** is correct.
2. Add the`CyclrObjectName` mergefield to the **EndPoint** URL and select **Save**.

    ![Example EndPoint: {{instanceURL}}/services/data/{{ApiVersion}}/objects/{{CyclrObjectName}}/describe/.](./images/enhanced_objects_2.png)

If you select the **Request Format** tab, the **Default Value** column shows the `CyclrObjectName` mergefield. (column of which field???)

    ![Object Name Mergefield 2](./images/enhanced_objects_3.png)

3. To enable field auto-discovery, go to the **Request Format** tab and select a method from the **Custom Fields Lookup Method** dropdown. The field auto discovery method can use the `CyclrObjectName` system mergefield, but dynamic field discovery uses the copied category so that the auto discovery method to be called can be located in any category.

</section>
<section class="card">

## Copy a category

1. In the Cyclr console, go to **Templates** > **Template Connectors** and select **Edit** on the connector you want to use.
2. Find the category you enabled customization for, and select the **Copy this Category to create a Custom Object Category** button.
    > **Note**: The copy button is only available for categories with the [**Category Customisation Enabled**](#enable-category-customization) toggle on.
3. Select an **Object** from the dropdown or and enter a name for the custom object. Cyclr uses the **Object Name** you enter as name of the copied category.
4. If you want to use a different mergefield value to the **Object Name**, you can enter an **Object Value**. 
5. Select **Copy**.

    ![Copy Category Modal](./images/enhanced_objects_5.png)

To identify the copied categories, the category list displays the new category with a copy symbol. Categories that you create are sorted alphabetically below the original category. Copied categories have a **Delete** button, and if you don't select a pre-existing **Object**, the category also has an **Edit** button.

If you enabled [field auto-discovery](#set-up-the-connector-method-category), you can select a method from the copied category to invoke the field auto-discovery. You can also **Add Fields** or **Generate Fields** manually if you expand the method, and the fields remain associated with the copied category.

</section>
<section class="card">

## View copied categories in the template builder

In the template builder, under **Application Connectors** in the sidebar, Cyclr identifies your copied categories with a star icon. Methods from the copied categories function the same as normal methods.

    ![Category List](./images/enhanced_objects_8.png)


When you copy a category, you create an account connector category which references the original connector category. Cyclr links any steps or custom fields specify ???with this account connector category. The only change to use the copied category is that you need to include the additional id when you work with a method.

</section>
