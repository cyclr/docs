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

<table class="alternate_rows" style="width:100%;table-layout:fixed;overflow-wrap:break-word;border-collapse:collapse;margin: 5px 0px 10px 0px;line-height: 125%;">
          <thead>
            <tr>
              <th style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">Search Operator</p>
              </th>
              <th style="padding:2.84px;width:7.1%;word-wrap:break-word;">
                <p style="font-size:1em !important;margin:0px;">L<wbr>ist/Record</p>
              </th>
              <th style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">Currency, Decimal Number, Time of Day</p>
              </th>
              <th style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">Date</p>
              </th>
              <th style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">Check Box</p>
              </th>
              <th style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">D<wbr>ocument, Image</p>
              </th>
              <th style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">Email Address, Free-Form Text, Long Text, Password, Percent, Phone Number, Rich Text, Text Area,</p>
              </th>
              <th style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">Multi Select</p>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">after</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">allof</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">any</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">anyof</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">before</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">between</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">contains</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">d<wbr>oesnotcontain</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">d<wbr>oesnotstartwith</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">equalto</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">g<wbr>reaterthan</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;word-wrap:break-word;">
                <p style="font-size:1em !important;margin:0px;">g<wbr>reaterthanorequalto</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">h<wbr>askeywords</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">is</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">isempty</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">isnot</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">i<wbr>snotempty</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">lessthan</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;word-wrap:break-word;">
                <p style="font-size:1em !important;margin:0px;">l<wbr>essthanorequalto</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">noneof</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">notafter</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">notallof</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">notbefore</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">n<wbr>otbetween</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">notequalto</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">n<wbr>otgreaterthan</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;word-wrap:break-word;">
                <p style="font-size:1em !important;margin:0px;">n<wbr>otgreaterthanorequalto</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">n<wbr>otlessthan</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;word-wrap:break-word;">
                <p style="font-size:1em !important;margin:0px;">n<wbr>otlessthanorequalto</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">noton</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">n<wbr>otonorafter</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">n<wbr>otonorbefore</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">notwithin</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">on</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">onorafter</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">o<wbr>norbefore</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">startswith</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
            <tr>
              <td style="padding:2.84px;width:10.2%;">
                <p style="font-size:1em !important;margin:0px;">within</p>
              </td>
              <td style="padding:2.84px;width:7.1%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:16.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:5.3%;">
                <p style="font-size:1em !important;margin:0px;">X</p>
              </td>
              <td style="padding:2.84px;width:6.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:9.8%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:35.5%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
              <td style="padding:2.84px;width:7.9%;">
                <p style="font-size:1em !important;margin:0px;">
              </p></td>
            </tr>
          </tbody>
        </table>
