---
title: Oracle NetSuite information
sidebar: cyclr_sidebar
permalink: netsuite-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Set select and multiselect fields

When you set select` and `multiselect` fields in a create or update method, you can either provide its `internalid` (actual value in NetSuite) or `name` (UI display text in NetSuite).

### Examples

```json
{
    "company": {
        "internalid": "300"
    },
    "custentity_categories": [
        {
            "internalid": "1"
        },
        {
            "internalid": "2"
        }
    ]
}
```

```json
{
    "company": {
        "name": "Cyclr"
    },
    "custentity_categories": [
        {
            "name": "Software"
        },
        {
            "name": "API"
        }
    ]
}
```

If both the `internalid` and `name` are provided, Cyclr only uses the `internalid` in the RESTlet.

</section>
<section class="card">

## Filter Objects 

The **List** methods return multiple items when you run them and you can filter the items to match specified criteria using the following fields:

- `Field`: (**Required**) The field in the NetSuite object you want to filter. For example, `name`.
- `Operator`: (**Required**) The operation you want to run against the field. For example, `is`, `greaterthan`, `contains`. See the table below for an extensive list of operators and the field types you can use them with.
- `Value`: (**Optional**) The value you want to compare the fields against with the Operator value.

### Multiple Filter Conditions

To use more than one filter condition, you need to use some Script in the NetSuite Step to add the conditions.  In the cycle builder, select the **Step Setup** button on the NetSuite Step, select **Advanced Settings**, and enter your script in the following format.

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

> **Note**: With script, you can add as many filter conditions as you need. For the script to work correctly, make sure that the numbers on the end of the properties are consecutive, without any breaks. If you add properties for `{...}_2`, `{...}_3`, skip 4 and add them for `{...}_5`, Cyclr ignores the fifth condition.

### Define filters in script

In the **List** methods you can skip the filters in the connector parameters and define all of your filters in script instead. To do this you need to start the script parameters from `..._1`. For example, `method_request_parameters.filter_field_1`. 

> **Note**: You need to set the **Get New/Updated** methods' script parameters from `{...}_2`, because the step defined the first set of parameters itself.

### Operators and Valid Field Types

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

</section>
<section class="card">

## NetSuite Saved Search to return 1000+ records

To retrieve more than 1,000 records, you need to create a **Saved Search** in NetSuite and use the appropriate **Run (object) Saved Search** method in the NetSuite Connector for the type of data you're returning. For example, to return contacts, you can use the **Run Contact Saved Search** method.

Set your **Saved Search** criteria to the data you want to receive so it only returns the ID values of the objects. When Cyclr calls the search, RESTlet retrieves the full objects for the objects before it returns the data.

You can find instructions for setting up a Saved Search in the [NetSuite Documentation](https://docs.oracle.com/cloud/latest/netsuitecs_gs/NSSRC/NSSRC.pdf#%5B%7B%22num%22%3A1548%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C90%2C723.6%2Cnull%5D).

</section>
