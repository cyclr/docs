---
title: NetSuite Connector Guide
sidebar: cyclr_sidebar
permalink: netsuite-connector
tags: [connector]
---

# NetSuite #

Filtering Lists Received
------------------------

The "List" methods e.g. GET requests which can return multiple items when run, can be filtered to better suite your needs.
Initially there are the `Field`, `Operater`, and `Value` query fields available if you only need to include one such query.

- `Field` \*required: is the field in the NetSuite object you wish to filter on for example "name".
- `Operater` \*required: is the operation you wish to run against the object e.g. "is", "greaterthan" etc. For an extensive list of operations and field types against which they can be used please click [here](https://system.netsuite.com/app/help/helpcenter.nl?fid=section_4345782273.html);]
- `Value` \*optional: is the value on against which the fields will be compared with using the operation.

Sometimes you will need to refine your results down even further with more filters. In order to add more filters you will need to go to `Step Setup -> Advanced Settings` and add script in the following manner:

```javascript
    function before_action() {
        method_request_parameters.filter_fields_1 = 'somefield';
        method_request_parameters.filter_op_1 = 'someoperator';
        method_request_parameters.filter_val_1 = 'somevalue';

        method_request_parameters.filter_fields_2 = 'somefield';
        method_request_parameters.filter_op_2 = 'someoperator';

        return true;
    }
```

You can add any number of filter parameters here in order to achieve your desired result, just increasing the number in an unbroken consecutive order.

*NOTE:* If you have added filters as connector parameters and want to add more via script, or are wanting to filter in "Get New/Updated" methods then you will need to start the script parameters from 2 e.g. `method_request_parameters.filter_fields_2`, as the first set are already defined by the step itself.

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
