---
title: General properties
sidebar: cyclr_sidebar
permalink: general-properties
tags: [templates]

menus:
    scripting:
        title: General properties
        identifier: general-properties
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">  

General properties are variables that you can access from most event scripts.

<table width="100%">
	<col style="width:35%">
	<col style="width:15%">
	<col style="width:50%">
    <thead>
  <tr>
    <th><strong>Object</strong></th>
    <th><strong>Type</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>script_execution_context</code></td>
    <td>string</td>
    <td>A string value you can use to identify the context your script executes in. The possible values are <code>RUNNING_TRANSACTION</code>, <code>CONNECTOR_TESTING</code>, or <code>STEP_TESTING</code>. </td>
  </tr>
  <tr>
    <td><code>method_response_fields</code></td>
    <td>array</td>
    <td>An array that contains a method’s response fields.</td>
  </tr>
  <tr>
    <td><code>method_response_fields_in_use</code></td>
    <td>array</td>
    <td>An array that contains the connector field names of method’s response fields that are in subsequent steps.</td>
  </tr>
</tbody>
</table>

</section>