---
title: Enhanced Objects
sidebar: cyclr_sidebar
permalink: enhanced-objects
tags: [connector-creation, enhanced, objects]
menus:
  custom-connector-creation:
    title: Enhanced Objects
    url: /enhanced-objects
---

To enable the copying of a category to be used for custom objects, please follow the steps below:

1. In connector management, find the connector you wish to edit, select the 'Methods' tab and find the category you wish to enable custom objects for. Click on the new **Edit Category** button and check the **Category Customisation Enabled** checkbox. This allows categories to be copied. To retrieve a collection of objects to offer the user, select an appropriate trigger from the **Object Lookup Trigger** dropdown.

    ![Object Lookup Trigger](./images/enhanced_objects_1.png)

2. It will often be necessary to use the object name or a value representing the object in connector method calls, for example in the method endpoint URL or the request body. To do so, simply use the new system mergefield **CyclrObjectName** as in the examples below. This new system mergefield gets populated with the name or value of the copied category.

    ![Object Name Mergefield](./images/enhanced_objects_2.png)
    ![Object Name Mergefield 2](./images/enhanced_objects_3.png)

3. To enable field auto-discovery, the existing functionality of specifying a **Custom Fields Lookup Method** should be used. The field auto discovery method to be called can use the **CyclrObjectName** system mergefield as above, however for dynamic field discovery, the name/value of the copied category is used, so the auto discovery method to be called can be located in any category.

    The connector Method Category is now setup. Below are the steps to copy a category in the builder.

4. In the builder, go to connector settings. Find the category that was edited in step 1, it should have a new toolbar with a **Copy** button. Click on the button and a **Copy Category** modal will open up. Depending on whether an object lookup trigger was specified in step 1 above, you will be offered a combination dropdown/text input or text inputs for the copied category name (this can also be considered the object name) and an optional category value. The value should be used if a different value to the category name should be used for the mergefield value or method calls. An example being your connector makes calls using an ObjectId = 999. Select an object from the dropdown or input a category name and copy the category.

    ![Copy Category Button](./images/enhanced_objects_4.png)
    ![Copy Category Modal](./images/enhanced_objects_5.png)

5. The category list should now display your new category whose name should be preceded by a copy/clone button for easy identification and it should be sorted alphabetically BELOW its origin category. It should also have its own toolbar with a **Delete** button and an **Edit** button if the object had not been selected by dropdown. Clicking on any of the copied methods should invoke field auto-discovery, assuming step 3 above was followed. Alternatively, custom fields can be added or generated manually as per usual and these fields will remain associated with this 'copied' category.

    ![Delete Button](./images/enhanced_objects_6.png)
    ![Adding Fields Manually](./images/enhanced_objects_7.png)

6. In the builder, under **Application Connectors**, your copied categories will be displayed with a star button at the very top of the category list within the connector, though this is purely for demonstration purposes at the moment. Methods can be dragged and dropped from the copied categories as usual. Assuming field auto-discovery was setup as in step 3 above, viewing step setup or mapping to a copied category method will invoke the field auto-discovery as per usual too.

    ![Category List](./images/enhanced_objects_8.png)
    ![Mapping](./images/enhanced_objects_9.png)

7. For all intents and purposes, the methods appear to have been copied. Under the hood, however, the category and methods have not been copied. Instead, an account connector category has been created which references the original connector category. Any steps or custom fields are linked with this account connector category. So everything behaves as normal barring the inclusion of the additional id when working with a method.
