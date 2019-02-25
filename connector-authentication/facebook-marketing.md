---
title: Facebook Marketing Authenticaiton
---

Partner Setup
-------------

Facebook Marketing API uses OAuth 2. You should sign up for an application on Facebook first and get an OAuth client ID and client secret.

Here is the official documentation for creating a Facebook app:

[https://developers.facebook.com/docs/apps/register](https://developers.facebook.com/docs/apps/register)

1.  Log into your Facebook account.
2.  Create a Facebook Developer account if you don’t already have one: [https://developers.facebook.com/](https://developers.facebook.com/)
3.  Create a new Facebook app: [https://developers.facebook.com/apps/](https://developers.facebook.com/apps/)

Below are the details you should provide:

**Platform**: Website

**Name**: your application name

**App Domain**: (two domains required) my.cyclr.com and your Cyclr partner domain e.g. app-h.cyclr.com

**Website**: your Cyclr partner domain e.g. https://app-h.cyclr.com

**Application Type**: Web Application

3.  Go to Cyclr Console (https://my.cyclr.com/console) > Connectors > Connector Library > Facebook Marketing API > Setup

**Client ID**: This is the App ID displayed after you create the Facebook app

**Client Secret**: This is the App Secret displayed after you create the Facebook app

4.  Don’t forget to make your Facebook app public. It’s in Development by default.

Your Facebook Marketing API connector is now set up! You can test it by installing it in one of your user accounts.

API Integration Guide
---------------------

Facebook Marketing API uses OAuth 2 Authorisation Code flow. It requires your end users to sign into Facebook and grant Cyclr access to their account.

To do this, call _/UpdateAccountConnectorOAuth_ with a one-time sign-in token.
