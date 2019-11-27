---
title: Vincere Connector Guide
sidebar: cyclr_sidebar
permalink: vincere-connector
tags: [connector]
---

Vincere Setup
---------------

For Cyclr to connect with the Vincere API you will need to select a suitable user account within Vincere. This account will require setting up, the steps to complete this are below.

_NOTE: We have experienced issues when using the Safari web browser so would recommend using another browser._

1. Login to the Vincere Application using the account specific URL, e.g. {%raw%}https://{{yourdomain}}.vincere.io/loginForm.do{%endraw%}
2. Select Settings > Marketplace
3. Select the API Tab
4. Click "Create new token" button, this will display the API Key
5. Click "Create new Client ID" button, this will display the Client ID
6. Enter the callback URL using your Cyclr Partner's **Service Domain** into the "Callback URL" field, e.g. <br /> {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}. <br /> Your Service Domain can be found in your Cyclr Partner Console under Settings > Integration Settings > Service Domain.


Connector Setup
---------------

The Connector now can be installed using the credentials obtained in the above steps:

**Client ID**: _Vincere Client ID_

**Secret**: _Leave this blank_

**Domain**:  _yourdomain_ (see your URL when accessing Vincere, {%raw%}https://{{yourdomain}}.vincere.io{%endraw%})

**API Key**: _Vincere API Key_
