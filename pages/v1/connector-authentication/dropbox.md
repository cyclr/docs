---
title: Dropbox Authentication
sidebar: cyclr_sidebar
permalink: dropbox-connector
tags: [connector]
---

## Partner Setup

#### Retrieving Client ID and Client Secret
* Navigate to [the app console](https://www.dropbox.com/developers/apps) page.
* Click "Create App".
* Click "Scoped access", choose either full access or specific folder access and enter a name for the app.
* Open the newly created app.
* Enter your redirect URL (`https://[Your Cyclr Service Domain]/connector/callback`).
* Note down the **App Key** and **App Secret**.
* Navigate to the **Permissions** tab.
* Tick the following permissions to fully use the connector:
  * **files.metadata.read** to use the "Search Files and Folders" method.
  * **files.content.read** to use the "Get Temporary File" method.
* **Don't forget to submit your changes.**

### Cyclr Setup

Setup your Dropbox App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Dropbox**
*   Click the **Setup** button

Enter the following values:

**Client ID**: Retrieved from the above steps.

**Client Secret**: Also retrieved from the above steps.


Your Dropbox connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
