---
title: Connector Methods
sidebar: cyclr_sidebar
permalink: connector-methods
tags: [connector-creation]
---

## Settings

These are descriptions of the API endpoints in a standard format.

| Property | Description | Standards |
| --- | --- | --- |
| Name | The name of the method to appear in the Cyclr UI for the user to see. | Should be short and snappy and have initial caps for nouns/verbs, lowercase for minor words (like “a” or “to”), e.g. “Delete Emails”, “Get All Contacts”, “Send to List”.  See below for suggested naming conventions. |
| Description | This is the description of the method to appear in the Cyclr UI for the user to understand what the method does and be informed of any special/interesting values to pass. | Can be quite lengthy if appropriate. Can also include links to helpful API documentation if useful.|
| Warning | | |
| Status | | |
| Comments | | |
| Category | Used to group methods in the Cyclr UI. | Try to keep to single, pluralised words, e.g. “Emails” or “Contacts”.|
| Subcategory | | |
| MethodType | This defines where the method will appear in the Cyclr UI: Action or Webhook. | |
| HttpMethod | This is the action to be performed on the API method. Supported methods are GET, POST, PATCH, PUT, DELETE. | |
| Endpoint | This is the URI to the API method. Not required if this Method Type is a webhook.| |
| Hide | This will hide the method in the Cyclr UI if set to true. |
| DataType | This is the data type used by the API, either Json, Xml, or Form. For GET, this is the Accept header. For POST, this is the request data. JSON is our recommended data type.| |
| Xml Root Element | The single root element for the XML document.| |

Connector naning conventions.

| Name | Purpose |
| --- | --- | 
| Get (ObjectNameSingular) | Used when the method retrieves a single object. |
| List (ObjectNamePlural)| Used when the method retrieves multiple object. |
| Create (ObjectNameSingular) | Used when the method creates an object. |
| Create  (ObjectNamePlural) | Used when the method creates an multiple objects from a single call. |
| Delete (ObjectNameSingular) | Used when the method deletes an object. |
| Update (ObjectNameSingular) | Used when the method updates an object. |

## Rate Limits

You can specify rate limits that apply to this method alone.

## Request Format / Response Format

Here you specify the request or response message format Fields. 

| Property | Description | Standards |
| --- | --- | ---
| Connector Field | The name of the field as used by the remote application’s API. Use Cyclr notation to locate the value, e.g. _[records].EmailAddress_ when receiving an array and retrieving the _EmailAddress _attribute from an element within that array (see _RequestFormat / ResponseFormat_ documentation). | |
| System Field | The name to use internally within Cyclr. Use the field as capitalised by the API and remove any spaces. Apps that have the same SystemField name can auto match values in the builder, saving time and making life easier.| |
| Display Name | The name of the field to be displayed in the Cyclr UI to the user. | |
| Description | This is the description of the Field to appear in the Cyclr UI for the user to understand how the Field is used. | Always include this and keep fairly short (no more than 100 characters).IsOptionalSet to `true` if the Field doesn’t have to be given a value. Leave out if it’s a required Field.Typically, take the _SystemField _value and add spaces or anything that might help describe it, e.g. in _G_oogle Sheets the _ConnectorField_ _entry.title_ used when working with Rows becomes simply _Row Title_. Think human readable. |
| Data Type | Options are: Text, Integer, Float, Boolean, Datetime, File, Decimal.  If the type is Datetime then a subtype can be entered to specify the standard and precision. | |
| Default Value | | |

## Parameters

You can specify Parameters specific to this method. Read more about [parameters](./connector-parameters)

## Script

You can add script to the connector to handle special situations. Read more about [scripting](./connector-scripting)

## Mergefields

A mergefields is placeholder will be substituted at runtime.

*   LastSuccessfulRunDate – is the last time the cycle successfully ran the method. This is useful to find newly created or updated records in an app. A format string needs to be provided. For example, _{% raw %}{{LastSuccessfulRunDate format=yyyy-MM-ddTHH:mm:ssZ}}{% endraw %}_.

