---
title: Connector authentication link
sidebar: cyclr_sidebar
permalink: connector-authentication-link
tags: [accounts]
---

If you require one of your clients to authenticate an account connector but they don't have access to Cyclr and don't want to share their credentials with you, you can use a connector authentication link and token.

This is an emailable link and token that allows your client to access Cyclr just to authenticate a particular account connector.

1.  Go to the account that contains the connector you want to authenticate.
2.  Open the **Connectors** menu.
3.  Select **Edit Connector** next to the connector to be authenticated.
4.  Select **Generate Setup Token**.
  *  Tokens you generate here expire after 5 minutes by default.  If you want, you can set a longer expiration using the date picker.
5.  Select **Generate** to see the token and a link to a web page where your user can enter it.

> **Note**: This token can only be used once, so you may need to go through these steps again if your user starts but doesn't complete the authentication.

If you need to authenticate more than one account connector, you can generate and send multiple setup tokens to your client but they should authenticate each connector before they move on to the next.
