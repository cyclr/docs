---
title: Connector Parameters
sidebar: cyclr_sidebar
permalink: connector-parameters
tags: [connector-creation]
menus:
  custom-connector-creation:
    title: Connector Parameters
    url: /connector-parameters
---

## Purpose

Parameters can be used to define a number of different properties to be used in an HTTP Request or Response, e.g. HTTP headers, mergefields and querystring values.

You can define Parameters at the Connector level or Method level.

If a Parameter is defined at the Connector level, it will be available to all the Methods.


## Parameter Definition

| Property | Description |
| --- | --- |
| TargetType | HttpHeader,  MergeField, QueryString, FilterField, ResponseField, Script, Index |
| TargetName | The name for the parameter.|
| DisplayName | Display name for the parameter.|
| Description | Description for the parameter.|
| Trigger | Trigger name for the parameter. If you want to dynamically show a list of parameter values for the user to choose from, set `TriggerName` as the trigger you want Cyclr to call. Please see the _Triggers_ section for details.|
| Hidden | Hide the parameter from the user interface. You can use this to hide internal parameters you want to send to an endpoint.|
| Optional | Set the parameter to be optional or required. The default is required (false).|


Connector level Parameters have these additional properties:

| Property | Description |
| --- | --- |
| Sensitive | The Parameter is treated as a password by masking the value in the interface. Use for sensitive values. |
| Account Connector Property | The Parameter is shown to the user when installing or setting up the Connector. |
| Partner Connector Property | The Parameter is available in the Cyclr Console's Application Connector Library entry, allowing it to be set once for use across all Account Connectors. |
| Multiline | The Parameter is displayed as a textbox allowing multiple lines to be entered, rather than a single line textbox. |

> **Warning**: A parameter cannot be both an Account Connector Property and a Partner Connector Property.  If both are selected, your connector may behave unpredictably.



## Types of Parameter

### HttpHeader

This will be added to the HTTP header.

### MergeField

The value of the Parameter will be merged into the HTTP call.  For example, Parameters can be merged into a URL endpoint to allow for a specific object to be requested.  The merge field is identifed by the double opening and closing curly braces.

"Endpoint": "https://ApplicationName/API/V2/customers/&#x7B;&#x7B;CustomerNo&#x7D;&#x7D;"

'CustomerNo is then specified as a Mergefield Parameter (without the braces) and the value provided will be merged into the URL.  The specification would look like this:

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hidden | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MergeField| CustomerNo | Customer Number | Provide a customer number. | Optional | false | false | NA |

### QueryString

This Parameter allows you to add values into the QueryString of the HTTP request.  It can allow for optional filtering criteria to be added to the call.  For example, if filtering was required for a specific customer on a 'List Orders' Method.

"Endpoint": "https://ApplicationName/API/V2/orders"

The specification would look like this:

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hidden | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QueryString| Customer | Customer Number | Provide a customer number. | Optional | false | false | NA |

The resulting call would look like this:

"Endpoint": "https://ApplicationName/API/V2/orders?Customer=8394995

### FilterField

Cyclr filter field (can set a date field as FilterField to filter new objects) 

### ResponseField

Response field

### Script

### Index

