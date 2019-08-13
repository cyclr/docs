---
title: Squareup Authentication
sidebar: cyclr_sidebar
permalink: squareup-connector
tags: [connector]
---

Authentication With Access Tokens
---------------------------------

Access tokens can be used in the connector in order to authenticate both the snadbox and production versions of the Squareup environment. 

In order to the access tokens go to the applications page in Squareup found [here](https://developer.squareup.com/apps).

- Create a `New Application` OR select `View Details` of an existing application which you'd like to connect to Cyclr.
![](./images/squareup_application.png)

- Copy the `Personal Access Token` seen on this page if you wish to connect to your production environment.
![](./images/squareup_credentials.png)

- Or scroll down to the sandbox section and copy the `Sandbox Access Token` from there if you wish to connect to your sandbox environment for staging.
![](./images/squareup_sandbox_credentials.png)

- Paste your token into the `API Key` field on the Connector Setup page.
![](./images/squareup_connector_setup.png)