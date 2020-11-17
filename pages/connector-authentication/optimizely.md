---
title: Optimizely Authentication
sidebar: cyclr_sidebar
permalink: optimizely-connector
tags: [connector]
---

## Partner Setup

First, login to your existing Optimizely Developer account or [sign up for one.](https://www.optimizely.com/rollouts/)

#### Retrieving OAuth2 Details

*   [Login](https://app.optimizely.com/v2/profile/api) to your Optimizely Developer Account.
*   Click **Profile** in the bottom left area of the navigation tree.
*   Navigate to the **API Access** tab.
*   Click **Generate New Token**.
*   Enter an appropriate name for the token and click **Create**.
*   Copy the generated **token** value.

### Cyclr Setup

Setup your Optimizely App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Optimizely**
*   Click the **Setup** button

Enter the following values:

**Personal Token**:  The **token** that we retrieved from the previous step.


Your Optimizely Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
