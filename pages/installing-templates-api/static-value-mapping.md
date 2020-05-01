---
title: Static Value Field Mapping
sidebar: cyclr_sidebar
permalink: static-value-mapping
tags: [installing]
---

_**A static value can be set as the field mapping, a static value is a value that will never change.**_

This value should be obtained from your user, or automatically assigned by your application, then provided to Cyclr like below:

Request:

````http
    POST /v1.0/steps/{Step ID}/fieldmappings/{Field ID}
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000 
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000

    {
      "MappingType": "StaticValue",
      "Value": "MyStaticValue"
    }
````

Response:

````json
    {
      "Field": {
        "Id": 283792,
        "Name": "Email",
        "Description": null,
        "IsOptional": false,
        "DataType": undefined,
        "TriggerName": null,
        "Values": [],
        "DisplayOrder": 1,
        "Triggers": []
      },
      "MappingType": "StaticValue",
      "SourceFieldId": null,
      "SourceStepId": null,
      "TriggerValue": null,
      "TriggerValueDisplayName": null,
      "Value": "MyStaticValue"
    }
````

[Field Mapping with Step Data](./field-mapping-with-step-data)  
[Value List Mapping](./value-list-mapping)  
[Cycle Activation](./cycle-activation)