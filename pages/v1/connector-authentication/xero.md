---
title: Xero Private Instance Authentication
sidebar: cyclr_sidebar
permalink: xero-private-connector
tags: [connector]
---

# Xero Private Instance #

Partner Setup
-------------

In order to authenticate the connector, you must first create a Private Application in Xero.

The official Xero documentation for this process can be found here:
[Creating a Xero Private Application](https://developer.xero.com/documentation/auth-and-limits/private-applications)

Once you have successfully created a private application within Xero, copy the consumer key as seen in the image below:

![](./images/consumer_key.PNG)

Paste this value into the Consumer Key field in the Cyclr Connector Authentication screen:

![](./images/consumer_key_connector.PNG)

Next open the `privatekey.pem` file - that you generated when creating your private application - in a text editor and copy the contents:

![](./images/privatekey_text.PNG)

Paste this into the Private Key field in the Cyclr Connector Authentication screen, making sure to remove any trailing whitespace:

![](./images/privatekey_connector.PNG)

Press `Next` and the connector should now be authenticated.

At this point it would be a good idea to run a test against one of the methods, just to make sure the authentication process has been completed successfully.
