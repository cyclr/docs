---
title: Brightspace Authentication
sidebar: cyclr_sidebar
permalink: brightspace-connector
tags: [connector]
---

## Partner Setup

#### Retrieving Client ID and Secret
*   Navigate to your Brightspace instance. 
*   Click on the cogs at the top right part of the screen, next to your account name. 
*   Click on "Locale Management" under the "Organisation Related" category. If you do not see the link, please make sure you are logged in as an administrator.
*   Navigate to the "OAuth 2.0" area.
*   Click "Register and app".
*   Enter an appropriate name, and enter your Cyclr redirect URL (https://``Your Service Domain``/connector/callback).
*   Enter the appropriate scopes for your integration. More information on specific scopes can be found [here](https://docs.valence.desire2learn.com/http-scopestable.html). If you would like to use all the methods available in the Brightspace connector, you should set this value as: `content:*:* core:*:* datahub:*:* enrollment:*:* extended-user-profile:values:manage grades:*:* quizzing:*:* users:*:*`.
*   Leave the access token lifetime as the default (3600).
*   Accept the agreement and click "Register".
*   On the next screen you should see a Client ID and Client Secret. Note these two values down.

### Cyclr Setup

Setup your Brightspace App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Brightspace**
*   Click the **Setup** button

Enter the following values:

**Domain**: Your Brightspace instance URL. This is the same URL you used to create the above app. If your Brightspace instance is "https://teaching.school.edu.uk/", you would enter "teaching.school.edu.uk".

**Client ID**: Retrieve from the above steps.

**Client Secret**: Also retrieved from the above steps.

**Scope**: The API scope, outlining what areas this connector has access to. More information can be found here: https://docs.valence.desire2learn.com/http-scopestable.html

**LE API Version**: The specific version you would like to use for all LE-based API calls. You should always use the most recent version unless you would like to use a specific version.

**LP API Version**: Same as above but for LP-based API calls.

**BFP API Version**: Same as above but for BFP-based API calls.


Your Brightspace Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
