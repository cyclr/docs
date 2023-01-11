
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

This document will explain what is needed to setup access to Instructure Canvas and install the connector.

### Instructure Canvas OAuth

You will need to be an admin of the Instructure Canvas installation to create OAuth details.

Within your Instructure Canvas web interface:

1. Go to **Admin** > **Developer Keys** 

    ![](./images/canvas-developer-keys.png)
2. Click the **+ Developer Key** button
3. Click **API Key**
4. Fill in the details:
   Set **Redirect URIs** to `https://[Your Cyclr service domain e.g. app-h.cyclr.com]/connector/callback`    
    ![](./images/canvas-api-key.png)
5. Save the key
6. Change the key **State** to `On`
7. Under **Details** save the number - this is your `Client ID`
8. Click **Show Key** and also save this number - this is your `Client Secret`

### Instructure Canvas Access Token ###

**This should not be used in a production environment! Only use the access token in a sandbox environment to test your Canvas installation. !!**

You will need to be an admin of the Instructure canvas installation to create an access token.

1. Go to **Account** > **Settings**
2. Click **New Access Token** 
3. Enter the appropriate details. We highly suggest setting an expiry date.
4. Save the generated access token - **you will not be able to see it again**


</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

In the connector setup enter the client ID and secret or your access token, as stated in the previous step.

Set the Base URL as your Instructure Canvas installation URL. This is the URL that you used to login to the web interface, for example if you used `http://cyclr.instructure.com/login/canvas` to login you should enter `http://cyclr.instructure.com` into this textbox. 

</div>

</section>

