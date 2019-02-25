---
title: Custom Connectors Parameters and Triggers
---

Overview
--------

You can make connectors more usable by using parameters and triggers. Examples include:

*   An add contact to list step can show available lists in a drop down
*   A get contacts step can be made into a get updates contacts step

Parameters
----------

Parameters are used to define a range of HTTP fields, e.g. HTTP headers, mergefields, query string parameters, etc.

You can define parameters at the connector level or method level. If a parameter is defined at the connector level, it will be global for all methods in the connector.

For example:
{% raw %}
    "Parameters": [
        {
            "TargetType": "QueryString",
            "TargetName": "before_created_date",
            "DisplayName": "Before Created Date",
            "Description": "Restrict the response to objects created before the date.",
            "IsOptional": true
        }
    ]
{% endraw %}

The **before_created_date** can then be used to filter objects to a specific range. Cyclr users will see this parameter in Step Setup.

Parameters can be defined in conjunction with URL endpoint mergefields, for example, if your URL looks like:

    "Endpoint": "https://example.com/{% raw %}{{AccountID}}{% endraw %}/objects",

Then you can specify **AccountID **as a mergefield parameter:
{% raw %}
    "Parameters": [
        {
            "TargetType": "MergeField",
            "TargetName": "AccountId",
            "DisplayName": "Account ID",
            "Description": "User account.",
            "IsOptional": false
        }
    ]
{% endraw %}

Here is a list of fields for parameter definition:

#### TargetType

There are five target types for Cyclr parameters. This will decide where the parameter locates.

*   HttpHeader: HTTP header
*   MergeField: Endpoint mergefield
*   QueryString: Query string parameter
*   FilterField: Cyclr filter field (can set a date field as FilterField to filter new objects)
*   ResponseField: Response field

#### TargetName

The name for the parameter.

#### DisplayName

The display name for the parameter.

#### Description

Description for the parameter.

#### TriggerName

Trigger name for the parameter. If you want to dynamically show a list of parameter values for the user to choose from, set `TriggerName` as the trigger you want Cyclr to call. Please see the _Triggers_ section for details.

#### IsOptional

Set the parameter to be optional or required. The default is required (false).

#### Hide

Hide the parameter from the user interface. You can use this to hide internal parameters you want to send to the endpoint.

Triggers
--------

Triggers are used for dynamic lookups. Let’s use the AccountId parameter as an example:

{% raw %}
    "Parameters": [
        {
            "TargetType": "MergeField",
            "TargetName": "AccountId",
            "DisplayName": "Account ID",
            "Description": "User account.",
            "IsOptional": false,
            "TriggerName": "Lookup Account"
        }
    ],
    "Triggers": [
    {
        "Name": "Lookup Account",
        "MethodName": "Get Accounts",
        "IdentifierKey": "[accounts].id",
        "HumanReadableKey": "[accounts].name"
    }
    ]
{% endraw %}

Note that when the user choose **Lookup** for the parameter **AccountId **in Step Setup, Cyclr will use the Lookup Account trigger, call **Get Accounts** and populate a list of accounts.

Triggers need to be defined at the connector level with a unique **Name**. **MethodName **is the method that Cyclr will call to populate parameter values.

**IdentifierKey **is the key value Cyclr will use. **HumanReadableKey **is the display value Cyclr will display in Step Setup.

For example, if a user chooses Account **Example **with ID **1000**, Cyclr will fill the mergefield with **1000**.

The API endpoint becomes:

    "https://example.com/1000/Objects"

[Learn About Custom Connector Scripting ](./scripting)