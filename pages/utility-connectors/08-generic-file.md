---
title: Generic File
sidebar: cyclr_sidebar
permalink: generic-file
tags: [utility-connector]
---

## Purpose

The **Generic File** Connector provides the **Create Delimited Text File** Method that creates delimited text content, for example Comma Separated Values (CSV) or Tab Separated Values text.  This content can then be sent to a remote FTP server as a new file.

## Create Delimited Text File Method

The Generic File Connector's **Create Delimited Text File** Method doesn't provide any initial "data fields" as it doesn't know the data you wish to use.  All it starts with are fields to define the structure of the content to be created: Delimiter and Include Header.

![Create Delimited Text File Method - Step Setup](./images/generic-file_create-delimited-text-file_step-setup.png)

You must therefore [add custom Request Fields](./adding-custom-fields) for the values you want to bring in as the "columns" of your data using Field Locations in this format:

```[].FieldName```

![Create Delimited Text File Method - Request Fields](./images/generic-file_create-delimited-text-file_request-fields.png)


You'll then be able to map to these Fields in the Builder from a previous Step that retrieves a list of data to convert into delimited text content.


You should ensure that the Cycle Setting for **Collection Splitting** doesn't split the data you're mapping from, otherwise the Method will generate separate file content for each record you're passing in.
