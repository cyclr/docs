---
title: Events
sidebar: cyclr_sidebar
permalink: events
tags: [templates]

menus:
    scripting:
        title: Events
        identifier: events
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">  

Events are functions that have an order of execution within Cyclr. You can use these functions to react to events that happen in Cyclr with your own script.

</section>
<section class="card"> 

## <code>before_webhook</code>

You can call `before_webhook` when a request is received and before you do anything else. You can use the method to decide if a request should continue or return a custom message to the caller instead.


<table width="100%">
	<col style="width:30%">
  <thead>
    <tr>
      <th><strong>Global object</strong></th>
      <th><strong>Description</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>method_endpoint</code></td>
      <td>The webhook request URL.</td>
    </tr>
    <tr>
      <td><code>method_request_headers</code></td>
      <td>The webhook request headers.</td>
    </tr>
    <tr>
      <td><code>method_request</code></td>
      <td>The webhook request body.</td>
    </tr>
    <tr>
      <td><code>method_request parameters</code></td>
      <td>The webhook request parameters.</td>
    </tr>
    <tr>
      <td><code>method_response_headers</code></td>
      <td>The response headers for the request.</td>
    </tr>
    <tr>
      <td><code>method_response</code></td>
      <td>The response body for the request.</td>
    </tr>
    <tr>
      <td><code>script_parameters</code></td>
      <td> An object that contains any available script parameters from the connector and method. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
    </tr>
    <tr>
      <td><code>return</code></td>
      <td>The return object set to <code>true</code> continues with the request to the third party API. The return object set to <code>false</code> aborts the request. <br><strong>Note</strong>: You can use <code>throw</code> for a more useful step error message.</td>
    </tr>
  </tbody>
</table>

</section>
<section class="card"> 

## <code>after_webhook</code>

You can call `after_webhook` immediately after a request to a webhook is received, regardless of the status of the cycle.


<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global object</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_response</code></td>
    <td>The POST object received by the Cyclr webhook.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>This object allows access to Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>cycle_step_id</code></td>
    <td>The ID of the step that executes the script.</td>
  </tr>
  <tr>
    <td><code>cycle_id</code></td>
    <td>The ID of the cycle the script runs in.</td>
  </tr>
  <tr>
    <td><code>cyclr_account_id</code></td>
    <td>The internal ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>external_account_id</code></td>
    <td>The external ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>The return object set to <code>true</code> continues with the request to the third party API. The return object set to <code>false</code> aborts the request. Note: You can use <code>throw</code> for a more useful step error message.</td>
  </tr>
</tbody>
</table>

</section>
<section class="card">

## <code>before_action</code>

You can call `before_action` before you make a request to an external API. Methods that use paging call this function before you retrieve each page.


<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global object</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_request_headers</code></td>
    <td>The HTTP headers for the request.</td>
  </tr>
  <tr>
    <td><code>method_request_parameters</code></td>
    <td> The querystring parameters for the request.</td>
  </tr>
  <tr>
    <td><code>method_request</code></td>
    <td>The object that’s posted to the third party API.</td>
  </tr>
  <tr>
    <td><code>method_request_mergefields</code></td>
    <td>The mergefields for the request.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>Allows access to Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>cycle_step_id</code></td>
    <td>The ID of the step that executes the script.</td>
  </tr>
  <tr>
    <td><code>cycle_id</code></td>
    <td>The ID of the cycle the script runs  in.</td>
  </tr>
  <tr>
    <td><code>cyclr_account_id</code></td>
    <td>The internal ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>external_account_id</code></td>
    <td>The external ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>last_successful_run_date</code></td>
    <td>The time value that indicates when a step last ran without error.</td>
  </tr>
  <tr>
    <td><code>action_data</code></td>
    <td>An object that persists data between some event handler functions, and allows you to pass data between them. You can access this object  in <code>before_action</code>, <code>after_action</code>, <code>after_action_paging</code>, <code>action_condition</code> and <code>after_error</code>.</td>
  </tr>
  <tr>
    <td><code>script_parameters</code></td>
    <td> An object that contains any available script parameters from the connector and method. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>The return object set to <code>true</code> continues with the request to the third party API. The return object set to <code>false</code> aborts the request. <br><strong>Note</strong>: You can use <code>throw</code> for a more useful step error message.</td>
  </tr>
</tbody>
</table>

</section>
<section class="card">


## <code>after_action</code>

You can call the `after_action` function when Cyclr receives a response from the external API. Methods that use paging call this function after Cyclr retrieves each page.

<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global object</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_endpoint</code></td>
    <td>The URL of the original request.</td>
  </tr>
  <tr>
    <td><code>method_request</code></td>
    <td>The POSt object that the third party API recieves.</td>
  </tr>
  <tr>
    <td><code>method_request_mergefields</code></td>
    <td>The mergefields for the request.</td>
  </tr>
  <tr>
    <td><code>method_response_headers</code></td>
    <td>The response headers for the request.</td>
  </tr>
  <tr>
    <td><code>method_response</code></td>
    <td>The object that contains the response data from the third party API. <br><strong>Note</strong>: If the method uses paging, this contains only the current page’s response.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>This object allows access to Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>cycle_step_id</code></td>
    <td>The ID of the step that executes the script.</td>
  </tr>
  <tr>
    <td><code>cycle_id</code></td>
    <td>The ID of the cycle the script runs in.</td>
  </tr>
  <tr>
    <td><code>cyclr_account_id</code></td>
    <td>The internal ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>external_account_id</code></td>
    <td>The external ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>action_data</code></td>
    <td>An object that persists data between some event handler functions, and allows you to pass data between them. You can access this object  in <code>before_action</code>, <code>after_action</code>, <code>after_action_paging</code>, <code>action_condition</code> and <code>after_error</code>.</td>
  </tr>
  <tr>
    <td><code>statusCode</code></td>
    <td>The response status code.</td>
  </tr>
  <tr>
    <td><code>reasonPhrase</code></td>
    <td>The response reason phrase.</td>
  </tr>
  <tr>
    <td><code>script_parameters</code></td>
    <td> An object that contains any available script parameters from the connector and method. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>Inbuilt Cyclr functions must return <code>true</code>.</td>
  </tr>
</tbody>
</table>

</section>
<section class="card">


## <code>after_action_paging</code>

You can call the `after_action_paging` function after Cyclr retrieves all pages of data, regardless of whether you use paging.

>**Note**: This function waits for inbound paging, and doesn’t wait for outbound paging to complete.

<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global object</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_request_headers</code></td>
    <td>The response headers for the request.</td>
  </tr>
  <tr>
    <td><code>method_request_parameters</code></td>
    <td>The parameters for the request.</td>
  </tr>
  <tr>
    <td><code>method_request_mergefields</code></td>
    <td>The mergefields for the request.</td>
  </tr>
  <tr>
    <td><code>method_response</code></td>
    <td>The object that contains the response data from the third party API.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>The object that allows access to Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>cycle_step_id</code></td>
    <td>The ID of the step that executes the script.</td>
  </tr>
  <tr>
    <td><code>cycle_id</code></td>
    <td>The ID of the cycle the script runs in.</td>
  </tr>
  <tr>
    <td><code>cyclr_account_id</code></td>
    <td>The internal ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>external_account_id</code></td>
    <td>The external ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>next_last_successful_run_date</code></td>
    <td>The object that allows you to set the <code>last_successful_run_date</code> value that a step uses on its next run.</td>
  </tr>
  <tr>
    <td><code>action_data</code></td>
    <td>An object that persists data between some event handler functions, and allows you to pass data between them. You can access this object  in <code>before_action</code>, <code>after_action</code>, <code>after_action_paging</code>, <code>action_condition</code> and <code>after_error</code>.</td>
  </tr>
  <tr>
    <td><code>script_parameters</code></td>
    <td> An object that contains any available script parameters from the connector and method. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>Inbuilt Cyclr functions must return<code>true</code>.</td>
  </tr>
</tbody>
</table>

</section>
<section class="card">

## <code>after_error</code>

You can call the `after_error` function when Cyclr receives an error from an external API.

<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global object</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_error</code></td>
    <td>The details of the error. For more information on handling errors, see the [Handle Errors from Third Party APIs](#handle-errors-from-third-party-apis) section.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>This object allows you to access Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>cycle_step_id</code></td>
    <td>The ID of the step that executes the script.</td>
  </tr>
  <tr>
    <td><code>cycle_id</code></td>
    <td>The ID of the cycle the script runs in.</td>
  </tr>
  <tr>
    <td><code>cyclr_account_id</code></td>
    <td>The internal ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>external_account_id</code></td>
    <td>The external ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>action_data</code></td>
    <td>An object that persists data between some event handler functions, and allows you to pass data between them. You can access this object  in <code>before_action</code>, <code>after_action</code>, <code>after_action_paging</code>, <code>action_condition</code> and <code>after_error</code>.</td>
  </tr>
  <tr>
    <td><code>script_parameters</code></td>
    <td> An object that contains any available script parameters from the connector and method. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>Inbuilt Cyclr functions must return <code>true</code>.</td>
  </tr>
</tbody>
</table>


</section>
<section class="card">

## <code>action_condition</code>

**Connector builder only**.

You can use the `action_condition` function to combine a method with a decision step, which means you can perform a test that directs a transaction through either the `true` or `false` exit point. Cyclr adds the `true` and `false` exit points if you include this function in a method. For more information, see the example script.


<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global objects</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_response</code></td>
    <td>The object that contains the response data from the third party API.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>The object that allows access to Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>cycle_step_id</code></td>
    <td>The ID of the step that executes the script.</td>
  </tr>
  <tr>
    <td><code>cycle_id</code></td>
    <td>The ID of the cycle the script runs in.</td>
  </tr>
  <tr>
    <td><code>cyclr_account_id</code></td>
    <td>The internal ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>external_account_id</code></td>
    <td>The external ID of the account the script runs in.</td>
  </tr>
  <tr>
    <td><code>action_data</code></td>
    <td>An object that persists data between some event handler functions, and allows you to pass data between them. You can access this object  in <code>before_action</code>, <code>after_action</code>, <code>after_action_paging</code>, <code>action_condition</code> and <code>after_error</code>.</td>
  </tr>
  <tr>
    <td><code>script_parameters</code></td>
    <td> An object that contains any available script parameters from the connector and method. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>Set the <code>return</code> object to <code>true</code> for the transaction to exit on the true route, and <code>false</code> to exit on the false route.</td>
  </tr>
</tbody>
</table>

### Example script


```
// Any records that pass the condition will continue down the green "True" path.
// Those that do not will take the red "False" path.

function action_condition() {
	if ([some test])
		return true;

	return false;
}

// If you want to send errored transactions (as opposed to successful calls that 
// fail the condition) down the false path, you will need to add after_error script.
```

</section>
<section class="card">

## <code>before_oauth2_authorise</code>

**Connector builder only**.

You can call the `before_oauth2_authorise` event before Cyclr makes an OAuth 2 authorize request.

<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global object</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_endpoint</code></td>
    <td>The URL for the OAuth authorisation endpoint.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>The object that allows access to Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>Inbuilt Cyclr functions must return <code>true</code>.</td>
  </tr>
</tbody>
</table>

</section>
<section class="card">

## <code>before_oauth2_token</code>

**Connector builder only**.

You can call the `before_oauth2_token	` event before Cyclr makes an OAuth 2 access token request.

<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global object</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_request_headers</code></td>
    <td>The HTTP headers for the request.</td>
  </tr>
  <tr>
    <td><code>method_request</code></td>
    <td>The object that’s posted to the OAuth 2 access token endpoint.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>The object that allows access to Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>script_parameters</code></td>
    <td> An object that contains any available script parameters from the connector and method. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>Inbuilt Cyclr functions must return <code>true</code>.</td>
  </tr>
</tbody>
</table>

</section>
<section class="card">

## <code>after_oauth2_token</code>

**Connector builder only**.

You can call the `after_oauth2_token` function after Cyclr makes an OAuth 2 access token request.

<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global object</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_response</code></td>
    <td>The object received from the OAuth 2 access token request.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>The object that allows access to Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>script_parameters</code></td>
    <td> An object that contains any available script parameters from the connector and method. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>Inbuilt Cyclr functions must return <code>true</code>.</td>
  </tr>
</tbody>
</table>

</section>
<section class="card">

## <code>before_oauth2_refresh</code>

**Connector builder only**.

You can call the `before_oauth2refresh` function before Cyclr makes an OAuth 2 refresh token request.

<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global object</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_request_headers</code></td>
    <td>The HTTP headers for the request.</td>
  </tr>
  <tr>
    <td><code>method_request</code></td>
    <td>The object that’s sent to the OAuth 2 refresh token request.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>The object that allows access to Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>script_parameters</code></td>
    <td> An object that contains any available script parameters from the connector and method. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>Inbuilt Cyclr functions must return <code>true</code>.</td>
  </tr>
</tbody>
</table>

</section>
<section class="card">

## <code>after_oauth2_refresh</code>

**Connector builder only**.

You can call the `after_oauth2_refresh` function after Cyclr makes an OAuth 2 refresh token request.

<table width="100%">
	<col style="width:30%">
<thead>
  <tr>
    <th><strong>Global object</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>method_response</code></td>
    <td>The object received from the OAuth 2 refresh token request.</td>
  </tr>
  <tr>
    <td><code>cycle_variables</code></td>
    <td>The object that allows access to Cycle variables. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>script_parameters</code></td>
    <td> An object that contains any available script parameters from the connector and method. <br><strong>Note</strong>: Changes aren't persisted across cycles.</td>
  </tr>
  <tr>
    <td><code>return</code></td>
    <td>Inbuilt Cyclr functions must return <code>true</code>.</td>
  </tr>
</tbody>
</table>

</section>