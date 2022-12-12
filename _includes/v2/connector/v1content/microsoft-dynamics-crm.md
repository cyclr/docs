
<section class="setup partner" markdown="1">

## Partner Setup

Dynamics CRM Online uses OAuth 2. Please sign up for an application on Microsoft first and get an OAuth client ID and client secret.

See here for the [official documentation for creating an Azure Active Directory application](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-integrating-applications).

We will summarise it in a few points:

1. Register a free Azure account or Dynamics Online trial account; log into your Azure or Dynamics Online account if you already have one. 
2. Go to Microsoft Azure portal > Azure Active Directory > App Registrations > New application registration.
   Below are the details you should provide:
   - **Name**: Your Application Name
   - **Application type**: Web app / API
   - **Reply URLs**: you must add a callback URL to allow Dynamics CRM to be used in your Cyclr Console and its accounts.
      The URL is:
      `https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback`
   - **Multi-tenanted**: Yes
   - **API Permissions**:
   -  In the API Permissions tab, apply the following permissions:
         **Microsoft Graph** : set by default
         **Dynamics CRM** : Delegated Permission of "user_impersonation" 
3. Go to Cyclr Console (https://yourCyclrInstance/console) > Connectors > Connector Library > Dynamics CRM Online > Setup
   - **Resource**: The beginning of your Microsoft Dynamics CRM account url. E.g: "https://example.crm.dynamics.com" without the quotes.
   - **Client ID**: This is the Application ID displayed in the portal
   - **Client Secret**: Create a Password
      Go to Microsoft Azure portal > Azure Active Directory > App Registrations > Your Application > Certificates & secrets
      Create a new secret and copy the `value` property: this is your secret value

Dynamics CRM Online connector is now set up! You can test it by installing it in one of your customer accounts.

</div>

</section>

<section class="userguide" markdown="1">

## Connector installation using Cyclr API Setup

<div class="section-content" markdown="1">

If you're installing the Microsoft Dynamics CRM Connector using the Cyclr API as part of an automated process, before obtaining an authentication token you should set the domain of the Dynamics CRM Online instance as follows:

Create an Account Connector Property named **Resource** and provide its value:

```
curl -X POST 
     -H 'Content-Type: application/json' 
     -H 'Accept: application/json' 
     -d '{
            "Name": "Resource",
            "Value": "https://example.crm.dynamics.com"
         }'
'https://yourCyclrInstance/v1.0/account/connectors/DYNAMICS_ACCOUNT_CONNECTOR_ID/properties'
```

After successfully creating the Account Connector Property, you can get a one-time sign-in token and call _/UpdateAccountConnectorOAuth_ to complete the user challenge.

</div>

</section>

<section class="faq" markdown="1">

## FAQ

<div class="section-content" markdown="1">

### Error: AADSTS500011

If you encounter the error **AADSTS500011: The resource principal named [Resource URL] was not found in the tenant named [Tenant ID]. This can happen if the application has not been installed by the administrator of the tenant or consented to by any user in the tenant. You might have sent your authentication request to the wrong tenant.**

Ensure you're using the correct **Resource URL** in the Connector's Setup.  This is the URL of your _customer's_ Microsoft Dynamics account and should be similar to `https://mycompany.crmXX.dynamics.com`.

If unsure, go to your _customer's_ Microsoft Dynamics account through a web browser and copy it from the address bar.

### Error: AADSTS65001

Follow the below step if you are getting the error **AADSTS65001: The user or administrator has not consented to use the application with ID " named ". Send an interactive authorization request for this user and resource.**

1.  In your _customer's_ Microsoft Azure portal, go to Azure Active Directory > App registrations > Your App name > API permissions
2.  Click the "Grant admin consent for ..." button to allow the app to be installed into their directory.  If the button is greyed out, the user you are logged in as doesn't have the appropriate permission - you may require an administrator to do this.

### Additional Filter Condition

Some methods provide "Additional Filter Condition" field. This can be used to filter results. The full MS Dynamics documentation is [here](https://docs.microsoft.com/en-us/powerapps/developer/common-data-service/webapi/query-data-web-api#filter-results). 
e.g. "and myCustomBool eq true"
Warning: Ensure lowercase is used for the operators. i.e. AND will not work, and will work.

### Additional Fields To Return

Some methods provide `Additional Fields To Return` field. 

This can be used to return addtional data. Add a custom response field to the method and then add the custom field to Additional Fields To Return. 

If there is more than one field use "," seperator.

</div>

</section>
