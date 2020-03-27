---
title: Zoho
sidebar: cyclr_sidebar
permalink: zoho
tags: [connector]
---

# Zoho #

## Partner Setup ##

This document will explain what is needed to setup access to Zoho and install the connector.

### OAuth Setup ###

You'll need to register your Cyclr Partner with Zoho so that you can obtain a Client Id and Secret.  This can be done by following the instructions here:
https://www.zoho.com/accounts/protocol/oauth-setup.html

The redirect URI in your Zoho app should be set as follows:

https://{{**Your Cyclr Service Domain e.g. app-h.cyclr.com**}}/connector/callback

You can find your **Service Domain** within your Cyclr Console from the **Settings** menu then **Integration Settings**.

### Connector Setup ###

Once you have your Client Id and Client Secret from Zoho, you can go to your Cyclr Console, click set them in your Console's Connector Library entry for Zoho CRM so they're automatically provided whenever you install the Connector in the future.
