---
title: Map fields
sidebar: cyclr_sidebar
permalink: set-step-field-mapping
tags: [installing]
menus:
    api-step-setup:
        title: Map fields
        identifier: set-step-field-mapping
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
_**Field Mappings are passed to the third party API as the request body.**_

For each Missing field mapping returned in the Step prerequisites request in step 7:

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
            "Values": [],
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

The IsOptional property indicates if a field mapping is optional or required before the Cycle can run.

There are multiple ways of setting a Field Mapping value.

[Static Value Field Mapping](./static-value-mapping)  
[Field Mapping with Step Data](./field-mapping-with-step-data)  
[Value List Mapping](./value-list-mapping)
</section>
