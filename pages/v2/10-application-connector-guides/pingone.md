---
title: PingOne Authentication
sidebar: cyclr_sidebar
permalink: pingone-connector
tags: [connector]
---

# Partner Setup

PingOne uses OAuth 2 Client Credentials for remote API access. You must register a worker application within PingOne to receive OAuth Client ID and Client Secret values to enable Cyclr to authenticate with PingOne.

The official documentation for creating an application can be found [here](https://apidocs.pingidentity.com/pingone/platform/v1/api/#getting-started).

## PingOne Setup – Register Your Application

Use the PingOne admin portal to configure your oAuth application. To create the application connection select the environment  that you wish to connect to and then:

 1. Click Connections.
 2. Click + Add Application.
 3. Select the Worker application type.
 4. Click Configure.
 5. Create the application profile by entering the following information:
 6. Application name. A unique identifier for the application. 
 9. Click Save and Close.
 10. Expand the application you have just created and click on the edit icon
 11. Select Configuration tab 
 12. Ensure Grant Type is set to "Client Credentials"
 13. TOKEN ENDPOINT AUTHENTICATION METHOD set to Client Secret Post
 14. Save the following information:
 * Client ID, Secret
 * From the "AUTHORIZATION URL" e.g. https://auth.pingone.eu/cd91070f-c371-480e-80b2-753c735f8aa1/as/authorize
 * Auth Domain would be "auth.pingone.eu"
 * Environment  ID would be ""cd91070f-c371-480e-80b2-753c735f8aa1"

## Cyclr Setup

Setup your PingOne connector within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **PingOne**
*   Click the **Setup** button

Enter the following values:

**Client ID**:  Client ID of the PingOne App

**Client Secret**: Secret of the PingOne App

 **Auth Domain**: e.g. "auth.pingone.eu", or "auth.pingone.com", or "auth.pingone.asia"
 
 **Environment ID**: UID for the environment you wish to connect to
