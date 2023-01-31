---
title: Pass data between two steps
sidebar: cyclr_sidebar
permalink: passing-data-between-two-steps
tags: [templates]
menus:
    create-cycle-templates:
        title: Pass data between two steps
        identifier: passing-data-between-two-steps
        toggleonly: menutoggleonly
        weight: 8
---
{::options parse_block_html="true" /}
<section class="card">
If you need to access information from a previous step in *script*, and you don't want to use Cyclr storage, one option is to pass the data via mapping.

## Passing a single value

Passing a single value to make it accessible in script can be as simple as mapping it to an available field.

Let's say you want to access a Customer ID from Step A, in script in Step B.  In Step B, you might have a field that's not required for your particular cycle, such as the **Note** field in the diagram below:

![Temporary Mapping](./images/temp-map.png)


You can map the field as pictured, access it, and then remove it from the request in script.

```javascript
function before_action(){
	var contact_id = method_request.note;
	// do something with contact_id
	delete method_request.note;
	return true;
}
```

If there isn't an appropriate field, you can add one:([https://docs.cyclr.com/adding-custom-fields](https://docs.cyclr.com/adding-custom-fields))

You will likely still want to delete the field after you use it, as above.

</section>
<section class="card">

## Passing multiple values

If you have more information to pass across, it may make sense to add multiple custom fields.  If there are a lot of fields however (an array perhaps), you have another option - passing all the values as one long string.

### Part 1 - Stringify the values in Step A

In the response from Step A, you'll need to stringify the value(s) you need and add this to the response. 

```javascript
function after_action_paging(){
	method_response.string_of_fields = JSON.stringify(method_response.array_to_shrink);
	return true;
}
```

You will need to add a custom field to the response of Step A to hold this string.  In the example above, the field location of this custom field would be ``string_of_fields``.

### Part 2 - Parse the values in Step B script

First, map the value to a field in Step B.  As above, you may need to create a field to temporarily hold this value (in the example below, I've named this field ``string_from_step_A``)

You'll then need to JSON.parse the string in script:
```javascript
function before_action(){
	var values_from_step_A = JSON.parse(method_request.string_from_step_A);
	// Access values_from_step_A as if it were a JSON array again
	delete method_request.string_from_step_A;
	return true;
}
```

</section>
