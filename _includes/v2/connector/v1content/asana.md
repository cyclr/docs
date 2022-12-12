
<section class="authentication" markdown="1">

## Authentication

| Type      | OAuth2 |
| Description |  |
| OAuth 2 Type |  |
| API Key Header | Authorization |
| Authorise URL | https://app.asana.com/-/oauth_authorize |
| Access Token URL | https://app.asana.com/-/oauth_token |
{: .table .vheader}

</section>

<section class="setup partner" markdown="1">

## Partner Setup


<div class="section-content required" markdown="1">

**Cyclr Service Domain**

Required to register an oAuth Application in Asana.

- Login to the Cyclr Partner Console 
- Go to Settings > General Settings > Service Domain
- Note the domain

</div>

<div class="section-content" markdown="1">

To register an oAuth Applicationin Asana:

- [Login](https://app.asana.com/-/login) or [sign up](https://asana.com/create-account) to an Asana account
- Go to **Account Settings** dialog
- Click the **Apps** tab
- Click **Add New Application**
- Enter the required details:
	| App Name      | A name for your application |
	| App URL | The url of your company website |
	| Redirect URL |  https://[Your Cyclr Service Domain]/connector/callback |
	{: .table }


The created app details include:
- ``Client ID`` : to uniquely identify your app to the Asana API 
- ``Client Secret`` : do not share or include in source code accessible outside your organisation.

</div>

</section>

<section class="setup partner" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Find the **Asana** Connector
- Click the **Setup** button

Enter the following values:

- **Client ID**: obtained from registering an application

- **Client Secret**: obtained from registering an application.

Your Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>