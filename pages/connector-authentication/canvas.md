---
title: Instructure Canvas
sidebar: cyclr_sidebar
permalink: canvas
tags: [connector]
---

## Partner Setup ##

This document will explain what is needed to setup access to Instructure Canvas and install the connector.

### Instructure Canvas OAuth ###

You will need to be an admin of the Instructure Canvas installation to create OAuth details.

Within your Instructure Canvas web interface:

1. Go to "Admin" > "Developer Keys". It will look like the interface below.

    ![](./images/canvas-developer-keys.png)
2. Click the "+ Developer Key" button, and then "API Key".
3. Fill in the details, and set the redirect URI to be {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}. Below is an example of a configured developer key.
    
    ![](./images/canvas-api-key.png)
4. Save the key. Change the "State" of the key to "On". Under "Details", save the number. Click "Show Key" and also save this number. This is your client ID and secret respectively.

### Instructure Canvas Access Token ###

**!! This should not be used in a production environment! Only use the access token in a sandbox environment to test your Canvas installation. !! **
You will need to be an admin of the Instructure canvas installation to create an access token.

1. Go to "Account" > "Settings".
2. Click "New Access Token". Enter the appropriate details. We highly suggest setting an expiry date.
3. Save the generated access token. You will not be able to see it again.


### Connector Setup ###
 In the connector setup enter the client ID and secret or your access token, as stated in the previous step.
 
 Set the Base URL as your Instructure Canvas installation URL. This is the URL that you used to login to the web interface, for example if you used "http://cyclr.instructure.com/login/canvas" to login you should enter "http://cyclr.instructure.com" into this textbox. 
