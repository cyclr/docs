---
title: SPS Commerce Authentication
sidebar: cyclr_sidebar
permalink: sps-commerce-connector
tags: [connector]
---

## Partner Setup

First, [login](https://developercenter.spscommerce.com/) to your existing SPS Commerce Developer account or [sign up for one.](https://developercenter.spscommerce.com/#/signup)

#### Retrieving OAuth2 Details

*   [Login](https://developercenter.spscommerce.com/) to your SPS Commerce Developer Account.
*   Click "Applications" located at the top of the page.
*   If you don't have an existing app:
    * Click "Create App".
    * Enter an appropriate name and description, and then click "Save and Continue".
    * Select "Web Service Application" as the App Type and click "Save and Continue".
    * Enter the redirect URL for your Cyclr account (https://[Your Cyclr Service Domain]/connector/callback) and click "Save and Continue".
*   Click on your existing app and navigate to the  "Connection Information" tab. Note down the **App ID** and **App Secret**.

### Cyclr Setup

Setup your SPS Commerce App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **SPS Commerce**
*   Click the **Setup** button

Enter the following values:

**Client ID**: The **App ID** that we retrieved from the "Connection Information" tab above.

**Client Secret**:  The **App Secret** that we retrieved from the "Connection Information" tab above.

Your SPS Commerce Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

### Setup Methods

#### Get JSON Transaction

This method requires you to add your own custom response fields. This can be accomplished in the connector editor by clicking the
"+" button under the **Response Fields** area.

A further explanation of how to do this can be found [here](https://docs.cyclr.com/adding-custom-fields).