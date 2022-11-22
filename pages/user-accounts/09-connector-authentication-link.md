---
title: Connector Authentication Link
sidebar: cyclr_sidebar
permalink: connector-authentication-link
tags: [managing-cyclr]
---

If you require one of your clients to authenticate an Account Connector, but they don't have access to Cyclr and don't wish to share their credentials with you, you can generate a **Connector Authentication Link**.

This is an emailable link that when clicked will go through the authentication and consent screens of a particular Account Connector.

To generate a Connector Authentication Link:

* Go to the Account containing the Connector you wish to authenticate.
* Open the **Connectors** menu.
* Click **Edit Connector** next to the Connector to be authenticated.
* Click **Generate Setup Token**.
* Tokens generated here will expire after 5 minutes by default.  If you wish, you can set a longer time before expiry here using the date picker.
* Click Generate.
* You will be presented with a sign-in token for your user, and a link to a site where they can enter it.

![Animated Demo](./images/sign-in-token.gif)

> This is a new way of delivering sign-in tokens, and was developed to address issues some users were having with their spam filters/email systems automatically clicking (_and therefore invalidating_) the links.

This token can only be used once, so you may need to go through these steps again if your user startsbut doesn't complete the sign-in process.
