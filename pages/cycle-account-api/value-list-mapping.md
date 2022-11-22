---
title: Value List Mapping
sidebar: cyclr_sidebar
permalink: value-list-mapping
tags: [installing]
---

**_Fields within a step may contain a set of pre-defined values that can be selected from, returned in the “Values” array below:_**

Request:

````http
    GET /v1.0/steps/{Step ID}/fieldmappings/{Field ID}
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

Response:

````json
    {
      "Field": {
        "Id": 283792,
        "Name": "Email",
        "Description": null,
        "IsOptional": false,
        "DataType": "Undefined",
        "TriggerName": null,
        "Values": [
          "List Option 1",
          "List Option 2",
          "List Option 3"
        ],
        "DisplayOrder": 1,
        "Triggers": []
      },
      "MappingType": "Ignore",
      "SourceFieldId": null,
      "SourceStepId": null,
      "TriggerValue": null,
      "TriggerValueDisplayName": null,
      "Value": null
    }
````

For these steps, the list of valid values should be presented to your user for them to make a selection. Their selection should then be used to update the field value:

````http
    POST /v1.0/steps/{Step ID}/fieldmappings/{Field ID} 
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000

    {
    "MappingType": "ValueList",
    "Value": "List Option 1"
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
      "MappingType": "ValueList",
      "SourceFieldId": null,
      "SourceStepId": null,
      "TriggerValue": null,
      "TriggerValueDisplayName": null,
      "Value": "List Option 1" 
    }
````

[Static Value Field Mapping](./static-value-mapping)  
[Field Mapping with Step Data](./field-mapping-with-step-data)  
[Cycle Activation](./cycle-activation)