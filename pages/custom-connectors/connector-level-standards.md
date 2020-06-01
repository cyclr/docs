---
title: Connector Level Standards
sidebar: cyclr_sidebar
permalink: connector-level-standards

Cyclr Connector Level Standards Guide
---------------------------

# Connector Details

|Setting|Description|
|--- | --- |
|Name|Should not include any version information |
|Version|Should left blank |
|Description|Should be from the product, google search result will likely give appropriate text|
|Logo|Should be 400x400 and scale down nicely |
|Authentication|Use oauth where available  |


# Settings

|Setting|Description|
|--- | --- |
|Status|  |
|Comments|  |
|Post Install Value Lookup Method|   |
|Inbound Paging|  |
|Inbound Page Size|  |
|Icon|  |

# Authentication

This specifies what type of authentication is used by the remote endpoint.

|Field|Description|
|---|---|
|Authentication Description|Displayed when a user installs the connector.|
|Authentication Type|[Dropdown with a selection of different authentication types to choose from.](###authentication-types)|

### Authentication Types

|Authentication Type|Description|
|---|---|
|API Key|The connector uses API key authentication. [Required fields.](###api-key)|
|Basic|The connector implements HTTP basic authentication.|
|OAuth1| The connector implements OAuth 1.0a authentication. [Required fields.](###oauth1)|
|OAuth2|The connector implements OAuth 2 authentication. [Required fields.](###oauth2)|
|Kerberos|The connector implements [Kerberos](https://en.wikipedia.org/wiki/Kerberos_(protocol)) authentication.|
|NetSuiteOAuth1|The connector implements NetSuiteOauth1. [Required fields.](###netsuitoauth1)|

### API Key

|Field|Description|
|---|---|
|API Key Header|  |

### OAuth1

|Field|Description|
|---|---|
|Authorise URL|  |
|Access Token URL|  |
|Request Token URL|  |

Click [here](https://tools.ietf.org/html/rfc5849) for further information on OAuth1.

### OAuth2

|Field|Description|
|---|---|
|OAuth 2 Type|The grant type implemented by the API.|
|Authorise URL|The URL|
|Access Token URL|  |

Click [here](https://oauth.net/2/) for further information on OAuth2.

### NetSuiteOAuth1

|Auth Type|Description|
|---|---|
|Access Token URL|  |
|Request TOken URL|  |

# Rate Limits
# Methods

|Setting|Description|
|--- | --- |
|Name|Should indicate what the method does  |
|Description|Should be provided and end with a "."  |
|Fields & Parameters|ID should be uppercase in display fields but Id in system fields |

System Field should be in PascalCase

Descriptions should end in "."

All entities should have Get, Get All, Create, Update, Delete unless not supported by API

Should provide lookup/triggers for ID's where possible

[Method Level Settings.](method-level-standards.md)<br><br> 
*Note:* Any settings at the method level will override those set at the connector level.

# Parameters

Parameters are used to define a range of HTTP fields. You can define parameters at the connector level or method level. If a parameter is defined at the connector level, it will be global for all methods in the connector.

### Parameter Fields

|Field|Description|
|---|---|
|Target Type|[Target Types](###target-types)|
|Target Name|The name for the parameter. Must match the API definition.|
|Display Name|The display name for the parameter. Should match Cyclr Standards.|
|Description|Description for the parameter. If possible use the API description.|
|Trigger|Trigger name for the parameter. If you want to dynamically show a list of parameter values for the user to choose from, set TriggerName as the trigger you want Cyclr to call. Please see the [Triggers](#triggers) section for details.|
|Hidden|Toggles whether or not a parameter will be shown to the user.|
|Optional|Toggles whether or not a parameter must be included.|
|Parameter Values|  |

### Target Types

|Target Type|Description|
|---|---|
|Http Header|Will create a header with the given key:value.|
|Merge Field|Will match with a place holder field in the endpoint. |
|Query String|Will be formatted and sent as part of the URL. E.g. "example-url.com?a=example&b=123" where 'a' and 'b' are both query string parameters.|
|Filter Field|  |
|Response Field|  |
|Script|  |
|Index|  |

### Account Connector Property

# Triggers

Triggers are used for dynamic lookups.

|Key|Description|
|---|---|
|IdentifierKey|The key value cyclr will use.|
|HumanReadableKey|The display value Cyclr will display to a user.|

E.g. for the JSON object below, the IdentifierKey would be `id` and the HumanReadableKey would be `name`
```json
{
  "id": "123",
  "name": "example"
}
```
