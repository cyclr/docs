---
title: Connector Authentication Link
sidebar: cyclr_sidebar
permalink: connector-authentication-link
tags: [managing-cyclr]
---

If you require one of your clients to authenticate an account connector but they don't have access to Cyclr and don't wish to share their credentials with you, you can use a connector authentication link and token.

This is an emailable link and token that allows your client to access Cyclr just to authenticate a particular account connector.

* Go to the account that contains the connector you wish to authenticate.
* Open the **Connectors** menu.
* Click **Edit Connector** next to the connector to be authenticated.
* Click **Generate Setup Token**.
* Tokens generated here will expire after 5 minutes by default.  If you wish, you can set a longer expiration using the date picker.
* Click **Generate**.
* You will be presented with a token and a link to a web page where your user can enter it.

![Animated Demo](./images/sign-in-token.gif)

This token can only be used once so you may need to go through these steps again if your user starts but doesn't complete the authentication.
