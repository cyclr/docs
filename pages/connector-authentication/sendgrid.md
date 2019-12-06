---
title: SendGrid Authentication
sidebar: cyclr_sidebar
permalink: sendgrid
tags: [connector]
---

## Partner Setup ##

SendGrid uses an API key for authentication, so you must gain an API key by visiting the SendGrid website.

First, navigate to the [SendGrid API keys](https://app.sendgrid.com/settings/api_keys) section.
Once you have logged in, you should be greeted by an empty page.

To create your first API Key, click the "Create API Key" button in the top-right corner of the page. You will then be shown a page where you can enter the name of your API key, and the permissions of the key:

![SendGrid - Create API Key page](./images/sendgrid-create-api-key.png)

Fill this out as you please, and then click "Create & View". You will then be greeted by another page that will show you your newly created API key. Copy this and keep it somewhere safe, as it states on the page you cannot access the key again.

![SendGrid - Create and View page](./images/sendgrid-create-and-view.png.png)

This key lets you integrate SendGrid with Cyclr. You can now navigate to the Connectors menu through the Cyclr Console, and then the Connector Library where you can click the setup button and enter your API key into the input box.

Your end-users should now be able to install the Connector into their own accounts.