---
title: Mailkit Authentication
sidebar: cyclr_sidebar
permalink: Mailkit-connector
tags: [connector]
---

## Partner Setup

First, login to your existing Mailkit account or [sign up for one.](https://app.mailkit.eu/)

#### Retrieving Authentication Details

*   [Login](https://app.mailkit.eu/) to your Mailkit Account.
*   Click Create App.
*   Enavigate to your Profile page, under the menu, click on Integration then API Settings.
*   You'll find a page that presents your User ID and MD5 Hash among other information.
*   Note the **User ID** and **MD5 Hash**.

### Cyclr Setup

Setup your Mailkit App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Mailkit**
*   Click the **Setup** button

Enter the following values:

**Client ID**:  The User ID that we retrieved from the app that we made.

**Client MD5**:  The MD5 Hash that we retrieved from the app that we made.


Your Mailkit Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
