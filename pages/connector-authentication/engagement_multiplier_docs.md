---
title: Engagement Multiplier Connector Guide
sidebar: cyclr_sidebar
permalink: engagement-multiplier-connector
tags: [connector]
---

## Authentication Credentials

The Engagement Multiplier connector is authenticated with OAuth2.0, as a result you will need a **Client ID** and **Client Secret**:

1. Login to your Engagement Multiplier **Developer** account [here](http://em.envisionitmedia.com)

2. Go to **Integrations** > **API Clients** from the dashboard menu

   ![engagement multiplier interface](./images/engage_multi_1.png)

3. If you have a client enabled you will see your **Client ID**, **Name** and **Secret**. If not, **Create New Client**

   ![engagement multiplier interface](./images/engage_multi_2.png)

4. Enter your application's **Name** and for **Redirect URL** enter **https://{service domain}/connector/callback**

   > Replace {service domain} with your service domain. That can be located in your Cyclr console under Settings > Integration Settings > Service Domain

   ![engagement multiplier interface](./images/engage_multi_3.png)

## Authenticate The Connector

1. Locate the Engagement Multiplier connector

   > Cyclr Console > Connectors > Connector Library > Engagement Multiplier

2. From the Edit Connector interface click 'Setup'

3. Enter the **Client ID** and **Client Secret** from your Engagement Multiplier **Developer** account created above, click **Next**

4. Click **Sign In**

   ![engagement multiplier interface](./images/engage_multi_5.png)

5. A popup will prompt you to login to your Engagement Multiplier account

6. You must login with your Engagement Multiplier **User** account credentials

7. You will recieve the following prompt to allow or deny access to your account, click **Authorize**

   ![engagement multiplier interface](./images/engage_multi_4.png)

Upon successful authorization you will be redirected to Cyclr. The connector is now authenticated and ready to use.

## User Guide

If you are unable to locate your Company ID, you can use the method 'Get Authenticated User'. It will retrieve among other things, the Company ID for the currently authenticated user.