---
title: Connector Parameters
sidebar: cyclr_sidebar
permalink: connector-parameters
tags: [connector-creation]
---

## Purpose

Parameters are used to define a range of HTTP fields, e.g. HTTP headers, mergefields, query string parameters, etc.

You can define parameters at the connector level or method level. If a parameter is defined at the connector level, it will be global for all methods in the connector.


## Parameter Definition

| Property | Description | Recommended Standards |
| --- | --- | --- |
| TargetType | HttpHeader,  MergeField, QueryString, FilterField, ResponseField, Script, Index | | 
| TargetName | The name for the parameter.| |
| DisplayName | Display name for the parameter.| |
| Description | Description for the parameter.| |
| TriggerName | Trigger name for the parameter. If you want to dynamically show a list of parameter values for the user to choose from, set `TriggerName` as the trigger you want Cyclr to call. Please see the _Triggers_ section for details.| |
| IsOptional | Set the parameter to be optional or required. The default is required (false).| |
| Hide | Hide the parameter from the user interface. You can use this to hide internal parameters you want to send to the endpoint.| |

## Types of Parameter

### HttpHeader

This will be added to the HTTP header.

### MergeField

The vaue of the parameter will be merged into the HTTP call.  For example, parameters can be merged into URL endpoint to allow for a specific object to be requested.  The merge field is identifed by the double opening and closing curly braces.

"Endpoint": "https://ApplicationName/API/V2/customers/&#x7B;&#x7B;CustomerNo&#x7D;&#x7D;"

'CustomerNo is then specified as a Mergefield Parameter (without the braces) and the value provided will be merged into the URL.  The specification would look like this:

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hiden | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MergeField| CustomerNo | Customer Number | Provide a customer number. | Optional | false | false | NA |

### QueryString

This parameters allows you to add values into the Query String of the HTTP request.  It can, for example. allow for optional filtering criteria to be added to the call.  For example, if filtering was required for a specific customer on the 'list orders method.

"Endpoint": "https://ApplicationName/API/V2/orders"

The specification would look like this:

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hiden | Value |
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

