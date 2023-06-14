---
title: General objects
sidebar: cyclr_sidebar
permalink: general-objects
tags: [templates]

menus:
    scripting:
        title: General objects
        identifier: general-objects
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">  

<table width="100%">
	<col style="width:25%">
	<col style="width:25%">
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
</table></div>

</section>