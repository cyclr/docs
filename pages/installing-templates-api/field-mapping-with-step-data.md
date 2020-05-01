---
title: Field Mapping with Step Data
sidebar: cyclr_sidebar
permalink: field-mapping-with-step-data
tags: [installing]
---

**_A Step Data mapping uses a value from a previous step response as the value for this steps request._**

Cyclr provides an endpoint to discover valid field mapping options for a given step.

Request:

````http
    GET /v1.0/steps/{Step ID}/fieldsformapping
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

Response:

````json
    [{
            "Id": 283797,
            "Name": "Member ID",
            "Description": null,
            "IsOptional": false,
            "DataType": "Undefined",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283798,
            "Name": "Email",
            "Description": null,
            "IsOptional": false,
            "DataType": "Undefined",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283799,
            "Name": "Status",
            "Description": null,
            "IsOptional": false,
            "DataType": "Undefined",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283800,
            "Name": "Average Open Rate",
            "Description": null,
            "IsOptional": false,
            "DataType": "Undefined",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283801,
            "Name": "Average Click Rate",
            "Description": null,
            "IsOptional": false,
            "DataType": "Undefined",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283802,
            "Name": "Member Rating",
            "Description": null,
            "IsOptional": false,
            "DataType": "Undefined",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283803,
            "Name": "Language",
            "Description": null,
            "IsOptional": false,
            "DataType": "Undefined",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283804,
            "Name": "Unique Email ID",
            "Description": null,
            "IsOptional": false,
            "DataType": "Text",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283805,
            "Name": "Email Type",
            "Description": null,
            "IsOptional": false,
            "DataType": "Text",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283806,
            "Name": "IP Signup Address",
            "Description": null,
            "IsOptional": false,
            "DataType": "Text",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283807,
            "Name": "Signup Timestamp",
            "Description": null,
            "IsOptional": false,
            "DataType": "DateTime",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283808,
            "Name": "Opt-In Timestamp",
            "Description": null,
            "IsOptional": false,
            "DataType": "DateTime",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283809,
            "Name": "List ID",
            "Description": null,
            "IsOptional": false,
            "DataType": "Text",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        },
        {
            "Id": 283810,
            "Name": "Opt-In IP",
            "Description": null,
            "IsOptional": false,
            "DataType": "Text",
            "TriggerName": null,
            "Values": null,
            "DisplayOrder": 0,
            "Triggers": []
        }
    ]
````

[Value List Mapping](./value-list-mapping)  
[Static Value Mapping](./static-value-mapping)  
[Cycle Activation](./cycle-activation)