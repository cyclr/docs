---
title: Install a template
sidebar: cyclr_sidebar
permalink: install-from-template
tags: [installing]
---

A Cycle is an instance of a template you install within an account.

To add a new cycle into your account based on an available template, install the template. There are two ways to install a template from your template library directly into an account:

* Use the console interface.
* Make a request through the Cyclr API.

## Install a template in the console

To install a template through the Cyclr interface:

1. Open your account.
2. Select **Templates**.
3. Search for the template you want to install and select **USE TEMPLATE**.

## Install a template with the Cyclr API

Request:

````http
POST /v1.0/templates/{Template ID}/install
Authorization: Bearer ****************************************************************
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
                "AccountConnectorId": 51,
                "Name": "Pipedrive",
                "Version": "1.0",
                "Authenticated": true,
                "StepCount": 1,
                "Icon": null
            },
            {
                "Id": 2582,
                "AccountConnectorId": 52,
                "Name": "MailChimp",
                "Version": "v3",
                "Authenticated": true,
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

> **Note**: If you install a template, Cyclr also installs all of the connectors the cycle needs to run.

## Related pages

*  [How to Get Template Prerequisites](./get-cycle-prerequisites)
*  [Template Installation](./template-installation)
