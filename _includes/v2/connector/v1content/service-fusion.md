

<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Before you can install your connector, you need to register an oAuth application with Service Fusion:

- In [OAuth Apps](https://admin.servicefusion.com/developerSettings/oauthApps), click **Add New OAuth App**to create new app if you don't already have one
- Enter the Name and Redirect URL
	`https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback`
- Click  **Add OAuth App**, you will be redirected to the page with the generated `Client ID` and `Client Secret` for your app
- Note the  `Client ID` and `Client Secret` of your app, you will need them in the next steps

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Service Fusion App within Cyclr:

-   go to your **Cyclr Console**
-   click the **Connectors** menu at the top
-   choose **Connector Library**
-   Search for **Service Fusion**
-   click the **Setup** button

Enter the following values:

**Client ID**: the _Consumer Key_ of your Salesforce Connected App

**Client Secret**: the _Consumer Secret_ of your Salesforce Connected App

</div>

</section>
