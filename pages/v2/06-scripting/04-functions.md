---
title: Functions
sidebar: cyclr_sidebar
permalink: functions
tags: [templates]

menus:
    scripting:
        title: Functions
        identifier: functions
        toggleonly: menutoggleonly
        weight: 4                                                                                    
---
{::options parse_block_html="true" /}
<section class="card">

Functions are specific tasks that you can use in your event scripts. 

</section>
<section class="card">

## <code>http_request</code>

You can use the `http_request` function to make external HTTP requests.

When you call the `http_request` function, you need to provide a JSON object with the following properties.

### <code>http_request</code> example

```js
function after_action() {
    var response = http_request({
        method: 'POST',
        url: 'https://someapi.com/createsomething',
        headers: {
            'Authorization': 'Bearer ' + method_auth_value,
            'Content-Type': 'application/on',
            'Accept': 'application/on'
        },
        data: JSON.stringify({ MyData: 'some value' })
    });


    return true;
}
```

| **Response property** | **Description** |
|---|---|
| `status_code` | The HTTP status code. |
| `headers` | Any HTTP headers. |
| `content` | The response body. |
| `request` | Details of the request made. |
{: .two-col .col2-75 }


</section>
<section class="card">

## <code>btoa</code>

You can use the `btoa` function to use a specified destination character set to encode a string to Base64. 

> **Note**: If you don’t provide a character set, the  default character set is `UTF-8.`

Cyclr supports the following character sets:

* `ASCII`
* `ISO-8859-1`
* `UTF-7`
* `UTF-8`
* `UTF-16`
* `UTF-16LE`
* `UTF-16BE`
* `UTF-32`
* `UTF-32LE`
* `UTF-32BE`


```js
var Utf8Base64Encoded = btoa("Hĕllō Wōrld"); // SMSVbGzFjSBXxY1ybGQ=
var AsciiBase64Encoded = btoa("Hĕllō Wōrld","ascii"); // SD9sbD8gVz9ybGQ=
var IsoBase64Encoded = btoa("Hĕllō Wōrld","iso-8859-1"); // SGVsbG8gV29ybGQ=
```

</section>
<section class="card">

## <code>atob</code>

You can use the `atob` function to  use a specified source character set to decode a Base64 encoded string, back to its original value. 

 > **Note**: If you don’t provide a character set, the  default character set is `UTF-8.`

Cyclr supports the following character sets:

* `ASCII`
* `ISO-8859-1`
* `UTF-7`
* `UTF-8`
* `UTF-16`
* `UTF-16LE`
* `UTF-16BE`


```js
var Utf8Base64Decoded = atob("SMSVbGzFjSBXxY1ybGQ="); // Hĕllō Wōrld
var AsciiBase64Decoded = atob("SD9sbD8gVz9ybGQ=","ascii"); // H?ll? W?rld
var IsoBase64Decoded = atob("SGVsbG8gV29ybGQ=","iso-8859-1"); // Hĕllō Wōrld
```

</section>
<section class="card">

## <code>cyclr_sign</code>

You can use the `cyclr_sign` function to sign a string. This allows you to encode data with an algorithm.

### <code>cyclr_sign</code> example

```js
var algorithm = 'HMAC-SHA1';
var signingKey = 'This is the signing key.';
var valueToSign = 'This is the string to sign.';
var signature = cyclr_sign(algorithm, signingKey, valueToSign);
```

Cyclr supports the following algorithms:

* `HMAC-SHA1`
* `HMAC-SHA256`
* `HMAC-SHA512`
* `RSA-SHA1`
* `RSA-SHA224`
* `RSA-SHA256`
* `RSA-SHA384`
* `RSA-SHA512`

</section>
<section class="card">

## <code>cyclr_csv_parse</code>

You can use the `cyclr_csv_parse` function to parse a CSV string.

### <code>cyclr_csv_parse</code> example

```js
var csv = '1,2,3\na,b,c';
var delimiter = ',';
var hasHeader = false;
var csvRecords =  cyclr_csv_parse(csv, delimiter, hasHeader);
```

</section>
<section class="card">

## <code>cyclr_xml_serialize</code>

You can use the `cyclr_xml_serialize` function to convert JSON to XML.

### <code>cyclr_xml_serialize</code> example

```js
var onObj = {
    note: {
        to: 'Tove',
        from: 'Jani',
        heading: 'Reminder',
        body: 'Dont forget me this weekend!'
    }
};


var onObjAsXml = cyclr_xml_serialize(onObj);


// Output:
//<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Dont forget me this weekend!</body></note>
```

</section>
<section class="card">

## <code>cyclr_xml_deserialize</code>

You can use the `cyclr_xml_deserialize` function to convert XML to JSON.

### <code>cyclr_xml_deserialize</code> example

```js
 var xmlStr = '<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Dont forget me this weekend!</body></note>';
  var xmlAsJson = cyclr_xml_deserialize(example);

// Output:
//   {
//     "note": {
//         "to": "Tove",
//         "from": "Jani",
//         "heading": "Reminder",
//         "body": "Dont forget me this weekend!"
//     }
//   }     
```

</section>
<section class="card">

## Storage Functions

Cyclr provides several storage functions that you can use in scripts to develop a Connector, or add to a step in a template or cycle.

There are two types of storage functions:

* `cyclr_storage_...()` allows you to access the same data on any steps in any cycle for a specific connector.
* `cycle_storage_...()` allows you to access data on any steps in a specific cycle.

The data that the storage functions work against is locked to the connector they’re called on. For example, if you write data using `cyclr_storage_set()` on a step from one connector, you can’t use `cyclr_storage_get()` to access that same data on a step from a different connector.

The storage functions available in their `cyclr_` versions are shown below. To use the cycle-restricted version, replace `cyclr_` with `cycle_`.

* `cyclr_storage_list_values()`
* `cyclr_storage_delete_all()`
* `cyclr_storage_delete(key)`
* `cyclr_storage_get(key)`
* `cyclr_storage_set(key, value)`
* `cyclr_storage_append(key, value)`
* `cyclr_storage_list_keys()`
* `cyclr_storage_increment(key, amount)`
* `cyclr_storage_decrement(key, amount)`

</section>


