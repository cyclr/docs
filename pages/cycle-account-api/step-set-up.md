---
title: Step Setup
sidebar: cyclr_sidebar
permalink: step-set-up
tags: [installing]
---

_**Templates in Cyclr may include steps that require mapping or parameter values that are specific to your end user’s use of those templates.**_

If the Cycle prerequisites method returned Steps that required mapping, you need to loop through them to determine what is required.

Request:

````http
    GET /steps/{Step ID}/prerequisites
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

Response:

````json
    [{
            "ReasonCode": 40,
            "Reason": "Missing parameter mapping",
            "ObjectType": "Parameter",
            "ObjectId": 16017
        },
        {
            "ReasonCode": 41,
            "Reason": "Missing field mapping",
            "ObjectType": "ConnectorFieldMapping",
            "ObjectId": 283792
        },
        {
            "ReasonCode": 41,
            "Reason": "Missing field mapping",
            "ObjectType": "ConnectorFieldMapping",
            "ObjectId": 283793
        },
        {
            "ReasonCode": 41,
            "Reason": "Missing field mapping",
            "ObjectType": "ConnectorFieldMapping",
            "ObjectId": 283794
        },
        {
            "ReasonCode": 41,
            "Reason": "Missing field mapping",
            "ObjectType": "ConnectorFieldMapping",
            "ObjectId": 283795
        },
        {
            "ReasonCode": 41,
            "Reason": "Missing field mapping",
            "ObjectType": "ConnectorFieldMapping",
            "ObjectId": 283796
        }
    ]
````

[How to Set Step Parameters](./set-step-parameters)
