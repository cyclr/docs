---
title: Intercom Authentication
sidebar: cyclr_sidebar
permalink: intercom-connector
tags: [connector]
---

## Intercom setup

Intercom uses OAuth 2 for remote API access. Register Cyclr within Intercom as your own app to get the OAuth Client ID and Client Secret values you need for Cyclr to authenticate with Intercom.

For more information, see the official Intercom documentation:
* [Creating an App](https://developers.intercom.com/building-apps/docs/get-started-developing-on-intercom)
* [Setting up OAuth](https://developers.intercom.com/building-apps/docs/setting-up-oauth)

## Cyclr setup

### Account setup

Cyclr asks you for the below values when you install the Intercom connector into an account:

| Value | Description |
| :------------- | :------------------------ |
| **Client ID**        | The Client ID from your Intercom account. |
| **Client Secret**    | The Client Secret from your Intercom account. |

You need to add a callback URL to use Intercom in your Cyclr console and accounts. The URL is {% raw %}`https://{{your Cyclr service domain}}/connector/callback`{% endraw %}.
> **Note**: You can find your Cyclr service domain in your Cyclr Console under **Settings** > **General Settings**.

### Required Permissions

Cyclr requires the following permissions to create integrations with Intercom:

* Read one user and one company
* Write conversations
* Read admins

### Choose the correct version

There are connectors for multiple versions of the Intercom API. The available endpoints differ in each version, so you need to use the connector that matches the version your Intercom app uses.

To find out which version your app is set to:

1. [Login](https://app.intercom.com/admins/sign_in?on_pageview_event=sign_in_nav) to your Intercom account.

2. Hover over the icon in the bottom left corner and select **Settings**.
   
3. From the settings page, select **Apps and integrations** > **Developer Hub**.

4. Once in the Developer Hub, select the relevant app.

5. The **Basic Information** page displays information about the app, including the version.
   
6. To change the version, select **Change version** and then select the version you want from the dropdown.
   
> **Note: You can view the [changelog](https://developers.intercom.com/building-apps/docs/api-changelog) for a detailed description of the differences between each API Version.**

## Use the Search Contacts method

There are two processes for sending a search request in the Search Contacts method:

*  Basic search: This allows you to use an operator to search for values within a single field. 
*  Multiple filters: This allows you to use multiple operators to search for values in multiple fields.

### Basic search

Use the first three fields to send a basic search:

1.  Enter a single field.
2.  Enter an operator that isn't `AND` or `OR`.
3.  Enter the value you want to search for.

> **Note**: You can search for multiple values in a comma separated list if you use an 'IN' or 'NIN' operator.

### Multiple filters

You can use multiple filters for a search:

1.  In the **Field** and **Value** fields, enter `Multiple`.
2.  Enter either an `AND` or an `OR` operator in the **Operator** field.
3.  Enter the multiple filter operator(s) in the **Multiple Filters Operator** field.
4.  Enter the field(s) in the **Multiple Filters Field** field.
5.  Enter the value(s) in the **Multiple Filters Value** field.

#### Search for a single value

To use multiple operators or multiple fields to search for a single value, repeat the value in the **Multiple Filters Value** field to match the number of filters.

 For example, if you use two fields to filter the search, enter the value twice:

| Field     | Provided values |
| ----------- | ----------- |
| `Operator`     | AND     |
| `Multiple Filters Operator`     | ~      |
| `Multiple Filters Field `  | name, email       |
| `Multiple Filters Value`  | Smith, Smith        |

The above fields produce the following request:
```json
{
    "query": {
        "operator": "AND",
        "value": [
            {
                "value": "Smith",
                "field": "name",
                "operator": "~"
            },
            {
                "value": "Smith",
                "field": "email",
                "operator": "~"
            }
        ]
    }
}
```
#### Search for multiple values

To search for multiple values with multiple operators or multiple fields, specify the operator or field for each value in a comma separated list. 

If you use a smaller number of operators or fields than values, the search request uses the last item in the list for the subsequent values. For example, if you use two operators to search for three values, the search request uses the second operator in the list for both the second and third value:

Provided request fields with less `Operators` and `Fields` than values :
| Field     | Provided values |
| ----------- | ----------- |
| `Operator`     | OR    |
| `Multiple Filters Operator`     | ~, =      |
| `Multiple Filters Field `  | location.city       |
| `Multiple Filters Value`  |  Brighton, Eastbourne, Hove       |

The above fields produce the following request:
```json
{
    "query": {
        "operator": "OR",
        "value": [
            {
                "value": "Brighton",
                "field": "location.city",
                "operator": "~"
            },
            {
                "value": "Eastbourne",
                "field": "location.city",
                "operator": "="
            },
            {
                "value": "Hove",
                "field": "location.city",
                "operator": "="
            }
        ]
    }
}
```
For more information on Intercom's fields, operators and values, see their [Search for contacts](https://developers.intercom.com/intercom-api-reference/reference/search-for-contacts) documentation. 
