---
title: Create Account
sidebar: cyclr_sidebar
permalink: create-account
tags: [installing]
---

A Cyclr account can contain account connectors and integrations, and typically has a one to one relationship with an account in your application.

If an account doesn't already exist, you can create one.

## Request

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
| **Name** | Defines the name for the new account. |
| **Description** | Optional: gives a description for the new account. |
| **Timezone** | Shows the timezone of the account as found in the **TZ database name** column of the [IANA Timezone list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
| **StepDataSuccessRetentionHours** | Optional: defines how long Cyclr retains data after a successful transaction. |
| **StepDataErroredRetentionHours** | Optional: defines how long Cyclr retains data after an unsuccessful transaction. |
| **TransactionErrorWebhookEnabled** | Optional: sends errors to the webhook URL if set to `true`. |
| **TransactionErrorWebhookUrl** | Optional: defines the webhook URL. |
| **TransactionErrorWebhookIncludeWarnings** | Optional: sends warnings to the webhook URL if set to `true`. |


## Response

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
| **CreatedDate** | The timestamp of account creation. |
| **Id** | The account ID. |
| **Name** | The account name. |
| **Description** | The account description. |
| **AuditInfo** | Any audit information for the account. |
| **TaskAuditInfo** | Any task audit information for the account. |
| **Timezone** | The account's timezone. |
| **StepDataSuccessRetentionHours** | The data retention in hours after a successful transaction. |
| **StepDataErroredRetentionHours** | The data retention in hours after an unsuccessful transaction. |
| **TransactionErrorWebhookEnabled** | Whether errors are sent to the webhook URL. |
| **TransactionErrorWebhookUrl** | The webhook URL. |
| **TransactionErrorWebhookIncludeWarnings** | Whether warnings are sent to wehook URL. |
