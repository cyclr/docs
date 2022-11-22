---
title: List Available Templates
sidebar: cyclr_sidebar
permalink: list-available-templates
tags: [installing]
---

_**Templates are integrations built by you in the Console’s drag-and-drop builder, they can be installed in your end user’s account. Your app would present a list or library of available templates to your end users.**_

Retrieve a list of all public templates within the Partner console.

Request:

````http
    GET /v1.0/templates
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
````
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
