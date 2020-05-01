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
        "Timezone": "Europe/London"
    }
````

| Parameter | Description |
| --- | --- |
| **Name** | The name for the new account |
| **Description** | Optional, a description for the account |
| **Timezone** | Timezone of the account as found in the "TZ database name" column of this [IANA Timezone list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) |


Response:

````http
    200 Ok
    {
        "Id": "00000000-0000-0000-0000-000000000000",
        "Name": "Test account 001",
        "Description": "An account we will use for testing",
        "AuditInfo": null,
        "Timezone": "Europe/London",
        "CreatedDate": "2017-12-06T15:54:06.6440352Z"
    }
````

| Parameter | Description |
| --- | --- |
| **Id** | The accounts ID |
| **Name** | The accounts name |
| **Description** | The accounts description |
| **AuditInfo** | Any audit info for the account |
| **Timezone** | The accounts timezone |
| **CreatedDate** | Timestamp of account creation |

[How to List Available Templates](./list-available-templates)
