---
title: Oracle NetSuite Connector Guide
sidebar: cyclr_sidebar
permalink: netsuite-connector
tags: [connector]
---

## RESTlet Installation

To enable REST APIs in NetSuite, a "RESTlet" file must be deployed in your NetSuite account.

To support the NetSuite Connector, Cyclr has its own RESTlet file.  Please get in touch with your Support Team to request this.

Once you have the Cyclr RESTlet file, follow the steps in this documentation.

### Locating your NetSuite Account ID

Your NetSuite Account ID is required when installing the NetSuite Connector within Cyclr and is found in your NetSuite account.

In NetSuite to go **Setup** > **Company** > **Company Information**

Then look for **ACCOUNT ID**.

It might also be located under **Setup** > **Integration** > **Webservice Preferences**

### Upload the RESTlet script to NetSuite

You can upload the RESTlet script file to NetSuite from Customization > Scripting > Scripts > New. Make sure you select RESTlet as the Type and enter the GET / POST / DELETE / PUT function names based on your RESTlet script.

![Example1](./images/Netsuite_1.png)

![Example2](./images/Netsuite_2_2.png)

### Deploy the RESTlet script

Once your script is uploaded, you need to deploy the script. Make a note of the External URL which will be used when you install the NetSuite connector in Cyclr.

![Example3](./images/Netsuite_3.png)

To locate the External URL in future, go to **Setup** > **Scripting** > **Script Deployments** and click the **View** option for the appropriate entry.

### Create an integration in NetSuite

To allow Cyclr to access the RESTlet securely, you need to set up a token-based authentication in NetSuite. You can create an integration under Setup > Integration > Manage Integrations > New. Check the token-based authentication on the setup page.

![Example4](./images/Netsuite_4.png)

Save the integration and copy the consumer key and consumer secret. You will need them when installing the NetSuite connector.

### Create an access token

Create an access token from Setup > Users/Roles > Access Tokens > New. The application name should be the integration you created in the previous step. Select a user who have access to make REST calls and permissions to the objects you would like Cyclr to access.

![Example5](./images/Netsuite_5.png)

Make a note of the token ID and token secret. Cyclr will ask for them when you install the NetSuite connector.

## Setting select and multiselect Fields

When setting `select` and `multiselect` fields in a create or update method, you can either provide its `internalid` (actual value in NetSuite) or `name` (UI display text in NetSuite).

Examples:

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

If both `internalid` and `name` are provided, only the `internalid` will be used in the RESTlet.

## Filtering Objects 

The "List" methods, which return multiple items when run, can be filtered to match specified criteria using the following Fields:

- `Field` \*required: is the field in the NetSuite object you wish to filter on for example "name".
- `Operator` \*required: is the operation you wish to run against the field e.g. "is", "greaterthan", "contains". See the table below for an extensive list of operators and field types against which they can be used.
- `Value` \*optional: is the value against which the fields will be compared using the Operator value.

### Multiple Filter Conditions

Sometimes you may need to use more than one filter condition.  To do this you'll need to use some Script in the NetSuite Step to add them in.  In the Builder, click the `Step Setup` button on the NetSuite Step, then choose `Advanced Settings` and enter Script similar to this:

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

*NOTE:* In the "List" methods you can opt to skip the filters in the connector parameters and simply define all of your filters in script. To do this you will need to start the script parameters from "..._1" e.g. `method_request_parameters.filter_field_1`. However, the "Get New/Updated" methods' script parameters must always be set from "..._2", as the first set are already defined by the step itself.

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

## NetSuite Saved Search to return 1000+ records

To retrieve more than 1,000 records, you will need to create a **Saved Search** in NetSuite, and then use the appropriate **Run (object) Saved Search** Method in the NetSuite Connector for the type of data you're returning, e.g. **Run Contact Saved Search**.

Your Saved Search should have criteria set for what you wish to retrieve and return only the ID values of the objects.  The RESTlet will then retrieve the full objects for them before returning that data when called by Cyclr.

You can find instructions for setting up a Saved Search in the [NetSuite Documentation](https://docs.oracle.com/cloud/latest/netsuitecs_gs/NSSRC/NSSRC.pdf#%5B%7B%22num%22%3A1548%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C90%2C723.6%2Cnull%5D).
