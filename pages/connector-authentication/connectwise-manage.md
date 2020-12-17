---
title: ConnectWise Manage Authentication
sidebar: cyclr_sidebar
permalink: connectwisemanage-connector
tags: [connector]
---

## Partner Setup

#### Retrieving Client ID
*   Navigate to the [Partner Client ID](https://developer.connectwise.com/ClientID/Partner_Client_IDs) or [Vendor Client ID](https://developer.connectwise.com/ClientID/Vendor_Client_IDs) page to retrieve your ID.
*   You can either create a new integration, or if you are unable to, apply for one.
*   To create a new integration, click the *Create New Integration* button and enter the appropriate information.
*   You will then be redirected to a page with your client ID.

### Cyclr Setup

Setup your ConnectWise Manage App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **ConnectWise Manage**
*   Click the **Setup** button

Enter the following values:

**Domain**:  Your API domain, and the domain you use to access the front-end website. [Here](https://developer.connectwise.com/Best_Practices/Manage_Cloud_URL_Formatting?mt-learningpath=manage) is a list of common URLs.

**API Version**:  The version of the API you would like to use. More details [here](https://developer.connectwise.com/Best_Practices/Manage_Versioning?mt-learningpath=manage).

**Client ID**: Retrieve from the above steps.

**Username**: This is your company ID followed by a plus sign (+) and then your username. For example: "companyId+username".

**Password**: This is the password you use to login to the front-end website.


Your ConnectWise Manage Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
