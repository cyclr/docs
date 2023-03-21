---
title: Data types
sidebar: cyclr_sidebar
permalink: data-types
keywords: [datatypes,data,type,types]
tags: [connector-creation]
menus:
    create-a-connector:
        title: Data types
        identifier: data-types
        toggleonly: menutoggleonly
        weight: 8
---
{::options parse_block_html="true" /}
<section class="card">
The following is a guide to the Data Types available at Request/Response body level, and those available when defining Connector Fields.


</section>
<section class="card">
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


</section>
<section class="card">
## Field formats

These data types can be set to define the format of the individual fields in the request/response.

<table>
  <thead>
    <tr>
      <th>Data Type</th>
      <th>Description</th>
      <th align="center">Example Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Boolean</td>
      <td>Example</td>
      <td align="center"><code>true</code></td>
    </tr>
    <tr>
      <td>DateTime</td>
      <td>Example</td>
      <td align="center"><code>2022-04-17T01:34:40.24Z</code></td>
    </tr>
    <tr>
      <td>Decimal</td>
      <td>Number, rounded to 12 decimal places</td>
      <td align="center"><code>123.456789012346</code></td>
    </tr>
    <tr>
      <td>Integer</td>
      <td>Example</td>
      <td align="center"><code>123</code></td>
    </tr>
    <tr>
      <td>Float</td>
      <td>Number, rounded to 14 decimal places</td>
      <td align="center"><code>123.45678901234568</code></td>
    </tr>
    <tr>
      <td>Text</td>
      <td>Value will be stored as a string</td>
      <td align="center"><code>"abc"</code></td>
    </tr>
    <tr>
      <td>File</td>
      <td>Holds the contents of a file</td>
      <td align="center">n/a</td>
    </tr>
    <tr>
      <td>Undefined</td>
      <td>Value will be passed unformatted</td>
      <td align="center">n/a</td>
    </tr>
  </tbody>
</table>

</section>
