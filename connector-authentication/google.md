---
title: Google Authentication
---

Partner Setup
-------------

Google apps, such as Google Sheets, Google Drive, etc., use OAuth 2. You should use your Google account to create authorization credentials first and get an **OAuth client ID** and **client secret**.

Here is the official documentation for creating authorization credentials:

[https://developers.google.com/identity/protocols/OAuth2WebServer#creatingcred](https://developers.google.com/identity/protocols/OAuth2WebServer#creatingcred)

1.  Sign up for a Google account; or log into your existing account if you already have one.
2.  Go to [https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials)

Below are the details you should provide:

**Application Type**: Web Application

**Name**: Your Application Name

**URL**: Your Cyclr Domain e.g. https://app-h.cyclr.com/

**Redirect URL**: [https://my.cyclr.com/connector/callback](https://my.cyclr.com/connector/callback), {% raw %}https://{{Your Cyclr Domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}

3.  Go to Cyclr Console (https://my.cyclr.com/console) > Connectors > Connector Library > Google Sheets/Drive/etc. > Setup

**Client ID**: This is the Client ID displayed in Google

**Client Secret**: This is the Client Secret displayed in Google

Your Google connector is now set up! You can test it by installing it in one of your user accounts.

API Integration Guide
---------------------

Google connectors use OAuth 2 Authorisation Code flow. It requires your end users to sign into Google and grant Cyclr access to their account.

To do this, call _/UpdateAccountConnectorOAuth_ with a one-time sign-in token.

Additional Setup for Google AdWords
-----------------------------------

The Google AdWords connector requires additional setup before you can access its API:

https://developers.google.com/adwords/api/docs/guides/signup

1.  Sign in or sign up for a Google AdWords manager account
2.  Go to SETUP > AdWords API Centre
3.  Complete the form to create a developer token
4.  Once you have created a developer token, go to Access level > Apply for Basic Access
5.  Submit the Adwords API Token Application

Make a note of your developer token, you will need it when you use Google AdWords methods in Cyclr.
