---
title: Wealthbox Authentication
sidebar: cyclr_sidebar
permalink: wealthbox-connector
tags: [connector]
---

## Partner Setup

First, [login](https://app.crmworkspace.com/users/login) to your existing Wealthbox account or [sign up for one.](https://www.wealthbox.com/)

You will require an **Access Token** to authenticate the connector.

#### Retrieving an Access Token.

*   [Login](https://app.crmworkspace.com/users/login) to your Wealthbox Account.
*   Click on the three dots in the top right corner of the window, and then click **Settings**.
*   Click **API Access** under the **Personal** header.
*   Create a new **Access Token** or skip this step if you already have one listed on the page.
    *   To create a new **Access Token**, click **Create Access Token**.
    *   Enter an appropriate label, and click **Save**.
*   Note down the **Access Token**, which is the line of text after the label. It will look similar to "d90b0cef4311gf85feb3y6c8c4f70d7b".

### Cyclr Setup

Setup your Wealthbox App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Wealthbox**
*   Click the **Setup** button

Enter the following values:

**API Key**: Enter the **Access Token** that we retrieved earlier here.

Your Wealthbox Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
