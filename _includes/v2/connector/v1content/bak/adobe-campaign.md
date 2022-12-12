
<section class="setup partner" markdown="1">

## Partner Setup
<div class="section-content" markdown="1">
To authenticate the Adobe Campaign connector, you will need the following pieces of information:

* Client ID
* Client Secret
* Private Key
* Tenant ID
</div>

To obtain the above, follow these steps:

### 1. Create a project in Adobe Developer Console

Integrations are now created as part of a "project" within Adobe Developer Console. For complete steps to creating a project in Console, begin by reading the Adobe Developer Console getting started guide and projects overview.

Once you have created a project, you will be able to add services including APIs, Adobe I/O Events registrations, and Adobe I/O Runtime.

### 2. Add an API to your project using Service Account authentication

To add an API that uses Service Account (JWT) authentication, follow the steps outlined in the guide for adding an API to a project using Service Account authentication.

During the API configuration process, you will be able to generate a key pair and download the private key.

When the API has been successfully connected, you will be able to access the newly generated credentials including Client ID and Client Secret, as well as generate an access token using the private key that you generated during configuration.

### 3. Tenant ID

Your Tenant ID is the first part of the URL when you log into Experience Cloud - so if your URL is https://example-company.marketing.adobe.com - your Tenant ID will be ``example-company``.

### 4. Authenticate your connector

You can now use the Client ID, Client Secret, API Key (the Private Key obtained above) and Tenant ID to authenticate your Adobe Campaign connector.  
</section>

For further information, visit [the official Adobe Campaign documentation](https://www.adobe.io/authentication/auth-methods.html#!AdobeDocs/adobeio-auth/master/AuthenticationOverview/ServiceAccountIntegration.md).
