---
title: Pass data between two steps
sidebar: cyclr_sidebar
permalink: passing-data-between-two-steps
tags: [templates]
menus:
    template-configuration:
        title: Pass data between two steps
        identifier: passing-data-between-two-steps
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">

If you need to access information from a previous step in script, and you don't want to use Cyclr storage, you can pass the data through the way you map the step's fields.

</section>
<section class="card">

## Pass a single value

To pass a single value to make it accessible in script, you can map the value to an available field.


For example, you might want to access a Customer ID from Step A, in script, in Step B.  In Step B, you can use a field that you don't need for your particular cycle, such as the **Note** field in the screenshot below:

<img src="../images/temp-map.png" alt="Temporary Mapping" width="80%">

If there isn't an appropriate field, you can [add a custom field](adding-custom-fields). You can map the field as pictured, access it, and then remove it from the request in script:

```javascript
function before_action(){
	var contact_id = method_request.note;
	// do something with contact_id
	delete method_request.note;
	return true;
}
```

</section>
<section class="card">

## Pass multiple values

If you have more information to pass across, you can add multiple custom fields.  If there are a lot of fields, such as am array, you can pass all the values as one long string:

### Stringify the values in Step A

In the response from Step A, you need to stringify the value(s) you need and add the string to the response: 

```javascript
function after_action_paging(){
	method_response.string_of_fields = JSON.stringify(method_response.array_to_shrink);
	return true;
}
```

You need to add a custom field to the response of Step A to hold this string.  In the example above, the field location of this custom field would be ``string_of_fields``.

### Parse the values in Step B script

First, map the stringified value to a field in Step B.  As above, you might need to create a field to temporarily hold this value (in the example below, the field is ``string_from_step_A``).

You then need to JSON.parse the string in script:
```javascript
function before_action(){
	var values_from_step_A = JSON.parse(method_request.string_from_step_A);
	// Access values_from_step_A as if it were a JSON array again
	delete method_request.string_from_step_A;
	return true;
}
```

</section>
