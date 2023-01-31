---
title: WebEOC Authentication
sidebar: cyclr_sidebar
permalink: webeoc-connector
tags: [connector]
---

## Partner Setup

This guide presumes that you already have a WebEOC account.

### Cyclr Setup

Setup your WebEOC App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **WebEOC**
*   Click the **Setup** button

Enter the following values:

**Base URL**: This is the first part of your WebEOC instance URL. For example, if you logged into the website using "https://webeoc.web.webeocasp.com/webeoc/" you would enter "https://webeoc.web.webeocasp.com" in this field.

**Username**:  WebEOC user to perform the requested operation. This can be the username you use to login to your instance.

**Password**: Password for the user specified by Username.

**Position**: Position the WebEOC user is assigned to. Optional.

**Incident**: WebEOC incident to log into while performing the requested operation. Optional.

**Board Name**: The board to perform the requested operations on.

If you do not know the "Board Input View" and "Board Display" that you want to use:

* Complete the setup.
* Navigate to your installed connector and run the "List Display Views" method, copy the name of a display view you would like to use.
* Also run the "List Input Views" method and copy the name of an input view you would like to use.
* Click the **Setup** button again and enter the values:

**Board Input View**: The input view that you gathered from the previous steps.

**Board Display**: The board display that you gathered from the previous steps.


Your WebEOC Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
