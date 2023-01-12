---
title: SugarCRM Authentication
sidebar: cyclr_sidebar
permalink: sugarcrm-connector
tags: [connector]
---

# SugarCRM #

API Integration Guide
---------------------

### __Before you start__

In order to avoid [login conflicts](https://support.sugarcrm.com/Documentation/Sugar_Developer/Sugar_Developer_Guide_9.0/Integration/Web_Services/REST_API/#Avoiding_Login_Conflicts_), you will need to set up a custom "platform" name in the portal.  It is best to name it something that describes and identifies your current integration.

### Registering a New SugarCRM "Platform" Value

1. As an admin in your SugarCRM instance, go to the Administration panel.

![Admin Panel](./images/sugarcrm1.png)

2. Select ``Configure API Platforms``.

![Configure API Platforms](./images/sugarcrm2.png)

3. Enter a value of your choosing for the new platform and click ``Add`` and then ``Save``.

![Name Platform](./images/sugarcrm3.png)


You'll then provide that Platform value when authenticating the SugarCRM Connector in Cyclr.


### __Authentication using Cyclr's API__

SugarCRM uses OAuth 2 Password Credentials.

If installing the SugarCRM connector using Cyclr's API, we won’t redirect your users to the SugarCRM sign-in screen. Instead, it requires three account connector properties to be provided: **Domain**, **Username** and **Password**.

First provide a SugarCRM Domain:

```
curl -X POST
     -H 'Content-Type: application/json' 
     -H 'Accept: application/json' 
     -d '{
            "Name": "Domain",
            "Value": "myaccount.sugarcrm.eu"
         }'
'https://yourCyclrInstance/v1.0/account/connectors/SUGAR\_ACCOUNT\_CONNECTOR\_ID/properties'
```

SugarCRM Domain should be in the format of “_myaccount.sugarcrm.eu_“. There’s no “https://” or final forward slash if your URL is “_https://myaccount.sugarcrm.eu/_“.

Platform should be the custom platform value you set earlier.

Set up SugarCRM Username and Password as account connector properties:

```
curl -X POST
     -H 'Content-Type: application/json'
     -H 'Accept: application/json'
     -d '{
            "Name": "Username",
            "Value": "myuser"
         }'
'https://yourCyclrInstance/v1.0/account/connectors/SUGAR\_ACCOUNT\_CONNECTOR\_ID/properties'
```

```
curl -X POST 
     -H 'Content-Type: application/json' 
     -H 'Accept: application/json'
     -d '{
            "Name": "Password",
            "Value": "mypassword"
         }'
'https://yourCyclrInstance/v1.0/account/connectors/SUGAR\_ACCOUNT\_CONNECTOR\_ID/properties' 
 ```

Same as the OAuth Redirect flow, call _/UpdateAccountConnectorOAuth_ with a one-time token. If the Domain, Username and Password are all correctly set up, your end-user will simply be redirected back to your application.

### Applying Filters To Calls

The following methods support the use of additional filters to refine your request:

- Get New And Updated Opportunities

- Search Opportunities

- Search Custom Objects

To apply an additional filter you should add a custom field to the request with a Field Location in the format of <em>field.operator</em> (example: campaign_name.$contains). You can then supply a value for that field when making your requests (example: 'Leads').

The supported filter operators are as follows:

| Operator    | Description                                                                             |
| :---------- | :-------------------------------------------------------------------------------------- |
| $equals     | Performs an exact match on that field.                                                  |
| $not_equals | Matches on non-matching values.                                                         |
| $starts     | Matches on anything that starts with the value.                                         |
| $ends       | Matches anything that ends with the value.                                              |
| $contains   | Matches anything that contains the value.                                               |
| $in         | Finds anything where field matches one of the values as specified as an array.          |
| $not_in     | Finds anything where field does not match any of the values as specified as an array.   |
| $is_null    | Checks if the field is null. This operation does not need a value specified.            |
| $not_null   | Checks if the field is not null. This operation does not need a value specified.        |
| $lt         | Matches when the field is less than the value.                                          |
| $lte        | Matches when the field is less than or equal to the value.                              |
| $gt         | Matches when the field is greater than the value.                                       |
| $gte        | Matches when the field is greater than or equal to the value.                           |

More information on adding custom fields can be found [here](https://docs.cyclr.com/adding-custom-fields).
