---
title: SugarCRM Authentication
sidebar: cyclr_sidebar
permalink: sugarcrm-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
# SugarCRM

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
'https://CyclrAPIDomain/v1.0/account/connectors/SUGAR\_ACCOUNT\_CONNECTOR\_ID/properties'
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
'https://CyclrAPIDomain/v1.0/account/connectors/SUGAR\_ACCOUNT\_CONNECTOR\_ID/properties'
```

```
curl -X POST 
     -H 'Content-Type: application/json' 
     -H 'Accept: application/json'
     -d '{
            "Name": "Password",
            "Value": "mypassword"
         }'
'https://CyclrAPIDomain/v1.0/account/connectors/SUGAR\_ACCOUNT\_CONNECTOR\_ID/properties' 
 ```

Same as the OAuth Redirect flow, call _/UpdateAccountConnectorOAuth_ with a one-time token. If the Domain, Username and Password are all correctly set up, your end-user will simply be redirected back to your application.

</section>
