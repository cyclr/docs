
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

To authenticate the connector you need a `Client ID` and `Client Secret` for the Podio App you wish to interact with.

To obtain these,  Podio requires your `Cyclr service domain`, which is available from your Cyclr console at **Settings** > **eneral Settings** > **Service Domain**


To generate these values:

1. Login to your Podio account
2. Go to **API Key Generator**
3. Enter the name of the application you wish to interact with
4. Enter a return URL (redirect URL) which is `https://{Cyclr service domain}/connector/callback`
5. Click **Generate API Key**

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. Login to your Cyclr console
2. Find the Podio connector under **Connectors** >  **Connector Library ** >  **Podio**
3. Click the open padlock
4. On the next page enter the `Client ID` and `Client Secret`

The connector is now authenticated and ready to use.

**NB** It may be the case that you require access to multiple Apps within one Podio account. Our tests have shown that authenticating the connector with one `Client ID` and `Client Secret` gives full functionality to the connector across all methods.

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### Obtaining the App ID

To find the ID of the App you wish to interact with, use the method **List Apps** . 

If the App is not listed, find the ID manually:

1. Locate the App in the Podio interface
2. Click the wrench button at the top right of the sidebar
3. Select **Developer**

   ![podio interface](./images/podio_screenshot_1.png)

4. **App ID for (App Name)** is listed on the next page

### Rate-Limits

For most of the actions included in this connector Podio imposes a rate limit of 250 calls per hour. As a result calls (including each page request) are staggered at 15 second intervals.

Podio supports a maximum page size of 500 objects. If the response to your request contains less than 500 objects you should not experience any delay.

</div>

</section>

