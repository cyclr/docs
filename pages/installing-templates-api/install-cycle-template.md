---
title: Install a Template
sidebar: cyclr_sidebar
permalink: install-from-template
tags: [installing]
---

_**A Cycle is an instance of a Template installed within an Account.**_

Install a new Cycle into an Account, based on one of the available Templates.

Request:

````http
    POST templates/{Template ID}/install
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

Response:

````json
    {
        "Id": "cf636e9c-13dd-47ea-b0e8-88a5bf7f7b00",
        "CreatedOnUtc": "2017-12-06T16:21:46.0499829Z",
        "TasksUsed": 0,
        "ErrorCount": 0,
        "WarningCount": 0,
        "Connectors": [
            {
                "Id": 2550,
                "Name": "Pipedrive",
                "Version": "1.0",
                "StepCount": 1,
                "Icon": null
            },
            {
                "Id": 2582,
                "Name": "MailChimp",
                "Version": "v3",
                "StepCount": 1,
                "Icon": null
            }
        ],
    "Status": "Paused",
    "LastSuccessfulRunDate": "0001-01-01T00:00:00",
    "InProgressTransactionCount": 0,
    "Name": "Pipedrive > MailChimp",
    "Description": null,
    "Shareable": false,
    "ContinueOnStepError": true,
    "LogStepDataRequests": true,
    "TemplateId": "7ad2265e-2ff0-477b-b913-cae1dfde2ea8"
}
````

Installing the Template will also install all the Connectors required for the Cycle to run.

[How to Get Template Prerequisites](./get-cycle-prerequisites)
