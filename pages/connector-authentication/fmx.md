---
title: FMX Authentication
sidebar: cyclr_sidebar
permalink: fmx-connector
tags: [connector]
---

## FMX setup

To setup the FMX connector in Cyclr, you need:

1. Your [**FMX Subdomain**](#get-fmx-subdomain).
2. Your FMX account **Username** and **Password**.

Contact your FMX account manager if you do not have the above.

<a name="get-fmx-subdomain"></a>

### Get FMX subdomain

Your FMX accounts exist under your FMX subdomain. Your FMX subdomain is contained within the URL you use to access FMX. For example, if your FMX URL is `https://cyclrtesting.gofmx.com`, then your FMX subdomain is `cyclrtesting`.

## Cyclr account setup

Cyclr asks you for the below value when you install the FMX connector into an account:

| Value             | Description                                    |
| :---------------- | :--------------------------------------------- |
| **FMX Subdomain** | The subdomain used to access your FMX account. |
| **Username**      | The username of your FMX account.              |
| **Password**      | The password of your FMX account.              |

## Additional information

### Create Schedule Requests (Module) custom object

Cyclr uses custom objects to dynamically create Schedule Requests method categories based on an FMX Module. To create a `Schedule Requests (Module)` custom object:

1. [Get a Schedule Request Module](#get-schedule-request-module).
2. [Create a Schedule Requests (Module) custom object](#create-schedule-requests-module-custom-object).
3. If required, [rename the Schedule Requests (Module) custom object](#rename-custom-object).

<a name="get-schedule-request-module"></a>

#### Get Schedule Request Module

To find a Schedule Request Module, from your FMX dashboard:

1. In the left-hand menu, find the Schedule Request Module you wish to use as a custom object.
2. Get the URL for this Schedule Request Module. This has the format `https://{{FmxSubdomain}}.gofmx.com/{{Module}}/requests`. For example, for the **Schedule Requests** Module, the URL is `https://cyclrtesting.gofmx.com/scheduling/requests`.
3. Get the Schedule Request Module from the URL for the Schedule Request Module. For example, the **Schedule Requests** Module is `scheduling`.

<a name="create-schedule-requests-module-custom-object"></a>

#### Create Schedule Requests (Module) custom object

To create a Schedule Request (Module) custom object, from the FMX connector settings page:

1. Under the **Methods & Fields** heading, select **Schedule Requests (Module)**.
2. Select the pink **Copy this Category to create a Custom Object Category** icon.
3. In the **Specify object name** field, enter the Schedule Request Module.
4. Select **Copy**.

### Create Work Requests (Custom Object) custom objects

Cyclr uses custom objects to dynamically create Work Request method categories based on an FMX Module and Work Request Type ID. To create a `Work Request (Custom Object)` custom object:

1. [Get a Work Request Module](#get-work-request-module-custom-object).
2. [Get a Work Request Type ID](#get-work-request-type-id-custom-object).
3. [Create a Work Requests (Custom Object) custom object](#create-work-requests-custom-object-custom-object).
4. If required, [rename the Work Requests (Custom Object) custom object](#rename-custom-object).

<a name="get-work-request-module-custom-object"></a>

#### Get Work Request Module

To find a Work Request Module, from your FMX dashboard:

1. In the left-hand menu, find the Work Request Module you wish to use as a custom object.
2. Get the URL for this Work Request Module. This has the format `https://{{FmxSubdomain}}.gofmx.com/{{Module}}-requests`. For example, for the **Maintenance Requests** Module, the URL is `https://cyclrtesting.gofmx.com/maintenance-requests`.
3. Get the Work Request Module. For example, the **Maintenance Requests** Module is `maintenance`.

<a name="get-work-request-type-id-custom-object"></a>

#### Get Work Request Type ID

To find a Work Request Type ID, from the FMX connector **Settings** page:

1. Under the **Methods & Fields** heading, select **Utilities**.
2. Select **List Work Request Type IDs**.
3. Select **Run**.
4. Enter the **Module**.
5. Get the Work Request Type ID from the **Return Value** of the Request Type ID field.

<a name="create-work-requests-custom-object-custom-object"></a>

#### Create Work Requests (Custom Object) custom object

To create a Work Request (Custom Object) custom object, from the FMX connector settings page:

1. Under the **Methods & Fields** heading, select **Work Requests (Module)**.
2. Select the pink **Copy this Category to create a Custom Object Category** icon.
3. In the **Specify object name** field, enter the Work Request Module, followed by a dot, followed by the Work Request Type ID. For example, for the `maintenance` module with Work Request Type ID `363065` enter `maintenance.363065`.
4. Select **Copy**.

### Create Work Requests (Module) custom object

Cyclr uses custom objects to dynamically create Work Request method categories based on an FMX Module. To create a `Work Requests (Module)` custom object you need a Work Request Module.

1. [Get a Work Request Module](#get-work-request-module-module).
2. [Create a Work Requests (Module) custom object](#create-work-requests-module-custom-object).
3. If required, [rename the Work Requests (Module) custom object](#rename-custom-object).

<a name="get-work-request-module-module"></a>

#### Get Work Request Module

To find a Work Request Module, from your FMX dashboard:

1. In the left-hand menu, find the Work Request Module you wish to use as a custom object.
2. Get the URL for this Work Request Module. This has the format `https://{{FmxSubdomain}}.gofmx.com/{{Module}}-requests`. For example, for the **Maintenance Requests** Module, the URL is `https://cyclrtesting.gofmx.com/maintenance-requests`.
3. Get the Work Request Module. For example, the **Maintenance Requests** Module is `maintenance`.

<a name="create-work-requests-module-custom-object"></a>

#### Create Work Requests (Module) custom object

To create a Work Request (Module) custom object, from the FMX connector settings page:

1. Under the **Methods & Fields** heading, select **Work Requests (Module)**.
2. Select the pink **Copy this Category to create a Custom Object Category** icon.
3. In the **Specify object name** field, enter the Work Request Module.
4. Select **Copy**.

<a name="rename-custom-object"></a>

### Rename custom object

To rename a custom object, from the FMX connector **Settings** page:

1. Under the **Methods & Fields** heading, select the custom object method category to rename.
2. Select the pink **Edit this Custom Object Category** icon.
3. Move the **Object Name** field to the **Object Value** field.
4. Update the **Object Name**.
5. Select **Save**.

### Manually map custom field

These method categories require custom fields to be manually mapped to be used:

- Schedule Requests
- Schedule Requests (Module)
- Work Requests
- Work Requests (Module)

#### Map request field

To map a request custom field for create or update methods, from the FMX connector **Settings** page:

1. Under the **Methods & Fields** heading, select the method category and then the method to map a request field for.
2. Under the **Request Fields** heading, select the pink **+** icon.
3. Enter the fields:
   | Field              | Description                                                  |
   | :----------------- | :----------------------------------------------------------- |
   | **Field Location** | The field location of the custom field. If the field is a single value, use the format `customField.value.{CustomFieldId}`. If the field can contain multiple values, use the format `customField.values.[{customFieldId}]`. For example, if the custom field ID is `692454` and has a single value, enter `customField.value.692454`, or has multiple values enter `customField.values.[692454]`. |
   | **Display Name**   | The Cyclr UI display name of the custom field. Optional.     |
   | **Description**    | The Cyclr UI description of  the custom field. Optional.     |
   | **Data Type**      | The data type of the custom field. This should match the data type of the custom field within FMX. |
4. Select **Create**. 

#### Map response field

To map a response custom field for get or list methods, from the FMX connector **Settings** page:

1. Under the **Methods & Fields** heading, select the method category and then the method to map a response field for.
2. Under the **Response Fields** heading, select the pink **+** icon.
3. Enter the fields:
   | Field              | Description                                                  |
   | :----------------- | :----------------------------------------------------------- |
   | **Field Location** | The field location of the custom field. If the field is a single value, use the format `[].customFields.{CustomFieldId}`. If the field can contain multiple values, use the format `[].customFields.[]{CustomFieldId}]`. For example, if the custom field ID is `692454` and has a single value, enter `[].customField.692454`, or has multiple values enter [].`customField.[692454]`. |
   | **Display Name**   | The Cyclr UI display name of the custom field. Optional.     |
   | **Description**    | The Cyclr UI description of  the custom field. Optional.     |
   | **Data Type**      | The data type of the custom field. This should match the data type of the custom field within FMX. |
4. Select **Create**.
