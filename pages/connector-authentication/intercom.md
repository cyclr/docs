---
title: Intercom Authentication
sidebar: cyclr_sidebar
permalink: intercom-connector
tags: [connector]
---

# Intercom #

Partner Setup
-------------

Intercom uses OAuth 2 for remote API access. You must register Cyclr within Intercom as your own App to receive OAuth Client ID and Client Secret values to enable Cyclr to authenticate with Intercom.

The official Intercom documentation describing the process can be found here:
* [Creating an App](https://developers.intercom.com/building-apps/docs/get-started-developing-on-intercom)
* [Setting up OAuth](https://developers.intercom.com/building-apps/docs/setting-up-oauth)

**Redirect URL**: you must add a callback URL to allow Intercom to be used in your Cyclr Console and it's accounts.

The URL is:

*   {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}

Your Cyclr Partner **Service Domain** can be found in your Cyclr Console under Settings > Integration Settings.

**Required Permissions**
* Read one user and one company
* Write conversations
* Read admins
