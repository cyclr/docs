---
title: Oracle Eloqua Connector Guide
sidebar: cyclr_sidebar
permalink: oracle-eloqua-connector
tags: [connector]
---

Oracle Eloqua Setup
---------------

To authenticate the Oracle Eloqua connector, you will need a Client ID and Client Secret.

To get these:

1. Enter your Eloqua instance and navigate to ``Settings > Platform Extensions > AppCloud Developer``.
2. Select ``Create App``.
3. Enter a name, description, the address of an icon for your app.
4. For the callback URL, enter https://``Your Service Domain``/connector/callback. Your service domain can be found in your Cyclr console under Settings > General Settings > Service Domain.
5. Press ``Save``.  It is not necessary to Add Services.
6. You will now recieve a Client ID and Client Secret.  You can use these to authenticate the connector.
