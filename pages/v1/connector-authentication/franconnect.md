---
title: FranConnect
sidebar: cyclr_sidebar
permalink: franconnect
tags: [connector]
---

## FranConnect ##

This document will explain what is needed to setup access to FranConnect and install the connector.

### Authentication Details Setup ###
Contact FranConnect to get a **Client ID** and **Client Secret**. Contact details can be found [here](https://docs.franconnect.net/#tag/Introduction).

### Connector Setup ###
In Cyclr's Connector Setup, enter the **Client ID** and **Client Secret** you were given into the appropriate fields.

**Company Code** is the part after "https://" and before "/fc" of the login URL.

For example, if the login URL for your FranConnect system is `https://developers.franconnect.net/fc`, then the company code will be `developers.franconnect.net`.

Sign in the the FranConnect account using the details provided and the connector will then be authenticated.
