---
title: Salesforce Pardot (OAuth)
sidebar: cyclr_sidebar
permalink: salesforce-pardot-oauth-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
The Salesforce Pardot (OAuth) connector uses OAuth 2.0 for remote API access. Cyclr requires a Salesforce connected app with specific OAuth scopes to gain access to the Salesforce Pardot API.


</section>
<section class="card">
## Salesforce setup

You need to do the following to setup Salesforce:


</section>
<section class="card">
## Create a connected app

You can find the Salesforce documentation on creating a connected app [here](https://help.salesforce.com/s/articleView?id=sf.connected_app_create.htm&type=5). You need to set up the connected app as follows:

1. Check **Enable OAuth Settings**.
2. Enter your Cyclr callback URL into **Callback URL** field with the following format:
    ```http
    https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback
    ```
3. Select the following scopes under **Selected OAuth Scopes**:
    - Perform requests at any time (refresh_token, offline_access)
    - Manage Pardot services (pardot_api)

You need to make note of the app's **Consumer Key** and **Consumer Secret** as they are needed during Cyclr setup.


</section>
<section class="card">
## Obtain your Pardot Business Unit ID

You can find your **Pardot Business Unit ID** as follows:

1. Go to **Setup** within Salesforce.
2. Enter **Pardot Account Setup** in the quick find box.

You need to make note of the **Pardot Business Unit ID**, it begins with "0Uv" and is 18 characters long, as it is needed during Cyclr setup. If you are unable to access the **Pardot Account Setup** page, please contact your Salesforce administrator.


</section>
<section class="card">
## Authenticate Salesforce Pardot with a user that has single sign-on enabled

To authenticate your Salesforce Pardot account, you need to log in at [pi.pardot.com](https://pi.pardot.com/) using the **Log In with Salesforce** button. This must be done by a user that has single sign-on enabled for their account.


</section>
<section class="card">
## Cyclr setup


</section>
<section class="card">
## Client installation

When using a template containing the Salesforce Pardot (OAuth) connector, clients will be prompted for the following information from previous sections:

-   **Client ID**: The **Consumer Key** from your Salesforce connected app.
-   **Client Secret**: The **Consumer Secret** from your Salesforce connected app.
-   **Business Unit ID**: The **Pardot Business Unit ID** from the **Pardot Account Setup** page within Salesforce.


</section>
<section class="card">
## Partner templates

To set up the Salesforce Pardot (OAuth) connector within a template:

1. Go to the **Cyclr Console**.
2. Click the **Templates** dropdown menu at the top of the page.
3. Click **Template Library**.
4. Click **Design New Template** and enter a **Template Name** to create a new template, or click **Edit Most Recent Draft** to change an existing template.
5. Click **+Add Application** in the right-hand menu.
6. Use the search bar to find the **Salesforce Pardot (OAuth)** connector and click **Install**.
7. Change the **Name** and **Description** as required and click **Next**.
8. Enter the following values from previous sections:
    - **Client ID**: The **Consumer Key** from your Salesforce connected app.
    - **Client Secret**: The **Consumer Secret** from your Salesforce connected app.
    - **Business Unit ID**: The **Pardot Business Unit ID** from the **Pardot Account Setup** page within Salesforce.
9. Click **Next**.

Your Salesforce Pardot (OAuth) connector is now set up! You can test it by running a method within the template it's installed in to confirm it returns data.

</section>
