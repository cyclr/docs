---
title: Mindbody Connector Guide
sidebar: cyclr_sidebar
permalink: mindbody-connector
tags: [connector]
---

Mindbody Setup
---------------

To setup the connector you need to access the configuration information within Mindbody. To do this a Mindbody [developer account](https://developers.mindbodyonline.com/Home/LogIn) will be needed.

Mindbody have two environments:
* _Sandbox_. Access to the sandbox environment following these [instructions](https://developers.mindbodyonline.com/PublicDocumentation/V6#using-sandbox).

   Site ID = -99
   
   Username = Siteowner

   Password = apitest1234

* _Production_ You will have to fill out a form and apply for access see these [instructions](https://developers.mindbodyonline.com/PublicDocumentation/V6#taking-application-live).

The API key can be found by going to Account > API Credentials. You can either create an API key or Show an existing key.

![](./images/mindbody_apikey.png)

You can also find the Site ID by following [this](https://support.mindbodyonline.com/s/article/206398178-How-do-I-find-my-Client-ID?language=en_US) guide.

Connector Setup
---------------

The Connector now can be installed using the credentials obtained in the above steps:

**Site ID**: `your_site_id`

**API-key**: `your_api_key`

**Username**: `username`

**Password**: `password`

