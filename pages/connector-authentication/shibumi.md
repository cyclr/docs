---
title: Shibumi Authentication
sidebar: cyclr_sidebar
permalink: shibumi-connector
tags: [connector]
---

## Partner Setup

#### Retrieving Client ID and Secret
* You can get your client ID and secret from your Shibumi contact.

#### Retrieving Username and Password
* Create a new user in your Shibumi enterprise. This user should only be used by the API, not by a human.
* Note down the newly created username and password for the user.

### Cyclr Setup

Setup your Shibumi App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Shibumi**
*   Click the **Setup** button

Enter the following values:

**Client ID**: The Client ID that was given to you by your Shibumi contact.

**Client Secret**:  The Client Secret that was given to you by your Shibumi contact.

**Username**: Retrieved from the previous steps.

**Password**: Also retrieved from the previous steps.

**Environment**: The API environment. This is usually "app".

**Enterprise ID**: The enterprise ID of your instance.


Your Shibumi Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
