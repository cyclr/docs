---
title: Vend Connector Guide
sidebar: cyclr_sidebar
permalink: vend-connector
tags: [connector]
---

## Authentication

---

Vend uses OAuth 2.0 for authentication. The following are the steps needed to give this connector authorization to access data from Vend stores:

### Vend Setup

* If you haven't done so already, [create a developer account](https://developers.vendhq.com/developer/sign-up) with Vend.

> NOTE: Your developer account credentials are independent of your Vend account so your existing Vend credentials will not work here.

* Once logged in go to [My Applications](https://developers.vendhq.com/developer/applications) page. 
* Create a new application by clicking the 'Add New Application' button and provide the requested information.
  * Redirect URI will be https://{ServiceDomain}/connector/callback. 
  * Your Service Domain can be found in Settings > General Settings > Service Domain in your Cyclr console.

> NOTE: Newly created apps are marked as Not Approved. This shouldn't be a problem, you can still use this app. Not Approved just means that you can only connect your application to 30 Vend stores. You only need to get Vend's approval for production ready, public applications.

* You will now have an application with a **Client ID** and **Client Secret**.

### Cyclr Setup

* The connector can now be installed. Enter your Client ID, Client Secret and Store Name into the Cyclr interface, click 'Next' and then 'Sign In' on the next page.

![connector setup](./images/vend_setup_img_2.png)

* You will be redirected to Vend's website where you will be guided through the login process.

![connector setup](./images/vend_setup_img_3.png)

* Allow Access.

![connector setup](./images/vend_setup_img_5.png)

* If the above steps completed successfully you will be redirected back to Cyclr. The connector is now installed and authenticated.
