---
title: NetSuite Connector Guide
sidebar: cyclr_sidebar
permalink: netsuite-connector
tags: [connector]
---

# NetSuite #

Filtering Lists of Objects
---------------

The "List" methods, which return multiple items when run, can be filtered to match specified criteria using the following Fields:

- `Field` \*required: is the field in the NetSuite object you wish to filter on for example "name".
- `Operator` \*required: is the operation you wish to run against the field e.g. "is", "greaterthan", "contains". See the table below for an extensive list of operators and field types against which they can be used.
- `Value` \*optional: is the value against which the fields will be compared using the Operator value.

#### Multiple Filter Conditions ####

Sometimes you may need to use more than one filter condition.  To do this you'll need to use some Script to the NetSuite Step to add them in.  In the Builder, click the `Step Setup` button on the NetSuite Step, then choose `Advanced Settings` and enter Script similar to this:

```javascript
function before_action() {
    // Adding a second filter:
    method_request_parameters.filter_field_2 = 'fieldA';
    method_request_parameters.filter_op_2 = 'equalto';
    method_request_parameters.filter_val_2 = 'somevalue';

    // Adding a third filter:
    // (this one doesn't require a `Value` property as it uses the "isnotempty" Operator)
    method_request_parameters.filter_field_3 = 'fieldB';
    method_request_parameters.filter_op_3 = 'isnotempty';

    return true;
}
```

These are the Script properties to use for each filter:

```javascript
method_request_parameters.filter_field_X
method_request_parameters.filter_op_X
method_request_parameters.filter_val_X
```


You can add any number of filter conditions using Script as you require.  Just be sure that the numbers on the end of the properties are consecutive, without any breaks.  If you add properties for "..._2", "..._3", skip 4 and add them for "..._5", your fifth condition will be ignored.


*NOTE:* If you have added filters as connector parameters and want to add more via script, or are wanting to filter in "Get New/Updated" methods then you will need to start the script parameters from "..._2" e.g. `method_request_parameters.filter_field_2`, as the first set are already defined by the step itself.



#### Operators and Valid Field Types ####

|Search Operator|List/Record|Currency, Decimal Number, Time of Day|Date|Check Box|Document, Image|Email Address, Free-Form Text, Long Text, Password, Percent, Phone Number, Rich Text, Text Area,|Multi Select|
|--- |--- |--- |--- |--- |--- |--- |--- |
|after|||X|||||
|allof|||||||X|
|any||X||||X||
|anyof|X||||X||X|
|before|||X|||||
|between||X||||||
|contains||||||X||
|doesnotcontain||||||X||
|doesnotstartwith||||||X||
|equalto||X||X||X||
|greaterthan||X||||||
|greaterthanorequalto||X||||||
|haskeywords||||||X||
|is||||X||X||
|isempty||X|X|||X||
|isnot||||||X||
|isnotempty||X|X|||X||
|lessthan||X||||||
|lessthanorequalto||X||||||
|noneof|X||||X||X|
|notafter|||X|||||
|notallof|||||||X|
|notbefore|||X|||||
|notbetween||X||||||
|notequalto||X||||||
|notgreaterthan||X||||||
|notgreaterthanorequalto||X||||||
|notlessthan||X||||||
|notlessthanorequalto||X||||||
|noton|||X|||||
|notonorafter|||X|||||
|notonorbefore|||X|||||
|notwithin|||X|||||
|on|||X|||||
|onorafter|||X|||||
|onorbefore|||X|||||
|startswith||||||X||
|within|||X|||||
