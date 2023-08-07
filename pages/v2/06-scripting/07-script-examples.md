---
title: Script examples
sidebar: cyclr_sidebar
permalink: script-examples
tags: []

menus:
    scripting:
        title: Script examples
        identifier: script-examples
        toggleonly: menutoggleonly
        weight: 7                                                                                 
---
{::options parse_block_html="true" /}
<section class="card">

## Make External Requests

You can write a script to call external API endpoints. If the API returns a URL which contains the real response object, you can call the external API endpoint.

For example, a webhook returns the following object to Cyclr:

```js
{
  "event": "object.updated",
  "api_url": "http://httpbin.org/get"
}
```

You can use `http_request` to call `api_url` and replace the webhook response with the updated object:

```js
function after_webhook() {
    var request = {
        method: 'GET',
        url: method_response.api_url,
        headers: {
            Accept: 'application/json'
        }
    };


    method_response = http_request(request).content;
    return true;
}
```

After you call `api_url`, Cyclr replaces `method_response` with the content of the HTTP call.

If you return `false` in the `after_webhook` function, you stop Cyclr from running the webhook. You can use this to filter webhook events.

</section>
<section class="card">

## Transform Key Value Pairs

To make use of key value pair responses, you need to use scripts. For example, an API can return the below representation of a contact:

```js



{
    "properties": [
        {
            "key": "email",
            "value": "example@example.com"
        }
    ]
}
```

To access the email field, you need to add a field in the method response with a connector location of `properties.email`. However, this doesn’t work as the cyclr is looking in the response for a properties object with a property named email to get the value from. To solve the issue, add the below function into the method scripts to transform the properties array into an object with properties for each key value pair.

```js
function after_action() {
    var original = method_response.properties;
    var properties = {};
    for (var i in original) {
        var key = original[i]['key'];
        var value = original[i]['value'];
        if (key == null || value == null) {
            continue;
        }


        properties[key] = value;
    }


    method_response.properties = properties;
    return true;
}
```


When you add the `after_action` function above, when Cyclr runs the method the `properties.email` field works as expected and you get the following result back:

```js
{
    "properties": {
        "email": "example@example.com"
    }
}
```

For a corresponding request method, such as adding a contact, you need to include the below function in the method scripts to perform the data transformation in reverse.

```js
function before_action() {
    method_request.properties = Object.keys(method_request.properties).map(function (propertyKey) {
        return {
            key: propertyKey,
            value: method_request.properties[propertyKey]
        };
    });


    return true;
}
```

</section>
<section class="card">

## Modify Parameters

Besides the HTTP request body, you can also use scripting to modify HTTP headers (`method_request_headers`) and query string parameters (`method_request_parameters`). 

This example shows how to transform the method request body to a XML string and save the string as a new parameter called `xmlData`:

```js
function before_action() {
    var xml = '<Records><Record>';
    for (var p in method_request) {
        xml += '<Field val=""' + p + '"">' + method_request[p] + '</Field>';
    }


    xml += '</Record></Records>';
    method_request_parameters.xmlData = xml;
    return true;
}
```

</section>
<section class="card">

## Handle Errors from Third Party APIs

You can use the scripting engine to catch and handle errors returned from third party APIs.

Cyclr exposes a received error response in the `after_error` function through the `method_error` object, which has the below properties:

*  `statusCode` – the HTTP status code returned by the third party API
*  `reasonPhrase` – the reason phrase returned by the third party API
*  `content` – the body content of the response from the third party API
*  `isError` – indicates that the error is an error. default: true, set to false if using isWarning or isSuccess
*  `isWarning` – set to true for Cyclr to log the error as a warning
*  `isSuccess` – set to true to change the error to success, update content to contain the success step data

For example, you can change an error into a warning:

```js
function after_error() {
    if (method_error != null && method_error.statusCode != null && method_error.statusCode.toString() === '400' && method_error.reasonPhrase === 'Email Address not valid' ) {
        method_error.isError = false;
        method_error.isWarning = true;
    }


    return true;
}
```

You can also change an error to a success:

```js
function after_error() {
    if (method_error != null && method_error.statusCode != null && method_error.statusCode.toString() === '400' && method_error.reasonPhrase === 'Email Address not valid') {
        method_error.isError = false;
        method_error.isSuccess = true;
        method_error.content = '{}';
    }


    return true;
}
```
</section>
<section class="card">

## Action Condition

**Connector builder only**.

To add true/false exits to a method, you can use the `action_condition` event:

```js
function action_condition() {
    if (/* Some logical comparison */) {
        return true;
    }


    return false;
}
```

In the example above, any records that pass the condition continue down the `true` path.  

To send errored transactions down the `false` path as well as successful calls that fail the condition, 
you can also use the `after_error` event script.

</section>