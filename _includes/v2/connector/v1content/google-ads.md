
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Enable the Google Ads API for a project within your workspace:

1. Set up OAuth 2.0 credentials to get your **Client ID** and **Client Secret** 
3. Get the **Developer Token** for your Google Ads account.
4. Get the end user's **Client Customer ID** for the Google Ads client account to be accessed via the API

### Google Ads API

See the [Google Ads API](https://support.google.com/googleapi/answer/6158841?hl=en) documentation for more information.

### Client ID and Client Secret

See the [Google OAuth 2.0](https://support.google.com/cloud/answer/6158849?hl=en) documentation.
Set up the fields below as follows:

- **Authorised redirect URIs**: Your Cyclr callback URL e.g. `https://{{Your Cyclr service domain }}/connector/callback` 

Note your **Client ID** and **Client Secret** which are required to set up the Google Ads connector in Cyclr.

### Developer Token

See the [Google's Developer Token documentation ](https://developers.google.com/google-ads/api/docs/first-call/dev-token) for more information.

### End user's Client Customer ID

See the [Google Ads Customer ID documentation ](https://support.google.com/google-ads/answer/1704344?hl=en-GB).

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. Go to the **Cyclr Console**
2. Select **Connectors** > **Application Connector Library** at the top of the page
3. Use the search box to find the Google Ads connector
4. Select the **Setup Required** icon
5. Enter the following values from the previous sections:
    - **Client ID**: Your **Client ID** noted during OAuth 2.0 authentication
    - **Client Secret**: Your **Client Secret** noted during OAuth 2.0 authentication
    - **Developer Token**: Your **Developer Token** from your Google Ads account
6. Select **Save Changes**

Your Google Ads connector is now set up! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data. This method requires a **client customer ID** to be provided on connector installation.

### Partner templates

To set up the Google Ads connector within a template:

1. Go to the **Cyclr Console**
2. Click the **Templates** dropdown menu at the top of the page
3. Click **Template Library**
4. Click **Design New Template** and enter a **Template Name** to create a new template, or click **Edit Most Recent Draft** to change an existing template
5. Click **+Add Application** in the right-hand menu
6. Use the search bar to find the **Google Ads** connector and click **Install**
7. Change the **Name** and **Description** as required and click **Next**
8. Enter the following values from the previous sections:
    - **Client ID**: Your **Client ID** noted during OAuth 2.0 authentication
    - **Client Secret**: Your **Client Secret** noted during OAuth 2.0 authentication
    - **Developer Token**: Your **Developer Token** you obtained from your Google Ads account.
    - **Client Customer ID**: The end user's **Client Customer ID** of the client account be accessed via the API
9. Click **Next**
10. Click **Sign In**
11. Click the corresponding Google Account to sign in
12. Click **Allow**

Your Google Ads connector is now set up! You can test it by running a method within the template it’s installed in to confirm it returns data.

</div>

</section>
