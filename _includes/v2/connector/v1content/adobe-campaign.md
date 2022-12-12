
<section class="authentication" markdown="1">

## Authentication

| Type      | OAuth2 |
| Description |  |
| OAuth 2 Type | ClientCredentials |
{: .table .vheader}

</section>

<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content required" markdown="1">

To authenticate the Adobe Campaign connector, you  need the following:

- Client ID
- Client Secret
- Private Key
- Tenant ID

</div>


Follow these steps to :

### 1. Create a project in Adobe Developer Console

Integrations are created as part of a "project" within Adobe Developer Console. 

For complete steps to create a project in Console, see the Adobe Developer Console 
- Getting Started Guide
- Projects Overview

Having created a project, add services including :
- APIs
- Adobe I/O Events registrations
- Adobe I/O Runtime

### 2. Add an API to a project using Service Account authentication

To add an API that uses Service Account (JWT) authentication, follow the steps outlined in the guide.

During the API configuration process, generate a key pair and download the private key.

Once the API has successfully connected you can:
- access the newly generated credentials including **Client ID** and **Client Secret**
- generate an access token using the **API Key** ( aka Private Key) generated during configuration.

### 3. Tenant ID

Your **Tenant ID** is the first part of the URL when you log into Experience Cloud.

If the URL is https://example-company.marketing.adobe.com, the Tenant ID is  ``example-company``.

### 4. Authenticate your connector

Use these to authenticate your Adobe Campaign connector:

- Client ID
- Client Secret
- API Key (the Private Key obtained above)
- Tenant ID 

For further information, visit [the official Adobe Campaign documentation](https://www.adobe.io/authentication/auth-methods.html#!AdobeDocs/adobeio-auth/master/AuthenticationOverview/ServiceAccountIntegration.md).

</section>




