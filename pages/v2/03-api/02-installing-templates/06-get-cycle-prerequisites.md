---
title: Get Cycle Prerequisites
sidebar: cyclr_sidebar
permalink: get-cycle-prerequisites
tags: [installing]
menus:
  installing-templates:
    title: Get Cycle Prerequisites
    url: /get-cycle-prerequisites
    weight: 6
---

**_A Cycle installed in an Account from a Template may have prerequisites that need to be fulfilled before the Cycle can be activated._**

The Cyclr API can provide information on the prerequisites for a Cycle to run.

Request:

````http
    GET /v1.0/cycles/{Cycle Id}/prerequisites
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

Response

````json
    [{
        "ReasonCode": 20,
        "Reason": "Unauthenticated connector",
        "ObjectType": "AccountConnector",
        "ObjectId": 36328
    },
    {
        "ReasonCode": 20,
        "Reason": "Unauthenticated connector",
        "ObjectType": "AccountConnector",
        "ObjectId": 36329
    },
    {
        "ReasonCode": 30,
        "Reason": "Missing mapping",
        "ObjectType": "Action",
        "ObjectId": "709b68ba-394e-4339-9550-abd0312e8dd5"
    }]
````

In this example, there are the following pre-requisites:

*   Two Connectors that are unauthenticated
*   A Step with a missing field mapping

<hr>

## Full list of potential prerequisites

| ReasonCode | Reason |
| ---------- | ------ |
|0|Unknown|
|10|Cycle must have at least two steps|
|11|All steps must be connected together and only one step can be the trigger|
|20|Unauthenticated connector|
|30|Missing mapping|
|31|Missing decision criteria|
|32|Missing delay time period|
|33|Missing date to wait until|
|40|Missing parameter mapping|
|41|Missing field mapping|
|42|Missing collection key mapping|
|43|Missing webhook key mapping|
|50|Missing left operand|
|51|Missing right operand|
|60| Missing delay unit|
|61| Missing delay interval|
|70| Missing wait until date|

[How to Authenticate Account Connector](./authenticate-account-connector)
