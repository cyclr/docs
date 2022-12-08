---
title: Docusign Connector Guide
sidebar: cyclr_sidebar
permalink: docusign-connector
tags: [connector]
---

Docusign Setup
---------------

For Cyclr to connect with the Docusign API you will need to create an "Application" in the Docusign account, as detailed below:

  > NB. This part is completed once, by a Partner.  The client/customer does not need their own separate application within Docusign.

1. Login to your Docusign Portal
2. Follow the Docusign [documentation](https://developers.docusign.com/platform/auth/authcode/authcode-get-token/) to create an oAuth application
3. Go to Settings > Intergrations > Apps and Keys 
4. Use the ADD APP AND INTERGRATION KEY button
5. Enter a name for your app
6. Make sure "Authorization Code Grant" is selected
7. Add a secret key and copy this for later
8. Add a "Redirect URI", this is  {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}
9. Enter a link to your privacy policy
10. Save the application
11. The intergration key will be needed in the steps below.
 

Connector Setup
---------------

The Connector now can be installed using the credentials obtained in the above steps:

**Client ID**: `Intergtation Key`

**Secret**: `Secret Key`
**Domain**: Sandbox Domain is "account-d.docusign.com" | Production Domain is "account.docusign.com"
**Scopes** (This is optional) Leave blank or you can reduce the scopes depending on the methods you require for interations. A space-separated list. Full list of scopes are [here](https://developers.docusign.com/platform/auth/reference/scopes/):  

You will then be prompted to log in, select your Hubspot and authorize access to the connector.
