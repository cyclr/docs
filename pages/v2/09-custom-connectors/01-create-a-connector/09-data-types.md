---
title: Data types
sidebar: cyclr_sidebar
permalink: data-types
keywords: [datatypes,data,type,types]
tags: [connector-creation]
menus:
    custom-connector-api:
        title: Data types
        identifier: data-types
        weight: 8
---

The following is a guide to the Data Types available at Request/Response body level, and those available when defining Connector Fields.

## Request/Response Data Types

These data types can be set to define the format of the entire request/response.

| Data Type | Description |
|---|---|
|Unknown|Passes no Content-Type/Accept Header|
|Xml|Passes a Content-Type/Accept header of `application/xml`|
|Json|Passes a Content-Type/Accept header of `application/json`|
|Form|Passes a Content-Type/Accept header of `application/x-www-form-urlencoded`|
|File|For uploading a file using multipart/form-data|
|PlainText|Passes/returns unformatted text|
|SimpleFile|For uploading and downloading files from the body|
|MultipartRelated|(Supported for use in Request Only)|

## Field formats

These data types can be set to define the format of the individual fields in the request/response.

| Data Type | Description | Example Value|
|---|---|:---:|
|Boolean| Example |`true`|
|DateTime| Example | `2022-04-17T01:34:40.24Z`|
|Decimal| Number, rounded to 12 decimal places | `123.456789012346`|
|Integer| Example| `123`|
|Float| Number, rounded to 14 decimal places | `123.45678901234568` |
|Text| Value will be stored as a string |`"abc"`
|File| Holds the contents of a file | n/a |
|Undefined| Value will be passed unformatted | n/a|