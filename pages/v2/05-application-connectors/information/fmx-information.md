---
title: FMX information
sidebar: cyclr_sidebar
permalink: fmx-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Schedule Requests (Module) custom objects

Cyclr uses custom objects to dynamically create **Schedule Requests** method categories based on an FMX module. To create a `Schedule Requests (Module)` custom object:

1. [Get the **Schedule Request** module](#get-schedule-request-module).
2. [Create the Schedule Requests (Module) custom object](#create-schedule-requests-module-custom-object).
3. If necessary, [rename the Schedule Requests (Module) custom object](#rename-custom-object).

<a name="get-schedule-request-module"></a>

### Get Schedule Request module

To find the **Schedule Request** module name, from your FMX dashboard:

1. In the left side menu, find the **Schedule Request** module you want to use as a custom object.
2. Get the URL for the **Schedule Request** module. The URL format is `https://{FmxSubdomain}.gofmx.com/{ModuleName}/requests`.
3. Get the **Schedule Request** `{ModuleName}` from the URL. For example, if the URL is `https://cyclrtesting.gofmx.com/scheduling/requests`, then module name is `scheduling`.

<a name="create-schedule-requests-module-custom-object"></a>

### Create the Schedule Requests (Module) custom object

To create a **Schedule Request (Module)** custom object, from the FMX connector **Settings** page in Cyclr:

1. Under the **Methods & Fields** heading, select **Schedule Requests (Module)**.
2. Select the pink **Copy this Category to create a Custom Object Category** icon.
3. In the **Specify object name** field, enter the **Schedule Request** module name.
4. Select **Copy**.

</section>
<section class="card">
## Work Requests (Custom Object) custom objects

Cyclr uses custom objects to dynamically create **Work Request** method categories based on an FMX module and a **Work Request** type ID. To create a `Work Request (Custom Object)` custom object:

1. [Get the **Work Request** module name](#get-work-request-module-custom-object).
2. [Get the **Work Request type ID**](#get-work-request-type-id-custom-object).
3. [Create the **Work Requests (Custom Object)** custom object](#create-work-requests-custom-object-custom-object).
4. If necessary, [rename the Work Requests (Custom Object) custom object](#rename-custom-object).

<a name="get-work-request-module-custom-object"></a>

### Get the Work Request module

To find the **Work Request** module name, from your FMX dashboard:

1. In the left side menu, find the **Work Request** module you want to use as a custom object.
2. Get the URL for the **Work Request** module. Th URL format is: `https://{FmxSubdomain}.gofmx.com/{ModuleName}-requests`.
3. Get the **Work Request** {ModuleName} from the URL. For example, the **Maintenance Requests** module URL is `https://cyclrtesting.gofmx.com/maintenance-requests`, so the module name is `maintenance`.

<a name="get-work-request-type-id-custom-object"></a>

### Get the Work Request Type ID

To find the **Work Request Type ID**, from the FMX connector **Settings** page in Cyclr:

1. Under the **Methods & Fields** heading, select **Utilities**.
2. Select **List Work Request Type IDs**.
3. Select **Run**.
4. Enter the work request module name.
5. Get the **Work Request Type ID** from the return value of the **Request Type ID** field.

<a name="create-work-requests-custom-object-custom-object"></a>

### Create the Work Requests (Custom Object) custom object

To create the `Work Requests (Custom Object)` custom object, from the FMX connector settings page in Cyclr:

1. Under the **Methods & Fields** heading, select **Work Requests (Custom Object)**.
2. Select the pink **Copy this Category to create a Custom Object Category** icon.
3. In the **Specify object name** field, enter `{ModuleName}.{WorkRequestTypeId}`. For example, for the `maintenance` module with **Work Request Type ID** `363065`, enter `maintenance.363065`.
4. Select **Copy**.

</section>
<section class="card">

## Work Requests (Module) custom object

Cyclr uses custom objects to dynamically create **Work Request** method categories based on an FMX Module. To create a `Work Requests (Module)` custom object you need a Work Request Module.

1. [Get a Work Request Module](#get-work-request-module-module).
2. [Create a Work Requests (Module) custom object](#create-work-requests-module-custom-object).
3. If necessary, [rename](#rename-custom-object) the **Work Requests (Module)** custom object.

<a name="get-work-request-module-module"></a>

### Get Work Request module

To find a **Work Request** module, from your FMX dashboard:

1. In the left side menu, find the **Work Request** module you want to use as a custom object.
2. Get the URL for the **Work Request** module. Th URL format is: `https://{FmxSubdomain}.gofmx.com/{ModuleName}-requests`.
3. Get the **Work Request** {ModuleName} from the URL. For example, the **Maintenance Requests** module URL is `https://cyclrtesting.gofmx.com/maintenance-requests`, so the module name is `maintenance`.

<a name="create-work-requests-module-custom-object"></a>

### Create the Work Requests (Module) custom object

To create the `Work Request (Module)` custom object, from the FMX connector settings page in Cyclr:

1. Under the **Methods & Fields** heading, select **Work Requests (Module)**.
2. Select the pink **Copy this Category to create a Custom Object Category** icon.
3. In the **Specify object name** field, enter the **Work Request** module name.
4. Select **Copy**.

<a name="rename-custom-object"></a>

</section>
<section class="card">
## Rename custom objects

To rename a custom object, from the FMX connector **Settings** page in Cyclr:

1. Under the **Methods & Fields** heading, select the custom object method category to rename.
2. Select the pink **Edit this Custom Object Category** icon.
3. Enter the value in the **Object Name** field into the **Object Value** field.
4. Update the **Object Name** field.
5. Select **Save**.

</section>
<section class="card">
## Manually map custom fields

These method categories require you to manually map custom fields to use them:

*  Schedule Requests
*  Schedule Requests (Module)
*  Work Requests
*  Work Requests (Module)

### Map the custom fields

You can map request custom fields for create or update methods, or response custom fields for get or list methods.

To map the fields, go to the FMX connector **Settings** page in Cyclr:

1. Under the **Methods & Fields** heading, select the method category and then the method you want to map a request field for.
2. Under the **Request Fields** or **Response fields** heading, select the pink **+** icon.
3. Enter the fields below:
   | **Field**              | **Description**                                                  |
   | :----------------- | :----------------------------------------------------------- |
   | **Field Location** | The field location of the custom field. If the field is a single value, use the format `customField.value.{CustomFieldId}`. If the field can contain multiple values, use the format `customField.values.[{customFieldId}]`. |
   | **Display Name**   | **Optional**: the Cyclr UI display name of the custom field.     |
   | **Description**    | **Optional**: the Cyclr UI description of the custom field.     |
   | **Data Type**      | The data type of the custom field. Make sure this value matches the data type of the custom field within FMX. |
4. Select **Create**. 

</section>
