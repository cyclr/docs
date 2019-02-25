---
title: Custom Connector Scripting
---

Events
------

Events are trigger at certain points allowing you to modify data. Script can be added at both the Connector & Method levels; Connector level event handlers will be called for all methods where as method level will only be called for that method. To add an event handler simply add a javascript function with the event name.

    function eventName() { /* Handle event here */ }

#### before_webhook

Called when a webook request has been received & before anything else is done. Method is used to decide if the request should be continued or return a custom message to the caller.

###### Global objects

*   **method_request**: The webhook request body
*   **method_request_headers**: The webhook request headers
*   **method_request_parameters**: The webhook request parameters
*   **method_endpoint**: The webhook request URL
*   **method_response**: The response body for the request
*   **method_response_headers**: The response headers for the request
*   **return**: true for the webhook to continue normal execution, false to stop execution of the request & send the response body/headers to the caller

#### after_webhook

Called after the webook has been caught.

###### Global object

*   **method_response**: object that was POSTed to the Cyclr webhook
*   **return**: true for the webhook to continue normal execution, false to ignore the webhook request

#### before_action

Called before Cyclr makes a request to an external API.

###### Global objects

*   **method_request**: object the will be posted to the third party API
*   **method_request_headers**: HTTP headers for the request
*   **method_request_parameters**: Querystring parameters for the request
*   **method_request_mergefields**: mergefields for the request
*   **return**: true to continue with the request to the third party API, false to abort the request (use throw for a more useful step error message)

#### after_action

Function is called when Cyclr has got a response from an external API

###### Global object

*   **method_response**: object that was received from the third party API.
*   **return**: true

#### after_error

Function is called when Cyclr received an error from an external API.

###### Global object

*   **error_response**: Details of the error, see : **Handle Errors from Third Party APIs** further down for more information on handling errors
*   **return**: true

#### before_oauth2_authorise

Function is called before Cyclr makes an OAuth 2 authorise request.

###### Global object

*   **method_endpoint**: URL for the OAuth authorise endpoint
*   **return**: true

#### before_oauth2_token

Called before Cyclr makes an OAuth 2 access token request.

###### Global object

*   **method_request**: Object that is going to be sent to the OAuth 2 access token endpoint
*   **method_request_headers**: HTTP headers for the request
*   **return**: true

#### after_oauth2_token

Called after Cyclr makes an OAuth 2 access token request.

###### Global object

*   **method_response**: response object that was received from the OAuth 2 access token request
*   **return**: true

#### before_oauth2_refresh

Called before Cyclr makes an OAuth 2 refresh token request.

###### Global object

*   **method_request**: request object that is going to be sent to the OAuth 2 refresh token request
*   **method_request_headers**: HTTP headers for the request
*   **return**: true

#### after_oauth2_refresh

Called after Cyclr makes an OAuth 2 refresh token request.

###### Global object

*   **method_response**: response object that was received from the OAuth 2 refresh token request.
*   **return**: true

Functions
---------

#### http_request

Function to make external HTTP requests.

#### atob

Function to convert a Base64 encoded string to a string.

#### btoa

Function to convert a string to a Base64 string.

Libraries
---------

Before calling any function from a library, please use `require("Library Name");`.

For example:

````require("moment");````

#### Moment.js

Library Name: moment

Description: Parse, validate, manipulate, and display dates and times in JavaScript.

External Documentation: https://momentjs.com/

#### CryptoJS

Library Name: crypto-js

Description: JavaScript library of crypto standards.

External Documentation: https://github.com/brix/crypto-js

Connector scripting examples
----------------------------

#### Make External Requests

You can write a script to call external API endpoints. This is especially useful if the API returns a URL which contains the real response object.

For example, a webhook returns the following object to Cyclr:

    {
       "event":"object.updated",
       "api_url":"http://httpbin.org/get"
    }

Use `http_request` to call `api_url` and replace the webhook response with the updated object:

    function after_webhook() {
      var request = {
        'method': 'GET',
        'url': method_response.api_url,
        'headers': {
          'Accept': 'application/json'
        }
      };
    
      var content = http_request(request).content;
      method_response = content;
      return true;
    }
    

After calling `api_url`, Cyclr will then replace `method_response` with the content of the HTTP call.

Return `false` in the `after_webhook` function will stop Cyclr from running the webhook. You can use this trick to filter webhook events.

When calling the `http_request` function, you can specify the request using:

*   method: HTTP method, e.g. GET, POST, DELETE, PUT, etc.
*   url: URL for the HTTP request
*   parameters: Query string parameter
*   headers: HTTP headers
*   data: HTTP request data

#### Transform Key Value Pairs

Making use of key value pair responses requires the use of scripting, consider an API that returns the below representation of a contact.

    {
       properties: [
         {  "key": "email",
            "value": "example@example.com" }
       ]
    }

To access the email field we would add a field in the method response with a connector location of **properties.email**. However this would not work as the cyclr is looking in the response for a properties object with a property named email to get the value from. To solve the issue we would add the below function into the method scripts, this function will transform the properties array into an object with properties for each key value pair.

    function after_action() {
      var original = method_response.properties;
      method_response.properties = {};
    
      for(var i = 0; i < original.length; i++) {
        var item = original[i];
        if(item['key'] == void(0))
          continue;
    
        var val = item['value'];
        if (val == void(0))
          continue;
    
        method_response.properties[item['key']] = val;
      }
    
      return true;
    }
    

Now when cyclr runs the method if will get the following result back and the **properties.email** field will work as expected.

    {
       properties: {
         "email": "example@example.com"
       }
    }
    

For a corresponding request method, e.g. adding a contact, we would need the below function in the method scripts to perform the data transformation in reverse.

    function before_action() {
        var original = method_request.properties;
        method_request.properties = [];
    
        for(var p in original) {
                method_request.properties.push({
                    'key': p,
                    'value': original[p]
                });
        }
        return true;
    }
    

#### Modify Parameters

Besides the HTTP request body, you can also use scripting to modify HTTP headers (`method_request_headers`) and query string parameters (`method_request_parameters`).

    function before_action(){
        var xmlData = '<Records><Record>';
    
        for (var p in method_request) {
            xmlData += '<Field val=""' + p + '"">' + method_request[p] + '</Field>';
        }
    
        xmlData += '</Record></Records>';
        method_request_parameters.xmlData = xmlData;
        return true;
    }
    

In this example, we transformed the method request body to a XML string and saved the string as a new parameter called `xmlData`.

**Handle Errors from Third Party APIs**

The scripting engine can be used to catch and handle errors returned from third party APIs.

*   **statusCode **– the HTTP status code returned by the third party API
*   **reasonPhrase** – the reason phrase returned by the third party API
*   **content **– the body content of the response from the third party API
*   **isError** – indicates that the error is an error. default: true, set to false if using isWarning or isSuccess
*   **isWarning **– set to true for Cyclr to log the error as a warning
*   **isSuccess **– set to true to change the error to success, update content to contain the success step data

Example: change an error to a warning

    function after_error() {
      if(method_error.statusCode.toString() == 400 && method_error.reasonPhrase == 'Email Address not valid'){
        method_error.isError = false;
        method_error.isWarning = true;
      }
      return true;
    }

Example: change an error to a success

    function after_error() {
      if(method_error.statusCode.toString() == 400 && method_error.reasonPhrase == 'Email Address not valid'){
        method_error.isError = false;
        method_error.isSuccess = true;
        method_error.content = '{}';
      }
      return true;
    }
    

#### Limitations

*   Execution time: 30 seconds. Script running will time out after 30 seconds.
*   External HTTP requests: for security reasons, we will use the same authentication method as the connector and the same authentication value when the connector was installed by the user. You cannot use the script to access or modify the authentication value.

[Learn About Inbound and Outbound Paging](./paging)