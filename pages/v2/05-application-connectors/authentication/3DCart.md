---
title: 3DCart Authentication
sidebar: cyclr_sidebar
permalink: 3DCart-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Partner Setup

First, login to your existing 3DCart Developer account or [sign up for one.](https://devportal.3dcart.com/login.asp)

Also login to your existing 3DCart Secure Store account or [sign up for a free trial.](https://www.shift4shop.com/login-page.html)

#### Retrieving OAuth2 Details

*   [Login](https://devportal.3dcart.com/login.asp) to your 3DCart Developer Account.
*   Click Add New.
*   Enter a name and hit next. When in your Developer Portal Dashboard, you'll need to enter the callback URL (https://[Your Cyclr Service Domain]/connector/callback) for your app. You will also need to provide the IP Address for the server that you're on in the IP White List.
*   | Server | URL | IP Address |
    | --- | --- | --- 
    | US (North Virginia) | my.cyclr.com | 52.22.119.215 |
    | UK (London) | my.cyclr.uk | 52.56.244.97 |
    | EU (Frankfurt) | eu.cyclr.com | 18.185.231.228 |
*   Set the scopes for your Application (Permissions on the right of the dashboard), **Contacts** & **Orders** are required.
*   In order to use **List Order Status** method, the scope **OrderStatus** must be selected.
*   Click Save.
*   Note the **Public Key**, **Client ID** and the **Secret Key** from this page.
*   You can also test the application at this stage, to ensure that it works with your 3DCart Store.

### Cyclr Setup

Setup your 3DCart within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **3DCart**
*   Click the **Setup** button

Enter the following values:

**Client ID**:  The Client ID that we retrieved from the app that we made.

**Client Secret**:  The Secret Key we retrieved from the app that we made.

*   You will then be prompted to log-in to your Secure Store

Your 3DCart Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>
