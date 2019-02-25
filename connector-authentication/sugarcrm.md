---
title: SugarCRM Authentication
---

API Integration Guide
---------------------

SugarCRM uses OAuth 2 Password Credentials.

When installing the SugarCRM connector in one of your customer accounts using Cyclr API, we won’t redirect your users to the SugarCRM sign-in screen. Instead, it requires three account connector properties to be set up: **Domain**, **Username** and **Password**.

First provide a SugarCRM Domain:

```
curl -X POST
     -H 'Content-Type: application/json' 
     -H 'Accept: application/json' 
     -d '{
            "Name": "Domain",
            "Value": "myaccount.sugarcrm.eu"
         }'
'https://api.cyclr.com/v1.0/account/connectors/SUGAR\_ACCOUNT\_CONNECTOR\_ID/properties'
```

SugarCRM Domain should be in the format of “_myaccount.sugarcrm.eu_“. There’s no “https://” or final forward slash if your URL is “_https://myaccount.sugarcrm.eu/_“.

Set up SugarCRM Username and Password as account connector properties:

```
curl -X POST
     -H 'Content-Type: application/json'
     -H 'Accept: application/json'
     -d '{
            "Name": "Username",
            "Value": "myuser"
         }'
'https://api.cyclr.com/v1.0/account/connectors/SUGAR\_ACCOUNT\_CONNECTOR\_ID/properties'
```

```
curl -X POST 
     -H 'Content-Type: application/json' 
     -H 'Accept: application/json'
     -d '{
            "Name": "Password",
            "Value": "mypassword"
         }'
'https://api.cyclr.com/v1.0/account/connectors/SUGAR\_ACCOUNT\_CONNECTOR\_ID/properties' 
 ```

Same as the OAuth Redirect flow, call _/UpdateAccountConnectorOAuth_ with a one-time token. If the Domain, Username and Password are all correctly set up, your end-user will simply be redirected back to your application.
