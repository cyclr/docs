---
title: List Available Templates
sidebar: cyclr_sidebar
permalink: list-available-templates
tags: [installing]
---

_**Templates are integrations built by you in the Console’s drag-and-drop builder, they can be installed in our end user’s account. Your app would present a list or library of available templates to your end users.**_

Retrieve a list of templates available to the Account you wish to install one for.

Request:

````http
    GET /v1.0/templates
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

**X-Cyclr-Account** is the ID of the account we are installing the template into

Response:

````json
    [
        {
            "Name": "Pipedrive > MailChimp",
            "Description": null,
            "Id": "7ad2265e-2ff0-477b-b913-cae1dfde2ea8",
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
            ]
        }
    ]
````

[How to Install a Template](./install-from-template)
