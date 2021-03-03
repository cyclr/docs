---
title: MRI Authentication
sidebar: cyclr_sidebar
permalink: mri-connector
tags: [connector]
---

## Partner Setup

### Retrieving Username
Your username is s C1, your Web Services user name is U1, your Web Services user password is Password, your MRI application database name is D1, and your assigned MIX partner key is P1. With the above information, your API user name would be "C1/D1/U1/P1".

### Cyclr Setup

Setup your MRI App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **MRI**
*   Click the **Setup** button

Enter the following values:

**Domain**: Your API domain, and the domain you use to access the front-end website. For example, if you logged into the website using this URL: "https://mri.services.com" you would enter "mri.services.com".

**Username**: This is explained above.

**Password**: This would be the password you used to login to the website with.


Your MRI Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
