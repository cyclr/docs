---
title: Squareup Authentication
sidebar: cyclr_sidebar
permalink: squareup-connector
tags: [connector]
---

Authentication With Access Tokens
---------------------------------

Access tokens can be used in the connector in order to authenticate both the sandbox and production versions of the Squareup environment. 

In order to obtain the access tokens go to the applications page in Squareup [here](https://developer.squareup.com/apps).

- Create a `New Application`, or select `View Details` of an existing application which you'd like to connect to Cyclr.
![](./images/squareup_application.png)

- If you wish to connect to the production enviroment. Copy the `Personal Access Token` seen on the page.
![](./images/squareup_credentials.png)

- If you wish to connect to the sandbox environment for staging. Scroll down to the sandbox section and copy the `Sandbox Access Token` from there.
![](./images/squareup_sandbox_credentials.png)

- Paste your token into the `API Key` field on the Connector Setup page.
![](./images/squareup_connector_setup.png)