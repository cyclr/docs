---
title: Create Account
sidebar: cyclr_sidebar
permalink: create-account
tags: [installing]
---

_**A Cyclr account contains Account Connectors and Integrations and will typically have a one to one relationship with an account in your application.**_

If an Account does not already exist, one should be created.

Request:

````http
    POST /v1.0/accounts
    Authorization: Bearer 0000000000000000000000000000000000000000000000000000000000000000

    {
        "Name": "Test Account 001",
        "Description": "An account we will use for testing",
        "Timezone": "Europe/London",
        "StepDataSuccessRetentionHours": 168,
        "StepDataErroredRetentionHours": 336,
        "TransactionErrorWebhookEnabled": true,
        "TransactionErrorWebhookUrl": "https://webhook/path/here",
        "TransactionErrorWebhookIncludeWarnings": false
    }
````

| Parameter | Description |
| --- | --- |
| **Name** | The name for the new account |
| **Description** | Optional, a description for the account |
| **Timezone** | Timezone of the account as found in the "TZ database name" column of this [IANA Timezone list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) |
| **StepDataSuccessRetentionHours** | Optional, how long data is retained after a successful transaction |
| **StepDataErroredRetentionHours** | Optional, how long data is retained after an unsuccessful transaction |
| **TransactionErrorWebhookEnabled** | Optional, true if errors to be sent to webhook URL |
| **TransactionErrorWebhookUrl** | Optional, webhook URL |
| **TransactionErrorWebhookIncludeWarnings** | Optional, true if wwarnings to be sent to webhook URL |


Response:

````http
    200 Ok
    {
        "CreatedDate": "2017-12-06T15:54:06.6440352Z"
        "Id": "00000000-0000-0000-0000-000000000000",
        "Name": "Test account 001",
        "Description": "An account we will use for testing",
        "AuditInfo": null,
    	"TaskAuditInfo": null,
        "Timezone": "Europe/London",
	    "NextBillDateUtc": "2022-12-14T11:00:55.4629051Z",
    	"StepDataSuccessRetentionHours": 168,
   	    "StepDataErroredRetentionHours": 336,
    	"TransactionErrorWebhookEnabled": true,
        "TransactionErrorWebhookUrl": "https://webhook/path/here",
    	"TransactionErrorWebhookIncludeWarnings": false
    }
````

| Parameter | Description |
| --- | --- |
| **CreatedDate** | Timestamp of account creation |
| **Id** | The accounts ID |
| **Name** | The accounts name |
| **Description** | The accounts description |
| **AuditInfo** | Any audit info for the account |
| **TaskAuditInfo** | Any task audit info for the account |
| **Timezone** | The accounts timezone |
| **StepDataSuccessRetentionHours** | Data retention after successful transaction |
| **StepDataErroredRetentionHours** | Data retention after unsuccessful transaction  |
| **TransactionErrorWebhookEnabled** | Whether errors are sent to webhook URL |
| **TransactionErrorWebhookUrl** | Webhook URL |
| **TransactionErrorWebhookIncludeWarnings** | Whether warnings are sent to wehook URL |

[How to List Available Templates](./list-available-templates)
