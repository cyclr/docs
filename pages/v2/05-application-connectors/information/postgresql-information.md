---
title: PostgreSQL information
sidebar: cyclr_sidebar
permalink: postgresql-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Access a table

Cyclr uses custom object categories to allow the PostgreSQL connector to access multiple database tables with a single connector. To access a table within a database, you need to create a Custom object category.

You can identify custom object categories on the PostgreSQL connector settings page with the ![The custom object category icon.](./images/postgresql-custom-object.png)
 icon to the left of the method category.

### Add a custom object category

From the PostgreSQL connector settings page:

1.  Under the **Methods & Fields** heading, select **Rows**.
2.  Select the ![The copy icon.](./images/postgresql-custom-object-copy.png)
 **Copy this Category to create a Custom object category** button.
3.  Select the **Select Object** dropdown.
4.  Select the schema and table name to access.
5.  Select **Copy**.

This adds a new method category with the schema and table name you select in step 4. The methods inside the method category target the same schema and table name.

### Remove a custom object category

From the PostgreSQL connector settings page:

1.  Under the **Methods & Fields** heading, select the custom object category you want to remove.
2.  Select the ![The bin icon.](./images/postgresql-custom-object-remove.png)
 **Delete this Custom object category** button.
3.  Select **Confirm**.

> **Note**: You cannot delete custom object categories if you are using methods from within them in cycles.

</section>

<section class="card">

## Select a custom object category primary key

You need to set a primary key when you use a custom object category method that selects a record based on the primary key. Cyclr supports composite primary keys.

The following methods requires you to set a primary key before a request can be sent:

- Delete Table Row
- Get Table Row
- Update Table Row
- Upsert Table Row

In the cycle builder, from the **Step setup** of a Custom object category method:

1. Select the **Ignore** dropdown.
2. Select **Lookup**.
3. Select **Select...**.
4. Select the primary key.

</section>

<section class="card">
 
## Use functions and procedures

Functions should be used when data is returned from the API. Procedures should be used no data is returned from the API. Manually calling functions or procedures requires the full function or procedure name along with any parameters to be entered.

Use these methods to execute PostgreSQL functions and procedures, both built in and user-created, in Cyclr:

- [Functions > Call Function](#call-function)
- [Functions > Call Function Manually](#call-function-manually)
- [Procedures > Call Procedure](#call-procedure)
- [Procedures > Call Procedure Manually](#call-procedure-manually)

PostgreSQL have documentation on [creating functions](https://www.postgresql.org/docs/current/sql-createfunction.html) and [creating procedures](https://www.postgresql.org/docs/current/sql-createprocedure.html).

### Find a function or procedure and its parameters

From the PostgreSQL **Connector Setup** page:

1. Under the **Methods and Fields** heading, expand the **Functions** or **Procedures** method category.
2. Select the **List Functions** or **List Procedures** method.
3. Select **Test**.
4. Enter any filter parameters and select **Run**.

The **Function Name** or **Procedure Name** is required to call the function or procedure. The **Arguments** (parameters) listed are required to map custom request fields.

### Functions

#### Call Function

The **Call Function** method uses a **Function Name** and optional **Parameters** to make a request. All functions are requested as the following:

```
SELECT * FROM <Function Name>(<Parameters>)
```

To call a function:

1. [Find a function and obtain any parameter information](#find-a-function-or-procedure-and-its-parameters).
2. [Add the parameters of the function as custom request fields](#function-or-procedure-parameters-to-custom-request-field). Optional, only if parameters are present.
3. [Add the response object fields as custom response fields](#response-object-field-as-a-custom-response-field).
4. [Setup the Call Function method](#call-function-or-call-procedure).

#### Call Function Manually

The **Call Function Manually** method uses a **Function** to make a request, this includes the full function name and optional parameters. All manual functions are requested as the following:

```
SELECT * FROM <Function>
```

To call a function manually:

1. [Find a function and obtain any parameter information](#find-a-function-or-procedure-and-its-parameters).
2. [Add the parameters of the function as custom request fields](#function-or-procedure-parameters-to-custom-request-field). Optional, only if parameters are present.
3. [Add the response object fields as custom response fields](#response-object-field-as-a-custom-response-field).
4. [Setup the Call Function Manually method](#call-function-manually-or-call-procedure-manually).

### Procedures

#### Call Procedure

The **Call Procedure** method uses a **Procedure Name** and optional **Parameters** to make a request. All procedures are requested as the following:

```
CALL <Procedure Name>(<Parameters>)
```

To call a procedure:

1. [Find a procedure and obtain any parameter information](#find-a-function-or-procedure-and-its-parameters).
2. [Add the parameters of the procedure as custom request fields](#function-or-procedure-parameters-to-custom-request-field). Optional, only if parameters are present.
3. [Setup the Call Procedure method](##call-function-or-call-procedure).

#### Call Procedure Manually

The **Call Procedure Manually** method uses a **Procedure** to make a request, this includes the full procedure name and optional parameters. All manual procedures are requested as the following:

```
SELECT * FROM <Procedure>
```

To call a procedure manually:

1. [Find a procedure and obtain any parameter information](#find-a-function-or-procedure-and-its-parameters).
2. [Add the parameters of the procedure as custom request fields](#function-or-procedure-parameters-to-custom-request-field). Optional, only if parameters are present.
3. [Setup the Call Procedure Manually method](#call-function-manually-or-call-procedure-manually).

### Add custom fields

#### Function or procedure parameters to custom request field

Add a function or procedure parameter as a custom request field to ensure the function or procedure in the request has the correct format. From the PostgreSQL **Connector Setup** page:

1. Under the **Methods and Fields** heading, expand the **Functions** or **Procedures** method category.

2. Select the **Call Function** or **Call Procedure** method.

3. Under the **Request Fields** heading, select the **+** to add a custom request field. Do this for every parameter listed in the previous step:

   | Field              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | The location of the field in the request. This should have the format `parameters.<Parameter Name>`. For example, if the parameter is `inputid` then enter `parameters.inputid`. |
   | **Display Name**   | The display name of the field in the Cyclr UI.               |
   | **Description**    | The description of the field in the Cyclr UI.                |
   | **Data Type**      | The data type of the parameter. This should match as closely as possible the data type of the parameter in PostgreSQL. For example, if the parameter data type is `varchar` then select `Text`. |

4. Select **Create**.

#### Response object field as a custom response field

Add a response object field as a custom response field to allow it to be mapped in a cycle. From the PostgreSQL **Connector Setup** page:

1. Under the **Methods and Fields** heading, expand the **Functions** method category.

2. Select the **Call Function** method.

3. Under the **Response Fields** heading, select the **+** to add a custom response field. If you have the response object already, select **Generate Fields** to generate custom response fields from it. Do this for every field in the response that needs to be mapped in a cycle:

   | Field              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | The location of the field in the response. Use object keys, separated by `.` for nested objects, as the field location. Use square brackets to indicate arrays in the response object and use `[].` if the response object itself is an array. |
   | **Display Name**   | The display name of the field in the Cyclr UI.               |
   | **Description**    | The description of the field in the Cyclr UI.                |
   | **Data Type**      | The data type of the field. This should match as closely as possible the data type of the response field in PostgreSQL. For example, if the parameter data type is `varchar` then select `Text`. |

4. Select **Create**.

### Setup methods

#### Call Function or Call Procedure

The Call Function and Call Procedure methods are setup in the same way. From the cycle builder:

1. Drag the **Call Function** or **Call Procedure** method into the cycle builder.
2. Select **Setup step**.
3. Select **Select...** for the **Function Name** or **Procedure Name** field.
4. Select **Lookup**.
5. Select the empty dropdown box under the **Selected Value** heading.
6. Select the function or procedure to call in the list by navigating the list or using the search feature.
7. Map any additional function or procedure parameters that were added as custom request fields.
8. Select **Close**. 

#### Call Function Manually or Call Procedure Manually

The Call Function Manually and Call Procedure Manually methods are setup in the same way. From the cycle builder:

1. Drag the **Call Function Manually** or **Call Procedure Manually** method into the cycle builder.
2. Select **Setup step**.
3. Select **Select...** for the **Function** or **Procedure** field.
4. Select **Type a Value**.
5. Enter the function name and any parameters into the field. For example if the function or procedure is named **getuserbyid** and has an **inputid** parameter with a value of `6`, enter `getuserbyid(6)`. Mergefields from previous mapped steps can be used here.
6. Select **Close**. 

</section>
