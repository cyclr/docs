---
title: Dynamic Custom Fields
sidebar: cyclr_sidebar
permalink: dynamic-custom-fields
tags: [connector-creation]
---

Adding Custom Fields Dynamically
----------------------------------

Cyclr can add custom fields dynamically to an authenticated connector, removing the need to add them manually for each installation.

There are two ways to do this:

1. If the API you are accessing has methods for retrieving object metadata, these can be used to define the fields.  <br>See [Enhanced Dynamic Custom Fields](#Enhanced).
2. If the API does not have such methods, Cyclr can parse an example response from an existing method. <br>See [Basic Dynamic Custom Fields](#Basic).

<a name="Enhanced">1. Enhanced Dynamic Custom Fields</a>
----------------------
1\. Identify the method within the API that will return the metadata for your object.  You will then need to [create this method within the connector](./connector-methods).<br><br>

Your goal now is to reshape the response of the method using connector script - to Cyclr's required format:

```json
[
  {
    "cyclr_field_location": "CustName",
    "cyclr_display_name": "Customer Name",
  },
  {
    "cyclr_field_location": "CustomerId",
    "cyclr_display_name": "Customer ID",
  }
]
```

2\.

How you restructure the data into the above format will naturally depend on the shape of your source data, but your connector script will look something like this:

```javascript
function after_action_paging() {
    if (method_response == null)
        return true;
    var original = method_response.data;
    var tempResponse = [];
    for (var i = 0; i < original.length; i++) {
        tempResponse.push({
            'cyclr_field_location': "[data]." + original[i].id,
            'cyclr_display_name': original[i].text
        });
    }
    method_response = tempResponse;
    return true;
}
```

3\. Having set the **Connector Fields** to match the example in step 2...
* ```[].cyclr_field_location```
* ```[].cyclr.display_name```
* etc

...you now need to set the **System Fields** appropriately.

> Please note that if you have used the "Generate Fields" functionality to create the fields above, the system field names will be incorrect - so you will now need to update them.

In the response of the method, set the **System Fields** to match [the table below](#systemfields), so that Cyclr can access the various parts of each field description.  In the above example, the mappings would look like this:

![](./images/basic-mappings.png)

4\. The only **required** fields are ```[].cyclr_field_location``` and ```[].cyclr.display_name```.

If you are mapping **data types** from the object description, you will need to add some scripting to the method.  

This will vary depending on the structure of your method response, but as an example:

```jsonc
// Example method response

[
  {
    "cyclr_field_location": "CustName",
    "cyclr_display_name": "Customer Name",
    "cyclr_is_readonly": false,
    "cyclr_data_type": "string"    
  }
]

```

```javascript
// Example method-level script

function after_action(){
  // Check for a response
  if(method_response == null)
  return;
  // Remap fields to values that Cyclr will understand
  for(var i=0;i<method_response.length;i++){
    method_response[i].cyclr_data_type = select_dt(method_response[i].cyclr_data_type);
  }
  return true;
}

function select_dt(item){
  /* The case values here will need to be changed to the values returned by your method, so
   instead of "string" it might be "str", and instead of "integer" it might be "int32".*/
  switch(item) {
  case "string":
    return 1;
    break;
  case "integer":
    return 2;
    break;
  default:
    return 1;
  }
}
```

5\. You should now update the response fields, to look similar to this example:
![](./images/basic-mappings-with-dt.png)

6\. Ensure that the **For Enhanced Custom Fields** option has been checked:
![](./images/for-enhanced-custom-fields.png)

7\. Now all you need to do is go to the method where you want to pick up custom fields, and select this method from the **Custom Fields Lookup Method** dropdown menu.  You can do this for the Request, the Response, or both as required:

![](./images/dynamic_custom_fields_image_2.png)

8\. Cyclr should now automatically map any custom fields for this method once it is installed.

### <a name="systemfields"></a>Table of System Fields

System Field | Description
--- | ---
cyclr_field_location | Location of the custom field, e.g. [items].custom_field ***(required)***
cyclr_display_name | The name to display the custom field as ***(required)***
cyclr_data_type | The data type of the custom field: *(optional)*<br>0=Not Defined<br>1=Text<br>2=Integer<br>3=Float<br>4=Boolean<br>5=Date Time
cyclr_data_type_format | Custom data type format for the custom field *(optional)*
cyclr_default_value | The default value to use for the custom field *(optional)*
cyclr_description | The description of the custom field *(optional)*
cyclr_is_optional | Indicates if the custom field is optional when part of a request *(optional)*
cyclr_is_readonly | Indicates if the custom field is read-only, if it is it won't be added to any requests *(optional)*

<a name="Basic">2. Basic Dynamic Custom Fields</a>
----------------------
1\. Select a method which is able to be called without any field or parameter values being set.  This will be your "Source" method.

2\. The response of this method should be in the same structure as your "Target" method (the method for which Cyclr will dynamically map custom fields).

```jsonc
// Example:
// Source method "List All Orders" response
{
  "orders": [
    {
      "id": 1,
      "name": "John",
      "added": "2020-01-01",
      "customfield1": "abcd"
    }
  ]
}

// Target method "List New Orders" Response
{
  "orders": [
    {
      "id": 29,
      "name": "Dave",
      "added": "2020-09-09",
      "customfield1": "wxyz"
    }
  ]
}
```

3\. Now all you need to do is go to the method where you want to pick up custom fields, and select this method from the **Custom Fields Lookup Method** dropdown menu.  You can do this for the Request, the Response, or both as required:

![](./images/dynamic_custom_fields_image_1.png)

Cyclr will then attempt to determine the correct Display Name and Data Type of the fields found in the response object.

For more control of the custom fields generated you will need to make use of [Enhanced Dynamic Custom Fields](#Enhanced).
