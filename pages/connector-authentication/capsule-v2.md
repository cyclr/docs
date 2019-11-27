---
title: Capsule Authentication
sidebar: cyclr_sidebar
permalink: capsule-connector
tags: [connector]
---

# Capsule v2 #

Partner Setup
-------------

Capsule v2 uses OAuth 2. You should sign up for an application on Capsule first and get an OAuth client ID and client secret.

Here is the official documentation for creating a Capsule OAuth 2 app:

[https://developer.capsulecrm.com/v2/overview/authentication#oauth-2](https://developer.capsulecrm.com/v2/overview/authentication#oauth-2)

1. Register a free Capsule account; or log into your existing account if you already have one.
2. Go to [https://developer.capsulecrm.com/clients/new ](https://developer.capsulecrm.com/clients/new)

    Below are the details you should provide:

    **Name**: Your Application Name

    **URL**: Your Cyclr service domain, e.g. https://app-h.cyclr.com/. This can be found in your Cyclr Console under Settings > Integration Settings > Service Domain.

    **Redirect URL**: you must add a callback URL to allow Capsule to be used in your Cyclr Console and it's accounts.

    The URL is:

    *   {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}

    **Application Type**: Web Application

3. Go to Cyclr Console (https://yourCyclrInstance/console) > Connectors > Connector Library > Capsule v2 > Setup

    **Client ID**: This is the Client ID displayed after you create the Capsule app

    **Client Secret**: This is the Client Secret displayed after you create the Capsule app

    **Authorise URL**: https://api.capsulecrm.com/oauth/authorise?scope=read+write

    **Access Token URL**: https://api.capsulecrm.com/oauth/token

Your Capsule v2 connector is now set up! You can test it by installing it in one of your user accounts.

API Integration Guide
---------------------

Capsule v2 connector uses OAuth 2 Authorisation Code flow. It requires your end users to sign into Capsule and grant Cyclr access to their account.

To do this, call _/UpdateAccountConnectorOAuth_ with a one-time sign-in token.