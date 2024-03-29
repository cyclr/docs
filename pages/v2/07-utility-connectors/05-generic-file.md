---
title: Generic File
sidebar: cyclr_sidebar
permalink: generic-file
tags: [utility-connector]
menus:
    utility-connectors:
        title: Generic File
        identifier: generic-file
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">
## Purpose

The **Generic File** Connector provides the **Create Delimited Text File** Method that creates delimited text content, for example Comma Separated Values (CSV) and Tab Separated Values text.  This content might then be sent to a remote FTP server as a new file using the **FTP Connector**.


</section>
<section class="card">
## Create Delimited Text File Method

The Generic File Connector's **Create Delimited Text File** Method doesn't provide any initial "data fields" as it doesn't know the data you wish to use.  The only default fields are are fields to define the structure of the content to be created: **Delimiter** and **Include Header**.

You must therefore [add custom Request Fields](./adding-custom-fields) for the values you want to bring in as the "columns" of your data using Field Locations in this format:

```
[].FieldName
```

![Create Delimited Text File Method - Request Fields](./images/generic-file.png)


You'll then be able to map to these Fields in the Builder from a previous Step that retrieves a list of data you wish to convert into delimited text content.



The generated text content is accessible through the **Content** Response Field and will be in the format you've specified.

Example of CSV output:

```
emailAddress,firstName
john@example.com,John
dave@example.com,Dave
```


Note: You should ensure that the Cycle's **Collection Splitting** Setting doesn't split the data you're mapping from, otherwise the Method will generate separate file content for each record you're passing in.

</section>
