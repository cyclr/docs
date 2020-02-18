---
title: Box Connector Guide
sidebar: cyclr_sidebar
permalink: box-connector
tags: [connector]
---

## Authentication

Box uses OAuth 2.0 for authentication. The following are the steps needed to give this connector authorization to Box applications:

### Box Console

 * If you have a Box account already, [sign in](https://account.box.com/login). Otherwise [create a new account](https://www.box.com/pricing).
 * Once signed in, go to 'Dev console' from the left hand menu. That will take you through to your apps. You can either select a pre-existing app or create a new one.

![connector setup](./images/box_setup_8.png)
![connector setup](./images/box_setup_1.png)

 * Once you have selected the app you would like to authenticate, on the following page click 'Configuration' from the left hand menu.

![connector setup](./images/box_setup_5.png)

 * In the configuration page make sure that 'Authentication method' is set to 'Standard OAuth 2.0 (User Authentication)'.

![connector setup](./images/box_setup_2.png)

 * Scroll down to find your **Client ID** and **Client Secret**. For Redirect URI enter: https://{{ServiceDomain}}/connector/callback (ServiceDomain should be substituted for your actual service domain)

> Your Cyclr service domain, e.g. yourcompany.cyclr.com can be found in your Cyclr Console under Settings > Integration Settings > Service Domain.

![connector setup](./images/box_setup_4.png)

### Cyclr Console

 * Locate the Box connector in the Cyclr console.

> (https://{{ServiceDomain}}/console) > Connectors > Connector Library > Box

 * Click the open padlock and on the next page enter your Client ID and Client Secret.

![connector setup](./images/box_setup_7.png)

 * Upon installation of the connector in your account, you will be redirected to Box and prompted to 'Grant access to Box'. Once completed, you will be redirected back to Cyclr where the connector is authenticated and ready to use.

![connector setup](./images/box_setup_9.png)
