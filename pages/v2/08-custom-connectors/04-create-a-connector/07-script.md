---
title: Scripting examples
sidebar: cyclr_sidebar
permalink: connector-scripting
keywords: action_data
redirect_from: "/custom-connector-scripting/"
tags: [connector-creation]
menus:
    create-a-connector:
        title: Script
        identifier: connector-scripting
        toggleonly: menutoggleonly
        weight: 7
---
{::options parse_block_html="true" /}
<section class="card">

You can use Javascript to manipulate data both before you send it and after you retrieve it. This allows you to move data between applications if they have different requirements for valid data.

For more information about using script with Cyclr and to see the script reference pages, see the section on [Scripting](scripting). 

</section>
<section class="card">

## Make external requests

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

## Transform key value pairs

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

To access the email field, you need to add a field in the method response with a connector location of `properties.email`. However, this doesn’t work as the cycle looks in the response for a properties object with a property named email to get the value from. To solve the issue, you can add the below function into the method scripts, and this function transforms the properties array into an object with properties for each key value pair.

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
If you add the `after_action` function, then when Cyclr runs the method, you get the following result back and the `properties.email` field works as expected:

```js
{
    "properties": {
        "email": "example@example.com"
    }
}
```

For a corresponding request method, such as to add a contact, you need to include the below function in the method scripts to perform the data transformation in reverse:

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

This example shows how to transform the method request body to a XML string and save the string as a new parameter called `xmlData`.

</section>
<section class="card">

## Action Condition

To add **True** or **False** exits to a method, you can use the action_condition event.

```js
function action_condition() {
    if (/* Some logical comparison */) {
        return true;
    }


    return false;
}
```

</section>
<section class="card">

## Handle Errors from Third Party APIs

The scripting engine can be used to catch and handle errors returned from third party APIs.

Cyclr exposes a received error response in the `after_error` function through the `method_error` object, which has these properties:

* `statusCode`: The HTTP status code returned by the third party API.
* `reasonPhrase`: The reason phrase returned by the third party API.
* `content`: The body content of the response from the third party API.
* `isError`: The indicator that the error is an error. The default value is `true`, but set to `false` if you use`isWarning` or `isSuccess`.
* `isWarning`: The value you set to `true` for Cyclr to log the error as a warning.
* `isSuccess`: The value you set to `true` to change the error to success, update content to contain the success step data.

### Change an error to a warning

```js
function after_error() {
    if (method_error != null && method_error.statusCode != null && method_error.statusCode.toString() === '400' && method_error.reasonPhrase === 'Email Address not valid' ) {
        method_error.isError = false;
        method_error.isWarning = true;
    }


    return true;
}
```

### Change an error to a success

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