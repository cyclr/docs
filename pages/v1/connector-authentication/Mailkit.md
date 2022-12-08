---
title: Mailkit Authentication
sidebar: cyclr_sidebar
permalink: Mailkit-connector
tags: [connector]
---

## Partner Setup

First, login to your existing Mailkit account or [sign up for one.](https://app.mailkit.eu/)

### Retrieving Authentication Details

*   [Login](https://app.mailkit.eu/) to your Mailkit Account.
*   Click Create App.
*   Enavigate to your Profile page, under the menu, click on Integration then API Settings.
*   You'll find a page that presents your User ID and MD5 Hash among other information.
*   Note the **User ID** and **MD5 Hash**.

### Cyclr Setup

You have the choice of authenticating the connector at either Partner level or Account level. Authenticating the connector at Partner level will result in all account installations of the connector sharing the same credentials. If you require each account installation to use separate credentials you should authenticate the connector at Account level.

Setup your Mailkit App within Cyclr:

### Partner Level

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Application Connector Library
*   Search for **Mailkit**
*   Click the **padlock** button

Enter the following values:

**Client ID**:  The User ID that we retrieved from the app that we made.

**Client MD5**:  The MD5 Hash that we retrieved from the app that we made.

Your Mailkit Connector is now setup at Partner level. You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

### Account Level

From within the account you wish to install the connector:

*   Click **Connectors** (top navigation bar) and then **Install New Application**
*   Search for **Mailkit** and click **Install**
*   You will be presented with a name and empty description for the installation, change these if preferred and then click 'Next'
*   Enter your **Client ID** and **Client MD5**, then click 'Next'

Your Mailkit connector is now setup at Account level. You can test it by executing one of the methods to confirm it can return some data.
