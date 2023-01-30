---
title: Sage 50cloud Connector
sidebar: cyclr_sidebar
permalink: sage-50cloud-connector
tags: [connector]
---

## Client Setup

### Setup SDATA
SDATA is the API functionality we use to communicate with the Sage 50cloud on-premise application. This must be setup within your Sage 50cloud application. 
We advise setting up a separate API user that Cyclr can use to access the API with. This allows you to restrict the amount of data that Cyclr can access.
* Login to your Sage 50cloud application.
* Navigate to **Settings** > **User Management** > **Users**.
* Create a new user.
##### User Setup
* Select **Standard** user type.
* Enter basic user details (username and password) in the **Profile** area. Note that this will be used for API authentication.
* Select which access points the user has. This restricts what data the API, and in turn Cyclr, can access.
* Enable **Remote Data Access**. Fill in the necessary details.
* Confirm the creation of the user.
##### Enable SDATA
* Navigate to **Tools** > **Internet Options** > **SData Settings**.
* Make sure it is enabled by ticking the **On** checkbox next to the name of your Sage 50cloud application.
* Click **Details** and note down the **Address**.

### Allow Cyclr access to your application
As Sage 50cloud is an on-premise application, you will need to open a connection to Cyclr. This guide will focus on a local computer connecting to Cyclr. As each router is different, this guide will be very generic. We recommend contacting your IT support team if possible to setup this part for you. If your application is running on an external provider (AWS, Azure etc.), you should seek information about how to open ports from their respective support resources.
* Navigate to your router interface. Your router manual will tell you the IP address.
* Login to your router and navigate to the port forwarding area.
* If the fields are required, enter the following:
  * IP Address: the local IP address of your device that is running the Sage 50cloud application. 
  * Internal port: the Sage 50cloud application port. If you have not changed this, it will be **5495**.
  * External port: the same as above. 
* Create the rule. Make sure it is enabled.
##### Strengthen security
While the above is all that is required to allow Cyclr to connect to your Sage 50cloud application, it is not secure. We advise following the below steps to secure your connection.
* We advise restricting your outside connection to only allow Cyclr access to the Sage 50cloud application. To do so, whitelist one or all of the [Cyclr IPs](https://docs.cyclr.com/cyclr-ip-whitelisting#toc) in your router or firewall.
* We also advise securing the connection using HTTPS instead of HTTP. There are multiple services that can enable this feature, such as Caddy and NGINX. Caddy also comes with the added benefit of automatic TLS certificate renewal built-in.

### Cyclr Setup

Setup your Sage 50cloud App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Sage 50cloud**
*   Click the **Setup** button

Enter the following values:

**Domain and Port**: The Sage 50cloud IP/domain and port e.g. **https://10.25.46.123:5495**

**Virtual Directory**: **sdata** unless changed in the Sage 50cloud settings.

**Application**: Name of the application. **Accounts50** unless changed.

**Contract Name**: An SData service can support several “integration contracts” side-by-side. For example, a typical Sage ERP service will support a crmErp contract which exposes the resources required by CRM integration (with schemas imposed by the CRM/ERP contract) and a native or default contract which exposes all the resources of the ERP in their native format. Default is "GCRM".

**Data Set**: Identifies the dataset when the application gives access to several datasets, such as several companies and production/test datasets. If the application can only handle a single dataset, or if it can be configured with a default dataset, a hyphen can be used as a placeholder for the default dataset.  several parameters are required to specify the dataset (for example database name and company id), they should be formatted as a single segment in the URL. For example, "dataset1;dataset2".

**Username**: The username of the user that you created in the first steps.

**Password**: The password of the user that you created in the first steps.

Your Sage 50cloud Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
