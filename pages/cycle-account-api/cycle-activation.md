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
    PUT /v1.0/cycles/{Cycle ID}/activate
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
| **Interval** | The frequency, in minutes, that the Cycle should run at - ignored if first step is webhook or RunOnce is true |
| **StartTime** | Optional, the time for the Cycle to start (UTC) |
| **RunOnce** | Optional, set to true for the Cycle to auto paused after the first run |

Valid Intervals:

| Interval | Time |
| --- | --- |
| 1 | 1 Minute |
| 5 | 5 Minutes |
| 15 | 15 Minutes |
| 30 | 30 Minutes |
| 60 | 1 Hour |
| 120 | 2 Hours |
| 180 | 3 Hours |
| 240 | 4 Hours |
| 360 | 6 Hours |
| 480 | 8 Hours |
| 720 | 12 Hours |
| 1440 | 1 Day |
| 10080 | 1 Week |

Response:

```http
    200 OK
```

The Cycle will then run at StartTime and run every Interval, unless RunOnce is true, in which case the Cycle will run one time at StartTime (or after StartTime if triggered by a webhook).
