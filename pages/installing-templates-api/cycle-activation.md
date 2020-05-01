---
title: Cycle Activation
sidebar: cyclr_sidebar
permalink: cycle-activation
tags: [installing]
---

_**When a cycle is installed in an account they are in a Paused state and must be activated to before any step requests will be processed.**_

When a Cycle has been installed and all of it’s prerequisites have been provided, the cycle can be activated like below:

Request:

````http
    POST /v1.0/cycles/{Cycle ID}/activate
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000

    {
        "StartTime": "2018-01-01T00:00:00Z",
        "Interval": 360,
        "RunOnce": false
    }
````

| Parameter | Description |
| --- | --- |
| **Interval** | The frequency that the Cycle should run at, ignored if first step is webhook |
| **StartTime** | Optional, the time for the Cycle to start (UTC) |
| **RunOnce** | Optional, set to true for the Cycle to auto paused after the first run |

Response:

```http
    200 OK
```

The Cycle will then run at StartTime and run every Interval (seconds), unless RunOnce is true, in which case the Cycle will run one time at StartTime (or after StartTime if triggered by a webhook).