---
title: DocuSign Connector Guide
sidebar: cyclr_sidebar
permalink: docusign-connector
tags: [connector]
---

DocuSign Setup
---------------

For Cyclr to connect with the DocuSign API you will need to create an "Application" in the DocuSign account, as detailed below:

  > NB. This part is completed once, by a Cyclr Partner.  Your customer does not need their own separate application within DocuSign.


The following steps take you through DocuSign's setup, as [documented here](https://developers.docusign.com/platform/auth/authcode/authcode-get-token/).

1. Login to your DocuSign Portal
2. Go to Settings > Integrations > Apps and Keys 
3. Use the ADD APP AND INTEGRATION KEY button
4. Enter a name for your app
5. Make sure "Authorization Code Grant" is selected
6. Add a secret key and copy this for later
7. Add a "Redirect URI", this is  `https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback`
8. Enter a link to your privacy policy
9. Save the application
10. The integration key will be needed in the steps below.
 

Connector Setup
---------------

The Connector now can be installed using the credentials obtained in the above steps:

**Client ID**: `Integration Key`

**Secret**: `Secret Key`

**Domain**: Sandbox Domain is "account-d.docusign.com" | Production Domain is "account.docusign.com"

**Scopes** (optional) Leave blank or you can reduce the scopes depending on the methods you require for interactions. Specified as a space-separated list. A full list of scopes can be found in [DocuSign's documentation](https://developers.docusign.com/platform/auth/reference/scopes/).

