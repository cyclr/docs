---
title: Connector Triggers
sidebar: cyclr_sidebar
permalink: connector-triggers
tags: [connector-creation]
---

## Triggers

Triggers are used for dynamic lookups. For example, if you want to provide a lookup of 'Account IDs' you must have already defined a method in the connector to 'list accounts'.  The trigger will then use the method once the connector is authenticated to allow a look up and select.

The response (_in JSON format_) from the trigger method 'list accounts' looks like this:

```json
{
  "accounts": [
    {
      "id": 1,
      "name": "Account 1"
    },
    {
      "id": 2,
      "name": "Account 2"
    }
  ]
}
```

The settings for an Accounts the Account Id lookup would look something like this:

| Property | Value | Usage |
| --- | --- | --- |
| Name | Select Accounts | Triggers need to be defined at the connector level with a unique Name. |
| Method | List Accounts | The method in the connector to call. | 
| IdentifierKey | [accounts].id" |  The ID field that will be used in an HTTP method by Cyclr. |
| HumanReadableKey | [accounts].name | The field that will allow the user to select the correct account. |

If the Trigger were to be used to provide a lookup to merge a value into an endpoint using a parameter, the specification would look like this:

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hiden | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MergeField| AccountId | Account ID | Provide an Account ID. | Select Accounts | false | false | NA |



