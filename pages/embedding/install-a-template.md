---
title: Install a Template
sidebar: cyclr_sidebar
permalink: install-a-template
tags: [embedding]
---

### Introduction

In this guide, you will use Cyclr API to install a template. Before you start, make sure you have published your template in the Console.

### Getting Templates

You can quickly get all the published templates using the following request:

#### Request

````bash
    curl -X GET
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
    -H "X-Cyclr-Account: 00000000-0000-0000-0000-000000000000"
    "https://yourCyclrInstance/v1.0/templates"
````

#### Response

````json
    [
      {
        "Name": "MailChimp New Subscriber",
        "Description": "Push new subscribers from MailChimp to Salesforce",
        "Id": "885662c2-de28-4760-bec4-2407120ac5f8",
        "Connectors": [
          {
            "Id": 1,
            "Name": "MailChimp",
            "Version": "3.0",
            "StepCount": 1,
            "Icon": "Base64 image"
          },
          {
            "Id": 2,
            "Name": "Salesforce",
            "Version": "v30.0",
            "StepCount": 1,
            "Icon": "Base64 image"
          }
        ]
      }
    ]
````

To filter your templates by a specific connector, simply add some parameters to fire a more complex request:

#### Request

````bash
    curl -X GET
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
    -H "X-Cyclr-Account: 00000000-0000-0000-0000-000000000000"
    "https://yourCyclrInstance/v1.0/templates?pageSize=10&page=1&orderBy=Name&sortOrderAsc=true&connectorName=MailChimp&connectorVersion=3.0&includeIcons=true"
````

### Displaying Templates

````html
    <div class='container' data-bind="foreach: templates">
    <div class="card">
        <div class="card-body">
            <div class="row">
                <div class="col-sm-2" data-bind="foreach: Connectors">
                    <img data-bind="attr:{'src':Icon}" style="width:64px;" />
                </div>
                <div class="col-sm-10">
                    <h4 class="card-title" data-bind="text: Name"></h4>
                    <p class="card-text" data-bind="text: Description"></p>
                </div>
                </div>
            </div>
        </div>
    </div>
````

You can see here we just listed all the templates in rows with their connector icons.

### Installing a Template

Now that all the templates have been displayed, let’s start the installation. Before beginning, be sure you have the following information:

1.  Template ID found in the Get Templates API response  
    `885662c2-de28-4760-bec4-2407120ac5f8`
2.  The installed name of the template, i.e. cycle name

#### Request

````bash
    curl -X POST
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
    -H "X-Cyclr-Account: 00000000-0000-0000-0000-000000000000"
    -H "Content-Type: application/json"
    -H "Accept: application/json" -d '{
        "Name": "My MailChimp Cycle"
    }'
    "https://yourCyclrInstance/v1.0/templates/885662c2-de28-4760-bec4-2407120ac5f8/install?includeIcons=false"
````

#### Response

````json
    {
        "Id": "aa08a1fe-9a42-4650-88b4-f6f8068cddeb",
        "CreatedOnUtc": "2017-11-30T12:15:03.878Z",
        "TasksUsed": 0,
        "ErrorCount": 0,
        "WarningCount": 0,
        "Connectors": [
            {
                "Id": 1,
                "Name": "MailChimp",
                "Version": "3.0",
                "StepCount": 1,
                "Icon": "Base64 image"
            },
            {
                "Id": 2,
                "Name": "Salesforce",
                "Version": "v30.0",
                "StepCount": 1,
                "Icon": "Base64 image"
            }
        ],
        "Status": "Paused",
        "LastSuccessfulRunDate": "2017-11-30T12:15:03.878Z",
        "InProgressTransactionCount": 0,
        "Name": "My MailChimp Cycle",
        "Description": "",
        "Shareable": false,
        "ContinueOnStepError": true,
        "LogStepDataRequests": true,
        "TemplateId": "885662c2-de28-4760-bec4-2407120ac5f8)"
    }
````
    
Once a template is installed, you can save its cycle ID `aa08a1fe-9a42-4650-88b4-f6f8068cddeb` in your database for future reference.
